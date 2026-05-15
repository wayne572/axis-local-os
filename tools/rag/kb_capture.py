from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CAPTURE_DIR = ROOT / "business" / "KNOWLEDGE_CAPTURE"


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug[:80] or "captured-note"


def build_note(title: str, source: str, tags: str, confidence: str, body: str) -> str:
    captured_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""# {title}

Status: captured
Date captured: {captured_at}
Source: {source}
Tags: {tags}
Confidence: {confidence}

## Summary

{body}

## Follow-Up Needed

- Review whether this should become permanent business knowledge.
- Confirm whether any client-sensitive details need redaction before wider use.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Capture a note into the Axis Knowledge Base")
    parser.add_argument("title", help="Short title for the captured knowledge")
    parser.add_argument("body", help="Information to remember")
    parser.add_argument("--source", default="manual capture", help="Where this information came from")
    parser.add_argument("--tags", default="knowledge", help="Comma-separated tags")
    parser.add_argument(
        "--confidence",
        default="needs review",
        choices=["confirmed", "needs review", "draft", "external claim"],
        help="Confidence level",
    )
    args = parser.parse_args()

    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    date_prefix = datetime.now().strftime("%Y-%m-%d")
    path = CAPTURE_DIR / f"{date_prefix}_{slugify(args.title)}.md"
    path.write_text(
        build_note(args.title, args.source, args.tags, args.confidence, args.body),
        encoding="utf-8",
    )
    print(f"Captured knowledge note: {path}")
    print("Next: run python tools/rag/kb_ingest.py")


if __name__ == "__main__":
    main()

