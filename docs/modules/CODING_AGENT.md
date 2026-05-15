# Coding Agent And Command Approval

Status: capability spec — pending build
Date: 2026-05-15
Owner: Wayne Francis

## Purpose

The Coding Agent is the first Axis Local OS capability that *executes* rather than only proposes. It turns the governed loop from a governed thinker into a governed doer.

It covers three action surfaces:

- shell commands
- file edits and writes
- workspace-scoped tool invocations (git, package managers, scripts)

Every action passes through the existing governed loop. Nothing runs without the correct approval level and an audit event.

## First Principle

No execution without review. No review without retrieval. No retrieval without sources.

A coding action must:

- be proposed by the loop, not invented mid-execution
- carry an explicit approval level (`none` / `review` / `approval`)
- be previewable in full before it runs
- write an audit event whether approved, blocked, or rejected
- never silently mutate state outside the declared target

## Approval Level Mapping

| Action class | Default level | Examples |
|---|---|---|
| Read-only inspection | `none` | `ls`, `cat`, `git status`, `git log`, `git diff`, dry-run formatters |
| File edit / write (workspace) | `review` | create / modify a file in the repo, draft a patch |
| Mutating local command | `approval` | `git commit`, `git checkout`, `pip install`, `npm install`, scripts that write outside the repo |
| External effect | `approval` | `git push`, network calls, deploys, API writes, anything reaching another system |
| Destructive | `approval` + confirm token | `rm`, `git reset --hard`, `git push --force`, drop / delete / truncate |

The default is intentionally conservative. Levels can be tightened per command but never silently relaxed.

## Constitution Alignment

The Coding Agent does not override the Axis Local OS constitution. It inherits:

- `no_execution_without_review: true`
- `audit_every_action: true`
- `human_approval_for_external_effects: true`
- `reviewed_memory_updates_only: true`

It adds two coding-specific rules:

- `no_command_without_preview: true` — the exact command string must be shown before execution
- `no_edit_without_diff: true` — the exact diff must be shown before write

## Allowlist And Blocklist

A small command allowlist is the safe default. Anything not on the allowlist is `approval`-level by default.

Initial allowlist (read-only, level `none`):

```text
ls, pwd, whoami, hostname
cat, head, tail, wc
git status, git log, git diff, git branch, git remote -v
python --version, node --version
```

Initial blocklist (never auto-runnable, requires explicit Wayne approval per call):

```text
rm, rmdir, del, Remove-Item -Recurse
git push --force, git reset --hard, git clean -fd
any --no-verify, --no-gpg-sign, --force
curl | sh, iwr | iex
shutdown, reboot
```

Anything not classified halts and routes to Wayne for triage.

## MVP Build Order

1. Spec and module registration (this file + entry in `axis_modules.py`).
2. Command preview surface — show command, working dir, approval level, predicted effect.
3. Diff preview surface — show unified diff for any proposed file edit.
4. Allowlist execution path for level `none` (read-only) with audit event.
5. Review-gated edit path for level `review` — diff shown, single approval, then write.
6. Approval-gated execution path for level `approval` — full preview + explicit confirm token.
7. Destructive-action path — approval + typed confirm phrase (e.g. retype the command).
8. Audit event schema extension for coding actions.
9. Rollback / undo surface for review-level edits.
10. Workspace scoping — refuse paths outside the declared workspace root.

## First Commands

```text
AXIS: CODE PREVIEW
AXIS: CODE RUN
AXIS: CODE EDIT
AXIS: CODE APPLY
AXIS: CODE UNDO
```

First CLI surface:

```powershell
python tools/local_os/axis_code.py preview "<command>"
python tools/local_os/axis_code.py run "<command>"
python tools/local_os/axis_code.py edit <path>
python tools/local_os/axis_code.py apply <patch_file>
python tools/local_os/axis_code.py undo <audit_id>
```

`preview` never executes. `run` requires the preview to have been shown and confirmed in the same session. `apply` requires the diff to have been shown. `undo` reverses a single prior review-level edit if the audit trail still has the pre-image.

## Audit Event Extension

In addition to the base governed-loop fields, every coding event records:

- command string (verbatim)
- working directory
- approval level resolved
- allowlist / blocklist match
- diff hash (for edits)
- exit code (for runs)
- stdout / stderr capture path
- rollback reference, if applicable

## Workspace Scoping

The Coding Agent operates inside a declared workspace root. By default this is the Axis Local OS repo (`AXIS_OS_CODEX_CURRENT/`).

- Reads outside the workspace require `review`.
- Writes outside the workspace require `approval` and an explicit out-of-scope acknowledgement.
- Network and external-system writes always require `approval`, regardless of workspace.

## Governance Rules

- Never run a command that has not been previewed in the same loop turn.
- Never write a file edit that has not been shown as a diff.
- Never auto-commit. Never auto-push.
- Never bypass hooks, signing, or verification flags.
- Never operate on a path the user did not name or that retrieval did not surface.
- Never use a destructive command as a shortcut to clear an obstacle.
- Always log, even on rejection.

## Failure Conditions

The Coding Agent halts and routes to Wayne if:

- a proposed command matches the blocklist
- a proposed edit targets a path outside the workspace without acknowledgement
- the approval level cannot be resolved
- the audit event cannot be written
- retrieval returned no sources but the action depends on project memory
- the diff or preview cannot be produced before execution

## Success Condition

Wayne can ask Axis to make a code change, see the exact command or diff, approve it once, and have Axis execute it locally with a full audit event written — and nothing else mutated.
