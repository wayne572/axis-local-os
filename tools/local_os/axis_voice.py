from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def render_status() -> str:
    return """# Axis Voice Intake

Status: spec ready, transcription engine not installed yet.

Safe workflow:

voice -> transcript -> review -> route -> draft/answer/proposed action -> approval

Recommended next implementation:

1. Install faster-whisper dependencies.
2. Add file transcription first.
3. Show transcript for review.
4. Route transcript through Axis modules.
5. Add microphone capture later.

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


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Axis Local OS voice intake")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("status", help="Show voice intake readiness")

    for command in ["transcribe", "route", "ask", "capture-draft"]:
        command_parser = subparsers.add_parser(command, help=f"Planned voice {command} command")
        command_parser.add_argument("audio_path", help="Path to a local audio file")

    parser.set_defaults(command="status")
    args = parser.parse_args()

    if args.command == "status":
        print(render_status())
    else:
        print(render_not_implemented(args.command, getattr(args, "audio_path", None)))


if __name__ == "__main__":
    main()

