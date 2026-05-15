# 08 - Testing And Signoff

Status: active draft
Purpose: Define how to test AXIS before use, sale, or handover.

## Testing Principle

Do not lock a product until it has been tested with realistic prompts.

Every test should check:
- startup
- routing
- output quality
- tracker behaviour
- boundaries
- handover readiness

## AXIS Core Test

Prompt:

```text
What is the current status?
```

Expected:
- Priority Pulse or workstream summary
- SF&W first
- Black Map excluded
- current blockers visible
- next action clear

## Client OS Test

Prompt:

```text
AXIS: NEW CLIENT
```

Expected:
- BUILD mode
- missing facts requested
- AI PA naming question asked once
- client OS template identified
- status marked `in review`
- no internal SF&W strategy included

## Solo Operator Test

Prompt:

```text
AXIS: SOLO START
```

Expected:
- setup check
- personal context requested
- AI PA naming question asked once
- daily / weekly / capture / decision routes available

Use full test plan:

`PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/SOLO_OPERATOR_OS_TEST_PLAN.md`

## Relationship Connector Test

Prompt:

```text
Run relationship pulse
```

Expected:
- follow-ups identified
- intro opportunities identified
- consent gates included
- relationship memory updated or update recommended

## Usage Tracking Test

Check:
- user is told what is tracked
- user can opt in or out where appropriate
- sensitive data is not collected unnecessarily
- improvement loop is clear
- legal wording is marked for review

## Signoff States

Use:
- active: being built
- in review: built but not approved
- locked: tested and approved
- archived: no longer active

## Lock Criteria

A product can be locked when:
- core files exist
- test plan passes
- offer wording is approved
- boundaries are documented
- usage tracking is reviewed
- handover process is clear
- Wayne signs it off

## Current Recommended Signoff

AXIS Claude Build:
active, needs full live test

Client OS Template:
active, needs sample client test

Solo Operator OS:
in review, needs Claude test and pricing decision

Usage Tracking:
active, needs legal wording review
