# DRIFT_BACKLOG.md

Status: cleared
Owner: @wayne572
Created: 2026-05-17
Cleared: 2026-05-17

## Status

All six pricing-drift items have been resolved. The DRIFT EXEMPT list in `tools/ci/check_drift.sh` is empty. The strict pricing guard now covers every live markdown file.

## Cleared Items

| # | File | Resolution |
|---|---|---|
| 1 | `DEVELOPER.md` | Pricing Rules section replaced with current ladder pointing to `business/PRICING_AUTHORITY.md`. Note added that Relationship Connector Mode is retired. |
| 2 | `PROJECTS/SFW_PROJECT_SOLUTIONS/offer/PRICING_AND_VALUE_GUIDE.md` | Full rewrite. Five-offer ladder, recommended default tiers in bold, Audit-to-Build conversion clause, Bundle path added, Connector Path replaced with OS Care Plan Path. |
| 3 | `PROJECTS/SFW_PROJECT_SOLUTIONS/offer/SME_AI_AUDIT_FUNNEL.md` | Audit price line replaced with ladder. Build entry price updated to GBP 6,500 (Foundation). Bundle option added. |
| 4 | `PROJECTS/SFW_PROJECT_SOLUTIONS/proposals/IMPLEMENTATION_PROPOSAL_TEMPLATE.md` | Pricing table replaced with five-offer ladder. Connector row removed. Quarterly-support field removed; monthly OS Care Plan retained. Tier selection field added. |
| 5 | `.../NO_CODE_DELIVERY_PLANS/02_SME_AI_AUTOMATION_AUDIT_DELIVERY_PLAN.md` | Header price line replaced with Audit ladder. Status moved from `active draft` to `active`. |
| 6 | `.../NO_CODE_DELIVERY_PLANS/04_RELATIONSHIP_CONNECTOR_MODE_DELIVERY_PLAN.md` | Reframed from standalone-offer delivery plan to workflow pattern reference. Status: `retired as standalone offer - reference only`. Pointed at OS Care Plan. |

## Source Of Truth

`business/PRICING_AUTHORITY.md`

## Next Time

If new drift is surfaced by CI, recreate this file as an active backlog and follow the cleanup process from the previous version (commit history).
