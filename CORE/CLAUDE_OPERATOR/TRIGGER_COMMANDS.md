# Trigger Commands

Status: active
Purpose: Defines universal trigger words for repeatable OS actions.

## Universal New Client Trigger

Trigger:

```text
AXIS: NEW CLIENT
```

## Purpose

Use this whenever Wayne is setting up a new client after an audit, discovery call, or signed project.

The trigger starts the client OS setup workflow.

## What Claude Must Do

When Wayne types:

```text
AXIS: NEW CLIENT
```

Claude must:

1. Switch to BUILD mode.
2. Confirm this is a new client setup.
3. Read:
   - `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/AUDIT_TO_CLIENT_OS_WORKFLOW.md`
   - `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/CLIENT_OS_TEMPLATE/README.md`
   - `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/CLIENT_OS_TEMPLATE/HANDOVER/CLIENT_HANDOVER_PACK_TEMPLATE.md`
4. Ask only for missing setup facts.
5. Include the one-time AI PA naming step.
6. Create or prepare a client OS copy from `CLIENT_OS_TEMPLATE`.
7. Mark the client copy `in review`.
8. Tell Wayne what was created and what still needs completion.

## Required Intake Questions

If not already provided, ask for:

1. Client name
2. Primary contact
3. Business type / sector
4. Main admin pain points
5. Workflows included in scope
6. Tools currently used
7. Any personal data, outreach data, or compliance concerns
8. Whether the client wants to name their AI PA, or keep the default `Axis`
9. Desired handover date

## Output Format

Claude should respond with:

```text
Mode: BUILD
Trigger: AXIS: NEW CLIENT

Client Setup Started

Client:
Status:
Missing Facts:
Assistant Name:
Files To Create:
Next Action:
```

## Guardrails

Claude must not:
- use another client's files as active truth
- include SF&W internal strategy in the client copy
- include Black Map material
- treat Hermes as active
- lock the client OS before review
- invent missing client facts
- ask the assistant naming question repeatedly after it has been answered

## Related Files

- `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/AUDIT_TO_CLIENT_OS_WORKFLOW.md`
- `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/CLIENT_OS_TEMPLATE`
- `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/CLIENT_OS_TEMPLATE/HANDOVER/CLIENT_HANDOVER_PACK_TEMPLATE.md`

---

## Solo Operator Trigger

Trigger:

```text
AXIS: SOLO START
```

## Purpose

Use this when Wayne is setting up or testing the personal / solo entrepreneur version of the OS.

This is for people who want to run work, business, personal admin, relationships, ideas, and weekly priorities through one AI operating layer.

## What Claude Must Do

When Wayne types:

```text
AXIS: SOLO START
```

Claude must:

1. Switch to BUILD mode if creating or configuring the OS.
2. Read:
   - `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/SOLO_OPERATOR_OS_TEMPLATE/README.md`
   - `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/SOLO_OPERATOR_OS_TEMPLATE/CLAUDE.md`
   - `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/SOLO_OPERATOR_OS_TEMPLATE/PERSONAL_CONTEXT.md`
3. Check whether first-time setup is complete.
4. If setup is incomplete, ask the one-time setup questions.
5. Ask whether the user wants to give the AI PA a name or keep `Axis`.
6. Route future requests to the relevant Solo Operator module.

## Related Solo Commands

- `AXIS: DAILY COMMAND`
- `AXIS: WEEKLY REVIEW`
- `AXIS: CAPTURE THIS`
- `AXIS: DECISION`
- `AXIS: ADMIN CLEAR-DOWN`
- `AXIS: BUSINESS BUILDER`
- `AXIS: 30 DAY REVIEW`

## Related Files

- `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/SOLO_OPERATOR_OS_TEMPLATE`
- `PROJECTS/SFW_PROJECT_SOLUTIONS/offer/SOLO_OPERATOR_OS_OFFER.md`
