# Greenfield Ops — Workflows

Per-client workflow set, derived from `business/WORKFLOW_LIBRARY.md` patterns and adapted to this client's stated priorities.

## Workflow: Client Onboarding (organised)

Purpose: Standardise the new-client onboarding process for Greenfield Ops.

Trigger: A new client is closed.

Steps:
1. Capture intake.
2. Confirm scope and stage.
3. Schedule onboarding session.
4. Issue welcome materials.
5. Move to delivery stage.

Outputs: Client moved from "closed / intake sent" to "build in progress" with intake on file.

Notes: Adapted from WORKFLOW_LIBRARY New Lead + Active Client Work patterns.

---

## Workflow: Delivery Tracking

Purpose: Ensure all delivery items are visible and progressed.

Trigger: Delivery stage begins.

Steps:
1. Populate `DELIVERY_CHECKLIST.md` from this file + `CLIENT_DELIVERY_PACK.md` + onboarding outputs.
2. Assign responsible party per item.
3. Update status as items move (Not Started → In Progress → Completed / Blocked).
4. Log activity to `TRACKER/DELIVERY_LOG.md` (when activated).
5. Surface blockers; capture explanations outside the checklist.

Outputs: Up-to-date checklist with evidence per Completed item.

---

## Workflow: Handover Preparation

Purpose: Ensure handover is clean and the client is ready to operate.

Trigger: Delivery items substantially complete.

Steps:
1. Validate `DELIVERY_CHECKLIST.md` per its rules.
2. Run walkthrough per `POST_LOCK_SUPPORT.md` Stage 1.
3. Confirm GDPR acknowledgement logged.
4. Execute Day-7 lock procedure per `handover.md` Section 10.
5. Transition to LOCKED state.

Outputs: Locked deployment; client owns ongoing use.
