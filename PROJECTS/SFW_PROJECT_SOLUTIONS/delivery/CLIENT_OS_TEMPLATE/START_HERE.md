# START_HERE.md - Client AI Operating System

## Start Sequence

Read in this order:

1. `CLAUDE.md`
2. `BUSINESS/CLIENT_CONTEXT.md`
3. `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`
4. Relevant workflow file under `WORKFLOWS`
5. Relevant module under `CORE/WORKFLOW_MODULES`

## First Client Setup

Before handover, complete:

- `BUSINESS/CLIENT_CONTEXT.md`
- `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`
- `BUSINESS/TRACKING/DECISION_LOG.md`
- `BUSINESS/TRACKING/SESSION_LOG.md`
- `HANDOVER/HANDOVER_CHECKLIST.md`

## Universal Setup Trigger

Use:

```text
AXIS: NEW CLIENT
```

This starts or reviews client setup.

During first-time setup only, ask whether the client wants to give their AI PA a name.

Default name:
Axis

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

## Support

If the client is unsure, Claude should explain the next action simply and refer to `TRAINING/USER_GUIDE.md`.
