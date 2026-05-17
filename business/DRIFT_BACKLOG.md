# DRIFT_BACKLOG.md

Status: active
Owner: @wayne572
Created: 2026-05-17
Purpose: Track pre-existing pricing drift surfaced by the production-line guard, pending Wayne sign-off on replacement wording.

## Why This File Exists

The CI drift guard (`tools/ci/check_drift.sh`) compares every live markdown file against `business/PRICING_AUTHORITY.md`. On the first scan it flagged real drift in client-facing files that still use superseded prices.

These files are **client-facing structural copy** (developer reference, offer guides, proposal templates, delivery plans). Per `CLAUDE.md` review enforcement, the wording for replacement copy is a Wayne decision, not an automated rewrite.

Until each is cleaned up, the file is listed under `DRIFT EXEMPT` in `tools/ci/check_drift.sh`. Remove it from that list as part of the cleanup commit.

## Drift Punch List

| # | File | Drift | Replace with |
|---|---|---|---|
| 1 | `DEVELOPER.md` (lines 195, 197) | `GBP 5,595` audit, `GBP 3,195/qtr` Relationship Connector | Audit ladder £2,500/£4,500/£6,500. Replace RCM line with OS Care Plan £750/£995/£1,495/mo. |
| 2 | `PROJECTS/SFW_PROJECT_SOLUTIONS/offer/PRICING_AND_VALUE_GUIDE.md` | `GBP 5,595` audit, `GBP 3,195/qtr` RCM, combined-bundle GBP 15,590 | Replace with current Audit ladder, Bundle ladder, and OS Care Plan ladder. |
| 3 | `PROJECTS/SFW_PROJECT_SOLUTIONS/offer/SME_AI_AUDIT_FUNNEL.md` | `GBP 5,595` audit price | Replace with Audit Core £4,500 (or Lite/Deep Dive range). |
| 4 | `PROJECTS/SFW_PROJECT_SOLUTIONS/proposals/IMPLEMENTATION_PROPOSAL_TEMPLATE.md` | `GBP 5,595` audit, `GBP 3,195/qtr` RCM | Use Audit ladder + OS Care Plan ladder. **Highest priority - this template goes to clients.** |
| 5 | `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/NO_CODE_DELIVERY_PLANS/02_SME_AI_AUTOMATION_AUDIT_DELIVERY_PLAN.md` | Header `Price: GBP 5,595, in review` | Replace with current Audit ladder. |
| 6 | `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/NO_CODE_DELIVERY_PLANS/04_RELATIONSHIP_CONNECTOR_MODE_DELIVERY_PLAN.md` | Header `Price: GBP 3,195 per quarter, in review` | Decision needed - retire delivery plan, or repoint to OS Care Plan ladder. |

## Cleanup Process

For each row:

1. Open the file, draft replacement wording referencing `business/PRICING_AUTHORITY.md`.
2. Apply via PR (DCoS Mode: BUILD, agents: messaging + qa).
3. Remove the file path from `DRIFT EXEMPT` in `tools/ci/check_drift.sh`.
4. CI must pass with the file no longer exempt.
5. Strike the row through (or delete it) once green.

## Source Of Truth

`business/PRICING_AUTHORITY.md`
