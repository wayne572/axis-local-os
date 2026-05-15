# PHASE6_VIRTUAL_LIFECYCLE_TEST.md

## 1. Status
Active - Virtual Test Layer

---

## 2. Purpose
This test simulates the full Axis AI v4 lifecycle without real-world execution.

It allows:

- safe testing
- system validation
- behaviour analysis
- refinement before live use

---

## 3. Core Principle

Simulate reality as closely as possible.

Do NOT shortcut decisions.

Act as if everything is real.

---

## 4. Test Scope

This test covers:

Marketing OS
-> Deal Sourcing OS
-> Sales OS
-> Client Delivery OS

Optional:
Market Operator OS (separate simulation)

---

## 5. Test Mode

Virtual (no real outreach, no real clients)

You must:

- simulate realistic responses
- follow full workflows
- log decisions honestly

---

## 6. Test Scenario Setup

Define a simple test business:

Example:

Service:
"Helping small businesses get more clients"

Audience:
Local businesses

Problem:
Inconsistent lead flow

---

## 7. Lifecycle Simulation

### Stage 1 - Marketing OS

Create:

- 3 content ideas
- 3 posts
- expected audience reaction

Simulate:

- engagement
- inbound message

---

### Stage 2 - Deal Sourcing OS

Simulate:

- 5 leads identified
- 5 outreach messages sent

Create:

- 2 replies
  - 1 positive
  - 1 neutral

---

### Stage 3 - Sales OS

Simulate conversation:

- run discovery
- qualify lead

Decide:

- YES (good fit)
- NO (reject)

---

### Stage 4 - Client Delivery OS

For the accepted lead:

- simulate onboarding
- define delivery plan
- simulate progress
- simulate completion

---

## 8. Market Operator Simulation (Optional)

Run:

- 3 trade scenarios
- YES / NO decisions
- journal outcomes

No real trading.

---

## 9. Logging Requirements

You must log:

- decisions made
- why decisions were made
- what worked
- what felt unclear

---

## 10. Evaluation Criteria

Check:

- Was each step clear?
- Did Claude logic hold?
- Did OS boundaries stay intact?
- Was next step always obvious?
- Was anything confusing?

---

## 11. Output Format

At the end, produce:

### Summary

- what worked
- what broke
- what felt unclear

### System Gaps

- missing steps
- unclear logic
- friction points

### Improvement Actions

- small fixes only
- no major redesign

---

## 12. Failure Conditions

Test fails if:

- steps are skipped
- decisions are rushed
- system is not followed
- logging is incomplete

---

## 13. Success Criteria

Test is successful if:

- full lifecycle completed
- system felt usable
- logic held across all stages
- issues were clearly identified

---

## 14. End State

After this test, you should know:

- where the system is strong
- where it needs refinement
- whether it is ready for live use

This is the final check before real-world execution.
