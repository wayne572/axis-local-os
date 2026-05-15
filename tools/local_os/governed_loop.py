from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
AUDIT_DIR = ROOT / ".axis" / "audit"
AUDIT_PATH = AUDIT_DIR / "governed_loop.jsonl"
MEMORY_REVIEW_DIR = ROOT / ".axis" / "memory_review"
STALE_AFTER_DAYS = 90

sys.path.insert(0, str(ROOT / "tools" / "rag"))
from kb_search import search  # noqa: E402


EXECUTION_TERMS = {
    "run",
    "execute",
    "install",
    "delete",
    "remove",
    "write",
    "edit",
    "modify",
    "move",
    "rename",
    "commit",
    "push",
    "deploy",
    "migrate",
    "send",
    "archive",
}

DESTRUCTIVE_TERMS = {
    "delete",
    "remove",
    "reset",
    "wipe",
    "drop",
    "destroy",
    "purge",
    "overwrite",
    "force",
}

MEMORY_TERMS = {
    "remember",
    "capture",
    "save this",
    "log this",
    "add to memory",
    "knowledge",
    "decision",
}


@dataclass
class SourceContext:
    source_id: str
    source_path: str
    title: str
    chunk_index: int
    modified_at: str
    stale: bool
    score: float
    preview: str


@dataclass
class GovernedResult:
    schema: str
    timestamp: str
    request: str
    task_type: str
    approval_level: str
    status: str
    proposed_action: str
    sources: list[SourceContext]
    stale_source_count: int
    memory_proposal_path: str | None
    audit_path: str


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def compact(text: str, max_chars: int = 420) -> str:
    value = re.sub(r"\s+", " ", text).strip()
    if len(value) <= max_chars:
        return value
    return value[: max_chars - 3].rstrip() + "..."


