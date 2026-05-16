from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "config" / "voice_intake.json"
AUDIT_DIR = ROOT / ".axis" / "audit"
AUDIT_PATH = AUDIT_DIR / "voice_intake.jsonl"

sys.path.insert(0, str(ROOT / "tools" / "local_os"))
from axis_modules import load_registry, route_module  # noqa: E402
from axis_answer import render_answer  # noqa: E402
from model_runtime import DEFAULT_GENERATE_TIMEOUT_SECONDS, generate_grounded  # noqa: E402


@dataclass
class VoiceIntakeConfig:
    enabled: bool
    engine: str
    model_size: str
    device: str
    compute_type: str
    beam_size: int
    allowed_extensions: list[str]


@dataclass
class VoiceTranscript:
    schema: str
    timestamp: str
    source_audio: str
    engine: str
    model_size: str
    language: str | None
    language_probability: float | None
    duration_seconds: float | None
    transcript: str
    raw_transcript: str | None
    transcript_corrected: bool
    uncertainty_notes: list[str]
    proposed_route: str
    proposed_next_action: str
    confirmation_required: bool
    audit_path: str


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def load_config() -> VoiceIntakeConfig:
    if not CONFIG_PATH.exists():
        raise SystemExit(f"Voice intake config not found: {CONFIG_PATH}")
    raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return VoiceIntakeConfig(
        enabled=bool(raw.get("enabled", True)),
        engine=raw.get("engine", "faster-whisper"),
        model_size=raw.get("model_size", "base"),
        device=raw.get("device", "cpu"),
        compute_type=raw.get("compute_type", "int8"),
        beam_size=int(raw.get("beam_size", 5)),
        allowed_extensions=list(raw.get("allowed_extensions", [".wav", ".mp3", ".m4a", ".flac", ".ogg"])),
    )


def faster_whisper_available() -> bool:
    return importlib.util.find_spec("faster_whisper") is not None


def write_audit(event: dict[str, Any]) -> None:
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    with AUDIT_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=True) + "\n")


def validate_audio_path(audio_path: str, config: VoiceIntakeConfig) -> Path:
    path = Path(audio_path).expanduser()
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    if not path.exists():
        raise SystemExit(f"Audio file not found: {path}")
    if not path.is_file():
        raise SystemExit(f"Audio path is not a file: {path}")
    if path.suffix.lower() not in {suffix.lower() for suffix in config.allowed_extensions}:
        allowed = ", ".join(config.allowed_extensions)
        raise SystemExit(f"Unsupported audio file type '{path.suffix}'. Allowed: {allowed}")
    return path


