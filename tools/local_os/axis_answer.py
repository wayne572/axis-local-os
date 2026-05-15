from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "local_os"))

from model_runtime import DEFAULT_GENERATE_TIMEOUT_SECONDS, generate_grounded  # noqa: E402


def compact_answer(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text.strip())


def render_answer(result) -> str:
    source_ids = result.source_ids or []
    lines = [
        "# Axis Answer",
        "",
        compact_answer(result.response or result.message),
        "",
        "## Sources",
    ]
    if source_ids:
        lines.extend(f"- `{source_id}`" for source_id in source_ids)
    else:
        lines.append("- No retrieved sources")
    lines.extend(
        [
            "",
            "## Runtime",
            "",
            f"Model: {result.model}",
            f"Provider: {result.provider}",
            f"Audit: {result.audit_path}",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Ask Axis Local OS with retrieved sources")
    parser.add_argument("question", help="Question to answer from local Axis context")
    parser.add_argument("--model", default="gemma4:latest", help="Local Ollama model to use")
    parser.add_argument("--provider", default=None, help="Provider name from config/local_model_runtime.json")
    parser.add_argument("--limit", type=int, default=3, help="Number of KB chunks to inject")
    parser.add_argument("--timeout", type=int, default=DEFAULT_GENERATE_TIMEOUT_SECONDS)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    result = generate_grounded(
        question=args.question,
        provider_name=args.provider,
        model=args.model,
        limit=args.limit,
        timeout=args.timeout,
    )
    if args.json:
        print(json.dumps(asdict(result), indent=2, ensure_ascii=True))
    else:
        print(render_answer(result))


if __name__ == "__main__":
    main()

