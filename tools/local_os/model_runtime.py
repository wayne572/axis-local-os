from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "config" / "local_model_runtime.json"
ROUTING_PATH = ROOT / "config" / "model_routing.json"
ENV_PATH = ROOT / ".env"
OPERATOR_PROFILE_PATH = ROOT / "CORE" / "OPERATOR_PROFILE.md"
AUDIT_DIR = ROOT / ".axis" / "audit"
MODEL_AUDIT_PATH = AUDIT_DIR / "model_runtime.jsonl"
DEFAULT_TIMEOUT_SECONDS = 5
DEFAULT_GENERATE_TIMEOUT_SECONDS = 120
HOSTED_TIMEOUT_SECONDS = 60
PROMPT_PREAMBLE_SECTIONS = [
    "How To Work With Wayne",
    "What Axis Does Not Do For Wayne",
]


def _load_env_file() -> None:
    if not ENV_PATH.exists():
        return
    import os
    for raw in ENV_PATH.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_env_file()

# Legacy fallback authority boosts kept for any source path not covered by the
# scope file's chunk-level authority_boost. The chunk-level boost is the
# canonical source of truth - this map only applies to chunks that have no
# scope-level boost (legacy index entries) and overlaps cleanly when both exist.
AUTHORITY_SOURCE_BOOSTS = {
    "AXIS_OS_CODEX_CURRENT\\AXIS_LOCAL_OS_SPEC.md": 20.0,
    "AXIS_OS_CODEX_CURRENT\\AXIS_BUILD_PLAN.md": 3.0,
    "AXIS_OS_CODEX_CURRENT\\README.md": 2.0,
}

sys.path.insert(0, str(ROOT / "tools" / "rag"))
from kb_search import search  # noqa: E402


@dataclass
class RuntimeConfig:
    provider_name: str
    provider_type: str
    base_url: str
    primary_model: str
    fallback_models: list[str]
    health_endpoint: str
    api_key_env: str | None = None
    anthropic_version: str | None = None


@dataclass
class RuntimeHealth:
    provider: str
    provider_type: str
    base_url: str
    available: bool
    primary_model: str
    primary_model_installed: bool
    installed_models: list[str]
    fallback_models: list[str]
    message: str


@dataclass
class ModelResponse:
    provider: str
    model: str
    prompt: str
    response: str
    done: bool
    message: str
    audit_path: str
    grounded: bool = False
    source_ids: list[str] | None = None


def load_config(path: Path = CONFIG_PATH) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Runtime config not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def get_runtime_config(provider_name: str | None = None) -> RuntimeConfig:
    config = load_config()
    selected = provider_name or config.get("default_provider")
    providers = config.get("providers", {})
    provider = providers.get(selected)
    if not provider:
        available = ", ".join(sorted(providers)) or "none"
        raise SystemExit(f"Unknown provider '{selected}'. Available providers: {available}")

    return RuntimeConfig(
        provider_name=selected,
        provider_type=provider.get("type", selected),
        base_url=provider["base_url"].rstrip("/"),
        primary_model=provider["primary_model"],
        fallback_models=list(provider.get("fallback_models", [])),
        health_endpoint=provider.get("health_endpoint", "/api/tags"),
        api_key_env=provider.get("api_key_env"),
        anthropic_version=provider.get("anthropic_version"),
    )


