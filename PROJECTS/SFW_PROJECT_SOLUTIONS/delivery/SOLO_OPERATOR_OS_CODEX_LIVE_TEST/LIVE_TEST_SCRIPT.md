# Live Test Script

Status: active
Purpose: Step-by-step test prompts for Solo Operator OS live testing.

## Test Rule

Run these tests in ChatGPT Codex using this live-test folder.

After each test, update `LIVE_TEST_LOG.md`.

## Test 1 - Startup

Prompt:

```text
AXIS: SOLO START
```

Expected result:
- Codex reads `PERSONAL_CONTEXT.md`.
- Codex sees setup is complete.
- Codex does not repeat first-time setup.
- Codex offers main choices: Daily Command Centre, Weekly Review, Capture, Decision Support, Admin Clear-Down, Business Builder.

## Test 2 - Daily Command

Prompt:

```text
AXIS: DAILY COMMAND
Today I need to review the partner HTML, decide the Solo Operator pricing message, reply to a potential partner, and tidy a few personal admin tasks. I have medium energy.
```

Expected result:
- top three priorities
- urgent admin
- follow-ups
- one business action
- one personal action
- energy-aware plan
- tracker update recommendation

## Test 3 - Capture

Prompt:

```text
AXIS: CAPTURE THIS
Idea: Solo Operator OS should be positioned as the permanent operating system for people who are tired of renting their business operations through subscriptions.
```

Expected result:
- idea summary
- category
- value
- minimum viable version
- next action
- state recommendation

## Test 4 - Decision

Prompt:

```text
AXIS: DECISION
Should I lock Solo Operator OS pricing at GBP 3,995 now, or keep it in review until after one live test?
```

Expected result:
- options
- trade-offs
- risks
- recommended next step
- what to stop or delay

## Test 5 - Admin Clear-Down

Prompt:

```text
AXIS: ADMIN CLEAR-DOWN
I need to review pricing, update the product manual, check legal wording, prepare a partner follow-up, and decide what to test next.
```

Expected result:
- categorised admin list
- risk flags
- smallest next action
- top three to clear first
- tracker update recommendation

## Test 6 - Business Builder

Prompt:

```text
AXIS: BUSINESS BUILDER
Help me turn Solo Operator OS into a sellable no-code product for solo consultants and freelancers.
```

Expected result:
- offer focus
- audience
- core promise
- first sales asset needed
- next action
- what remains in review

## Test 7 - Weekly Review

Prompt:

```text
AXIS: WEEKLY REVIEW
This week we built the product manual, outreach pack, simulations, pricing guide, no-code delivery plans, partner HTML, and this live-test build.
```

Expected result:
- wins
- open loops
- decisions needed
- admin backlog
- relationship follow-ups
- next week focus

## Test 8 - 30 Day Review

Prompt:

```text
AXIS: 30 DAY REVIEW
Run a pretend review as if I have been using Solo Operator OS for 30 days.
```

Expected result:
- clarity review
- follow-through review
- admin review
- business progress review
- relationship review
- system fit
- next 30-day actions

## Test 9 - Landing Page Draft And Edit

Prompt:

```text
AXIS: DRAFT LANDING PAGE
Draft a landing page for Solo Operator OS. It should sell the permanent ownership angle, avoid hype, explain who it is for, and make clear this is an operating system, not another AI chat tool.
```

Expected result:
- offer is clear in the first five seconds
- audience is specific
- permanent ownership angle is strong
- Wayne Francis / SF&W Project Solutions brand structure is correct
- Axis AI is treated as product/OS logic, not the trading company
- pricing is either omitted or marked in review
- CTA is simple
- copy avoids hype

Follow-up prompt:

```text
AXIS: FINAL COPY PASS
Review this landing page for clarity, positioning, offer fit, brand correctness, overclaiming, and missing CTA.
```

Expected result:
- copy is tightened without unnecessary rewriting
- changes are explained briefly
- final version is clean and publishable after Wayne review

## Pass Standard

The system passes when:
- output is specific
- next action is clear
- it references relevant trackers
- it avoids hype
- it respects boundaries
- it does not drift into general chatbot behaviour
- landing-page copy follows `DEVELOPER.md`
