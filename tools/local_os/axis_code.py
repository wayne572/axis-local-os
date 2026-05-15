from __future__ import annotations

import argparse
import json
import re
import shlex
import sys
from dataclasses import asdict, dataclass
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


def write_audit_event(result: PreviewResult) -> None:
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    with AUDIT_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(asdict(result), ensure_ascii=True) + "\n")


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

    for name in ("run", "edit", "apply", "undo"):
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

    print(f"`{args.command}` is not implemented yet. Only `preview` is available in this stub.")
    print("See docs/modules/CODING_AGENT.md for the build order.")
    sys.exit(2)


if __name__ == "__main__":
    main()
