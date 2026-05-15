# DELIVERY CHECKLIST — Greenfield Ops

## STATUS
Active — Post-Onboarding

Source-of-truth files:
- `CLIENTS/greenfield_ops/CLIENT_WORKFLOWS.md`
- `CLIENTS/greenfield_ops/CLIENT_DELIVERY_PACK.md`
- `CLIENTS/greenfield_ops/ONBOARDING.md`

---

## CHECKLIST

### PHASE 1 — INITIAL DELIVERY

- [ ] Confirm intake captured and reviewed
  - Description: Verify INTAKE.md complete with Sections 1–7
  - Source: ONBOARDING.md (intake validation)
  - Responsible: operator
  - Status: Completed

- [ ] Activations recorded
  - Description: Verify ACTIVATIONS.md reflects Sales OS / Acquisition / Conversion as active
  - Source: ONBOARDING.md (Block G)
  - Responsible: operator
  - Status: Completed

---

### PHASE 2 — CORE DELIVERY

- [ ] Workflow set populated
  - Description: Three workflows (Client Onboarding / Delivery Tracking / Handover Preparation) defined per CLIENT_WORKFLOWS.md
  - Source: CLIENT_WORKFLOWS.md
  - Responsible: operator
  - Status: Completed

- [ ] Delivery pack documented
  - Description: All 6 pack-content items listed in CLIENT_DELIVERY_PACK.md
  - Source: CLIENT_DELIVERY_PACK.md
  - Responsible: operator
  - Status: Completed

- [ ] DELIVERY_LOG.md activation
  - Description: Operator confirms DELIVERY_LOG.md activation request to Wayne (file currently missing in TRACKER/)
  - Source: CLIENT_WORKFLOWS.md (Delivery Tracking workflow Step 4)
  - Responsible: operator
  - Status: Blocked

---

### PHASE 3 — FINALISATION

- [ ] Walkthrough material prepared
  - Description: Walkthrough script aligned with POST_LOCK_SUPPORT.md Stage 1 checklist
  - Source: CLIENT_WORKFLOWS.md (Handover Preparation workflow Step 2)
  - Responsible: operator
  - Status: In Progress

- [ ] GDPR acknowledgement logged
  - Description: data_ack row appended to TRACKER/GDPR_LOG.md
  - Source: ONBOARDING.md (GDPR responsibility model)
  - Responsible: client (acknowledgement) + operator (logging)
  - Status: Completed

- [ ] Handover record drafted
  - Description: HANDOVER.md created with Date / Slug / Checklist status / Waivers
  - Source: ONBOARDING.md (Handover expectation)
  - Responsible: operator
  - Status: In Progress

---

## STATUS RULES

- Items must not be marked "Completed" unless action is executed and output exists.
- "Blocked" must include explanation outside this file.
- No assumed completion.

## HANDOVER REQUIREMENT

Before lock: all critical items Completed (with evidence) OR incomplete acknowledged OR DCoS waiver granted. The Blocked item below must have an explanation outside this file before handover can complete.

---

## MULTI-CLIENT NOTE

This file is per-client at `CLIENTS/greenfield_ops/DELIVERY_CHECKLIST.md`. Conforms to the Multi-Client Note in the master template at `business/HANDOVER/DELIVERY_CHECKLIST.md`.
