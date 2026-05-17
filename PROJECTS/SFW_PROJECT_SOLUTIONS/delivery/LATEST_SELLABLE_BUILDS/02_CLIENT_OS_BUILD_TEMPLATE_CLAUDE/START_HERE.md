# START_HERE.md - Client AI Operating System

## Start Sequence

Read in this order:

1. `CLAUDE.md`
2. `BUSINESS/CLIENT_CONTEXT.md`
3. `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`
4. `V4_OPERATING_LOGIC.md`
5. Relevant workflow file under `WORKFLOWS`
6. Relevant module under `CORE/WORKFLOW_MODULES`

## First Client Setup

Before handover, complete:

- `BUSINESS/CLIENT_CONTEXT.md`
- `GROWTH_BUILD_BLUEPRINT_TEMPLATE.md` if this is a Growth build
- `TEAM_ACCESS_AND_ROLE_MAP.md` if more than one user is involved
- `OWNER_COMMAND_CENTRE_EXAMPLE.md`
- `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`
- `BUSINESS/TRACKING/DECISION_LOG.md`
- `BUSINESS/TRACKING/SESSION_LOG.md`
- `V4_OPERATING_LOGIC.md`
- `HANDOVER/CLIENT_OS_GROWTH_ACCEPTANCE_TESTS.md` if this is a Growth build
- `HANDOVER/FIRST_7_DAYS_ADOPTION_PLAN.md`
- `HANDOVER/CLIENT_OS_GROWTH_HANDOVER_SCRIPT.md`
- `HANDOVER/HANDOVER_CHECKLIST.md`
- `SHIPPING_CHECKLIST.md`

## Universal Setup Trigger

Use:

```text
AXIS: NEW CLIENT
```

This starts or reviews client setup.

During first-time setup only, ask whether the client wants to give their AI PA a name.

Default name:
Axis

## V4 Operating Loop

Every workflow should move through:

```text
Capture -> Structure -> Operate -> Review -> Memory Update
```

Only update durable memory when the note, decision, relationship detail, or workflow rule will be useful beyond the current session.

## Daily Use

Client can ask:

```text
What needs my attention today?
```

Claude should return:
1. urgent items
2. due follow-ups
3. workflow blockers
4. next three actions

## Idea To Memory

Client can ask:

```text
AXIS: IDEA TO MEMORY
```

Claude should:
1. capture the idea
2. structure it into plan, workflow change, decision, or backlog
3. identify owner, status, and next action
4. review for scope and risk
5. update the correct tracker or memory only if appropriate

## Module Use

Available modules are explained in:

`CORE/WORKFLOW_MODULES/CLIENT_MODULE_GUIDE.md`

Clients can ask naturally. They do not need to know module names.

## Weekly Use

Client can ask:

```text
Run the weekly review.
```

Claude should return:
- active work
- completed work
- blockers
- overdue actions
- decisions needed
- next week priorities

## Care Package Review

Client or SF&W can ask:

```text
AXIS: CARE REVIEW
```

Claude should review:

- `GOVERNANCE/AI_OS_CONTROL_REGISTER.md`
- `GOVERNANCE/AGENT_FREEZE_PROTOCOL.md`
- `GOVERNANCE/SOURCE_TRUST_AND_PROMPT_INJECTION_CHECK.md`
- `CARE_PACKAGE/CARE_PACKAGE_OPERATING_STANDARD.md`
- `CARE_PACKAGE/MONTHLY_MEMORY_AUDIT.md`
- `CARE_PACKAGE/AI_USAGE_AND_ROI_TRACKER.md`
- `CARE_PACKAGE/PLATFORM_CHANGE_WATCH.md`
- `TEMPLATES/TONE_AND_STYLE_PROFILE.md`

Return changes made, risks found, value created, and next review date.

## Growth Delivery Standard

For Client OS Growth, do not build before Audit, scope, blueprint, role map, acceptance tests, and handover/adoption plan are complete.

Do not mark a Growth build ready until the V4 operating loop, memory discipline, and governance checks have been tested.

Do not mark a Growth build ready until the care package path is also visible.

## Support

If the client is unsure, Claude should explain the next action simply and refer to `TRAINING/USER_GUIDE.md`.
