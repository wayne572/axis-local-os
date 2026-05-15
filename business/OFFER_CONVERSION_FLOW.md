# OFFER CONVERSION FLOW

## STATUS
Optional OS — Inactive by default

Activation:
- Must be explicitly enabled during onboarding (Sales OS activation)
- If not activated, DCoS blocks all routing into this system

---

## PURPOSE

The Offer Conversion Flow defines how a qualified lead progresses from:

→ interest → clarity → decision

This system provides **decision structure**, not commercial content.

---

## SYSTEM POSITION

Acquisition → Conversion → Onboarding → Delivery

---

## ENTRY CONDITION

This flow begins only when:

- A lead has been captured through CLIENT_ACQUISITION_SYSTEM.md
- The lead is engaged (active conversation or intake initiated)

No cold or unqualified leads may enter this flow.

---

## STEP 1 — PROBLEM CLARIFICATION

Objective:
Ensure the prospect clearly understands their problem.

Actions:

- Confirm problem statement
- Validate context
- Clarify impact

Rules:

- Do not introduce solutions prematurely
- Do not frame offers

---

## STEP 2 — SOLUTION FRAMING

Objective:
Present a structured way forward.

Actions:

- Explain approach
- Outline process
- Describe expected transformation (non-quantified)

Rules:

- No pricing references
- No packages or tiers
- No guarantees

---

## STEP 3 — FIT CONFIRMATION

Objective:
Determine whether the prospect is suitable.

Signals:

- Alignment with system capability
- Readiness to proceed
- Mutual understanding

Outcomes:

- Fit → proceed
- Not fit → exit flow

---

## STEP 4 — DECISION PROMPT

Objective:
Move from discussion to decision.

Actions:

- Present clear next step
- Ask for confirmation of intent

Rules:

- No pressure tactics
- No urgency manipulation
- No artificial scarcity

---

## STEP 5 — CONVERSION EVENT

Definition:

The moment a prospect agrees to proceed.

System action:

- Create CLIENTS/<slug>/
- Trigger CLIENT_ONBOARDING_FLOW.md

Restrictions:

- No pricing stored
- No payment handling
- No commercial terms recorded

---

## ROUTING RULES

Allowed:

→ CLIENT_ONBOARDING_FLOW.md

Blocked:

- Direct to delivery
- Direct to handover
- Direct to system access

---

## LOGGING (OPTIONAL — CONVERSION_LOG)

If enabled:

Log file:

TRACKER/CONVERSION_LOG.md

Each entry must include:

- timestamp
- lead_source
- client_slug (if created)
- decision_status (proceed / not proceed)

Exclusions:

- pricing
- deal value
- revenue

---

## ACTIVATION CONTROL

This system is OFF by default.

Activation requires:

- Explicit selection during onboarding
- Sales OS activation

DCoS must:

- Confirm activation before routing
- Block usage if inactive

---

## SYSTEM BOUNDARIES

This system must remain separate from:

- CLIENT_ACQUISITION_SYSTEM.md (lead generation)
- CLIENT_ONBOARDING_FLOW.md (setup)
- DELIVERY systems

No overlap allowed.

---

## COMPLIANCE + LIABILITY

- No guarantees may be implied
- No outcomes may be represented as certain
- No commercial commitments are formalised here

Axis AI provides structure only.

Client is responsible for:

- communication
- decision handling
- any commercial agreement outside this system

---

## FAILURE CONDITIONS

DCoS must halt flow if:

- Unqualified leads enter
- Pricing language appears
- Offers are embedded
- Flow is used without activation
- Routing bypasses onboarding

---

## END STATE

Conversion is complete when:

- Prospect agrees to proceed
- CLIENTS/<slug>/ is created
- Onboarding is triggered