def fetch_json(
    url: str,
    timeout: int = DEFAULT_TIMEOUT_SECONDS,
    payload: dict[str, Any] | None = None,
    extra_headers: dict[str, str] | None = None,
) -> dict[str, Any]:
    data = None
    headers = {"Accept": "application/json"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    if extra_headers:
        headers.update(extra_headers)
    request = Request(url, data=data, headers=headers)
    with urlopen(request, timeout=timeout) as response:
        raw = response.read().decode("utf-8")
    return json.loads(raw)


def get_api_key(config: RuntimeConfig) -> str | None:
    import os
    if not config.api_key_env:
        return None
    return os.environ.get(config.api_key_env) or None


def _redacted_health(config: RuntimeConfig, available: bool, message: str, installed: list[str] | None = None) -> RuntimeHealth:
    return RuntimeHealth(
        provider=config.provider_name,
        provider_type=config.provider_type,
        base_url=config.base_url,
        available=available,
        primary_model=config.primary_model,
        primary_model_installed=False,
        installed_models=installed or [],
        fallback_models=config.fallback_models,
        message=message,
    )


def claude_health(config: RuntimeConfig) -> RuntimeHealth:
    key = get_api_key(config)
    if not key:
        return _redacted_health(config, False, f"Missing API key. Set {config.api_key_env} in .env or environment.")
    url = f"{config.base_url}{config.health_endpoint}"
    headers = {
        "x-api-key": key,
        "anthropic-version": config.anthropic_version or "2023-06-01",
    }
    try:
        payload = fetch_json(url, timeout=DEFAULT_TIMEOUT_SECONDS, extra_headers=headers)
    except HTTPError as error:
        return _redacted_health(config, False, f"Claude responded with HTTP {error.code}. Check key validity and model access.")
    except URLError:
        return _redacted_health(config, False, "Claude API is not reachable. Check network or DNS.")
    except TimeoutError:
        return _redacted_health(config, False, "Claude health check timed out.")
    except json.JSONDecodeError:
        return _redacted_health(config, False, "Claude returned a non-JSON response.")

    installed = sorted(model.get("id", "") for model in payload.get("data", []) if model.get("id"))
    primary_installed = config.primary_model in installed
    msg = "Claude API reachable and primary model is in the allowed list." if primary_installed else (
        f"Claude API reachable but primary model `{config.primary_model}` is not in the visible model list."
    )
    return RuntimeHealth(
        provider=config.provider_name,
        provider_type=config.provider_type,
        base_url=config.base_url,
        available=True,
        primary_model=config.primary_model,
        primary_model_installed=primary_installed,
        installed_models=installed,
        fallback_models=config.fallback_models,
        message=msg,
    )


def openai_health(config: RuntimeConfig) -> RuntimeHealth:
    key = get_api_key(config)
    if not key:
        return _redacted_health(config, False, f"Missing API key. Set {config.api_key_env} in .env or environment.")
    url = f"{config.base_url}{config.health_endpoint}"
    headers = {"Authorization": f"Bearer {key}"}
    try:
        payload = fetch_json(url, timeout=DEFAULT_TIMEOUT_SECONDS, extra_headers=headers)
    except HTTPError as error:
        return _redacted_health(config, False, f"OpenAI responded with HTTP {error.code}. Check key validity.")
    except URLError:
        return _redacted_health(config, False, "OpenAI API is not reachable.")
    except TimeoutError:
        return _redacted_health(config, False, "OpenAI health check timed out.")
    except json.JSONDecodeError:
        return _redacted_health(config, False, "OpenAI returned a non-JSON response.")

    installed = sorted(model.get("id", "") for model in payload.get("data", []) if model.get("id"))
    primary_installed = config.primary_model in installed
    msg = "OpenAI API reachable and primary model is in the allowed list." if primary_installed else (
        f"OpenAI API reachable but primary model `{config.primary_model}` is not in the visible model list."
    )
    return RuntimeHealth(
        provider=config.provider_name,
        provider_type=config.provider_type,
        base_url=config.base_url,
        available=True,
        primary_model=config.primary_model,
        primary_model_installed=primary_installed,
        installed_models=installed,
        fallback_models=config.fallback_models,
        message=msg,
    )


def claude_generate(prompt: str, config: RuntimeConfig, model: str, timeout: int) -> tuple[str, bool, str, dict[str, Any]]:
    key = get_api_key(config)
    if not key:
        return "", False, f"Missing API key. Set {config.api_key_env} in .env.", {}
    url = f"{config.base_url}/v1/messages"
    headers = {
        "x-api-key": key,
        "anthropic-version": config.anthropic_version or "2023-06-01",
    }
    payload = {
        "model": model,
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": prompt}],
    }
    try:
        raw = fetch_json(url, timeout=timeout, payload=payload, extra_headers=headers)
    except HTTPError as error:
        return "", False, f"Claude generation failed with HTTP {error.code}.", {}
    except URLError:
        return "", False, "Claude API is not reachable.", {}
    except TimeoutError:
        return "", False, "Claude generation timed out.", {}
    except json.JSONDecodeError:
        return "", False, "Claude returned a non-JSON response.", {}

    content_blocks = raw.get("content", [])
    text = "".join(block.get("text", "") for block in content_blocks if block.get("type") == "text")
    usage = raw.get("usage", {}) or {}
    metrics = {
        "prompt_tokens": usage.get("input_tokens"),
        "completion_tokens": usage.get("output_tokens"),
    }
    done = bool(raw.get("stop_reason"))
    msg = "Hosted Claude call completed. No tools executed, no memory updated."
    return text, done, msg, metrics


def openai_generate(prompt: str, config: RuntimeConfig, model: str, timeout: int) -> tuple[str, bool, str, dict[str, Any]]:
    key = get_api_key(config)
    if not key:
        return "", False, f"Missing API key. Set {config.api_key_env} in .env.", {}
    url = f"{config.base_url}/v1/chat/completions"
    headers = {"Authorization": f"Bearer {key}"}
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
    }
    try:
        raw = fetch_json(url, timeout=timeout, payload=payload, extra_headers=headers)
    except HTTPError as error:
        return "", False, f"OpenAI generation failed with HTTP {error.code}.", {}
    except URLError:
        return "", False, "OpenAI API is not reachable.", {}
    except TimeoutError:
        return "", False, "OpenAI generation timed out.", {}
    except json.JSONDecodeError:
        return "", False, "OpenAI returned a non-JSON response.", {}

    choices = raw.get("choices", [])
    text = choices[0].get("message", {}).get("content", "") if choices else ""
    usage = raw.get("usage", {}) or {}
    metrics = {
        "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
    }
    done = bool(choices and choices[0].get("finish_reason"))
    msg = "Hosted OpenAI call completed. No tools executed, no memory updated."
    return text, done, msg, metrics


