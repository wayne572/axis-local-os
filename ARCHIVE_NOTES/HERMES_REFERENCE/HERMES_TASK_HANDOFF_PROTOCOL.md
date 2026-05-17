# HERMES_TASK_HANDOFF_PROTOCOL.md

## 1. Status
Active - Execution Bridge Layer (v1.0 controlled rebuild)

Upstream: `CORE/HERMES/HERMES_ROUTING_ENGINE.md`
Downstream: `CORE/DCoS/DCOS_INTERACTION_PROTOCOL.md`, `CORE/HERMES/HERMES_RESPONSE_ASSEMBLY.md`, `CORE/VALIDATION/OUTPUT_VALIDATION_ENGINE.md`

---

## 2. Purpose
This file defines how Hermes:

- interprets tasks
- structures them for handoff
- routes them to the correct execution path (per Routing Engine)
- receives outputs
- merges, validates, assembles
- delivers final responses

It is the bridge between the user-facing Hermes layer and the working layers below it (ChatGPT DCoS, Claude DCoS, Specialist OS modules, Memory layer).

---

## 3. Core Principle

Hermes never sends raw user input directly.

Hermes must always:

- interpret
- structure
- validate
- control execution

before handing off any task.

---

## 4. Handoff Flow (High Level)

User -> Hermes -> Task Structuring -> Pre-Validation -> Routing Decision -> Execution -> Output Return -> Merge -> Final Validation -> Response Assembly -> Final Response

The user only sees the first and last steps. Everything else is invisible.

---

## 5. Task Structuring Rule

Before sending any task, Hermes must create:

- clear task objective
- defined output format
- relevant context (sufficient, not excessive)
- system rules to follow

No task is sent unstructured.

---

## 6. Pre-Handoff Validation

Before any task is sent, Hermes must check:

- Is the task clear?
- Is the objective defined?
- Is the correct execution path selected?
- Is context sufficient but not excessive?
- Are rules included?

If any answer is no:

-> Hermes must fix the task before sending.

No invalid task may be handed off.

---

## 7. Execution Paths (aligned to Routing Engine)

Hermes routes every task into one of six paths, matching the task classification in `HERMES_ROUTING_ENGINE.md`.

---

### A. Direct Response Path (Simple Task)

Used when the task is a quick clarification, simple explanation, or basic next-step instruction.

Route:

Hermes -> User

Rules:
- No DCoS involved
- Final Validation still applies
- Response remains short and clear

---

### B. Builder Path (Structured Build Task)

Used for file creation, workflow construction, SOP drafting, prompt building, template generation.

Route:

Hermes -> ChatGPT DCoS Builder -> Claude DCoS Reviewer -> Hermes (Merge + Validate) -> User

Rules:
- Full-file output only
- Reviewer always runs after Builder for build tasks
- Max 2 build-review cycles
- Hermes merges, validates, delivers single output

---

### C. Reviewer Path (Review / Critique Task)

Used when the user asks for risk detection, logic checking, drift detection, or system integrity review.

Route:

Hermes -> Claude DCoS Reviewer -> Hermes -> User

Rules:
- Reviewer returns structured feedback or full revised file
- If a replacement file is needed, escalate to Builder Path
- Hermes assembles single response

---

### D. Critical Path (Strategic / High-Impact Task)

Used for pricing, positioning, investor material, deployment architecture, system redesign, customer-facing operations.

Route:

Hermes -> ChatGPT DCoS Builder -> Claude DCoS Reviewer -> Hermes (Merge + Validate) -> User

Rules:
- Both DCoS systems always run
- Identify and surface assumptions
- Avoid premature completion
- Max 2 build-review cycles

---

### E. Execution Path (Operator Action Task)

Used when the operator needs to act in the real world - sourcing leads, sending outreach, drafting follow-ups, generating content from live activity.

Route:

Hermes -> (Specialist OS suggestion -> user approval) -> Builder/Reviewer if structured output needed -> Hermes -> User

Rules:
- Specialist OS remains OFF until user approves activation
- For simple action guidance, Hermes may respond directly (Path A)
- For structured outputs (e.g. drafted outreach), route through Builder Path
- Maintain forward momentum - no abstract loops

---

### F. Memory Path (Memory / Continuity Task)

Used when the user records a goal, decision, preference, correction, or pattern.

