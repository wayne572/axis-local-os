from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import shlex
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


OUTPUT_CHAR_LIMIT = 8000
DEFAULT_RUN_TIMEOUT = 30
APPLY_PREVIEW_MAX_AGE_SECONDS = 1800


ROOT = Path(__file__).resolve().parents[2]
AUDIT_DIR = ROOT / ".axis" / "audit"
AUDIT_PATH = AUDIT_DIR / "coding_agent.jsonl"
ROLLBACK_DIR = ROOT / ".axis" / "rollback"


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


def parse_iso(value: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value)
    except (TypeError, ValueError):
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed


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


@dataclass
class ApplyResult:
    schema: str
    timestamp: str
    target_path: str
    workspace_root: str
    in_workspace: bool
    out_of_scope_acknowledged: bool
    expected_diff_hash: str
    matched_preview_timestamp: str | None
    matched_preview_age_seconds: int | None
    pre_apply_sha256: str | None
    new_sha256: str
    new_lines_count: int
    classification: str
    approval_level: str
    halt_reason: str | None
    written: bool
    rollback_path: str | None
    audit_path: str


def find_matching_preview(target_resolved: Path, diff_hash: str) -> dict[str, Any] | None:
    if not AUDIT_PATH.exists():
        return None
    match: dict[str, Any] | None = None
    target_str = str(target_resolved)
    with AUDIT_PATH.open("r", encoding="utf-8") as handle:
        for raw in handle:
            try:
                event = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if event.get("schema") != "axis-local-os-coding-agent-edit-preview-v1":
                continue
            if event.get("target_path") != target_str:
                continue
            if event.get("diff_hash") != diff_hash:
                continue
            match = event
    return match


def apply_edit(target: Path, new_content: str, expected_diff_hash: str, out_of_scope: bool) -> ApplyResult:
    target_resolved = target.resolve()
    in_workspace = is_within_workspace(target_resolved)
    halt_reason: str | None = None
    written = False
    rollback_path: str | None = None
    pre_apply_sha: str | None = None
    matched_ts: str | None = None
    matched_age: int | None = None
    classification = "apply_blocked"
    approval_level = "approval"

    new_sha = sha256_text(new_content)
    new_lines = new_content.count("\n") + (0 if new_content.endswith("\n") or not new_content else 1)

    if not in_workspace and not out_of_scope:
        halt_reason = "target is outside workspace root and out-of-scope was not acknowledged"

    if halt_reason is None:
        match = find_matching_preview(target_resolved, expected_diff_hash)
        if match is None:
            halt_reason = (
                "no matching edit preview found in the audit log. Run `axis_code.py edit` first "
                "and pass its diff_hash via --confirm."
            )
        else:
            matched_ts = match.get("timestamp")
            preview_dt = parse_iso(matched_ts) if matched_ts else None
            if preview_dt is None:
                halt_reason = "matched preview audit entry is missing a parseable timestamp"
            else:
                age = (now_utc() - preview_dt).total_seconds()
                matched_age = int(age)
                if age > APPLY_PREVIEW_MAX_AGE_SECONDS:
                    halt_reason = (
                        f"matched preview is {int(age)}s old (limit {APPLY_PREVIEW_MAX_AGE_SECONDS}s). "
                        "Re-run `edit` to refresh the diff_hash."
                    )
                elif match.get("blocked_reasons"):
                    halt_reason = "matched preview was blocked - cannot apply"
                elif not in_workspace and not match.get("out_of_scope_acknowledged"):
                    halt_reason = "out-of-scope flag must have been acknowledged at preview time"
                else:
                    approval_level = match.get("approval_level", "review")
                    if approval_level not in {"review", "approval"}:
                        halt_reason = f"approval level `{approval_level}` cannot be applied"
                    else:
                        # Drift check: current file sha must match the preview's recorded old_sha256.
                        expected_old = match.get("old_sha256")
                        if target_resolved.exists() and target_resolved.is_file():
                            current_text, current_binary = read_text_file(target_resolved)
                            if current_binary:
                                halt_reason = "target is binary - apply path does not write binary files"
                            else:
                                pre_apply_sha = sha256_text(current_text)
                                if expected_old is not None and pre_apply_sha != expected_old:
                                    halt_reason = (
                                        f"file drift detected. preview saw old_sha256={expected_old}, "
                                        f"current sha256={pre_apply_sha}. Re-run `edit` to refresh."
                                    )
                        else:
                            current_text = ""
                            pre_apply_sha = None
                            if expected_old is not None:
                                halt_reason = "preview expected an existing file but target is missing now"

    if halt_reason is None:
        try:
            ROLLBACK_DIR.mkdir(parents=True, exist_ok=True)
            if target_resolved.exists():
                timestamp = now_utc().strftime("%Y%m%dT%H%M%SZ")
                rb = ROLLBACK_DIR / f"{timestamp}_{expected_diff_hash[:12]}.preimage"
                rb.write_bytes(current_text.encode("utf-8"))
                rollback_path = str(rb.relative_to(ROOT))
            target_resolved.parent.mkdir(parents=True, exist_ok=True)
            target_resolved.write_bytes(new_content.encode("utf-8"))
            written = True
            classification = "apply_write"
        except OSError as exc:
            halt_reason = f"write failed: {exc}"

    result = ApplyResult(
        schema="axis-local-os-coding-agent-apply-v1",
        timestamp=now_utc().isoformat(),
        target_path=str(target_resolved),
        workspace_root=str(ROOT),
        in_workspace=in_workspace,
        out_of_scope_acknowledged=out_of_scope,
        expected_diff_hash=expected_diff_hash,
        matched_preview_timestamp=matched_ts,
        matched_preview_age_seconds=matched_age,
        pre_apply_sha256=pre_apply_sha,
        new_sha256=new_sha,
        new_lines_count=new_lines,
        classification=classification,
        approval_level=approval_level,
        halt_reason=halt_reason,
        written=written,
        rollback_path=rollback_path,
        audit_path=str(AUDIT_PATH.relative_to(ROOT)),
    )
    write_audit_event(result)
    return result


