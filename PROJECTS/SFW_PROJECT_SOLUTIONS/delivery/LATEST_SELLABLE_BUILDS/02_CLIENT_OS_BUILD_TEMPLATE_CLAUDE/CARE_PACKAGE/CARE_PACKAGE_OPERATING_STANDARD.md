# AI OS Care Package Operating Standard

Status: template
Purpose: Define recurring care that keeps the client OS useful, current, safe, and governed.

## Care Package Promise

The client AI OS is operational infrastructure, not a one-time setup.

The care package keeps it:

- current
- safe
- useful
- aligned to client workflows
- governed as AI platforms and business processes change

## Monthly Care Review

Run monthly:

1. Review active workflows in `GOVERNANCE/AI_OS_CONTROL_REGISTER.md`.
2. Run `CARE_PACKAGE/MONTHLY_MEMORY_AUDIT.md`.
3. Update `CARE_PACKAGE/AI_USAGE_AND_ROI_TRACKER.md`.
4. Check platform changes using `CARE_PACKAGE/PLATFORM_CHANGE_WATCH.md`.
5. Review frozen, stale, or retired workflows.
6. Check whether master template updates should be selectively applied.
7. Record shipped-build changes in `CARE_PACKAGE/BUILD_UPDATE_LOG.md`.
8. Confirm new risks, value created, and next improvements.

## Care Outputs

Each care review should produce:

- changes made
- risks found
- memory updates approved or removed
- workflows improved
- measurable value
- build updates applied
- client decisions needed
- next review date

## Managed Build Rule

Treat every shipped build as a managed client OS, not a one-off folder.

Do not overwrite a shipped client build wholesale from the master template.

Use the delivery-level `TEMPLATE_UPDATE_REGISTER.md` to decide whether an update should be applied, then log the exact change in `CARE_PACKAGE/BUILD_UPDATE_LOG.md`.
