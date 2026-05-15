from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import shlex
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
AUDIT_DIR = ROOT / ".axis" / "audit"
AUDIT_PATH = AUDIT_DIR / "coding_agent.jsonl"


READ_ONLY_ALLOWLIST = {
    "ls",
    "pwd",
    "whoami",
    "hostname",
    "cat",
    "head",
    "tail",
    "wc",
    "echo",
}

READ_ONLY_GIT_SUBCOMMANDS = {
    "status",
    "log",
    "diff",
    "branch",
    "show",
    "remote",
    "config",
    "rev-parse",
    "describe",
    "ls-files",
}

VERSION_CHECK_FLAGS = {"--version", "-V"}

MUTATING_COMMANDS = {
    "pip",
    "pip3",
    "npm",
    "yarn",
    "pnpm",
    "pipx",
    "poetry",
    "uv",
    "cargo",
    "go",
}

EXTERNAL_GIT_SUBCOMMANDS = {"push", "fetch", "pull", "clone"}

DESTRUCTIVE_TOKENS = {
    "rm",
    "rmdir",
    "del",
    "shutdown",
    "reboot",
}

DESTRUCTIVE_PHRASES = [
    "git push --force",
    "git push -f",
    "git reset --hard",
    "git clean -fd",
    "git clean -f",
    "remove-item -recurse",
    "rm -rf",
]

BLOCKED_FLAGS = {"--no-verify", "--no-gpg-sign"}

PIPE_TO_SHELL_PATTERNS = [
    re.compile(r"curl[^|]*\|\s*(sh|bash|zsh|powershell|pwsh|cmd)", re.IGNORECASE),
    re.compile(r"iwr[^|]*\|\s*iex", re.IGNORECASE),
    re.compile(r"wget[^|]*\|\s*(sh|bash|zsh)", re.IGNORECASE),
]


@dataclass
class PreviewResult:
    schema: str
    timestamp: str
    command: str
    working_dir: str
    workspace_root: str
    approval_level: str
    classification: str
    allowlist_match: bool
    blocklist_match: bool
    blocked_reasons: list[str]
    notes: list[str]
    executed: bool
    audit_path: str


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def tokenize(command: str) -> list[str]:
    try:
        return shlex.split(command, posix=True)
    except ValueError:
        return command.split()


def matches_pipe_to_shell(command: str) -> bool:
    return any(pattern.search(command) for pattern in PIPE_TO_SHELL_PATTERNS)


def classify_command(command: str) -> tuple[str, str, bool, bool, list[str], list[str]]:
    """Return (classification, approval_level, allowlist_match, blocklist_match, blocked_reasons, notes)."""

    lower = command.lower()
    tokens = tokenize(command)
    head = tokens[0] if tokens else ""
    blocked_reasons: list[str] = []
    notes: list[str] = []

    # Blocklist checks first - destructive intent always halts.
    if matches_pipe_to_shell(command):
        blocked_reasons.append("pipe-to-shell pattern (curl|sh, iwr|iex, etc.)")
    for phrase in DESTRUCTIVE_PHRASES:
        if phrase in lower:
            blocked_reasons.append(f"destructive phrase: {phrase}")
    if head in DESTRUCTIVE_TOKENS:
        blocked_reasons.append(f"destructive command: {head}")
    for flag in BLOCKED_FLAGS:
        if flag in tokens:
            blocked_reasons.append(f"blocked flag: {flag}")

    if blocked_reasons:
        return "destructive_or_blocked", "approval+confirm", False, True, blocked_reasons, notes

    # Empty / unparseable
    if not head:
        return "unclassified", "approval", False, False, blocked_reasons, ["empty command"]

    # Read-only allowlist
    if head in READ_ONLY_ALLOWLIST:
        return "read_only", "none", True, False, blocked_reasons, notes

    # Version checks: any binary with --version is read-only
    if len(tokens) >= 2 and tokens[1] in VERSION_CHECK_FLAGS:
        return "read_only", "none", True, False, blocked_reasons, [f"version check on {head}"]

    # Git subcommands split read-only / external / mutating
    if head == "git":
        sub = tokens[1] if len(tokens) > 1 else ""
        if sub in READ_ONLY_GIT_SUBCOMMANDS:
            return "read_only_git", "none", True, False, blocked_reasons, [f"git {sub}"]
        if sub in EXTERNAL_GIT_SUBCOMMANDS:
            return "external_git", "approval", False, False, blocked_reasons, [f"git {sub} reaches a remote"]
        notes.append(f"git {sub} mutates local repo state")
        return "mutating_git", "approval", False, False, blocked_reasons, notes

    # Package managers / installers - always approval level
    if head in MUTATING_COMMANDS:
        notes.append(f"{head} can install or mutate dependencies")
        return "mutating_install", "approval", False, False, blocked_reasons, notes

    # python / node script invocations - workspace mutating by default
    if head in {"python", "python3", "node", "powershell", "pwsh", "bash", "sh"}:
        notes.append(f"{head} executes a script that may mutate state")
        return "script_execution", "approval", False, False, blocked_reasons, notes

    # Unknown - conservative default
    notes.append("command not classified - default to approval")
    return "unclassified", "approval", False, False, blocked_reasons, notes


