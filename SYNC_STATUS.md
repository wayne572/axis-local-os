# AXIS Sync Status

Status: active
Last reviewed: 2026-05-17
Purpose: Prevent drift between the Codex working copy and Wayne's master OS folder.

## Source-Of-Truth Decision

Current master OS:

`D:\Wayne AI OS\Axis OS_v4`

Current Codex optimisation copy:

`D:\Axis AI - ChatGPT OS\AXIS_OS_CODEX_CURRENT`

Decision:

The Codex copy is the GitHub-backed optimisation workspace. Axis OS v4 has now been created in Wayne's master OS folder and mirrored into this GitHub-backed repo.

Current active master:

`D:\Wayne AI OS\Axis OS_v4`

Previous master:

`D:\Wayne AI OS\Axis OS_v3` - superseded fallback only.

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
| 2026-05-17 | Created Sonjie Francis V4 Solo OS build at `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/CLIENT_READY_SOLO_BUILDS/SONJIE_FRANCIS_CARE_CREATOR_SOLO_OS`, tailored to care rota/workplace process and TikTok/content direction, updated client/workstream indexes, and mirrored it into Codex repo | synced to master and GitHub |
| 2026-05-17 | Updated Codex-specific OS guidance (`AGENTS.md`, `CODEX.md`, `CODEX_USER_GUIDE.md`) to use Axis OS v4 logic, V4 infrastructure files, and `D:\Wayne AI OS\Axis OS_v4`; synced the same files back to Wayne's V4 master folder | synced to master and GitHub |
| 2026-05-17 | Created `D:\Wayne AI OS\Axis OS_v4` from v3, added `CORE/AXIS_INFRASTRUCTURE`, updated V4 entry files, backed up v3, mirrored V4 into GitHub repo, and pushed `main` to `wayne572/axis-local-os` | synced to master and GitHub |
| 2026-05-16 | Added voice transcript correction with `--transcript`; synced to Wayne AI OS and verified corrected voice ask | synced to master |
| 2026-05-16 | Activated RAG in `D:\Wayne AI OS\Axis OS_v3` by building `.kb/index.json`; synced conditional authority-boost search fix into master; verified Wayne Copilot and pricing retrieval plus sourced answer | synced to master |
| 2026-05-16 | Refreshed `D:\Wayne AI OS\Axis OS_v3` from Codex/GitHub `main` at `c22b632`; copied 499 tracked files without deleting master-only material | synced to master |
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

Run the V4 acceptance checks:

- live Claude startup test
- infrastructure review
- Client OS test
- Solo Operator test
- idea-to-memory workflow test