def normalise_model_name(name: str) -> str:
    return name.split(":", 1)[0].lower()


def ollama_health(config: RuntimeConfig) -> RuntimeHealth:
    url = f"{config.base_url}{config.health_endpoint}"
    try:
        payload = fetch_json(url)
    except HTTPError as error:
        return RuntimeHealth(
            provider=config.provider_name,
            provider_type=config.provider_type,
            base_url=config.base_url,
            available=False,
            primary_model=config.primary_model,
            primary_model_installed=False,
            installed_models=[],
            fallback_models=config.fallback_models,
            message=f"Ollama responded with HTTP {error.code}. Check the local runtime.",
        )
    except URLError:
        return RuntimeHealth(
            provider=config.provider_name,
            provider_type=config.provider_type,
            base_url=config.base_url,
            available=False,
            primary_model=config.primary_model,
            primary_model_installed=False,
            installed_models=[],
            fallback_models=config.fallback_models,
            message="Ollama is not reachable. Install/start Ollama, then retry.",
        )
    except TimeoutError:
        return RuntimeHealth(
            provider=config.provider_name,
            provider_type=config.provider_type,
            base_url=config.base_url,
            available=False,
            primary_model=config.primary_model,
            primary_model_installed=False,
            installed_models=[],
            fallback_models=config.fallback_models,
            message="Ollama health check timed out. The service may be starting or blocked.",
        )
    except json.JSONDecodeError:
        return RuntimeHealth(
            provider=config.provider_name,
            provider_type=config.provider_type,
            base_url=config.base_url,
            available=False,
            primary_model=config.primary_model,
            primary_model_installed=False,
            installed_models=[],
            fallback_models=config.fallback_models,
            message="Ollama returned a non-JSON response.",
        )

    installed = sorted(model.get("name", "") for model in payload.get("models", []) if model.get("name"))
    installed_normalised = {normalise_model_name(name) for name in installed}
    primary_installed = normalise_model_name(config.primary_model) in installed_normalised
    if primary_installed:
        message = "Local runtime is reachable and the primary model appears to be installed."
    else:
        message = (
            "Local runtime is reachable, but the primary model is not installed. "
            f"Install it with: ollama pull {config.primary_model}"
        )

    return RuntimeHealth(
        provider=config.provider_name,
        provider_type=config.provider_type,
        base_url=config.base_url,
        available=True,
        primary_model=config.primary_model,
        primary_model_installed=primary_installed,
        installed_models=installed,
        fallback_models=config.fallback_models,
        message=message,
    )