def relative_or_absolute(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def render_status() -> str:
    config = load_config()
    dependency = "available" if faster_whisper_available() else "not installed"
    enabled = "yes" if config.enabled else "no"
    return f"""# Axis Voice Intake

Status: file transcription configured.

Enabled: {enabled}
Engine: {config.engine}
Model size: {config.model_size}
Device: {config.device}
Compute type: {config.compute_type}
Dependency: faster-whisper {dependency}

Safe workflow:

voice -> transcript -> review -> route -> draft/answer/proposed action -> approval

Commands:

python tools/local_os/axis_voice.py transcribe path/to/audio.wav
python tools/local_os/axis_voice.py route path/to/audio.wav
python tools/local_os/axis_voice.py ask path/to/audio.wav --confirm-transcript
python tools/local_os/axis_voice.py ask path/to/audio.wav --transcript "Corrected transcript" --confirm-transcript

Governance:

- No command execution directly from voice.
- No message sending directly from voice.
- No permanent memory update directly from voice.
- Human review stays in the loop.
"""


def render_not_implemented(command: str, audio_path: str | None) -> str:
    source = f"\nRequested audio file: {audio_path}\n" if audio_path else ""
    return f"""# Axis Voice Intake

Command requested: {command}
{source}
This command is planned but not implemented yet.

Next safe build step:

Add local file transcription using faster-whisper, then print a transcript for review before any routing or action.
"""


def dependency_error(config: VoiceIntakeConfig, audio_path: str) -> str:
    write_audit(
        {
            "schema": "axis-local-os-voice-intake-v1",
            "timestamp": now_utc().isoformat(),
            "command": "transcribe",
            "source_audio": audio_path,
            "engine": config.engine,
            "status": "blocked_missing_dependency",
            "message": "faster-whisper is not installed.",
        }
    )
    return """# Axis Voice Intake

Status: blocked

`faster-whisper` is not installed in this Python environment, so no transcription was attempted.

Install step for review:

```powershell
python -m pip install faster-whisper
```

After install:

```powershell
python tools/local_os/axis_voice.py transcribe path/to/audio.wav
```

Audit: .axis/audit/voice_intake.jsonl
"""


def transcribe_audio(audio_path: str, transcript_override: str | None = None) -> VoiceTranscript:
    config = load_config()
    if not config.enabled:
        raise SystemExit("Voice intake is disabled in config/voice_intake.json")
    if config.engine != "faster-whisper":
        raise SystemExit(f"Unsupported voice intake engine: {config.engine}")

    path = validate_audio_path(audio_path, config)
    if not faster_whisper_available():
        raise SystemExit(dependency_error(config, relative_or_absolute(path)))

    from faster_whisper import WhisperModel  # noqa: WPS433

    model = WhisperModel(config.model_size, device=config.device, compute_type=config.compute_type)
    segments, info = model.transcribe(str(path), beam_size=config.beam_size)
    segment_list = list(segments)
    raw_transcript = " ".join(segment.text.strip() for segment in segment_list).strip()
    transcript = transcript_override.strip() if transcript_override else raw_transcript
    uncertainty_notes: list[str] = []
    if not raw_transcript:
        uncertainty_notes.append("No transcript text was detected.")
    if transcript_override:
        uncertainty_notes.append("Transcript was manually corrected before routing or asking.")
    if any(getattr(segment, "no_speech_prob", 0.0) > 0.6 for segment in segment_list):
        uncertainty_notes.append("Some segments may contain silence or unclear speech.")
    if any(getattr(segment, "avg_logprob", 0.0) < -1.0 for segment in segment_list):
        uncertainty_notes.append("Some segments had low confidence and should be reviewed carefully.")

    route = route_module(load_registry(), transcript) if transcript else "No route proposed because transcript is empty."
    result = VoiceTranscript(
        schema="axis-local-os-voice-intake-v1",
        timestamp=now_utc().isoformat(),
        source_audio=relative_or_absolute(path),
        engine=config.engine,
        model_size=config.model_size,
        language=getattr(info, "language", None),
        language_probability=round(float(getattr(info, "language_probability", 0.0)), 4)
        if getattr(info, "language_probability", None) is not None
        else None,
        duration_seconds=round(float(getattr(info, "duration", 0.0)), 2)
        if getattr(info, "duration", None) is not None
        else None,
        transcript=transcript,
        raw_transcript=raw_transcript if transcript_override else None,
        transcript_corrected=bool(transcript_override),
        uncertainty_notes=uncertainty_notes,
        proposed_route=route,
        proposed_next_action=(
            "Review the transcript. If it is accurate, copy the text into the intended Axis command "
            "or run the next governed step explicitly."
        ),
        confirmation_required=True,
        audit_path=str(AUDIT_PATH.relative_to(ROOT)),
    )
    write_audit(asdict(result) | {"status": "transcribed"})
    return result


def render_transcript(result: VoiceTranscript) -> str:
    notes = result.uncertainty_notes or ["No uncertainty notes reported by the transcription wrapper."]
    lines = [
        "# Axis Voice Transcript",
        "",
        f"Source audio: {result.source_audio}",
        f"Engine: {result.engine}",
        f"Model size: {result.model_size}",
        f"Timestamp: {result.timestamp}",
        f"Language: {result.language or 'unknown'}",
        f"Duration seconds: {result.duration_seconds if result.duration_seconds is not None else 'unknown'}",
        "",
        "## Transcript",
        "",
        result.transcript or "[No transcript text detected.]",
        "",
    ]
    if result.transcript_corrected and result.raw_transcript is not None:
        lines.extend(
            [
                "## Raw Transcript",
                "",
                result.raw_transcript or "[No raw transcript text detected.]",
                "",
            ]
        )
    lines.extend(["## Uncertainty Notes", ""])
    lines.extend(f"- {note}" for note in notes)
    lines.extend(
        [
            "",
            "## Proposed Route",
            "",
            result.proposed_route,
            "",
            "## Proposed Next Action",
            "",
            result.proposed_next_action,
            "",
            "Confirmation required: yes",
            "",
            "## Audit",
            "",
            result.audit_path,
        ]
    )
    return "\n".join(lines)


def render_ask_blocked(result: VoiceTranscript) -> str:
    return "\n".join(
        [
            render_transcript(result),
            "",
            "## Voice Ask",
            "",
            "Status: blocked pending transcript review",
            "",
            "No model answer was generated.",
            "",
            "Review the transcript above. If it is accurate, rerun with `--confirm-transcript`.",
        ]
    )


def ask_from_audio(
    audio_path: str,
    confirm_transcript: bool,
    transcript_override: str | None,
    model: str,
    provider: str | None,
    limit: int,
    timeout: int,
):
    transcript = transcribe_audio(audio_path, transcript_override)
    if not confirm_transcript:
        write_audit(
            {
                "schema": "axis-local-os-voice-intake-v1",
                "timestamp": now_utc().isoformat(),
                "command": "ask",
                "source_audio": transcript.source_audio,
                "status": "blocked_pending_transcript_review",
                "transcript_chars": len(transcript.transcript),
                "transcript_corrected": transcript.transcript_corrected,
                "confirmation_required": True,
            }
        )
        return transcript, None

    answer = generate_grounded(
        question=transcript.transcript,
        provider_name=provider,
        model=model,
        limit=limit,
        timeout=timeout,
    )
    write_audit(
        {
            "schema": "axis-local-os-voice-intake-v1",
            "timestamp": now_utc().isoformat(),
            "command": "ask",
            "source_audio": transcript.source_audio,
            "status": "answered_after_transcript_confirmation",
            "transcript_chars": len(transcript.transcript),
            "transcript_corrected": transcript.transcript_corrected,
            "raw_transcript": transcript.raw_transcript,
            "model": answer.model,
            "provider": answer.provider,
            "answer_audit_path": answer.audit_path,
            "source_ids": answer.source_ids,
            "confirmation_required": False,
        }
    )
    return transcript, answer


def render_voice_ask(transcript: VoiceTranscript, answer) -> str:
    if answer is None:
        return render_ask_blocked(transcript)
    return "\n".join(
        [
            render_transcript(transcript),
            "",
            "## Confirmed Voice Ask",
            "",
            "Transcript was explicitly confirmed with `--confirm-transcript`.",
            "A corrected transcript was used." if transcript.transcript_corrected else "The raw transcript was used.",
            "",
            render_answer(answer),
        ]
    )


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Axis Local OS voice intake")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("status", help="Show voice intake readiness")

    command_help = {
        "transcribe": "Transcribe a local audio file for review",
        "route": "Transcribe a local audio file and propose a module route",
        "ask": "Transcribe a local audio file and optionally ask Axis after explicit confirmation",
        "capture-draft": "Planned voice capture draft command",
    }
    for command in ["transcribe", "route", "ask", "capture-draft"]:
        command_parser = subparsers.add_parser(command, help=command_help[command])
        command_parser.add_argument("audio_path", help="Path to a local audio file")
        command_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
        command_parser.add_argument(
            "--transcript",
            default=None,
            help="Manual transcript correction to use for routing or asking after audio transcription",
        )
        if command == "ask":
            command_parser.add_argument(
                "--confirm-transcript",
                action="store_true",
                help="Confirm the displayed transcript is accurate enough to send to Axis Answer",
            )
            command_parser.add_argument("--model", default="gemma4:latest", help="Local Ollama model to use")
            command_parser.add_argument(
                "--provider",
                default=None,
                help="Provider name from config/local_model_runtime.json",
            )
            command_parser.add_argument("--limit", type=int, default=3, help="Number of KB chunks to inject")
            command_parser.add_argument("--timeout", type=int, default=DEFAULT_GENERATE_TIMEOUT_SECONDS)

    parser.set_defaults(command="status")
    args = parser.parse_args()

    if args.command == "status":
        print(render_status())
    elif args.command in {"transcribe", "route"}:
        result = transcribe_audio(args.audio_path, args.transcript)
        if args.json:
            print(json.dumps(asdict(result), indent=2, ensure_ascii=True))
        else:
            print(render_transcript(result))
    elif args.command == "ask":
        transcript, answer = ask_from_audio(
            audio_path=args.audio_path,
            confirm_transcript=args.confirm_transcript,
            transcript_override=args.transcript,
            model=args.model,
            provider=args.provider,
            limit=args.limit,
            timeout=args.timeout,
        )
        if args.json:
            payload = {
                "transcript": asdict(transcript),
                "answer": asdict(answer) if answer else None,
                "status": "answered" if answer else "blocked_pending_transcript_review",
            }
            print(json.dumps(payload, indent=2, ensure_ascii=True))
        else:
            print(render_voice_ask(transcript, answer))
    else:
        print(render_not_implemented(args.command, getattr(args, "audio_path", None)))


if __name__ == "__main__":
    main()
