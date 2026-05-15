# Client AI Operating System Template

Status: active template
Purpose: Client-ready AI OS package produced after an SF&W audit or implementation project.

## What This Is

This is the client copy.

It is not a simplified notes folder. It is a working operating system for an SME client, built from the same logic as the SF&W Claude OS:
- clear operator instructions
- workflow modules
- lifecycle tracking
- validation
- relationship and follow-up memory
- compliance-aware usage
- handover and training

## What This Is Not

This is not the internal SF&W build.

Do not include:
- SF&W strategy files
- Wayne's internal workstreams
- source archives
- other client files
- Black Map material
- old Hermes architecture
- internal pricing or sales strategy unless relevant to the client's signed scope

## How To Use

For each client:

1. Copy this folder.
2. Rename it to `[CLIENT_NAME]_AI_OS`.
3. Complete `BUSINESS/CLIENT_CONTEXT.md`.
4. Complete `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`.
5. Remove any modules not included in the client's scope.
6. Add the client's approved workflows.
7. For Growth builds, complete `GROWTH_BUILD_BLUEPRINT_TEMPLATE.md`, `TEAM_ACCESS_AND_ROLE_MAP.md`, and `HANDOVER/CLIENT_OS_GROWTH_ACCEPTANCE_TESTS.md`.
8. Add sample records under `SAMPLE_RECORDS/`.
9. Run the handover and shipping checklists.
10. Mark the client OS as `in review`.
11. Lock only after Wayne and the client sign off.

## Universal Trigger

Use this command to start or review setup:

```text
AXIS: NEW CLIENT
```

## Client Module Guide

Client-facing module guide:

`CORE/WORKFLOW_MODULES/CLIENT_MODULE_GUIDE.md`

Use this in handover to explain what the OS can do.

## Growth Additions

Growth builds should also use:

- `GROWTH_BUILD_BLUEPRINT_TEMPLATE.md`
- `TEAM_ACCESS_AND_ROLE_MAP.md`
- `OWNER_COMMAND_CENTRE_EXAMPLE.md`
- `HANDOVER/CLIENT_OS_GROWTH_ACCEPTANCE_TESTS.md`
- `HANDOVER/FIRST_7_DAYS_ADOPTION_PLAN.md`
- `HANDOVER/CLIENT_OS_GROWTH_HANDOVER_SCRIPT.md`
- `HANDOVER/GROWTH_CHANGE_CONTROL.md`
- `SAMPLE_RECORDS/`
- `SHIPPING_CHECKLIST.md`

## Template Status

This template is reusable, but every client copy must be reviewed before handover.
