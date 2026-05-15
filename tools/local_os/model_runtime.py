from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "config" / "local_model_runtime.json"
DEFAULT_TIMEOUT_SECONDS = 5


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


def fetch_json(url: str, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> dict[str, Any]:
    request = Request(url, headers={"Accept": "application/json"})
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


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Check Axis Local OS local model runtime health")
    parser.add_argument("--provider", default=None, help="Provider name from config/local_model_runtime.json")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    health = check_health(args.provider)
    if args.json:
        print(json.dumps(health.__dict__, indent=2, ensure_ascii=True))
    else:
        print(render_health(health))


if __name__ == "__main__":
    main()