def check_health(provider_name: str | None = None) -> RuntimeHealth:
    config = get_runtime_config(provider_name)
    if config.provider_type == "ollama":
        return ollama_health(config)
    if config.provider_type == "claude":
        return claude_health(config)
    if config.provider_type == "openai":
        return openai_health(config)
    raise SystemExit(f"Provider type '{config.provider_type}' is not implemented yet.")


def write_model_audit(event: dict[str, Any]) -> None:
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    with MODEL_AUDIT_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=True) + "\n")


def generate_once(
    prompt: str,
    provider_name: str | None = None,
    model: str | None = None,
    timeout: int = DEFAULT_GENERATE_TIMEOUT_SECONDS,
) -> ModelResponse:
    config = get_runtime_config(provider_name)
    selected_model = model or config.primary_model
    metrics: dict[str, Any] = {}

    if config.provider_type == "ollama":
        url = f"{config.base_url}/api/generate"
        payload = {
            "model": selected_model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.2},
        }
        try:
            raw_response = fetch_json(url, timeout=timeout, payload=payload)
            response_text = raw_response.get("response", "")
            done = bool(raw_response.get("done", False))
            message = "Local model response generated. No tools were executed and no memory was updated."
        except HTTPError as error:
            response_text, done, message = "", False, f"Ollama generation failed with HTTP {error.code}."
        except URLError:
            response_text, done, message = "", False, "Ollama is not reachable. Run the health check before generating."
        except TimeoutError:
            response_text, done, message = "", False, "Model generation timed out."
        except json.JSONDecodeError:
            response_text, done, message = "", False, "Ollama returned a non-JSON generation response."

    elif config.provider_type == "claude":
        response_text, done, message, metrics = claude_generate(prompt, config, selected_model, min(timeout, HOSTED_TIMEOUT_SECONDS))

    elif config.provider_type == "openai":
        response_text, done, message, metrics = openai_generate(prompt, config, selected_model, min(timeout, HOSTED_TIMEOUT_SECONDS))

    else:
        raise SystemExit(f"Provider type '{config.provider_type}' is not implemented yet.")

    result = ModelResponse(
        provider=config.provider_name,
        model=selected_model,
        prompt=prompt,
        response=response_text,
        done=done,
        message=message,
        audit_path=str(MODEL_AUDIT_PATH.relative_to(ROOT)),
    )
    audit_event: dict[str, Any] = {
        "schema": "axis-local-os-model-runtime-v1",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "provider": result.provider,
        "provider_type": config.provider_type,
        "model": result.model,
        "endpoint": config.base_url,
        "prompt_chars": len(prompt),
        "response_chars": len(response_text),
        "done": done,
        "message": message,
        "hosted": config.provider_type in {"claude", "openai"},
    }
    if metrics:
        audit_event.update(metrics)
    write_model_audit(audit_event)
    return result


_preamble_cache: dict[str, Any] = {"text": None, "mtime": None}


def load_operator_preamble() -> str:
    """Extract prompt-relevant sections from OPERATOR_PROFILE.md.

    Pulls the `## How To Work With Wayne` and `## What Axis Does Not Do For Wayne`
    sections from the canonical operator profile so every model call sees the
    operator's communication style, teaching-mode structure, decision-support
    structure, and the constitutional don't-list. Cached by file mtime so
    edits to the profile take effect on next call without restart.
    """
    if not OPERATOR_PROFILE_PATH.exists():
        return ""
    try:
        mtime = OPERATOR_PROFILE_PATH.stat().st_mtime
    except OSError:
        return ""
    if _preamble_cache["mtime"] == mtime and _preamble_cache["text"] is not None:
        return _preamble_cache["text"]

    try:
        raw = OPERATOR_PROFILE_PATH.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""

    sections: list[str] = []
    current_section: str | None = None
    current_lines: list[str] = []
    for line in raw.splitlines():
        if line.startswith("## "):
            heading = line[3:].strip()
            if current_section in PROMPT_PREAMBLE_SECTIONS and current_lines:
                sections.append(f"## {current_section}\n" + "\n".join(current_lines).strip())
            if heading in PROMPT_PREAMBLE_SECTIONS:
                current_section = heading
                current_lines = []
            else:
                current_section = None
                current_lines = []
            continue
        if current_section in PROMPT_PREAMBLE_SECTIONS:
            current_lines.append(line)
    if current_section in PROMPT_PREAMBLE_SECTIONS and current_lines:
        sections.append(f"## {current_section}\n" + "\n".join(current_lines).strip())

    preamble = "\n\n".join(sections).strip()
    _preamble_cache["mtime"] = mtime
    _preamble_cache["text"] = preamble
    return preamble


