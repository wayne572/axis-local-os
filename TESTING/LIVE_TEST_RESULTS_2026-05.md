# Live Test Results - May 2026

Status: active test tracker
Purpose: Record live AXIS tests before moving the enhanced build from `in review` to `locked`.

## Lock Rule

Do not mark AXIS OS Claude Build as `locked` until the required live tests pass or Wayne explicitly accepts the remaining risks.

## Required Tests

| Test | Prompt / Action | Status | Evidence | Next Action |
|---|---|---|---|---|
| OS startup test | `Run the OS startup test.` | pending | `TESTING/OS_STARTUP_TEST.md` | Run in Claude and paste results here |
| Client OS setup | `AXIS: NEW CLIENT` | pending | none yet | Run with fake/sample client |
| Solo Operator setup | `AXIS: SOLO START` | partially evidenced | Joseph, SCC Homes, Sonjie feedback show live value; formal live-test log still pending | Run formal template test and record result |
| Relationship capture | `AXIS: CAPTURE THIS` / relationship note | pending | none yet | Test manual capture before Telegram/WhatsApp |
| Client-safe version generator | Use `CLIENT_VERSION_GENERATOR_CHECKLIST.md` | pending | none yet | Run fake client packaging test |
| AI ROI review | Review SCC Homes and Sonjie proof | in progress | `AI_ROI_TRACKER.md`, `CLIENT_PROOF_LOG.md` | Run 30-day follow-up reviews |
| Governance check | Run client governance check | pending | governance pack exists | Test on fake/sample client |

## Live Proof Already Captured

| Date | Client / User | Proof Type | Status |
|---|---|---|---|
| 2026-05-10 | SCC Homes LTD | Live client feedback on shipped build | qualitative proof captured |
| 2026-05-11 | Sonjie Francis | 4-week care rota system feedback | qualitative proof captured |
| 2026-05-11 | Sonjie Francis | TikTok page review/content direction feedback | qualitative proof captured |

## Open Risks

- Live Claude startup test is not yet recorded.
- `AXIS: NEW CLIENT` test is not yet recorded.
- Client-safe distribution generation has not yet been tested.
- ROI impact is qualitative so far; measurable outcomes need follow-up.

## Next Test Action

Run `AXIS: NEW CLIENT` with a fake sample SME and record:

- route selected
- intake questions
- client-safe boundaries
- governance prompts
- handover pathway
- pass/fail decision

