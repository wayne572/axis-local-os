# Solo Operator OS Test Plan

Status: active
Purpose: Confirm the Solo Operator OS works before selling or handing it over.

## Test 1 - Startup

Prompt:

```text
AXIS: SOLO START
```

Expected result:
- Claude reads the Solo Operator OS instructions
- Claude checks whether setup is complete
- Claude asks the first-time setup questions if needed
- Claude asks whether the user wants to name the AI PA

## Test 2 - Daily Command

Prompt:

```text
AXIS: DAILY COMMAND
I have two calls, a proposal to write, three messages to reply to, and I need to book a dentist appointment.
```

Expected result:
- top three priorities
- admin action
- follow-ups
- personal action
- business action
- tracker update recommendation

## Test 3 - Idea Capture

Prompt:

```text
AXIS: CAPTURE THIS
I think I could sell a setup service for freelancers who keep missing follow-ups.
```

Expected result:
- idea summary
- category
- value
- minimum viable version
- next action
- state recommendation

## Test 4 - Decision Support

Prompt:

```text
AXIS: DECISION
Should I spend this week building a landing page or contacting five warm leads?
```

Expected result:
- options
- trade-offs
- risks
- recommendation
- next action

## Test 5 - Admin Clear-Down

Prompt:

```text
AXIS: ADMIN CLEAR-DOWN
I need to renew insurance, reply to HMRC, book a car service, and sort three invoices.
```

Expected result:
- categorised admin list
- risk flags
- smallest next action
- top three to clear first
- professional advice boundary if needed

## Test 6 - 30 Day Review

Prompt:

```text
AXIS: 30 DAY REVIEW
```

Expected result:
- review of clarity, follow-through, admin, business, relationships, and system fit
- next 30-day actions
- decision to keep, enhance, simplify, or archive unused parts

## Pass Criteria

The Solo Operator OS passes when:
- all trigger commands work
- Claude routes to the right module
- output is practical and specific
- tracker updates are recommended
- high-risk boundaries are respected
- the user leaves with a next action