def write_audit_event(result: Any) -> None:
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    with AUDIT_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(asdict(result), ensure_ascii=True) + "\n")


@dataclass
class EditPreviewResult:
    schema: str
    timestamp: str
    target_path: str
    workspace_root: str
    in_workspace: bool
    out_of_scope_acknowledged: bool
    target_exists: bool
    target_is_binary: bool
    old_sha256: str | None
    new_sha256: str
    diff_hash: str
    lines_added: int
    lines_removed: int
    approval_level: str
    classification: str
    blocked_reasons: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    diff_preview: str = ""
    written: bool = False
    audit_path: str = ""


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def looks_binary(data: bytes) -> bool:
    if b"\x00" in data:
        return True
    sample = data[:8192]
    if not sample:
        return False
    text_bytes = sample.translate(None, bytes(range(32, 127)) + b"\n\r\t\b\f")
    return (len(text_bytes) / max(1, len(sample))) > 0.30


def read_text_file(path: Path) -> tuple[str, bool]:
    raw = path.read_bytes()
    if looks_binary(raw):
        return "", True
    return raw.decode("utf-8", errors="replace"), False


def is_within_workspace(target: Path) -> bool:
    try:
        target.resolve().relative_to(ROOT)
        return True
    except ValueError:
        return False


def edit_preview(target: Path, new_content: str, out_of_scope: bool) -> EditPreviewResult:
    target_resolved = target.resolve()
    in_workspace = is_within_workspace(target_resolved)
    blocked: list[str] = []
    notes: list[str] = []

    target_exists = target_resolved.exists() and target_resolved.is_file()
    target_is_binary = False
    old_content = ""
    old_sha: str | None = None

    if target_exists:
        old_content, target_is_binary = read_text_file(target_resolved)
        old_sha = sha256_text(old_content) if not target_is_binary else None

    new_sha = sha256_text(new_content)

    if target_is_binary:
        blocked.append("target is binary - diff preview not supported")

    if not in_workspace and not out_of_scope:
        blocked.append("target path is outside workspace root and out-of-scope was not acknowledged")
    elif not in_workspace and out_of_scope:
        notes.append("out-of-scope write acknowledged - still requires approval")

    diff_lines: list[str] = []
    added = 0
    removed = 0
    if not target_is_binary:
        old_lines = old_content.splitlines(keepends=True) if target_exists else []
        new_lines = new_content.splitlines(keepends=True)
        relative_label = (
            str(target_resolved.relative_to(ROOT)) if in_workspace else str(target_resolved)
        )
        from_label = relative_label if target_exists else f"{relative_label} (new file)"
        diff_iter = difflib.unified_diff(
            old_lines,
            new_lines,
            fromfile=from_label,
            tofile=relative_label,
            n=3,
        )
        for line in diff_iter:
            diff_lines.append(line)
            if line.startswith("+") and not line.startswith("+++"):
                added += 1
            elif line.startswith("-") and not line.startswith("---"):
                removed += 1

    diff_preview = "".join(diff_lines)
    diff_hash = sha256_text(diff_preview) if diff_preview else sha256_text(new_sha)

    if blocked:
        approval_level = "approval+confirm" if any("binary" in r for r in blocked) else "approval"
        classification = "edit_blocked"
    elif not target_exists:
        approval_level = "review"
        classification = "edit_create"
        notes.append("target file does not exist - this would create a new file")
    elif old_content == new_content:
        approval_level = "none"
        classification = "edit_no_op"
        notes.append("new content is identical to current file - nothing to write")
    else:
        approval_level = "review"
        classification = "edit_modify"

    if not in_workspace and approval_level == "review":
        approval_level = "approval"
        notes.append("out-of-scope edits escalate from review to approval")

    result = EditPreviewResult(
        schema="axis-local-os-coding-agent-edit-preview-v1",
        timestamp=now_utc().isoformat(),
        target_path=str(target_resolved),
        workspace_root=str(ROOT),
        in_workspace=in_workspace,
        out_of_scope_acknowledged=out_of_scope,
        target_exists=target_exists,
        target_is_binary=target_is_binary,
        old_sha256=old_sha,
        new_sha256=new_sha,
        diff_hash=diff_hash,
        lines_added=added,
        lines_removed=removed,
        approval_level=approval_level,
        classification=classification,
        blocked_reasons=blocked,
        notes=notes,
        diff_preview=diff_preview,
        written=False,
        audit_path=str(AUDIT_PATH.relative_to(ROOT)),
    )
    write_audit_event(result)
    return result