def render_apply_text(result: ApplyResult) -> str:
    lines = [
        "# Axis Coding Agent - Apply",
        "",
        f"Target: {result.target_path}",
        f"In workspace: {result.in_workspace}",
        f"Out-of-scope acknowledged: {result.out_of_scope_acknowledged}",
        f"Expected diff_hash: {result.expected_diff_hash}",
        f"Matched preview timestamp: {result.matched_preview_timestamp or 'no match'}",
        f"Matched preview age (s): {result.matched_preview_age_seconds if result.matched_preview_age_seconds is not None else 'n/a'}",
        f"Pre-apply sha256: {result.pre_apply_sha256 or 'n/a (new file)'}",
        f"New sha256: {result.new_sha256}",
        f"Classification: {result.classification}",
        f"Approval level: {result.approval_level}",
        f"Written: {result.written}",
        f"Rollback path: {result.rollback_path or 'n/a'}",
    ]
    if result.halt_reason:
        lines.extend(["", "## Halt Reason", "", result.halt_reason])
    if result.written:
        lines.extend(["", "## Result", "", "File written. Rollback pre-image stored. Use `axis_code.py undo` once available."])
    lines.extend(["", "## Audit", "", result.audit_path])
    return "\n".join(lines)


@dataclass
class UndoResult:
    schema: str
    timestamp: str
    target_path: str
    workspace_root: str
    matched_apply_timestamp: str | None
    matched_apply_new_sha256: str | None
    rollback_source: str | None
    pre_undo_sha256: str | None
    restored_sha256: str | None
    redo_preimage_path: str | None
    classification: str
    halt_reason: str | None
    restored: bool
    audit_path: str


