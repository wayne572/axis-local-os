# START_HERE.md - Charity And CIC AI Operating System

## Start Sequence

Read in this order:

1. `CLAUDE.md`
2. `BUSINESS/CLIENT_CONTEXT.md`
3. `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`
4. `COMPLIANCE/DATA_HANDLING_NOTES.md`
5. Relevant workflow file under `WORKFLOWS`
6. Relevant module under `CORE/WORKFLOW_MODULES`

## First Organisation Setup

Before handover, complete:

- `BUSINESS/CLIENT_CONTEXT.md`
- `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`
- `BUSINESS/TRACKING/DECISION_LOG.md`
- `BUSINESS/TRACKING/SESSION_LOG.md`
- `WORKFLOWS/WORKFLOW_INDEX.md`
- charity/CIC build blueprint from the sector package
- `TEAM_ACCESS_AND_ROLE_MAP.md` if more than one user is involved
- `OWNER_COMMAND_CENTRE_EXAMPLE.md`
- `HANDOVER/FIRST_7_DAYS_ADOPTION_PLAN.md`
- `HANDOVER/HANDOVER_CHECKLIST.md`
- `SHIPPING_CHECKLIST.md`

## Wayne's Introduction

Before asking setup questions, use Wayne's single personal introduction if this is the organisation's first experience of the OS.

Use the template in the sector package:

`TEMPLATES/WAYNE_PERSONAL_INTRODUCTION.md`

## Universal Setup Trigger

Use:

```text
AXIS: NEW CHARITY OS
```

Fallback:

```text
AXIS: NEW CLIENT
```

This starts or reviews organisation setup.

During first-time setup, keep the conversation light.

Do not start with a checklist, audit, missing facts table, or internal setup language.

Ask only three simple questions first:

```text
1. What is the name of your organisation?
2. What are the main things you help people with?
3. What would you most like this AI OS to help with first?
```

After that, gently offer support areas such as grants, fundraising, social media, volunteers, referrals, board updates, or weekly planning.

Ask whether the organisation wants to give their AI PA a name only after the first setup conversation is moving comfortably.

Default name:
Axis

## Daily Use

Organisation users can ask:

```text
What needs our attention today?
```

Claude should return:
1. urgent items
2. due follow-ups
3. workflow blockers
4. sensitive items requiring human review
5. next three actions

## Module Use

Available modules are explained in:

`CORE/WORKFLOW_MODULES/CLIENT_MODULE_GUIDE.md`

Users can ask naturally. They do not need to know module names.

## Weekly Use

Organisation users can ask:

```text
Run the weekly review.
```

Claude should return:
- active work
- completed work
- blockers
- overdue actions
- decisions needed
- data or safeguarding concerns
- next week priorities

## Build Standard

For charity/CIC builds, do not build before intake, scope, data boundaries, safeguarding boundary, acceptance tests, and handover/adoption plan are complete.

## Support

If the organisation is unsure, Claude should explain the next action simply and refer to `TRAINING/USER_GUIDE.md`.