def render_edit_text(result: EditPreviewResult) -> str:
    lines = [
        "# Axis Coding Agent - Edit Preview",
        "",
        f"Target: {result.target_path}",
        f"Workspace root: {result.workspace_root}",
        f"In workspace: {result.in_workspace}",
        f"Out-of-scope acknowledged: {result.out_of_scope_acknowledged}",
        f"Target exists: {result.target_exists}",
        f"Target is binary: {result.target_is_binary}",
        f"Classification: {result.classification}",
        f"Approval level: {result.approval_level}",
        f"Lines added: {result.lines_added}",
        f"Lines removed: {result.lines_removed}",
        f"Old sha256: {result.old_sha256 or 'n/a'}",
        f"New sha256: {result.new_sha256}",
        f"Diff hash: {result.diff_hash}",
        f"Written: {result.written}",
    ]
    if result.blocked_reasons:
        lines.extend(["", "## Blocked Reasons"])
        lines.extend(f"- {reason}" for reason in result.blocked_reasons)
    if result.notes:
        lines.extend(["", "## Notes"])
        lines.extend(f"- {note}" for note in result.notes)
    lines.extend(["", "## Diff", ""])
    if result.target_is_binary:
        lines.append("(binary file - no diff)")
    elif not result.diff_preview:
        lines.append("(no changes)")
    else:
        lines.append("```diff")
        lines.append(result.diff_preview.rstrip("\n"))
        lines.append("```")
    lines.extend(["", "## Decision", ""])
    if result.blocked_reasons:
        lines.append("HALT. Resolve blocked reasons before any write.")
    elif result.approval_level == "none":
        lines.append("No-op. Nothing to write.")
    elif result.approval_level == "review":
        lines.append("Diff shown. Single review-level approval required before write. Use `axis_code.py apply` once that exists.")
    else:
        lines.append("Approval-level edit. Diff must be confirmed in the same loop turn before any write.")
    lines.extend(["", "## Audit", "", result.audit_path])
    return "\n".join(lines)


