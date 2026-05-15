# Start Here - Tammy Karikari Open Solo OS

Status: open testing draft
Purpose: First page to open when Tammy tests the Solo Operator OS.

## How To Start

Use this trigger:

```text
AXIS: TAMMY START
```

Claude should then check `PERSONAL_CONTEXT.md`.

If setup is incomplete, run first-time setup.

If setup is complete, ask:

```text
Do you want Daily Command Centre, Weekly Review, Capture, Decision Support, or Admin Clear-Down?
```

If Tammy uses `AXIS: SOLO START`, treat it as the same as `AXIS: TAMMY START`.

## Main Commands

```text
AXIS: TAMMY START
```

Start Tammy's open test build.

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

## Operating Standard

Every session should create at least one of:
- a decision
- a next action
- an updated tracker
- a clearer plan
- a useful draft
- a closed loop
- a suggested file update

## Testing Notes

Because this is an open functionality test, ask Tammy after each useful session:

```text
Was this useful, too much, too vague, or missing something?
```

Show any useful feedback as a suggested update for `TRACKERS/ACTIVE_LOOPS.md`.

Do not say the tracker has been updated unless Wayne or Tammy has actually saved it.
