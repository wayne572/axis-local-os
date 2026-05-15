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
AUDIT_DIR = ROOT / ".axis" / "audit"
MODEL_AUDIT_PATH = AUDIT_DIR / "model_runtime.jsonl"
DEFAULT_TIMEOUT_SECONDS = 5
DEFAULT_GENERATE_TIMEOUT_SECONDS = 120


@dataclass
class RuntimeConfig:
    provider_name: str
    provider_type: str
    base_url: str
    primary_model: str
    fallback_models: list[str]
    health_endpoint: str


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
    )


def fetch_json(
    url: str,
    timeout: int = DEFAULT_TIMEOUT_SECONDS,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    data = None
    headers = {"Accept": "application/json"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = Request(url, data=data, headers=headers)
    with urlopen(request, timeout=timeout) as response:
        raw = response.read().decode("utf-8")
    return json.loads(raw)


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
    if config.provider_type != "ollama":
        raise SystemExit(f"Provider type '{config.provider_type}' is not implemented yet.")
    return ollama_health(config)


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
    if config.provider_type != "ollama":
        raise SystemExit(f"Provider type '{config.provider_type}' is not implemented yet.")

    selected_model = model or config.primary_model
    url = f"{config.base_url}/api/generate"
    payload = {
        "model": selected_model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2
        },
    }

    try:
        raw_response = fetch_json(url, timeout=timeout, payload=payload)
        response_text = raw_response.get("response", "")
        done = bool(raw_response.get("done", False))
        message = "Model response generated. No tools were executed and no memory was updated."
    except HTTPError as error:
        response_text = ""
        done = False
        message = f"Ollama generation failed with HTTP {error.code}."
    except URLError:
        response_text = ""
        done = False
        message = "Ollama is not reachable. Run the health check before generating."
    except TimeoutError:
        response_text = ""
        done = False
        message = "Model generation timed out."
    except json.JSONDecodeError:
        response_text = ""
        done = False
        message = "Ollama returned a non-JSON generation response."

    result = ModelResponse(
        provider=config.provider_name,
        model=selected_model,
        prompt=prompt,
        response=response_text,
        done=done,
        message=message,
        audit_path=str(MODEL_AUDIT_PATH.relative_to(ROOT)),
    )
    write_model_audit(
        {
            "schema": "axis-local-os-model-runtime-v1",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "provider": result.provider,
            "model": result.model,
            "prompt_chars": len(prompt),
            "response_chars": len(response_text),
            "done": done,
            "message": message,
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
    lines = [
        "# Axis Local OS Model Response",
        "",
        f"Provider: {result.provider}",
        f"Model: {result.model}",
        f"Done: {'yes' if result.done else 'no'}",
        "",
        "## Governance",
        "",
        "This call is model-only. It did not run tools, change files, or update memory.",
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

    parser.set_defaults(command="health")
    args = parser.parse_args()

    if args.command == "prompt":
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
