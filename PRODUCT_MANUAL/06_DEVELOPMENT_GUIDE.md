# 06 - Development Guide

Status: active draft
Purpose: Explain how to improve AXIS without breaking the product.

## Development Principle

Enhance the system without losing functionality.

Before changing anything, ask:
- what current capability does this affect?
- where does that capability live?
- is it preserved, enhanced, superseded, archived, or excluded?

## Do Not Break

Protect:
- `CLAUDE.md`
- `START_HERE.md`
- `CORE/CLAUDE_OPERATOR/TRIGGER_COMMANDS.md`
- `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`
- `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/CLIENT_OS_TEMPLATE`
- `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/SOLO_OPERATOR_OS_TEMPLATE`

## Adding A New Capability

Use this process:

1. Define the use case.
2. Decide whether it belongs in internal AXIS, Client OS, Solo Operator OS, or specialist playbooks.
3. Create or update the relevant workflow file.
4. Add the trigger if needed.
5. Add tracker entry if it becomes a workstream.
6. Add test case.
7. Mark as `in review`.
8. Only lock after testing.

## Editing Existing Files

When editing:
- keep plain English
- avoid hype
- avoid hidden assumptions
- preserve lifecycle states
- preserve command triggers
- preserve client boundaries
- avoid importing archived files wholesale

## Adding Telegram Or WhatsApp

Treat Telegram and WhatsApp as access channels.

They should send messages into AXIS for:
- capture
- reminders
- daily check-in
- relationship logging
- admin logging

They should not become separate truth stores.

## Adding A New Client Template

Do not edit the master client template for a single client.

Instead:
1. Copy `CLIENT_OS_TEMPLATE`.
2. Rename it for the client.
3. Fill in client context.
4. Mark as `in review`.
5. Test workflows.
6. Lock only after review.

## Adding A New Solo Operator Copy

Do not edit the master Solo Operator template for a single user.

Instead:
1. Copy `SOLO_OPERATOR_OS_TEMPLATE`.
2. Rename it for the user.
3. Complete setup questionnaire.
4. Fill in personal context.
5. Test daily command, capture, decision, admin clear-down, and weekly review.
6. Create the mobile-friendly start guide.
7. Rebuild the zip after adding the guide.
8. Mark as `in review`.

## Documentation Rule

If a feature is important enough to sell, it needs:
- offer file
- workflow file
- delivery checklist
- test plan
- boundary note
- handover guide if client-facing
- mobile-friendly HTML guide if client-facing

## Development Roadmap

Near term:
- test Client OS Template with sample audit
- test Solo Operator OS in Claude
- decide pricing
- review usage tracking wording
- create SME audit checklist and outreach pack

Medium term:
- Telegram quick capture
- WhatsApp access
- relationship pulse testing
- repeatable client onboarding process
- productised landing pages

Later:
- web dashboard
- self-hosted memory
- multi-agent runtime
- analytics layer
- packaged open-source edition