def preview(command: str, working_dir: Path) -> PreviewResult:
    classification, approval_level, allow, block, reasons, notes = classify_command(command)
    result = PreviewResult(
        schema="axis-local-os-coding-agent-preview-v1",
        timestamp=now_utc().isoformat(),
        command=command,
        working_dir=str(working_dir),
        workspace_root=str(ROOT),
        approval_level=approval_level,
        classification=classification,
        allowlist_match=allow,
        blocklist_match=block,
        blocked_reasons=reasons,
        notes=notes,
        executed=False,
        audit_path=str(AUDIT_PATH.relative_to(ROOT)),
    )
    write_audit_event(result)
    return result


def render_text(result: PreviewResult) -> str:
    lines = [
        "# Axis Coding Agent - Preview",
        "",
        f"Command: {result.command}",
        f"Working dir: {result.working_dir}",
        f"Workspace root: {result.workspace_root}",
        f"Classification: {result.classification}",
        f"Approval level: {result.approval_level}",
        f"Allowlist match: {result.allowlist_match}",
        f"Blocklist match: {result.blocklist_match}",
        f"Executed: {result.executed}",
    ]
    if result.blocked_reasons:
        lines.extend(["", "## Blocked Reasons"])
        lines.extend(f"- {reason}" for reason in result.blocked_reasons)
    if result.notes:
        lines.extend(["", "## Notes"])
        lines.extend(f"- {note}" for note in result.notes)
    lines.extend(["", "## Decision", ""])
    if result.blocklist_match:
        lines.append("HALT. This command matches the blocklist. Requires explicit Wayne approval and a typed confirm token before any execution path is built.")
    elif result.approval_level == "none":
        lines.append("This command is read-only and within the allowlist. Safe to execute once the executor path is built.")
    elif result.approval_level == "review":
        lines.append("This command needs review. A diff or change summary must be shown before any write.")
    else:
        lines.append("This command needs explicit approval. The preview must be shown and confirmed in the same loop turn before execution.")
    lines.extend(["", "## Audit", "", result.audit_path])
    return "\n".join(lines)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Axis Local OS coding agent - preview-only stub")
    subparsers = parser.add_subparsers(dest="command", required=True)

    preview_parser = subparsers.add_parser("preview", help="Classify a command and show approval decision without executing")
    preview_parser.add_argument("cmd", help="Command string to preview")
    preview_parser.add_argument("--cwd", default=str(ROOT), help="Working directory the command would run in")
    preview_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    edit_parser = subparsers.add_parser("edit", help="Show a unified diff for a proposed file change without writing it")
    edit_parser.add_argument("target", help="Target file path the edit would write to")
    source_group = edit_parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument("--from", dest="from_path", help="Path to a file containing the proposed new content")
    source_group.add_argument("--stdin", action="store_true", help="Read proposed new content from stdin")
    edit_parser.add_argument("--out-of-scope", action="store_true", help="Acknowledge that the target is outside the workspace root")
    edit_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    for name in ("run", "apply", "undo"):
        sub = subparsers.add_parser(name, help=f"{name} - not yet implemented")
        sub.add_argument("rest", nargs=argparse.REMAINDER)

    args = parser.parse_args()

    if args.command == "preview":
        result = preview(args.cmd, Path(args.cwd).resolve())
        if args.json:
            print(json.dumps(asdict(result), indent=2, ensure_ascii=True))
        else:
            print(render_text(result))
        return

    if args.command == "edit":
        if args.stdin:
            new_content = sys.stdin.read()
        else:
            new_content = Path(args.from_path).read_text(encoding="utf-8")
        result_edit = edit_preview(Path(args.target), new_content, args.out_of_scope)
        if args.json:
            print(json.dumps(asdict(result_edit), indent=2, ensure_ascii=True))
        else:
            print(render_edit_text(result_edit))
        return

    print(f"`{args.command}` is not implemented yet. Only `preview` and `edit` are available in this stub.")
    print("See docs/modules/CODING_AGENT.md for the build order.")
    sys.exit(2)


if __name__ == "__main__":
    main()
