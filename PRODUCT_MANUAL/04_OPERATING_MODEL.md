# 04 - Operating Model

Status: active draft
Purpose: Explain how AXIS works internally.

## The Operating Sequence

AXIS works through this sequence:

1. Claude reads startup files.
2. Claude identifies the mode.
3. Claude checks current workstreams.
4. Claude reads relevant venture, project, or specialist files.
5. Claude produces the requested output.
6. Claude validates the output.
7. Claude updates or proposes tracker updates.

## Startup Files

Core startup files:
- `CLAUDE.md`
- `START_HERE.md`
- `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`
- `BUSINESS/VENTURES/VENTURE_REGISTRY.md`
- `CORE/CLAUDE_OPERATOR/CLAUDE_OPERATOR_MODEL.md`
- `CORE/CLAUDE_OPERATOR/TRIGGER_COMMANDS.md`

## Mode Discipline

AXIS should work in one mode at a time.

If no mode is given, it defaults to ORCHESTRATE.

Mode switching should be deliberate and clear.

## Routing

AXIS routes work based on the request:

| Request | Route |
|---|---|
| priority, roadmap, decision | ORCHESTRATE |
| asset, document, workflow | BUILD |
| prospects, outreach, pipeline | LEAD |
| research, trends, market intelligence | LEARN |
| audit, review, QA | REVIEW |
| client setup | `AXIS: NEW CLIENT` |
| personal / solo OS | `AXIS: SOLO START` |

## DCoS Lifecycle

Every meaningful item should have a state:
- active
- in review
- locked
- archived

Rules:
- Nothing leaves active without review.
- Locked means shipped or signed off.
- Locked items are superseded, not casually edited.
- No orphan tasks.

## Review Gate

Before important output is treated as final, AXIS checks:
- Does this answer the request?
- Is the next action clear?
- Are risks visible?
- Is it in Wayne's tone?
- Does it avoid invented facts?
- Does it preserve the OS structure?
- Does it avoid excluded ventures?
- Are data and consent handled properly?

## Specialist Playbooks

Specialist OS files are playbooks.

Claude reads them when useful, but the user should experience one operator.

This avoids making the product feel fragmented.

## Access Channels

Claude is the operator.

Telegram and WhatsApp are planned capture and access channels.

They should support:
- quick notes
- voice-note capture
- follow-up logging
- daily check-ins
- relationship capture
- admin reminders

They should not hold separate business truth.