def _authority_score(item: tuple[float, dict[str, Any]]) -> float:
    score, chunk = item
    # Chunk-level boost was applied inside score_chunk. Only apply the legacy
    # path-map boost when the chunk has no scope-level boost of its own.
    if float(chunk.get("authority_boost", 0.0)) > 0:
        return score
    return score + AUTHORITY_SOURCE_BOOSTS.get(chunk.get("source_path", ""), 0.0)


def build_grounded_prompt(question: str, limit: int) -> tuple[str, list[dict[str, Any]]]:
    raw_results = search(question, max(limit * 3, limit))
    results = sorted(
        raw_results,
        key=_authority_score,
        reverse=True,
    )[:limit]
    sources: list[dict[str, Any]] = []
    context_blocks: list[str] = []

    for rank, (score, chunk) in enumerate(results, start=1):
        source_id = chunk.get("id") or f"{chunk.get('source_path')}::chunk-{chunk.get('chunk_index')}"
        source = {
            "rank": rank,
            "score": round(float(score), 4),
            "source_id": source_id,
            "source_path": chunk.get("source_path", "unknown"),
            "title": chunk.get("title", "Untitled"),
            "chunk_index": chunk.get("chunk_index", 0),
        }
        sources.append(source)
        context_blocks.append(
            "\n".join(
                [
                    f"[SOURCE {rank}]",
                    f"source_id: {source['source_id']}",
                    f"path: {source['source_path']}",
                    f"title: {source['title']}",
                    "text:",
                    chunk.get("text", ""),
                ]
            )
        )

    context = "\n\n".join(context_blocks) or "No retrieved Axis Local OS context was found."
    preamble = load_operator_preamble()
    preamble_block = (
        f"\nOperator profile (canonical from CORE/OPERATOR_PROFILE.md):\n\n{preamble}\n"
        if preamble
        else ""
    )
    prompt = f"""You are answering inside Axis Local OS. The operator is Wayne Francis.
{preamble_block}
Governance rules:
- Answer only from the retrieved Axis context below.
- Cite exact source_id values for project-memory claims.
- Put citations in backticks, for example `AXIS_OS_CODEX_CURRENT\\AXIS_LOCAL_OS_SPEC.md::chunk-1`.
- Do not cite SOURCE numbers as final citations.
- If the retrieved context is insufficient, say what is missing.
- Do not claim project history from general model memory.
- Do not run tools, edit files, or update memory.
- Pricing is authoritative from retrieved chunks marked pricing_authority or sales_authority. Never restate pricing from model memory.

Retrieved Axis context:
{context}

Question:
{question}

Answer:
"""
    return prompt, sources


def generate_grounded(
    question: str,
    provider_name: str | None = None,
    model: str | None = None,
    limit: int = 4,
    timeout: int = DEFAULT_GENERATE_TIMEOUT_SECONDS,
) -> ModelResponse:
    prompt, sources = build_grounded_prompt(question, limit)
    result = generate_once(prompt, provider_name, model, timeout)
    result.grounded = True
    result.source_ids = [source["source_id"] for source in sources]
    write_model_audit(
        {
            "schema": "axis-local-os-grounded-model-call-v1",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "provider": result.provider,
            "model": result.model,
            "question_chars": len(question),
            "prompt_chars": len(prompt),
            "response_chars": len(result.response),
            "source_ids": result.source_ids,
            "operator_preamble_applied": bool(load_operator_preamble()),
            "operator_preamble_chars": len(load_operator_preamble()),
            "done": result.done,
            "message": result.message,
        }
    )
    return result


