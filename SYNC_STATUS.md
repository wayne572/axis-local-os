# AXIS Sync Status

Status: active
Last reviewed: 2026-05-13
Purpose: Prevent drift between the Codex working copy and Wayne's master OS folder.

## Source-Of-Truth Decision

Current master OS:

`D:\Wayne AI OS\Axis OS_v3`

Current Codex optimisation copy:

`D:\Axis AI - ChatGPT OS\AXIS_OS_CODEX_CURRENT`

Decision:

The Codex copy is the active optimisation workspace. Changes made here are not automatically live in the master OS until reviewed and copied back to `D:\Wayne AI OS\Axis OS_v3`.

## Sync-Critical Files

These files must be reviewed before treating the master OS as updated:

| File | Direction | Status |
|---|---|---|
| `CLAUDE.md` | Codex -> master after review | pending sync review |
| `START_HERE.md` | Codex -> master after review | pending sync review |
| `README.md` | Codex -> master after review | pending sync review |
| `AGENTS.md` | Codex authority; optionally sync summary into master docs | Codex updated 2026-05-13 |
| `CODEX.md` | Codex-only unless master needs Codex instructions | Codex authority |
| `business/OFFERS.md` | Codex -> master after review | updated to current catalogue, pending sync review |
| `business/BRAND.md` | Codex -> master after review | updated commercial path, pending sync review |
| `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/CURRENT_TEMPLATE_POINTERS.md` | Codex -> master after review | updated Growth/Solo template pointers, pending sync review |
| `CLIENT_SAFE_DISTRIBUTION.md` | Codex -> master after review | pending sync review |
| `business/TRACKING/ACTIVE_WORKSTREAMS.md` | Codex -> master after review | pending sync review |
| `PROJECTS/SFW_PROJECT_SOLUTIONS/tracking/AI_ROI_TRACKER.md` | Codex -> master after review | pending sync review |
| `PROJECTS/SFW_PROJECT_SOLUTIONS/tracking/CLIENT_PROOF_LOG.md` | Codex -> master after review | new file, pending sync review |

## Recent Codex Changes To Review

| Date | Change | Master sync status |
|---|---|---|
| 2026-05-11 | Optimisation scan report created | not required for live OS unless Wayne wants it in master |
| 2026-05-11 | SCC Homes proof captured | pending sync |
| 2026-05-11 | Sonjie rota proof captured | pending sync |
| 2026-05-11 | Sonjie TikTok proof captured | pending sync |
| 2026-05-11 | Client-safe distribution spec updated | pending sync |
| 2026-05-11 | Current template pointers added | pending sync |
| 2026-05-11 | Archive guardrails added | pending sync |
| 2026-05-11 | Live test results tracker added | pending sync |
| 2026-05-11 | Pricing and legal review tracker added | pending sync |
| 2026-05-11 | Axis final sales, delivery, audit, and mobile client success documentation created | final docs created outside OS; Claude handoff added |
| 2026-05-11 | Claude/Codex session handoff files added for final documentation pickup | ready for Claude pickup |
| 2026-05-13 | Business Bible created: `final-docs-drafts/AXIS_AI_OS_BUSINESS_BIBLE.md` | final docs source; referenced from Codex OS |
| 2026-05-13 | Mobile Business Bible created: `final-docs-drafts/AXIS_AI_OS_BUSINESS_BIBLE_MOBILE.html` | final docs source; referenced from Codex OS |
| 2026-05-13 | Master delivery SOP created: `final-docs-drafts/AXIS_BUILD_DELIVERY_MASTER_SOP.md` | final docs source; referenced from Codex OS |
| 2026-05-13 | Canonical Client OS template updated with Growth blueprint, role map, acceptance tests, adoption plan, handover script, change control, sample records, and shipping checklist | pending master sync review |
| 2026-05-13 | Canonical Solo Operator template updated with simple guide, first 7 days guide, acceptance tests, shipping checklist, and platform notes | pending master sync review |
| 2026-05-13 | Active OS entry points updated to reference Business Bible, mobile HTML, Master SOP, OS Care Plan, and current canonical templates | pending master sync review |

## Sync Rule

Before copying anything to master:

1. Confirm the Codex file is current.
2. Confirm the matching master file has not changed independently.
3. Copy only reviewed files.
4. Record the sync in this file.
5. Do not sync archive material, duplicate builds, or generated ZIP/PDF artefacts unless Wayne explicitly asks.

## Next Sync Action

Review current Business Bible and delivery SOP first:

`D:\Axis AI - ChatGPT OS\final-docs-drafts\AXIS_AI_OS_BUSINESS_BIBLE.md`

`D:\Axis AI - ChatGPT OS\final-docs-drafts\AXIS_BUILD_DELIVERY_MASTER_SOP.md`

Mobile reading version:

`D:\Axis AI - ChatGPT OS\final-docs-drafts\AXIS_AI_OS_BUSINESS_BIBLE_MOBILE.html`

Then review earlier handoff if needed:

`D:\Axis AI - ChatGPT OS\AXIS_WAYNE_AI_OS_HANDOFF_2026-05-11.md`

After Wayne signoff, copy the updated OS entry points, offers file, brand file, template pointers, and canonical template additions into the master OS folder if that folder is still being used as the master.
