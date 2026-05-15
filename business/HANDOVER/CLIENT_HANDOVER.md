# CLIENT HANDOVER

## STATUS
Pending → Completed → Locked

---

## PURPOSE

This document formalises the transition of the system from Axis AI to the client.

It ensures:

- Delivery has been validated
- Responsibilities are clearly transferred
- Compliance awareness is acknowledged
- The system is moved into a LOCK state

---

## HANDOVER TRIGGER

Handover begins when:

- Onboarding is complete
- DELIVERY_CHECKLIST.md exists
- System is ready for final validation

---

## STEP 1 — CHECKLIST POPULATION (MANDATORY)

Before validation, the DELIVERY_CHECKLIST.md must be populated.

Population rules:

- All items must be derived from:
  - CLIENT_WORKFLOWS.md
  - CLIENT_DELIVERY_PACK.md
  - onboarding outputs

- Each item must include:
  - Description
  - Source
  - Responsible
  - Status

DCoS must halt if:

- Checklist is empty
- Items lack source attribution
- Delivery scope is not reflected

---

## STEP 2 — DELIVERY VALIDATION

The DELIVERY_CHECKLIST.md must be satisfied per its own rules:

- All critical items marked Completed (with evidence), OR
- Any incomplete items explicitly acknowledged during handover, OR
- An explicit DCoS waiver granted and logged

Additional rules:

- Items marked "Blocked" must have explanation recorded outside the checklist
- No item may be assumed complete

---

## STEP 3 — SYSTEM REVIEW

The client must be made aware of:

- What has been delivered
- What is not included
- Any incomplete or acknowledged items

This step ensures clarity — not sales or expansion.

---

## STEP 4 — RESPONSIBILITY TRANSFER

Upon completion of handover:

The client assumes full responsibility for:

- System usage
- Operational decisions
- Compliance execution
- Any modifications post-lock

Axis AI:

- Provides structure only
- Does not operate or manage the system post-handover

---

## STEP 5 — GDPR ACKNOWLEDGEMENT

The client must confirm:

- Understanding of data handling responsibilities
- That Axis AI does not provide compliance guarantees

This acknowledgement must be recorded in:

TRACKER/GDPR_LOG.md

---

## STEP 6 — HANDOVER RECORD

Record the following:

- Date of handover
- Client slug
- Checklist status (complete / acknowledged gaps)
- Any waivers applied

---

## STEP 7 — LOCK ACTIVATION

Once handover is complete:

System enters LOCK state.

Effects:

- No structural changes allowed
- No onboarding re-entry
- No delivery continuation

Allowed:

→ POST_LOCK_SUPPORT.md (if defined)

---

## FAILURE CONDITIONS

DCoS must halt handover if:

- DELIVERY_CHECKLIST.md is missing
- Checklist is not populated
- Validation rules are not met
- Responsibility transfer is unclear
- GDPR acknowledgement is missing

---

## END STATE

Handover is complete when:

- Delivery is validated
- Client responsibility is acknowledged
- GDPR acknowledgement is logged
- System is LOCKED
