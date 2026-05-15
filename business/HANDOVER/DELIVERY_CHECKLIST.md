# DELIVERY CHECKLIST

## STATUS
Active — Post-Onboarding

---

## PURPOSE

This checklist ensures all required delivery actions are:

- clearly defined
- tracked
- completed before handover lock

It acts as the **execution assurance layer**.

---

## SOURCE OF TRUTH

This checklist is derived from:

- CLIENT_WORKFLOWS.md
- CLIENT_DELIVERY_PACK.md
- Onboarding outputs

No items should be added without a source.

---

## STRUCTURE

Each checklist item must follow this format:

- [ ] ITEM_NAME
  - Description:
  - Source: (workflow / delivery pack reference)
  - Responsible: (client / operator)
  - Status: Not Started / In Progress / Completed / Blocked

---

## CHECKLIST

### PHASE 1 — INITIAL DELIVERY

- [ ]
  - Description:
  - Source:
  - Responsible:
  - Status: Not Started

---

### PHASE 2 — CORE DELIVERY

- [ ]
  - Description:
  - Source:
  - Responsible:
  - Status: Not Started

---

### PHASE 3 — FINALISATION

- [ ]
  - Description:
  - Source:
  - Responsible:
  - Status: Not Started

---

## STATUS RULES

- Items must not be marked "Completed" unless:
  - Action is executed
  - Output exists (if applicable)

- "Blocked" must include explanation outside this file (log or notes)

- No assumed completion

---

## HANDOVER REQUIREMENT

Before handover lock:

- All critical items must be marked Completed
OR
- Any incomplete items must be explicitly acknowledged during handover

This checklist is used as the **final validation reference**.

---

## LOGGING (DELIVERY_LOG)

All checklist activity must be logged.

Log file:

TRACKER/DELIVERY_LOG.md

Each log entry must include:

- timestamp
- client_slug
- checklist_item
- action (started / completed / blocked)
- responsible_party

---

## SYSTEM RULES

- No pricing references
- No revenue tracking
- No performance metrics
- No automation logic

---

## FAILURE CONDITIONS

DCoS must flag if:

- Checklist is missing
- Items are incomplete at handover without acknowledgement
- Items are marked completed without evidence
- Checklist does not reflect delivery scope

---

## END STATE

Delivery is complete when:

- Checklist items are completed or acknowledged
- Handover is executed
- System transitions to lock state

---

## MULTI-CLIENT NOTE (for future use)

In multi-client environments:

- Each client must maintain their own:
  `CLIENTS/<slug>/DELIVERY_CHECKLIST.md`

- No shared checklist allowed across clients

This system is currently operating in single-client mode unless explicitly expanded.
