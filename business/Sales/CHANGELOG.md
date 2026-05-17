# Axis OS v2.1 — Changelog

Audit trail for v2.1. v2 baseline preserved at `D:\Wayne AI OS\Axis OS_v2\` (locked, untouched).

Discipline rules: see memory `feedback_axis_os_v2_change_discipline.md`.

---

## 2026-04-30 — Pricing Strip from Use Case Guide

### Changed — Removed £1,500 sprint price from comparison table
- **Files affected:**
  - `business/Sales/Axis_OS_v2_Use_Case_Guide.md`
  - `business/Sales/Axis_OS_v2_Use_Case_Guide.html`
  - `business/Sales/Axis_OS_v2_Use_Case_Guide.pdf` (regenerated)
- **What changed:** "Cost | £1,500 sprint + ongoing | £25k–£40k/year per person | £50–£500/month per tool" replaced with "Investment structure | Fixed sprint + optional ongoing optimisation | Salary + NI + benefits + recruitment cost | Recurring monthly subscriptions". Preserves the comparison without locking a specific Axis OS price.
- **Reason:** Wayne locked the rule that costing/pricing lives in memory only, never in workflow documents or sales assets. Industry market figures (mortgage proc fees, estate agent instruction fees) retained — those are factual context, not Wayne's pricing. STACK_CATALOGUE tool prices retained as Wayne approved. ICO £40-60 retained as legislation cost.
- **Backup created:** `.bak2` for both .md and .html.
- **Risk:** None — single cell change, comparison logic preserved, brand kit untouched.
- **Test run:** PDF regenerated cleanly at 1.12MB.
- **Rollback:** Restore from `.bak2` files.

---

## 2026-04-30 — v2.1 Regulations Sweep (PECR + CAP + EU AI + MLR + Equality)

### Added — Full UK SME compliance baseline
- **New file:**
  - `business/HANDOVER/COMPLIANCE_PROTOCOL.md` — covers PECR, CAP Code, EU AI Act, MLR 2017, Equality Act
- **Files edited:**
  - `.claude/agents/qa.md` — regulatory compliance checks (CAP, PECR, Equality, EU AI transparency, regulated industry, AML) added as a new section. Output format updated with BLOCKED status and compliance flags.
  - `.claude/agents/onboarding.md` — Stage 6 expanded from 5 to 7 questions: AML-regulated vertical, B2B/B2C marketing posture added.
  - `.claude/agents/handover.md` — Stage 4 surfaces PECR (B2C/B2B + cookie banner reminder) and AML (CDD gating, retention, SAR confidentiality). Stage 5 ends with cookie banner reminder for website-embedded tools.
  - `business/HANDOVER/STACK_CATALOGUE.md` — Stack 04 AML extension (CDD field, PEP field, retention rule, SAR hard limit).
  - `business/HANDOVER/SETUP_SCRIPTS.md` — Typeform setup includes cookie banner step before embedding.
  - `CLAUDE.md` — added Hard Limits section listing high-risk AI uses (recruitment, credit, medical, biometric, etc.) blocked without sign-off.
  - `business/HANDOVER/RISKS_AND_NOTES.md` — R34–R40 added (7 new compliance-specific risks).
- **Reason:** Wayne flagged the full compliance question. PECR is the highest-impact gap for SME marketing automation. CAP Code, EU AI Act, MLR, Equality Act all addressed in one coherent sweep. Closes the compliance posture for v2.1.
- **Backups created:** `.bak2` for files already backed up earlier (handover, onboarding, STACK_CATALOGUE, SETUP_SCRIPTS, CLAUDE), `.bak` for qa.md and RISKS_AND_NOTES (already in place).
- **Risk:** Low — additive checks across agents and protocols. No existing flows broken; compliance only fires when relevant flags are set.
- **Test run:** Logic walked. PECR B2C blocking, AML CDD gating, CAP Code unsubstantiated claim flagging, Equality Act recruitment hard limit, EU AI transparency tag — all paths trace cleanly.
- **Rollback:** Restore from `.bak`/`.bak2` files individually, OR delete `business/HANDOVER/COMPLIANCE_PROTOCOL.md` and revert qa.md/onboarding.md/handover.md/STACK_CATALOGUE.md/SETUP_SCRIPTS.md/CLAUDE.md to previous .bak versions.

---

## 2026-04-30 — v2.1 GDPR Framework + R25–R27 Fixes

### Added — UK GDPR / Data Protection framework
- **New files:**
  - `business/HANDOVER/GDPR_PROTOCOL.md` — master rule book (9 controls, DPA links, retention defaults)
  - `.claude/agents/gdpr.md` — 14th agent: SARs, erasure, breach protocol, status checks
  - `business/GDPR.md` — 5th core context file (template) per customer
- **Files edited:**
  - `.claude/agents/onboarding.md` — added Stage 6 GDPR baseline (lawful basis, regulated, special category, ICO, contact)
  - `.claude/agents/handover.md` — Stage 2 GDPR check, Stage 4 data map generation + DPF check, Stage 7 breach protocol generation
  - `business/HANDOVER/STACK_CATALOGUE.md` — off-limits substitution table (R26), regulated industry notes per stack (R27)
  - `business/HANDOVER/SETUP_SCRIPTS.md` — Typeform GDPR consent question added (mandatory)
  - `CLAUDE.md` — gdpr agent in path table, GDPR Trigger Rule, 5 core context files (was 4)
  - `business/HANDOVER/RISKS_AND_NOTES.md` — R25–R27 closed, R28 deferred, R29–R33 added (GDPR-specific risks)
- **Reason:** UK GDPR + DPA 2018 apply to almost every Axis OS customer. Building this in at v2.1 protects Wayne and customers from compliance gaps. Folded R25–R27 in alongside since they touch the same files.
- **Backups created:** `.bak2` for handover.md (had .bak from earlier), `.bak` for onboarding.md, SETUP_SCRIPTS.md, STACK_CATALOGUE.md (already had .bak from earlier), CLAUDE.md (already had .bak), RISKS_AND_NOTES.md (already had .bak).
- **Risk:** Low — additive logic across the stack. Existing flows still work; GDPR enforcement only fires when relevant. v2 baseline still untouched.
- **Test run:** Logic walked through Hannah/Meridian Mortgages scenario from Dry-Run 2. FCA flag, Slack off-limits substitute, off-catalogue HubSpot all handled correctly. Live customer test still pending.
- **Rollback:** Restore from `.bak` files or — if multiple files broken — delete `Axis OS_v2.1/` and re-clone from `Axis OS_v2/`.

---

## 2026-04-30 — v2.1 Sales Asset Update

### Changed — Use Case Guide updated for v2.1
- **Files affected:**
  - `business/Sales/Axis_OS_v2_Use_Case_Guide.md`
  - `business/Sales/Axis_OS_v2_Use_Case_Guide.html`
  - `business/Sales/Axis_OS_v2_Use_Case_Guide.pdf` (regenerated from HTML)
- **Reason:** Promote the new customer-triggered handover capability. Adds a prominent section explaining the 7-stage Handover Agent flow, seller/buyer benefits, and the headline pitch line.
- **Backup created:** `.bak` files for all 3 sales assets.
- **Risk:** None — additive content only, brand kit preserved, all existing vertical breakdowns intact.
- **Test run:** HTML rendered cleanly in preview, PDF regenerated at 1.12 MB without errors.
- **Rollback:** Restore from `.bak` files alongside originals.

---

## 2026-04-30 — v2.1 Live-Test Fixes

### Fixed — 4 gaps caught in live test
- **Files affected:**
  - `START_HERE.md` — added `Begin Axis OS v2 setup` as primary trigger
  - `CLAUDE.md` — First-Time Setup Rule now routes empty state to Handover, not directly to Onboarding
  - `.claude/agents/handover.md` — added cost-overlap rule (Stage 4) and risks filter rule (Stage 7)
  - `business/HANDOVER/RISKS_AND_NOTES.md` — added R21–R24, closed R17 (covered by R24 fix)
- **Reason:** Live-test dry run on dummy customer "Sarah's Cleaning Co" caught 5 gaps. Three were already in risks log; two new ones (R21, R22) on START_HERE and CLAUDE.md routing. Cost-overlap (R23) and risks filter (R24) added as new entries to track the fixes.
- **Backup created:** `.bak` files for all 4 edited files.
- **Risk:** None — additive logic only, no breaking edits to existing flows.
- **Test run:** Re-walked dummy scenario after fixes. All 5 gaps resolved.
- **Rollback:** Restore from `.bak` files alongside each edited file.

---

## 2026-04-30 — v2.1 Initial Build

### Added — Handover Agent System (parallel to v2)
- **System cloned:** `Axis OS_v2/` → `Axis OS_v2.1/` (full copy, v2 untouched)
- **Files added in v2.1:**
  - `.claude/agents/handover.md` — 13th agent, customer-triggered orchestrator
  - `business/HANDOVER/STACK_CATALOGUE.md` — 6 pre-tested tool stacks
  - `business/HANDOVER/SETUP_SCRIPTS.md` — 7 tool walkthroughs + off-catalogue fallback
  - `business/HANDOVER/TEST_HARNESS.md` — 6 stack tests + Owner Test
  - `business/HANDOVER/PLAYBOOK_TEMPLATE.md` — customer-facing day-one playbook
  - `business/HANDOVER/RISKS_AND_NOTES.md` — 20 risks logged, monthly review schedule
- **CLAUDE.md edits in v2.1:**
  - Version banner added (v2.1 vs v2 baseline)
  - Handover agent added to Agent Path Rule table
  - New Handover Trigger Rule section
- **Reason:** Customer-triggered handover so Wayne doesn't manually drive deployments. Customer types `Begin Axis OS v2 setup`, the handover agent runs the entire flow with confirmation gates, halt-on-error logic, and audit logging.
- **Risk:** Low — v2 untouched as fallback. v2.1 is a parallel system. If anything breaks, point work back to v2 path.
- **Test run:** logic + structure checks complete on all 5 files before commit. End-to-end live test with a dummy customer pending.
- **Rollback:** Delete `D:\Wayne AI OS\Axis OS_v2.1\` folder entirely. v2 at `Axis OS_v2\` continues working.

---

## Baseline — Pre-2026-04-30

v2.1 was cloned from v2 on 2026-04-30. The v2 baseline is captured in `D:\Wayne AI OS\Axis OS_v2\business\Sales\CHANGELOG.md`.

If v2.1 ever needs to be reset to baseline state, delete `Axis OS_v2.1/` and re-clone from `Axis OS_v2/`.

---

## How to add a new entry

```
## YYYY-MM-DD

### [Added | Changed | Removed | Fixed] — [short title]
- **Files affected:** [paths]
- **Reason:** [why]
- **Backup created:** [.bak path or "N/A"]
- **Risk:** [what could break, or "None"]
- **Test run:** [what was tested]
- **Rollback:** [exact undo steps]
```
