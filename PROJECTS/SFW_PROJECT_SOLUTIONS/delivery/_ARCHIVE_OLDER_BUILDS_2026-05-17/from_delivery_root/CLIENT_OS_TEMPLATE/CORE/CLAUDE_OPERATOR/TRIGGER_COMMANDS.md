# Trigger Commands

Status: active
Purpose: Defines trigger words inside a client OS copy.

## Client Setup Trigger

Trigger:

```text
AXIS: NEW CLIENT
```

## Template Behaviour

Inside a copied client OS, this trigger means:

Complete or review first-time setup for this client.

Claude should:
1. Read `BUSINESS/CLIENT_CONTEXT.md`.
2. Read `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`.
3. Read `HANDOVER/HANDOVER_CHECKLIST.md`.
4. Identify missing setup facts.
5. Ask the one-time assistant naming question if no assistant name is set.
6. Confirm which workflows are active.
7. Mark incomplete setup items `in review`.

## Output Format

```text
Mode: BUILD
Trigger: AXIS: NEW CLIENT

Client Setup Review

Client:
Missing Facts:
Assistant Name:
Incomplete Files:
Workflows To Confirm:
Next Action:
```

## Guardrails

Do not:
- invent missing client facts
- ask the naming question repeatedly once answered
- lock the client OS before handover
- add workflows outside agreed scope
- change compliance notes without review
