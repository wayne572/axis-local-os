# Airtable Database Demo

Status: demo asset
Purpose: Show how AXIS AI OS can turn a real Airtable reference link and a messy business need into a safe, structured demo database plan.

## Demo Principle

This demo is not for touching Wayne's current Airtable database.

It shows the process:

```text
existing Airtable reference -> safe boundary -> test base plan -> table build prompt -> demo outcome
```

## Existing Airtable Reference

Use this as reference only:

```text
https://airtable.com/appgAvB8R0sNnhTps/tblUd1ajHmKozINu2/viwMFEW4Flfa7rPTa?blocks=hide
```

Extracted IDs:

| Item | ID |
|---|---|
| Existing base | `appgAvB8R0sNnhTps` |
| Existing table | `tblUd1ajHmKozINu2` |
| Existing view | `viwMFEW4Flfa7rPTa` |

## Safety Boundary

Do not create, edit, delete, import, or seed records into the existing base.

For the demo, create a new empty base called:

```text
AXIS Demo - Client Delivery Hub
```

If demonstrating without Airtable access, show the table plan and prompt only.

## Demo Story

Wayne wants to show a prospect that AXIS AI OS can build the database layer of a client delivery system.

The prospect has:

- leads in one place
- client audit answers in another
- delivery tasks in another
- no joined-up view of audit, build, handover, and review

AXIS turns that into a structured Airtable build plan.

## Demo Files

| File | Use |
|---|---|
| `AIRTABLE_DEMO_TABLE_SPEC.md` | Table design for the demo database |
| `CLAUDE_AIRTABLE_DEMO_PROMPT.md` | Prompt Wayne can paste into Claude AI OS |
| `DEMO_WALKTHROUGH.md` | Talk track and screen-by-screen demo flow |

## Demo Command

```text
AXIS: AIRTABLE DATABASE DEMO
```

Expected output:

- confirms the live base is read-only reference
- explains the safe new test base
- creates or describes the demo table structure
- adds fictional SME sample rows
- shows next actions for forms, views, and handover

## Fictional SME

Use:

```text
Harbour & Holt Kitchens Ltd
Client code: HHK-TEST
```

This keeps the demonstration aligned with the AXIS Audit to Client OS Growth pathway.