def render_health(health: RuntimeHealth) -> str:
    installed = ", ".join(health.installed_models) if health.installed_models else "none detected"
    fallback = ", ".join(health.fallback_models) if health.fallback_models else "none configured"
    lines = [
        "# Axis Local OS Model Runtime Health",
        "",
        f"Provider: {health.provider}",
        f"Type: {health.provider_type}",
        f"Base URL: {health.base_url}",
        f"Available: {'yes' if health.available else 'no'}",
        f"Primary model: {health.primary_model}",
        f"Primary installed: {'yes' if health.primary_model_installed else 'no'}",
        f"Fallback models: {fallback}",
        f"Installed models: {installed}",
        "",
        health.message,
    ]
    return "\n".join(lines)


def render_model_response(result: ModelResponse) -> str:
    source_ids = result.source_ids or []
    lines = [
        "# Axis Local OS Model Response",
        "",
        f"Provider: {result.provider}",
        f"Model: {result.model}",
        f"Done: {'yes' if result.done else 'no'}",
        f"Grounded: {'yes' if result.grounded else 'no'}",
        "",
        "## Governance",
        "",
        "This call is model-only. It did not run tools, change files, or update memory.",
    ]
    if source_ids:
        lines.extend(
            [
                "",
                "## Retrieved Source IDs",
                "",
                *[f"- `{source_id}`" for source_id in source_ids],
            ]
        )
    lines.extend(
        [
            "",
            "## Prompt",
            "",
            result.prompt,
            "",
            "## Response",
            "",
            result.response or result.message,
            "",
            "## Audit",
            "",
            result.audit_path,
        ]
    )
    return "\n".join(lines)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Check or call the Axis Local OS local model runtime")
    subparsers = parser.add_subparsers(dest="command")

    health_parser = subparsers.add_parser("health", help="Check local runtime health")
    health_parser.add_argument("--provider", default=None, help="Provider name from config/local_model_runtime.json")
    health_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    prompt_parser = subparsers.add_parser("prompt", help="Send one governed prompt to the local model")
    prompt_parser.add_argument("prompt", help="Prompt text to send to the model")
    prompt_parser.add_argument("--provider", default=None, help="Provider name from config/local_model_runtime.json")
    prompt_parser.add_argument("--model", default=None, help="Override model name, for example gemma4:latest")
    prompt_parser.add_argument("--timeout", type=int, default=DEFAULT_GENERATE_TIMEOUT_SECONDS)
    prompt_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    grounded_parser = subparsers.add_parser("grounded", help="Retrieve Axis context, then send one prompt")
    grounded_parser.add_argument("question", help="Question to answer from retrieved Axis context")
    grounded_parser.add_argument("--provider", default=None, help="Provider name from config/local_model_runtime.json")
    grounded_parser.add_argument("--model", default=None, help="Override model name, for example gemma4:latest")
    grounded_parser.add_argument("--limit", type=int, default=4, help="Number of KB chunks to inject")
    grounded_parser.add_argument("--timeout", type=int, default=DEFAULT_GENERATE_TIMEOUT_SECONDS)
    grounded_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    parser.set_defaults(command="health")
    args = parser.parse_args()

    if args.command == "grounded":
        result = generate_grounded(args.question, args.provider, args.model, args.limit, args.timeout)
        if args.json:
            print(json.dumps(asdict(result), indent=2, ensure_ascii=True))
        else:
            print(render_model_response(result))
    elif args.command == "prompt":
        result = generate_once(args.prompt, args.provider, args.model, args.timeout)
        if args.json:
            print(json.dumps(asdict(result), indent=2, ensure_ascii=True))
        else:
            print(render_model_response(result))
    else:
        health = check_health(getattr(args, "provider", None))
        if getattr(args, "json", False):
            print(json.dumps(asdict(health), indent=2, ensure_ascii=True))
        else:
            print(render_health(health))


if __name__ == "__main__":
    main()
