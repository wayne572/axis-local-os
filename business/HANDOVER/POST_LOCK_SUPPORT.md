# Post-Lock Support

> **Use:** Day 7+ rider for the `handover` agent. After a client deployment is locked (Day-7 lock procedure complete in `handover.md` Section 10), the work shifts from build to adoption. This file defines the two stages that happen *after* lock: walkthrough and early support.

---

## Stage 1 — Client Walkthrough

### Trigger
Deployment is locked (Day 7). Client is ready to be shown the system.

### Objective
Make sure the client understands how to use the system daily — confidence over completeness.

### Actions (checklist)
- [ ] Onboarding walkthrough completed
- [ ] Client understands daily use
- [ ] Client understands weekly review
- [ ] Questions answered (open ones captured as concrete items)

Plus, ad-hoc during the call:
- Show where AI helps and where it doesn't
- Identify any gaps that warrant a small post-lock fix

### Reads
- `business/CLIENTS/<client_slug>/PLAYBOOK.md` (multi-client) **or** `business/HANDOVER/PLAYBOOK_<slug>.md` (single-client)
- `business/CLIENTS/<client_slug>/BRAND.md`, `OFFERS.md`, `CONTENT_THEMES.md` — for talking points only
- `business/HANDOVER/COMPLIANCE_PROTOCOL.md` — for any compliance questions raised in the call

### Output
- `walkthrough_done` confirmation
- Open-questions list captured in the per-client risks file (`CLIENTS/<client_slug>/RISKS.md` or root `RISKS_AND_NOTES.md`)

### Review
- Any written guidance produced for the client → routed to `qa` before sending
- Recordings or scripts containing client data → handled per `GDPR_PROTOCOL.md`

---

## Stage 2 — Early Support

### Trigger
Walkthrough complete. Client begins using the system.

### Objective
Support adoption. Fix early friction. Confirm the system is real to the client, not a deck.

### Actions
- Confirm first real use (not a demo run)
- Collect feedback on what's working and what isn't
- Identify blockers; route them appropriately
- Refine system elements only when blockers are real (not pre-emptive polishing)

### Reads
- Per-client `RISKS.md` (or root `RISKS_AND_NOTES.md`)
- `business/EXECUTION_TRACKER.md` (filtered by client)
- `business/INPUTS/SESSION_SUMMARY.md`

### Output (checklist — within first week)
- [ ] Client is using the system
- [ ] No confusion reported
- [ ] Friction identified
- [ ] Improvements noted

Plus:
- Adoption confirmation logged
- Any new risks appended to the appropriate risks file

### Review
- External update to the client → `qa`
- Structural change to the deployed system → `spec-review`
- GDPR-relevant feedback (data handling, subject rights) → route to `gdpr`

---

## Routing

`handover` does not run these stages itself. After the Day-7 lock:

- DCoS dispatches each post-lock action to the appropriate specialist (`session-summary`, `qa`, `pipeline`, `gdpr`, `workflow` for fixes, etc.)
- `handover` may be re-invoked only to refresh the playbook or to log a post-lock risk

The deployment status in `ACTIVE_CLIENTS.md` stays `live` throughout post-lock. It changes to `paused` or `closed` only when the client says so.

---

## Final rule

Post-lock support is light by default. Walkthrough and early support exist to confirm adoption — not to extend the build.

If a client asks for new functionality during this period, it's a new scope, not a fix. Route accordingly via DCoS.

---

### Responsibility Reminder

The system provided is a structured operational framework.

All ongoing use, decisions, and actions taken using the system remain the responsibility of the client organisation.

Axis AI does not operate or manage the system after handover.