def find_latest_apply(target_resolved: Path) -> dict[str, Any] | None:
    if not AUDIT_PATH.exists():
        return None
    match: dict[str, Any] | None = None
    target_str = str(target_resolved)
    with AUDIT_PATH.open("r", encoding="utf-8") as handle:
        for raw in handle:
            try:
                event = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if event.get("schema") != "axis-local-os-coding-agent-apply-v1":
                continue
            if event.get("target_path") != target_str:
                continue
            if not event.get("written"):
                continue
            if not event.get("rollback_path"):
                continue
            match = event
    return match


def undo_apply(target: Path) -> UndoResult:
    target_resolved = target.resolve()
    halt_reason: str | None = None
    restored = False
    matched_ts: str | None = None
    matched_new_sha: str | None = None
    rollback_source: str | None = None
    pre_undo_sha: str | None = None
    restored_sha: str | None = None
    redo_path: str | None = None
    classification = "undo_blocked"

    match = find_latest_apply(target_resolved)
    if match is None:
        halt_reason = "no apply event with a written rollback pre-image found for this target"
    else:
        matched_ts = match.get("timestamp")
        matched_new_sha = match.get("new_sha256")
        rollback_rel = match.get("rollback_path")
        rollback_source = rollback_rel
        rollback_abs = ROOT / rollback_rel if rollback_rel else None
        if not rollback_abs or not rollback_abs.exists():
            halt_reason = f"rollback pre-image missing on disk: {rollback_rel}"
        elif not target_resolved.exists():
            halt_reason = "target file no longer exists - nothing to undo against"
        else:
            current_text, current_binary = read_text_file(target_resolved)
            if current_binary:
                halt_reason = "target is binary - undo path does not handle binary"
            else:
                pre_undo_sha = sha256_text(current_text)
                if matched_new_sha and pre_undo_sha != matched_new_sha:
                    halt_reason = (
                        f"drift since apply. apply wrote new_sha256={matched_new_sha}, "
                        f"current sha256={pre_undo_sha}. Resolve manually before undo."
                    )
                else:
                    try:
                        ROLLBACK_DIR.mkdir(parents=True, exist_ok=True)
                        ts = now_utc().strftime("%Y%m%dT%H%M%SZ")
                        redo = ROLLBACK_DIR / f"{ts}_redo.preimage"
                        redo.write_bytes(current_text.encode("utf-8"))
                        redo_path = str(redo.relative_to(ROOT))
                        restored_bytes = rollback_abs.read_bytes()
                        restored_content = restored_bytes.decode("utf-8", errors="replace")
                        target_resolved.write_bytes(restored_bytes)
                        restored = True
                        restored_sha = sha256_text(restored_content)
                        classification = "undo_restore"
                    except OSError as exc:
                        halt_reason = f"undo write failed: {exc}"

    result = UndoResult(
        schema="axis-local-os-coding-agent-undo-v1",
        timestamp=now_utc().isoformat(),
        target_path=str(target_resolved),
        workspace_root=str(ROOT),
        matched_apply_timestamp=matched_ts,
        matched_apply_new_sha256=matched_new_sha,
        rollback_source=rollback_source,
        pre_undo_sha256=pre_undo_sha,
        restored_sha256=restored_sha,
        redo_preimage_path=redo_path,
        classification=classification,
        halt_reason=halt_reason,
        restored=restored,
        audit_path=str(AUDIT_PATH.relative_to(ROOT)),
    )
    write_audit_event(result)
    return result