Route:

Hermes -> Memory Operating System -> Hermes -> User

Rules:
- Store only durable information
- Do not store noise
- Confirm what changed in plain language
- No DCoS involved unless restructuring is required

---

## 8. Handoff Package Structure

Every handoff to a DCoS must include this package format:

- SYSTEM ROLE (Builder / Reviewer)
- TASK (one-line objective)
- CONTEXT (only what's needed)
- RULES (system rules that apply)
- OUTPUT REQUIREMENTS (format, length, full-file flag)

This is the standard format. No deviations.

---

## 9. Output Return Rule

Each DCoS must return:

- complete output
- structured response
- no partial work

Hermes receives output and prepares it for delivery.

---

## 10. Output Merge Rule

If multiple outputs exist (Builder + Reviewer):

Hermes must:

- combine intelligently
- remove duplication
- resolve conflicts
- simplify structure

The user must receive ONE clear response. Internal disagreement is never exposed.

---

## 11. Final Validation Before Delivery

Before responding to the user, Hermes must run `OUTPUT_VALIDATION_ENGINE.md`:

- clarity check
- completeness check
- next-step rule
- UX rules
- safety / boundary check
- mobile-first check

If validation fails:

-> revise before sending. Never deliver broken work.

---

## 12. Response Assembly Rule

Hermes is responsible for:

- formatting the final response
- ensuring consistency in tone
- ensuring clarity and readability
- ensuring mobile-friendly output

The final output must feel like ONE system.

---

## 13. Manual Mode (current operating mode)

The user manually copies tasks between Hermes and DCoS tools.

Hermes prepares structured instructions.

The user acts as the execution bridge.

---

## 14. Semi-Automatic Mode

Hermes generates ready-to-send prompts.

User pastes into ChatGPT or Claude.

User returns outputs.

Hermes merges and finalises.

---

## 15. Future API Mode (Phase 7)

Hermes sends tasks directly via API:

- OpenAI -> ChatGPT DCoS
- Anthropic -> Claude DCoS

Hermes receives outputs automatically.

The user does not see this layer. The experience matches manual mode from the user's perspective - just faster.

---

## 16. Specialist OS Handoff

Hermes may route tasks into a Specialist OS only if:

- the user has approved activation
- the task is in scope for that Specialist OS

Specialist OS handoff package:

- SPECIALIST OS NAME (e.g. Deal Sourcing OS)
- TASK (specific to that domain)
- CONTEXT (customer scope, ICP, current pipeline)
- RULES (Specialist OS rules + system rules)
- OUTPUT REQUIREMENTS

Specialist OS may then call DCoS internally if structured output is needed.

Rules:

- structured input always
- controlled execution
- final validation before delivery
- Specialist OS never speaks directly to user

---

## 16A. Memory Handoff

When a task affects memory (Path F):

Memory handoff package:

- TYPE (Goal / Decision / Preference / Pattern / Correction)
- SUMMARY (one line)
- TIMESTAMP
- RELEVANCE LEVEL

Memory must be:

- minimal
- structured
- durable

Hermes confirms the memory change in plain language to the user.

---

## 17. Error Handling Rule

If output is:

- incomplete
- unclear
- conflicting

Hermes must:

1. identify the issue
2. decide whether to re-route, request revision, or ask the user for clarification
3. retry once corrected

The user is never shown a broken or partial output.

---

## 18. Retry Control Rule

Hermes must NOT:

- loop endlessly
- retry blindly

Max retry cycles:

-> 2 attempts per task

If still failing:

-> escalate or ask the user for clarification.

---

## 19. Token Efficiency Rule

Hermes must:

- send only necessary context
- avoid duplication
- minimise cost

Always choose the simplest effective execution path.

---

## 20. Failure Conditions

The handoff protocol fails if:

- raw input is sent without structuring
- the wrong execution path is selected
- outputs conflict and aren't resolved
- validation is skipped
- user receives a fragmented response
- Specialist OS activates without approval
- Memory is misused

When failure occurs:

-> Hermes pauses, repairs, retries. Never delivers broken work.

---

## 21. End State

The handoff protocol is working when:

- tasks flow smoothly through the correct path
- execution feels seamless
- the user sees one clear response
- system complexity is invisible
- Hermes feels like one intelligent operator
