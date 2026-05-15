# CLAUDE_OPERATOR CORE - TESTING WORKFLOW

## 1. Status
Active - Build Validation Layer

---

## 2. Purpose
This file defines how to test the Claude Core System before moving on to the next build phase.

The goal is to confirm that the rules in the Claude files actually produce the right behaviour in real conversation - not just on paper.

If a test fails, the related Core file is updated, and the test is re-run.

---

## 3. Core Principle

A system is only as good as the behaviour it produces.

If the rules are correct but the behaviour is wrong:

-> the rules need fixing.

Testing makes this visible.

---

## 4. Testing Flow

1. Pick a test scenario
2. Run it through Claude (in current manual mode)
3. Compare the response against the expected behaviour
4. Mark Pass or Fail
5. If Fail - fix the related Core file, re-run

---

## 5. What to Test

The Claude Core System has six behaviour areas. Each must be tested.

- **Conversation** - tone, clarity, structure
- **Routing** - task classification, AI selection
- **Specialist OS Activation** - off by default, suggested only when relevant
- **Memory** - what is remembered, what is ignored
- **Task Handoff** - structured packages, no raw input passed downstream
- **Response Assembly** - one voice, clear next step

---

## 6. Test Scenarios

### A. Conversation Tests
1. Send a vague request: "help me with my business."
   -> Expected: Claude asks 1-2 simple clarifying questions. Does not guess.

2. Send a clear simple request: "what's a good way to track tasks?"
   -> Expected: short direct answer, short explanation, clear next step.

3. Send a messy multi-topic request.
   -> Expected: Claude splits it, confirms order, handles one at a time.

---

### B. Routing Tests
4. Ask for a creative draft: "write me a LinkedIn post about consulting."
   -> Expected: routed to ChatGPT-style execution. User never told.

5. Ask for a logic check: "review this plan for risks."
   -> Expected: routed to Claude-style execution. User never told.

6. Ask for a build + review: "draft my outreach email and stress-test it."
   -> Expected: dual execution, one merged response.

---

### C. Specialist OS Activation Tests
7. Talk casually about marketing once.
   -> Expected: no Specialist OS activation. Claude responds normally.

8. Repeatedly ask about sales process and pipeline.
   -> Expected: Claude suggests Sales OS activation, explains why, asks for approval.

9. Reply "yes" to activation.
   -> Expected: Claude confirms activation scope (this task only / session / project).

10. Change topic mid-session after activation.
    -> Expected: Claude deactivates the Specialist OS and says so plainly.

---

### D. Memory Tests
11. State a goal: "I want to focus on growing my consulting business."
    -> Expected: stored as Goal. Reused silently in future responses.

12. State a one-off detail: "today I'm at a coffee shop."
    -> Expected: not stored. Treated as ephemeral.

13. Correct a previous answer: "actually, I prefer plain English, drop the jargon."
    -> Expected: stored as Correction. Future responses reflect it.

14. Ask Claude to forget something.
    -> Expected: Claude confirms removal.

---

### E. Task Handoff Tests
15. Send a complex build request.
    -> Expected: Claude does not pass raw input to DCoS. Pre-handoff validation runs. A structured package is created.

16. Force a failing output (e.g. give contradictory instructions).
    -> Expected: Claude retries up to 2 times, then asks the user for clarification.

---

### F. Response Assembly Tests
17. Trigger a dual-execution task.
    -> Expected: one merged response. No "ChatGPT said / Claude said" framing.

18. Ask a long question that needs detail.
    -> Expected: summary first, then structured detail, ending with a clear next step.

19. Read responses on a phone.
    -> Expected: short paragraphs, mobile-friendly, no walls of text.

20. Ask something Claude cannot confidently answer.
    -> Expected: Claude admits uncertainty and asks a clarifying question.

---

## 7. Pass / Fail Criteria

For each test, mark:

- **Pass** - behaviour matched the expected outcome.
- **Fail** - behaviour did not match. Note what happened.

A test fails if:
- the user has to ask twice for clarity
- a Specialist OS activates without approval
- the response is fragmented or feels like multiple voices
- the next step is missing
- raw user input was forwarded to a DCoS unchanged
- memory was misused (stored noise or missed a real signal)

---

## 8. Fix Loop

When a test fails:

1. Identify which Core file owns the rule that broke.
2. Update that file (full-file replacement - no patches).
3. Re-run the failing test.
4. If it now passes, move on. If not, repeat.

Owner files by area:

- Conversation -> CLAUDE_OPERATOR_CONVERSATION_ENGINE.md
- Routing -> CLAUDE_OPERATOR_ROUTING_ENGINE.md
- Specialist OS -> CLAUDE_OPERATOR_SPECIALIST_OS_ACTIVATION.md
- Memory -> MEMORY_OPERATING_SYSTEM.md
- Task Handoff -> CLAUDE_OPERATOR_TASK_HANDOFF_PROTOCOL.md
- Response Assembly -> CLAUDE_OPERATOR_RESPONSE_ASSEMBLY.md

---

## 9. Test Log Format

For each run, log:

```
Test #: [number]
Date: [date]
Scenario: [short description]
Expected: [what should happen]
Result: [what happened]
Pass / Fail: [mark]
Notes: [if failed, which file needs updating]
```

Test logs save to:
`AXIS_AI_v4/TESTING/LOGS/`

---

## 10. Exit Criteria

The Claude Core System passes testing when:

- all 20 scenarios pass on the same run
- no Specialist OS activates without user approval
- every response includes a clear next step
- memory captures only what should be captured
- the user never sees the seam between ChatGPT DCoS and Claude DCoS

Once passed:

-> the system is ready for the next build phase

---

## 11. Failure Conditions

The testing layer has failed if:

- tests are skipped to move forward
- failed tests are not logged
- fixes are made without re-running the test
- partial fixes are applied (patches instead of full-file replacement)

If any of these happen, pause and reset the test cycle.

---

## 12. End State

Testing is working when:

- the rules in the Claude Core files match the behaviour in real use
- failures are caught early
- the user experience is consistent across every test scenario
- the system is ready to build on, not patch on

Stable foundation. Confident next phase.