def render_undo_text(result: UndoResult) -> str:
    lines = [
        "# Axis Coding Agent - Undo",
        "",
        f"Target: {result.target_path}",
        f"Matched apply timestamp: {result.matched_apply_timestamp or 'no match'}",
        f"Apply new_sha256: {result.matched_apply_new_sha256 or 'n/a'}",
        f"Rollback source: {result.rollback_source or 'n/a'}",
        f"Pre-undo sha256: {result.pre_undo_sha256 or 'n/a'}",
        f"Restored sha256: {result.restored_sha256 or 'n/a'}",
        f"Redo pre-image: {result.redo_preimage_path or 'n/a'}",
        f"Classification: {result.classification}",
        f"Restored: {result.restored}",
    ]
    if result.halt_reason:
        lines.extend(["", "## Halt Reason", "", result.halt_reason])
    if result.restored:
        lines.extend(["", "## Result", "", "Pre-image restored. A redo pre-image of the just-undone state is stored under .axis/rollback."])
    lines.extend(["", "## Audit", "", result.audit_path])
    return "\n".join(lines)


@dataclass
class RunResult:
    schema: str
    timestamp: str
    command: str
    working_dir: str
    workspace_root: str
    classification: str
    approval_level: str
    allowlist_match: bool
    blocklist_match: bool
    blocked_reasons: list[str]
    notes: list[str]
    executed: bool
    exit_code: int | None
    stdout: str
    stderr: str
    stdout_truncated: bool
    stderr_truncated: bool
    timed_out: bool
    halt_reason: str | None
    audit_path: str


def truncate(text: str, limit: int = OUTPUT_CHAR_LIMIT) -> tuple[str, bool]:
    if len(text) <= limit:
        return text, False
    return text[:limit] + "\n...[truncated]", True


def run_command(command: str, working_dir: Path, timeout: int) -> RunResult:
    classification, approval_level, allow, block, reasons, notes = classify_command(command)
    halt_reason: str | None = None
    executed = False
    exit_code: int | None = None
    stdout_text = ""
    stderr_text = ""
    stdout_truncated = False
    stderr_truncated = False
    timed_out = False

    if approval_level != "none":
        halt_reason = (
            f"approval level `{approval_level}` is above `none`. Read-only execution path "
            "only runs allowlisted, read-only commands. Use the preview path and seek approval."
        )
    elif block:
        halt_reason = "command matches the blocklist"
    else:
        tokens = tokenize(command)
        try:
            proc = subprocess.run(
                tokens,
                cwd=str(working_dir),
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False,
                shell=False,
            )
            executed = True
            exit_code = proc.returncode
            stdout_text, stdout_truncated = truncate(proc.stdout or "")
            stderr_text, stderr_truncated = truncate(proc.stderr or "")
        except subprocess.TimeoutExpired as exc:
            timed_out = True
            halt_reason = f"command exceeded timeout of {timeout}s"
            stdout_text, stdout_truncated = truncate(exc.stdout.decode("utf-8", "replace") if exc.stdout else "")
            stderr_text, stderr_truncated = truncate(exc.stderr.decode("utf-8", "replace") if exc.stderr else "")
        except FileNotFoundError as exc:
            halt_reason = f"executable not found: {exc.filename}"
        except OSError as exc:
            halt_reason = f"os error: {exc}"

    result = RunResult(
        schema="axis-local-os-coding-agent-run-v1",
        timestamp=now_utc().isoformat(),
        command=command,
        working_dir=str(working_dir),
        workspace_root=str(ROOT),
        classification=classification,
        approval_level=approval_level,
        allowlist_match=allow,
        blocklist_match=block,
        blocked_reasons=reasons,
        notes=notes,
        executed=executed,
        exit_code=exit_code,
        stdout=stdout_text,
        stderr=stderr_text,
        stdout_truncated=stdout_truncated,
        stderr_truncated=stderr_truncated,
        timed_out=timed_out,
        halt_reason=halt_reason,
        audit_path=str(AUDIT_PATH.relative_to(ROOT)),
    )
    write_audit_event(result)
    return result