def parse_timestamp(value: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed


def is_stale(modified_at: str) -> bool:
    parsed = parse_timestamp(modified_at)
    if parsed is None:
        return True
    return (now_utc() - parsed).days > STALE_AFTER_DAYS


def classify_request(request: str) -> tuple[str, str]:
    lower = request.lower()
    words = set(re.findall(r"[a-zA-Z0-9_-]+", lower))

    if any(term in lower for term in MEMORY_TERMS):
        task_type = "memory_update"
        approval_level = "review"
    elif words & DESTRUCTIVE_TERMS:
        task_type = "destructive_execution"
        approval_level = "approval"
    elif words & EXECUTION_TERMS:
        task_type = "execution_or_file_change"
        approval_level = "approval"
    elif any(term in lower for term in ["what", "summarise", "summarize", "explain", "review"]):
        task_type = "retrieval_answer"
        approval_level = "none"
    else:
        task_type = "planning"
        approval_level = "review"

    return task_type, approval_level


def build_sources(request: str, limit: int) -> list[SourceContext]:
    results = search(request, limit)
    sources: list[SourceContext] = []
    for score, chunk in results:
        modified_at = chunk.get("modified_at", "")
        source_id = chunk.get("id") or f"{chunk.get('source_path')}::chunk-{chunk.get('chunk_index')}"
        sources.append(
            SourceContext(
                source_id=source_id,
                source_path=chunk.get("source_path", "unknown"),
                title=chunk.get("title", "Untitled"),
                chunk_index=int(chunk.get("chunk_index", 0)),
                modified_at=modified_at,
                stale=is_stale(modified_at),
                score=round(float(score), 4),
                preview=compact(chunk.get("text", "")),
            )
        )
    return sources


def proposed_action_for(request: str, task_type: str, approval_level: str, sources: list[SourceContext]) -> str:
    if not sources:
        return (
            "No source-backed context was retrieved. Treat this as a fresh request, "
            "ask for source material if project memory is required, and avoid claiming prior Axis history."
        )
    if approval_level == "approval":
        return (
            "Prepare a concrete execution plan with cited context, then request explicit human approval "
            "before running commands, changing files, calling external services, or mutating git/database state."
        )
    if task_type == "memory_update":
        return (
            "Create a memory-review draft only. Do not promote it into permanent Axis memory until Wayne reviews it."
        )
    return (
        "Answer or plan using the retrieved sources below. Cite source IDs for project-memory claims "
        "and flag any stale context before relying on it."
    )


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug[:70] or "memory-proposal"


def maybe_create_memory_proposal(request: str, sources: list[SourceContext], enabled: bool) -> str | None:
    if not enabled:
        return None

    MEMORY_REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = now_utc().strftime("%Y%m%dT%H%M%SZ")
    path = MEMORY_REVIEW_DIR / f"{timestamp}_{slugify(request)}.md"
    source_lines = "\n".join(f"- `{source.source_id}`" for source in sources) or "- No retrieved source"
    content = f"""# Memory Review Draft

Status: needs human review
Created: {now_utc().isoformat()}
Source: Axis Local OS governed loop

## Proposed Memory

{request}

## Retrieved Sources

{source_lines}

## Review Checklist

- Confirm this is true and useful.
- Redact sensitive client or personal details if needed.
- Move into `business/KNOWLEDGE_CAPTURE/` only after review.
- Rebuild the KB with `python tools/rag/kb_ingest.py` after approval.
"""
    path.write_text(content, encoding="utf-8")
    return str(path.relative_to(ROOT))


def write_audit_event(result: GovernedResult) -> None:
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    payload: dict[str, Any] = asdict(result)
    payload["sources"] = [asdict(source) for source in result.sources]
    with AUDIT_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def render_text(result: GovernedResult) -> str:
    lines = [
        "# Axis Local OS Governed Loop",
        "",
        f"Request: {result.request}",
        f"Task type: {result.task_type}",
        f"Approval level: {result.approval_level}",
        f"Status: {result.status}",
        f"Stale sources: {result.stale_source_count}",
        "",
        "## Proposed Action",
        "",
        result.proposed_action,
        "",
        "## Retrieved Sources",
    ]
    if not result.sources:
        lines.append("")
        lines.append("No matching source-backed context found.")
    else:
        for index, source in enumerate(result.sources, start=1):
            stale_label = "stale" if source.stale else "current"
            lines.extend(
                [
                    "",
                    f"{index}. `{source.source_id}`",
                    f"   Path: {source.source_path}",
                    f"   Title: {source.title}",
                    f"   Modified: {source.modified_at} ({stale_label})",
                    f"   Preview: {source.preview}",
                ]
            )
    if result.memory_proposal_path:
        lines.extend(["", "## Memory Review Draft", "", result.memory_proposal_path])
    lines.extend(["", "## Audit", "", result.audit_path])
    return "\n".join(lines)


def run_governed_loop(request: str, limit: int, approved: bool, propose_memory: bool) -> GovernedResult:
    task_type, approval_level = classify_request(request)
    sources = build_sources(request, limit)
    if approval_level == "approval":
        status = "approved" if approved else "blocked_pending_review"
    elif approval_level == "review":
        status = "ready_for_review"
    else:
        status = "ready"
    proposed_action = proposed_action_for(request, task_type, approval_level, sources)
    memory_proposal_path = maybe_create_memory_proposal(request, sources, propose_memory)
    result = GovernedResult(
        schema="axis-local-os-governed-loop-v1",
        timestamp=now_utc().isoformat(),
        request=request,
        task_type=task_type,
        approval_level=approval_level,
        status=status,
        proposed_action=proposed_action,
        sources=sources,
        stale_source_count=sum(1 for source in sources if source.stale),
        memory_proposal_path=memory_proposal_path,
        audit_path=str(AUDIT_PATH.relative_to(ROOT)),
    )
    write_audit_event(result)
    return result


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Run the Axis Local OS governed assistant loop")
    parser.add_argument("request", help="User request to classify, retrieve context for, and audit")
    parser.add_argument("--limit", type=int, default=5, help="Number of source chunks to retrieve")
    parser.add_argument("--approved", action="store_true", help="Mark approval-required work as approved")
    parser.add_argument(
        "--propose-memory",
        action="store_true",
        help="Create a review-only memory proposal under .axis/memory_review",
    )
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    result = run_governed_loop(args.request, args.limit, args.approved, args.propose_memory)
    if args.json:
        payload = asdict(result)
        payload["sources"] = [asdict(source) for source in result.sources]
        print(json.dumps(payload, indent=2, ensure_ascii=True))
    else:
        print(render_text(result))


if __name__ == "__main__":
    main()
