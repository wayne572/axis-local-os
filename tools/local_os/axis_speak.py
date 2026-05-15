from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "config" / "voice_reply.json"
AUDIT_DIR = ROOT / ".axis" / "audit"
AUDIT_PATH = AUDIT_DIR / "voice_reply.jsonl"
DEFAULT_TIMEOUT_SECONDS = 30


@dataclass
class VoiceReplyConfig:
    enabled: bool
    default_provider: str
    fallback_provider: str
    output_dir: Path
    providers: dict[str, dict[str, Any]]


def load_config() -> VoiceReplyConfig:
    if not CONFIG_PATH.exists():
        raise SystemExit(f"Voice reply config not found: {CONFIG_PATH}")
    raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return VoiceReplyConfig(
        enabled=bool(raw.get("enabled", False)),
        default_provider=raw.get("default_provider", "kokoro_fastapi"),
        fallback_provider=raw.get("fallback_provider", "piper"),
        output_dir=ROOT / raw.get("output_dir", ".axis/voice_reply"),
        providers=raw.get("providers", {}),
    )


def write_audit(event: dict[str, Any]) -> None:
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    with AUDIT_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=True) + "\n")


def provider_status(config: VoiceReplyConfig, provider_name: str | None = None) -> str:
    selected = provider_name or config.default_provider
    provider = config.providers.get(selected)
    if not provider:
        available = ", ".join(sorted(config.providers)) or "none"
        raise SystemExit(f"Unknown voice provider '{selected}'. Available providers: {available}")

    lines = [
        "# Axis Voice Reply Status",
        "",
        f"Enabled: {'yes' if config.enabled else 'no'}",
        f"Default provider: {config.default_provider}",
        f"Fallback provider: {config.fallback_provider}",
        f"Selected provider: {selected}",
        f"Provider type: {provider.get('type')}",
        f"Output dir: {config.output_dir.relative_to(ROOT)}",
    ]

    if provider.get("type") == "openai_compatible_speech":
        base_url = provider.get("base_url", "").rstrip("/")
        endpoint = provider.get("speech_endpoint", "/v1/audio/speech")
        lines.extend(["", f"Kokoro-style endpoint: {base_url}{endpoint}"])
        lines.append("Runtime check: use `say` after enabling and starting the local TTS server.")
    elif provider.get("type") == "piper_cli":
        lines.extend(["", f"Piper command: {provider.get('command', 'piper')}"])
        lines.append("Runtime check: planned fallback, not implemented yet.")

    if not config.enabled:
        lines.extend(
            [
                "",
                "Voice reply is configured but disabled.",
                "Set `enabled` to true in config/voice_reply.json after a local TTS provider is running.",
            ]
        )
    return "\n".join(lines)


def synthesize_openai_compatible(
    text: str,
    config: VoiceReplyConfig,
    provider_name: str,
    timeout: int,
) -> Path:
    provider = config.providers[provider_name]
    base_url = provider["base_url"].rstrip("/")
    endpoint = provider.get("speech_endpoint", "/v1/audio/speech")
    output_format = provider.get("response_format", "wav")
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output_path = config.output_dir / f"{timestamp}_{provider_name}.{output_format}"
    payload = {
        "model": provider.get("model", "kokoro"),
        "voice": provider.get("voice", "af_heart"),
        "input": text,
        "response_format": output_format,
    }

    request = Request(
        f"{base_url}{endpoint}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Accept": "audio/*"},
    )
    config.output_dir.mkdir(parents=True, exist_ok=True)
    with urlopen(request, timeout=timeout) as response:
        output_path.write_bytes(response.read())
    return output_path


def say(text: str, provider_name: str | None = None, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> str:
    config = load_config()
    selected = provider_name or config.default_provider
    provider = config.providers.get(selected)
    if not provider:
        available = ", ".join(sorted(config.providers)) or "none"
        raise SystemExit(f"Unknown voice provider '{selected}'. Available providers: {available}")

    if not config.enabled:
        return """# Axis Voice Reply

Voice reply is configured but disabled.

No audio was generated.

Next:
1. Start a local Kokoro-FastAPI-compatible TTS server.
2. Set `enabled` to true in config/voice_reply.json.
3. Retry this command.
"""

    if provider.get("type") != "openai_compatible_speech":
        return f"# Axis Voice Reply\n\nProvider `{selected}` is configured but not implemented yet."

    try:
        output_path = synthesize_openai_compatible(text, config, selected, timeout)
        message = f"Audio generated: {output_path.relative_to(ROOT)}"
        success = True
    except HTTPError as error:
        output_path = None
        message = f"TTS provider returned HTTP {error.code}."
        success = False
    except URLError:
        output_path = None
        message = "TTS provider is not reachable. Start the local Kokoro-FastAPI server and retry."
        success = False
    except TimeoutError:
        output_path = None
        message = "TTS request timed out."
        success = False

    write_audit(
        {
            "schema": "axis-local-os-voice-reply-v1",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "provider": selected,
            "text_chars": len(text),
            "success": success,
            "output_path": str(output_path.relative_to(ROOT)) if output_path else None,
            "message": message,
        }
    )
    return "\n".join(["# Axis Voice Reply", "", message, "", f"Audit: {AUDIT_PATH.relative_to(ROOT)}"])


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Axis Local OS voice reply")
    subparsers = parser.add_subparsers(dest="command")

    status_parser = subparsers.add_parser("status", help="Show voice reply status")
    status_parser.add_argument("--provider", default=None)

    say_parser = subparsers.add_parser("say", help="Generate speech from text")
    say_parser.add_argument("text", help="Text to speak")
    say_parser.add_argument("--provider", default=None)
    say_parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)

    parser.set_defaults(command="status")
    args = parser.parse_args()

    if args.command == "say":
        print(say(args.text, args.provider, args.timeout))
    else:
        print(provider_status(load_config(), args.provider))


if __name__ == "__main__":
    main()

