# Start Here - Solo Operator OS Live Test

Status: active
Purpose: First page to open when running the Solo Operator OS live-test build.

## Live-Test Context

This build is configured for Wayne Francis as the test user.

Setup is already complete in `PERSONAL_CONTEXT.md`, so Codex should not repeat first-time setup unless instructed to test onboarding.

For the live test script, read:

`LIVE_TEST_SCRIPT.md`

For pass/fail criteria, read:

`ACCEPTANCE_CHECKLIST.md`

For landing pages, product copy, positioning, and client-facing wording, read:

`DEVELOPER.md`

## How To Start

Use this trigger:

```text
AXIS: SOLO START
```

Codex should then check `PERSONAL_CONTEXT.md`.

If setup is incomplete, run first-time setup.

If setup is complete, ask:

```text
Do you want Daily Command Centre, Weekly Review, Capture, Decision Support, or Admin Clear-Down?
```

## Main Commands

```text
AXIS: DAILY COMMAND
```

Run the daily command centre.

```text
AXIS: WEEKLY REVIEW
```

Run the weekly review.

```text
AXIS: CAPTURE THIS
```

Turn a messy note, voice note, idea, or message into structured action.

```text
AXIS: DECISION
```

Help the user make a decision using options, risks, trade-offs, and next action.

```text
AXIS: ADMIN CLEAR-DOWN
```

List and prioritise personal admin.

```text
AXIS: BUSINESS BUILDER
```

Focus on offers, leads, content, sales, delivery, or revenue actions.

```text
AXIS: 30 DAY REVIEW
```

Review whether the OS is improving clarity, follow-through, admin, business progress, and relationships.

```text
AXIS: DRAFT LANDING PAGE
```

Draft a landing page using the structure and quality checks in `DEVELOPER.md`.

```text
AXIS: REVIEW COPY
```

Review and improve copy for clarity, positioning, brand correctness, and overclaiming.

```text
AXIS: POSITIONING CHECK
```

Check offer positioning before making copy public.

```text
AXIS: FINAL COPY PASS
```

Clean wording, remove hype, and check brand consistency.

## Operating Standard

Every session should create at least one of:
- a decision
- a next action
- an updated tracker
- a clearer plan
- a useful draft
- a closed loop

## Test Logging

After each live test, update:

`LIVE_TEST_LOG.md`