def render_run_text(result: RunResult) -> str:
    lines = [
        "# Axis Coding Agent - Run",
        "",
        f"Command: {result.command}",
        f"Working dir: {result.working_dir}",
        f"Classification: {result.classification}",
        f"Approval level: {result.approval_level}",
        f"Allowlist match: {result.allowlist_match}",
        f"Blocklist match: {result.blocklist_match}",
        f"Executed: {result.executed}",
        f"Exit code: {result.exit_code}",
        f"Timed out: {result.timed_out}",
    ]
    if result.blocked_reasons:
        lines.extend(["", "## Blocked Reasons"])
        lines.extend(f"- {reason}" for reason in result.blocked_reasons)
    if result.notes:
        lines.extend(["", "## Notes"])
        lines.extend(f"- {note}" for note in result.notes)
    if result.halt_reason:
        lines.extend(["", "## Halt Reason", "", result.halt_reason])
    if result.executed:
        lines.extend(["", "## stdout", ""])
        lines.append(result.stdout if result.stdout else "(empty)")
        if result.stdout_truncated:
            lines.append("(stdout truncated)")
        if result.stderr.strip():
            lines.extend(["", "## stderr", "", result.stderr])
            if result.stderr_truncated:
                lines.append("(stderr truncated)")
    lines.extend(["", "## Audit", "", result.audit_path])
    return "\n".join(lines)


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

    run_parser = subparsers.add_parser("run", help="Execute a read-only allowlisted command (level `none` only)")
    run_parser.add_argument("cmd", help="Command string to execute")
    run_parser.add_argument("--cwd", default=str(ROOT), help="Working directory")
    run_parser.add_argument("--timeout", type=int, default=DEFAULT_RUN_TIMEOUT, help="Timeout in seconds")
    run_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    apply_parser = subparsers.add_parser("apply", help="Write a previously-previewed edit to disk, gated on diff_hash and old-sha drift check")
    apply_parser.add_argument("target", help="Target file path")
    apply_src = apply_parser.add_mutually_exclusive_group(required=True)
    apply_src.add_argument("--from", dest="from_path", help="Path to file with the new content")
    apply_src.add_argument("--stdin", action="store_true", help="Read new content from stdin")
    apply_parser.add_argument("--confirm", dest="diff_hash", required=True, help="diff_hash from the matching `edit` preview audit entry")
    apply_parser.add_argument("--out-of-scope", action="store_true", help="Acknowledge out-of-scope (must also have been set at preview time)")
    apply_parser.add_argument("--json", action="store_true", help="Print JSON")

    undo_parser = subparsers.add_parser("undo", help="Restore the latest apply pre-image for a target")
    undo_parser.add_argument("target", help="Target file path to undo the most recent apply for")
    undo_parser.add_argument("--json", action="store_true", help="Print JSON")

    args = parser.parse_args()

    if args.command == "preview":
        result = preview(args.cmd, Path(args.cwd).resolve())
        if args.json:
            print(json.dumps(asdict(result), indent=2, ensure_ascii=True))
        else:
            print(render_text(result))
        return

    if args.command == "run":
        result_run = run_command(args.cmd, Path(args.cwd).resolve(), args.timeout)
        if args.json:
            print(json.dumps(asdict(result_run), indent=2, ensure_ascii=True))
        else:
            print(render_run_text(result_run))
        sys.exit(0 if result_run.executed and result_run.exit_code == 0 else (result_run.exit_code or 1))

    if args.command == "undo":
        result_undo = undo_apply(Path(args.target))
        if args.json:
            print(json.dumps(asdict(result_undo), indent=2, ensure_ascii=True))
        else:
            print(render_undo_text(result_undo))
        sys.exit(0 if result_undo.restored else 1)

    if args.command == "apply":
        if args.stdin:
            new_content = sys.stdin.read()
        else:
            new_content = Path(args.from_path).read_text(encoding="utf-8")
        result_apply = apply_edit(Path(args.target), new_content, args.diff_hash, args.out_of_scope)
        if args.json:
            print(json.dumps(asdict(result_apply), indent=2, ensure_ascii=True))
        else:
            print(render_apply_text(result_apply))
        sys.exit(0 if result_apply.written else 1)

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
