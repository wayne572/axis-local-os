# Workflow Library (Axis OS v3)

Reusable workflow patterns for delivery, operations, and client execution.

---

## Workflow: <Name>

Purpose:
<what this workflow achieves>

Trigger:
<when this workflow is used>

Steps:
1.
2.
3.

Outputs:
<what gets produced>

Notes:
<optional constraints / variations>

---

This file will be populated during Phase 3 harvest.

---

## Workflow: New Lead

Purpose:
Capture and progress every new lead so nothing is lost on first touch.

Trigger:
A new lead comes in (form fill, referral, inbound message, networking contact, etc.).

Steps:
1. Log the lead in `PIPELINE.md` under Leads.
2. Set the lead stage (per `## Pipeline Stages Reference` — New / Contacted / Engaged / Qualified / Proposal).
3. Record the next action and owner.
4. Follow up within the defined timeframe for the current stage.
5. Update stage and last-contact after each meaningful interaction.

Outputs:
A current pipeline row with a clear next action and owner.

Notes:
If the lead converts to a client, transition stages per `## Client Stage Vocabulary` (Closed / Intake Sent → onwards).

---

## Workflow: Active Client Work

Purpose:
Keep ongoing client tasks visible, owned, and moving.

Trigger:
A client task or project is active (post-handover, in-flight delivery, or post-lock support work).

Steps:
1. Confirm current priority for the client.
2. Confirm owner of the next step.
3. Confirm next action and target completion.
4. Update status as work moves (`routed` → `in progress` → `awaiting review` → `done`).
5. Mark complete, or progress the client to the next stage in `## Client Stage Vocabulary`.

Outputs:
The work is current, visible in `PIPELINE.md` / `ACTIVE_CLIENTS.md`, and moving.

Notes:
If the client triggers a structural change request, route via DCoS to `spec-review` rather than absorbing into active work.

---

## Workflow: Weekly Review

Purpose:
Reset focus and surface delays before they compound.

Trigger:
End of the working week (or fixed weekly slot).

Steps:
1. Review the pipeline — leads and active clients.
2. Review active work — what's open, what's stuck.
3. Identify delays and blockers.
4. Reset priorities for the coming week.
5. Record next week's focus in the appropriate session-summary or weekly note.

Outputs:
An up-to-date system, a short list of priorities, and a clear set of blockers to resolve.

Notes:
Run `Status` (DCoS command) before the review to get a clean snapshot of `EXECUTION_TRACKER.md`.

---

## Workflow: Follow-Up

Purpose:
Ensure no lead, task, or client item sits without a next step.

Trigger:
A lead, task, or client item needs a response or next step (no recent contact, awaiting reply, or stage stalled).

Steps:
1. Check the current status in `PIPELINE.md` / `EXECUTION_TRACKER.md`.
2. Confirm what response or action is needed.
3. Send follow-up or take the action (route through `outreach` for messaging, with `qa` review for client-facing).
4. Record outcome.
5. Set the next action if the item is still open; close if resolved.

Outputs:
Every open item has a logged next step or is closed with a recorded outcome.

Notes:
Default cadence: 5–7 days for warm follow-up, longer for nurture. Client-facing follow-up messages go through `qa` before send.
