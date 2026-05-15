# Axis OS v3 — Changelog

---

## 2026-05-03 — Governance Spec Pair (Instance Tracking + Client-Safe Distribution)

**Created two governance specs at v3 root:**

### `SYSTEM_INSTANCE_TRACKING.md` (active)
- Status: Active
- Assigns UUID v4 `instance_id` to every deployment
- 10-field schema (id / slug / display_name / date / tier / device / operator / fingerprint_ref / status / notes)
- Canonical log: `TRACKER/INSTANCE_LOG.md` (forward placeholder; never auto-created)
- DCoS enforcement: halt any `CLIENTS/<slug>/` creation without registered instance
- Leak detection via SHA-256 fingerprint comparison
- Status states: active / archived / revoked (append-only, no mutation)
- System rules: no pricing / revenue / PII / business-performance tracking — deployment integrity only

### `CLIENT_SAFE_DISTRIBUTION.md` (spec — pending build approval)
- Status: Spec — pending build approval
- Operationalises LICENSE.md + DISTRIBUTION_POLICY.md Tiers 1 + 2
- Generated build at `Axis OS_v3_CLIENT_SAFE/` (treated as output, never edited in place)
- Whitelist: LICENSE, redacted DISTRIBUTION_POLICY, START_HERE (redacted), README, per-client context, handover templates, compliance protocols
- Blacklist: CLAUDE.md, CHANGELOG, SYSTEM_INSTANCE_TRACKING, all `.claude/agents/`, EXECUTION_TRACKER / EXECUTION_RULES / AGENT_RESOLUTION / DEAL_LOG / WORKFLOW_LIBRARY / Optional OS specs / ACTIVE_CLIENTS, all `TRACKER/`, all `docs/`, all `INPUTS/`, all `V3 Axis/`, locked legacy
- 9 generation rules (read-only source / whitelist enforcement / per-client scoping / redaction / pricing scrub / validation gate / instance registration / fingerprint embed)
- Never-include rule: DCoS prompt, Post-Creation Validation prompt, orchestration prompts, enforcement logic — never distributable, even Tier 3
- Failure conditions covering blacklist breach, pricing token, validation gate fail, instance registration fail, fingerprint embed fail

**Why both at root level:** governance specs sit alongside LICENSE / DISTRIBUTION_POLICY for visibility. They are operator-side; both are blacklisted from client-safe distributions.

**Pricing scrub:** clean — both files contain zero pricing tokens.

**Post-Creation Validation Gate:** PASS for both files.

**Lock-rule note:** same as LICENSE / DISTRIBUTION_POLICY — documentary additions, non-behavioural; pending Wayne's call on version stamp.

**Outstanding follow-ups:**
- Build of the actual `Axis OS_v3_CLIENT_SAFE/` distribution (Option B2) requires approval before execution
- `INSTANCE_LOG.md` first creation requires Wayne's authorisation
- Fingerprinting mechanism needs a concrete implementation (deferred — sha256 of artefact subset is the spec'd default)

---

## 2026-05-03 — System Distribution Policy (active)

**Created:** `Axis OS_v3/DISTRIBUTION_POLICY.md` — defines how Axis OS may be distributed, shared, and deployed. Three-tier access model (View / Operator / Full Restricted). Names DCoS, POST_CREATION_VALIDATION_PROMPT, internal orchestration prompts, and system enforcement logic as **non-distributable**. Mandates per-client `CLIENTS/<slug>/` instances and traceability via client identifier + instance reference.

**Companion to:** `LICENSE.md` (legal terms) — DISTRIBUTION_POLICY.md is the operational implementation of the LICENSE.

**Naming note:** policy references `POST_CREATION_VALIDATION_PROMPT.md` while the actual file is `POST_CREATION_VALIDATION.md`. Both refer to the same artefact; rename pending in the deferred follow-ups.

**Pricing scrub:** clean.

**Post-Creation Validation Gate result:** PASS.

---

## 2026-05-03 — Axis OS License (active)

**Created:** `Axis OS_v3/LICENSE.md` — proprietary license declaring system ownership, permitted use (internal operations, own business workflows, customisation within own environment), prohibited use (copy/replicate/resell/sublicense/share/reproduce/create derivatives for resale), system component protection (DCoS / agent prompts / workflows / file structures / validation), no-warranty clause, liability disclaimer (Axis AI provides structure only), enforcement (access termination / usage revocation), version-control note (applies across all versions unless explicitly replaced).

**Position:** filed at v3 root alongside `CLAUDE.md`, `START_HERE.md`, `CHANGELOG.md`, `README.md`.

**Lock-rule note:** strict reading of Phase 5 lock requires version increment for structural changes. License addition is documentary (non-behavioural) and additive — no agent, store, template, or rule modified. Filed as non-breaking documentation addition; pending Wayne's call on version stamp (v3.0.1 / v3.1 / no bump).

**Pricing scrub:** clean — zero pricing tokens.

**Post-Creation Validation Gate result:** PASS.

---

## 2026-05-03 — Phase 5 — System Lock (Axis OS_v3)

- Axis OS_v3 is now **LOCKED and ACTIVE**
- All core components constructed, validated, and aligned
- Pricing Neutrality enforced across all modules
- Legacy system archived (`business/` → backup)

**System status:**

- Ready for first real client deployment
- No further structural changes permitted without version increment
- All future updates must follow controlled patch or version upgrade process

**Snapshot:**

- Axis OS_v3 considered stable baseline
- Serves as system of record going forward

---

### Lock-time inventory

| Layer | Count / State |
|---|---|
| Active agents (`.claude/agents/`) | 17 (16 spec inventory + intake-capture; orchestrator retired) |
| Core context files | 5 (BRAND, OFFERS, CONTENT_THEMES, MEMORY, GDPR) — all pricing-neutral |
| Operational stores | EXECUTION_TRACKER, DEAL_LOG, PIPELINE, ACTIVE_CLIENTS, GDPR_LOG (TRACKER/) |
| Handover artefacts | PLAYBOOK_TEMPLATE, INTAKE_TEMPLATE, CLIENT_DATA_ACK, POST_LOCK_SUPPORT, DELIVERY_CHECKLIST, CLIENT_HANDOVER, GDPR_PROTOCOL, COMPLIANCE_PROTOCOL, RISKS_AND_NOTES, SETUP_SCRIPTS, STACK_CATALOGUE (flagged for pricing phase), TEST_HARNESS |
| Optional OS specs (root) | CLIENT_ACQUISITION_SYSTEM, OFFER_CONVERSION_FLOW, WORKFLOW_LIBRARY |
| Validation infrastructure | POST_CREATION_VALIDATION + POST_CREATION_VALIDATION_GATE |
| Legacy `D:\Wayne AI OS\business\` | Empty (55 files moved to `D:\backup\…\legacy-archive\`) |
| Frozen prior versions | v2 LOCKED, v2.1 LOCKED |
| Backup | Full snapshot + per-file mirrors + legacy-archive at `D:\backup\pre-wayne-ai-os-import\` |
| Stale duplicates | Both stubbed |
| Auto-memory | Pricing flipped to under-review; v3 active across all entries |
| Global `~/.claude/CLAUDE.md` | Compliance Responsibility Model + v3 paths active |

### Change-control rules going forward

- **Patch:** targeted edit to existing v3 files. Must pass Post-Creation Validation Gate. Logged in CHANGELOG and EXECUTION_TRACKER.
- **Version increment:** required for any structural change (new agent, new core file, new Optional OS, schema change to a store). New version becomes v3.1 / v4 etc. with its own backup snapshot before changes begin.
- **No bypass:** the gate, multi-client scoping, Pricing Neutrality, Compliance Responsibility, and append-only store rules are non-bypassable for the lifetime of this lock.

### Known follow-ups deferred to post-lock work

1. Stack catalogue + Sales Use Case Guide pricing rewrite (waits for the dedicated pricing/costing phase)
2. Optional `acquisition` specialist agent (decide rules-only vs author)
3. `dcos.md` + `onboarding.md` Block G — explicit naming of Acquisition OS / Sales OS / Marketing OS in lists
4. `POST_CREATION_VALIDATION.md` rename to `POST_CREATION_VALIDATION_PROMPT.md` (cosmetic naming alignment)
5. Empty `D:\Wayne AI OS\business\` folder may be removed manually if desired
6. Stale duplicates `Axis OS_v3/.claude/agents/{gdpr,handover}.md` may be moved to `D:\backup\…\stale-agents\` in a future cleanup

### Final declaration

**Axis OS v3 — locked, active, stable, ready for first real client deployment.**

🇯🇲 ✊🏿

---

## 2026-05-03 — Phase 4 — Legacy Archive (Batch Operation)

- Moved all legacy `business/` files to:
  `D:\backup\pre-wayne-ai-os-import\legacy-archive\`

- Files preserved as-is for audit purposes
- Axis OS_v3 confirmed as sole active system of record
- Eliminates risk of accidental reference to legacy logic

**Counts:**
- 55 files moved (51 root files + 3 in `INPUTS/` + 1 LEGACY.md marker)
- Source directory `D:\Wayne AI OS\business\` is now empty
- Source directory itself retained (empty) — can be removed manually if desired

**Operation type:** move (not delete). All content recoverable from `legacy-archive/` if needed.

**Files archived (notable categories):**
- Top 10 harvested / superseded / skipped: CLIENT_ONBOARDING_FLOW, CLIENT_DELIVERY_PACK, CLIENT_INTAKE, CLIENT_WORKFLOWS, SOP, DELIVERY_CHECKLIST, CLIENT_ACQUISITION_SYSTEM, OFFER_CONVERSION_FLOW, CLIENT_HANDOVER, AUDIT_TEMPLATE
- Pre-v3 system files: SYSTEM*.md (5 files), CONTEXT_FULL.md, ORCHESTRATOR_USAGE.md, AGENT_RESOLUTION.md (legacy schema)
- Pre-v3 client docs: CLIENT_HELP, CLIENT_INTERFACE, CLIENT_SYSTEM_MAP, CLIENT_STATUS_DASHBOARD, CLIENT_DAILY_VIEW, CLIENT_WEEKLY_REVIEW
- Pre-v3 ops: DAILY, MORNING, PROCUREMENT*, OBSIDIAN_*, TELEGRAM_EXTENSION, SETUP
- Duplicates of v3 names: BRAND, OFFERS, MEMORY, PIPELINE, ACTIVE_CLIENTS, CONTENT_THEMES, SYSTEM_REVIEW, EXECUTION_RULES, SESSION_SUMMARY
- Legacy markers: LEGACY.md
- INPUTS subfolder: INSIGHTS.md, NOTION_LOGS.md, WORK_LOG.md
- Sundry: AUDIT_TEMPLATE, CV, DESIGN, PRODUCT, PROJECTS, LEAD_TRACKING, ONBOARDING_SCRIPT (empty), CONTENT_ENGINE, EXECUTION_SHORTCUTS, SPEC_REVIEW, SYSTEM_LOG, SYSTEM_ENTRY

**Active system state confirmed:**
- v3 root: `D:\Wayne AI OS\Axis OS_v3\` — sole system of record
- v2 + v2.1: locked, untouched, available as rollback
- Backup: `D:\backup\pre-wayne-ai-os-import\` — full snapshot + per-file mirrors + Phase 4 legacy-archive

---

## 2026-05-03 — Offer Conversion Flow spec (OFFER_CONVERSION_FLOW.md)

**Created:** `business/OFFER_CONVERSION_FLOW.md` — Optional OS spec for the conversion phase between Acquisition and Onboarding. Inactive by default; gated under Sales OS activation. 5-step flow (Problem Clarification → Solution Framing → Fit Confirmation → Decision Prompt → Conversion Event) with routing rules, optional logging, activation control, system boundaries, compliance + liability, and failure conditions.

**Supersedes:** legacy `D:\Wayne AI OS\business\OFFER_CONVERSION_FLOW.md` (Top 10 #8). Legacy file untouched; eligible for Phase 4 archive.

**System position:** Acquisition → **Conversion** → Onboarding → Delivery. Strict separation from each.

**Activation gate:** Sales OS — must be explicitly enabled in onboarding Block G. DCoS blocks all routing into this system when inactive.

**Conversion event:** triggers `CLIENTS/<slug>/` creation and routes to `CLIENT_ONBOARDING_FLOW.md`. No pricing stored, no payment handling, no commercial terms recorded — strictly decision structure only.

**Logging (optional):** `TRACKER/CONVERSION_LOG.md` — defined but not auto-created. First write attempt halts and routes to Wayne for approval.

**Pricing scrub:** clean — zero pricing tokens (£, GBP, EUR, $, 2500, 497, 1500). Multiple word matches on "pricing/cost/fee/budget" all in anti-pricing rule context (forbidding pricing inside the spec).

**Compliance + Liability:** embedded — no guarantees, no certainty claims, no commercial commitments inside the system. Client responsible for communication, decision handling, and any external commercial agreement.

**Post-Creation Validation Gate result:** PASS.

**Note:** Closes Phase 3 Top 10. Remaining: Phase 4 archive batch.

---

## 2026-05-03 — Validation Gate — Patch Confirmation

- All modified files passed validation checks:
  - Path correctness
  - Pricing neutrality
  - No duplication
  - Correct activation state
  - Logging consistency

- No new files were created during this patch cycle
- Validation gate applied to overwrite conditions successfully

Scope: covers the cycle from the GDPR_LOG relocation through the system-wide reference alignment, GDPR_LOG stub path update, stale-duplicate replacement, and HANDOVER_LOG placeholder clarification. All changes were either targeted edits to existing files or controlled stub overwrites. No fresh file creations introduced.

---

## 2026-05-03 — Logging Standardisation — TRACKER Migration

- Moved GDPR_LOG.md from root (business/) to /AXIS_OS/TRACKER/
- Established TRACKER/ as canonical location for all system logs
- Aligned GDPR_LOG with ACQUISITION_LOG, DELIVERY_LOG, HANDOVER_LOG
- Prevents path inconsistency across modules

### HANDOVER_LOG Placeholder Clarification

- `HANDOVER_LOG.md` is **defined but not yet activated**.
- It will be created only when handover event tracking requires a dedicated log (separate from `EXECUTION_TRACKER.md` rows that already record handover routing).
- Until then, no file should be created. Per the never-auto-create rule, any reference to `TRACKER/HANDOVER_LOG.md` is a forward placeholder; first attempt to write to it must halt and route to Wayne for explicit approval.

**Reference alignment sweep (Patch 3):**
- `.claude/agents/onboarding.md` — line 126 path updated
- `.claude/agents/gdpr.md` — Section 6 read list, Section 7 write table, Section 4 multi-client clause (3 occurrences)
- `Axis OS_v3/CLAUDE.md` — line 113 GDPR trigger handler
- `Axis OS_v3/business/HANDOVER/CLIENT_DATA_ACK.md` — Step 1 trigger procedure + Step 3 tracker row format (2 occurrences)
- `Axis OS_v3/business/HANDOVER/GDPR_PROTOCOL.md` — erasure logging step + DPA quick-reference table (2 occurrences)
- `business/HANDOVER/CLIENT_HANDOVER.md` — already aligned (Step 5 references `TRACKER/GDPR_LOG.md`)

**Skipped (deliberately retained):**
- v2.1 paths (locked legacy)
- `Axis OS_v3/.claude/agents/gdpr.md` (stale duplicate inside v3 folder; flagged for archive)
- `business/GDPR_LOG.md` (the deprecation stub — keeps the old path for redirect)
- `EXECUTION_TRACKER.md` historical proof-location rows (audit fidelity per append-only rule)
- `CHANGELOG.md` historical entries (audit fidelity)

---

## 2026-05-03 — GDPR_LOG.md relocated to TRACKER/

Aligns the GDPR log with the canonical TRACKER/ path convention used by `ACQUISITION_LOG.md` and `DELIVERY_LOG.md` references in the new specs.

**Move:**
- Old path: `Axis OS_v3/business/GDPR_LOG.md` (now a deprecation stub)
- New path: `Axis OS_v3/TRACKER/GDPR_LOG.md` (full content + 3 existing event rows preserved)

**Stub content** (verbatim per Wayne's wording, retains the canonical reference `/AXIS_OS/TRACKER/GDPR_LOG.md`):
> # DEPRECATED — GDPR_LOG LOCATION MOVED
> This file has been relocated to: /AXIS_OS/TRACKER/GDPR_LOG.md
> Do not write to this file.
> All new entries must go to the TRACKER location.

**Path-naming note:** Wayne's stub references `/AXIS_OS/TRACKER/`. The actual on-disk path is `Axis OS_v3/TRACKER/`. Both refer to the same canonical store. Future Phase 4/5 work should reconcile naming (e.g., rename folder to `AXIS_OS/` to match canonical wording, or update Wayne's references to use `Axis OS_v3/TRACKER/`).

**Event types added:** `escalation` event type explicitly listed (was implicit before the relocation).

**Outstanding follow-up — agent specs still reference the old path:**
- `.claude/agents/dcos.md`, `gdpr.md`, `onboarding.md`, `handover.md`, `intake-capture.md`, `deal-sourcing.md` — references to `business/GDPR_LOG.md` should be updated to `TRACKER/GDPR_LOG.md`.
- `business/HANDOVER/CLIENT_DATA_ACK.md`, `CLIENT_HANDOVER.md`, `GDPR_PROTOCOL.md`, `COMPLIANCE_PROTOCOL.md` — same.
- `business/EXECUTION_TRACKER.md` proof-location entries reference `business/GDPR_LOG.md` historically; left as-is for audit fidelity.

Until the agent-spec sweep is done, agents writing to `business/GDPR_LOG.md` will hit the stub and should halt rather than overwrite the deprecation message. **Recommend follow-up patch on next turn.**

**Post-Creation Validation Gate:** PASS for both files (new TRACKER file PASS; old path now a stub which is allowed under "version upgrade").

---

## 2026-05-03 — CLIENT_HANDOVER.md (process runbook) filed

**Created:** `business/HANDOVER/CLIENT_HANDOVER.md` — process runbook formalising the transition from Axis AI to the client. 7-step flow (Checklist Population → Delivery Validation → System Review → Responsibility Transfer → GDPR Acknowledgement → Handover Record → Lock Activation) with halt conditions and end-state.

**Supersedes:** legacy `D:\Wayne AI OS\business\CLIENT_HANDOVER.md` (Top 10 #9, ~0.6 KB skeleton). Legacy file untouched; eligible for Phase 4 archive.

**Cross-references existing artefacts:**
- `DELIVERY_CHECKLIST.md` — Steps 1 + 2 invoke its population and validation rules
- `CLIENT_WORKFLOWS.md`, `CLIENT_DELIVERY_PACK.md`, onboarding outputs — source-of-truth for checklist items
- `TRACKER/GDPR_LOG.md` — Step 5 logs GDPR acknowledgement
- `POST_LOCK_SUPPORT.md` — only allowed continuation after Step 7 lock

**Alignment with `handover.md` agent:**
- Step 1 mirrors handover Section 10 Step 0 (Checklist Population)
- Step 2 mirrors Precondition #8 (Delivery Checklist Validation)
- Step 4 mirrors the Compliance Responsibility Model
- Step 5 mirrors `CLIENT_DATA_ACK.md` trigger procedure
- Step 7 mirrors Section 10 Day-7 Lock procedure

The runbook is a human-readable process map; the agent spec remains the executable rule source. They are intentionally redundant for clarity.

**Pricing scrub:** clean — zero pricing tokens. (One word "expansion" in Step 3, used in anti-sales context.)

**Post-Creation Validation Gate result:** PASS.

---

## 2026-05-03 — DELIVERY_CHECKLIST.md upgraded (phased + logged + per-item)

**Replaced:** `business/HANDOVER/DELIVERY_CHECKLIST.md` — old 16-checkbox internal gate replaced with a richer per-client delivery tracking spec. New structure:
- Phased (Phase 1 Initial → Phase 2 Core → Phase 3 Finalisation)
- Per-item: Description / Source / Responsible / Status (Not Started / In Progress / Completed / Blocked)
- Source-of-truth bound: CLIENT_WORKFLOWS.md + CLIENT_DELIVERY_PACK.md + onboarding outputs
- Logging discipline: append-only `TRACKER/DELIVERY_LOG.md` (timestamp / client_slug / checklist_item / action / responsible_party)
- System Rules: no pricing / no revenue / no performance metrics / no automation logic
- Failure Conditions for DCoS to flag
- Handover Requirement: all critical items Completed (with evidence) OR incomplete acknowledged at handover

**Patched:** `.claude/agents/handover.md` Section 10 precondition #8 — updated to reference the checklist's own rules (Completed-with-evidence / acknowledged / DCoS-waiver) rather than the prior "all 16 items checked" phrasing.

**Not created (intentional):** `business/TRACKER/DELIVERY_LOG.md` — log path referenced but not auto-created. Per never-auto-create rule; instantiated when the first per-client delivery activity requires it (with Wayne's approval).

**Pricing scrub:** clean — single grep match on "No pricing references" is an anti-pricing rule statement.

**Post-Creation Validation Gate result:** PASS (see Validation: pass note in tracker row).

**Note:** Supersedes the Harvest #2 16-checkbox version. The richer spec is more operationally useful for per-client tracking but requires the per-checklist instantiation discipline noted in handover Section 10.

---

## 2026-05-03 — Post-Creation Validation Gate (mandatory, non-bypassable)

**Created:** `docs/POST_CREATION_VALIDATION_GATE.md` — enforcement rule that requires the validator prompt to run immediately after any new file creation, overwrite, or version upgrade in the active system.

**Modified:** `.claude/agents/dcos.md` — new section `## Post-Creation Validation Gate (mandatory, non-bypassable — active 2026-05-03)` inserted before Pricing Neutrality. Defines trigger, execution, decision logic, enforcement, and out-of-scope cases (append-only system stores excluded).

**Companion file:** `docs/POST_CREATION_VALIDATION.md` (the validator prompt itself, filed in the previous turn). The Gate calls it.

**Decision logic:**
- PASS → file accepted; tracker records `Validation: pass`; downstream continues
- FAIL → file rejected; execution halts; tracker records `Validation: fail`; no automatic fixes

**Out of scope:**
- Append-only writes to system stores (`EXECUTION_TRACKER.md`, `GDPR_LOG.md`, `DEAL_LOG.md`, future `ACQUISITION_LOG.md`) — routine logging, validator does not run on tracker append rows.
- Files outside `Axis OS_v3/` and `.claude/agents/`.

**Note:** Naming clarification — Wayne's reference to "POST_CREATION_VALIDATION_PROMPT.md" maps to the existing `POST_CREATION_VALIDATION.md` (no rename performed; both gate and validator now exist at canonical paths in `docs/`).

---

## 2026-05-03 — Acquisition OS spec (CLIENT_ACQUISITION_SYSTEM.md)

**Created:** `business/CLIENT_ACQUISITION_SYSTEM.md` — fresh v3-aligned spec for the Optional Acquisition OS module. Defines an inactive-by-default top-of-funnel layer with 8 blocks (Channel / Message / Capture / Qualification / Routing / Tracking / Activation / Boundaries), strict separation from Sales OS / Offer Conversion / Delivery, and a hard rule that all leads pass through `intake-capture`.

**Supersedes:** legacy `D:\Wayne AI OS\business\CLIENT_ACQUISITION_SYSTEM.md` (Top 10 #7, ~0.7 KB skeleton). Legacy file untouched; eligible for Phase 4 archive.

**Activation:** OFF by default. Enabled per-client only via onboarding Block G. Activation persisted in `business/CLIENTS/<client_slug>/ACTIVATIONS.md` per the canonical activation store.

**Not created (intentional):**
- `business/TRACKER/ACQUISITION_LOG.md` — log path is referenced but not auto-created. Per never-auto-create rule; log will be created when the first per-client activation requires it (with Wayne's approval).
- No `business/CLIENTS/` directory — still absent until first multi-client deployment.

**Compliance + pricing:** spec embeds Pricing Neutrality + Compliance Responsibility Model — no pricing references, no guarantees, client owns outreach actions and regulatory compliance.

**Pricing scrub:** clean — spec text contained no pricing tokens.

**Note:** Acquisition OS is in addition to the existing Deal Sourcing OS revenue layer. Acquisition is top-of-funnel (lead capture); Deal Sourcing is opportunity research. Activation of one does not imply the other.

---

## 2026-05-03 — Phase 3 Legacy Harvest #10 (AUDIT_TEMPLATE.md → audit agent)

**Source harvested:** `D:\Wayne AI OS\business\AUDIT_TEMPLATE.md` (legacy, marked LEGACY 2026-05-03)

**Action:** Internal Diagnostic Axes Checklist added to `.claude/agents/audit.md` (Path B).

**What was imported (4 axes, 12 triggers):**
- Workflow Gaps — unclear process ownership / repeated manual handoffs / missing or inconsistent workflow steps
- Follow-Up Issues — missed replies / delayed chasing / no clear next action after contact
- Admin Problems — duplicated admin work / manual data movement / avoidable spreadsheet or document handling
- System Issues — tools not connected / information spread across too many places / no reliable source of truth

**Targets written:**
- Update: `.claude/agents/audit.md` — new section `## Diagnostic Axes Checklist` inserted after `## What to Look For`, before `## Rules`.

**Not changed:** `business/V3 Axis/AUDIT_RESPONSE_TEMPLATE.md` left untouched. The deliverable structure for clients is unaffected.

**Not imported (deliberate):** Purpose / Summary / Final Diagnosis prose (already covered by v3 template); empty placeholder bullets.

**Pricing scrub:** clean — source contained no pricing tokens.

**Note:** Legacy harvest Phase 3 — Unit #10. Internal diagnostic discipline only; client-facing output unchanged.

---

## 2026-05-03 — Full-system Pricing Neutralisation Pass

Scanned every file under `D:\Wayne AI OS\Axis OS_v3\` and `.claude\agents\` for pricing tokens (`£`, `GBP`, `$`, `EUR`, `2,500`, `497`, `1,500`, plus word-bounded `price`, `cost`, `fee`, `budget`, `quote`).

**Files modified (active prices stripped or replaced with `[PRICING TO BE DEFINED]`):**
- `business/OFFERS.md` — full rewrite. All £ figures (£2,500, £497, £1,500, £8,464, £3,000) replaced with placeholder. v2 references updated to v3. Agent count corrected (12 → 16). Pricing Strategy Note rewritten as deferred.
- `business/HANDOVER/RISKS_AND_NOTES.md` — R7 note: "£5/mo … sub-£500 starter offer" → "low monthly tooling cost … low-entry starter offer; pricing `[PRICING TO BE DEFINED]`".
- `business/INPUTS/SESSION_SUMMARY.md` — Apollo upgrade reference (~£39/mo) → "(cost `[PRICING TO BE DEFINED]`)".

**Files flagged (not edited — entirely pricing-based or stale duplicates):**
- `business/HANDOVER/STACK_CATALOGUE.md` — tool subscription catalogue with ~30+ £ figures. Entirely pricing-structured. Flagged for the pricing phase to rewrite.
- `business/Sales/Axis_OS_v2_Use_Case_Guide.md` — sales asset; ~10 ICP revenue bands and ROI signals in £. Also v2-branded. Flagged for separate sales-asset refresh.
- `business/Sales/Axis_OS_v2_Use_Case_Guide.html` — same content as the .md.
- `business/Sales/Axis_OS_v2_Use_Case_Guide.pdf` — generated artefact; will refresh from .md.
- `Axis OS_v3/.claude/agents/handover.md` — **stale duplicate** inside the v3 folder (canonical is `D:\Wayne AI OS\.claude\agents\handover.md`). Contains v2.1-era stack pricing in template strings. Flagged for archive.

**Files preserved (intentionally retained pricing references):**
- `business/HANDOVER/GDPR_PROTOCOL.md` — ICO statutory fee (£40–£60) — UK regulatory fact, not Axis pricing.
- `business/HANDOVER/COMPLIANCE_PROTOCOL.md` — PECR fine ranges (£500k max / £50–200k typical) — statutory enforcement reference.
- `.claude/agents/handover.md` (canonical) and `.claude/agents/onboarding.md` — ICO £40–£60 fee references kept as statutory facts; Pricing Neutrality clauses unchanged.
- `CHANGELOG.md`, `business/HANDOVER/DELIVERY_CHECKLIST.md`, all agent rule sections, `business/Sales/CHANGELOG.md` — pricing tokens appear only inside rule documentation or historical changelog records (not active pricing).
- `.claude/agents/audit.md` ("lack of cost visibility"), `.claude/agents/outreach.md` ("discuss pricing when appropriate"), `.claude/agents/intake-capture.md` (rule references) — behaviour rules, not figures.

**Total pricing instances actively removed/replaced:** 12 in OFFERS.md, 1 in RISKS_AND_NOTES.md, 1 in SESSION_SUMMARY.md = **14**.

**Pricing instances flagged for later phase:** ~50+ across STACK_CATALOGUE.md, Use_Case_Guide.md, Use_Case_Guide.html, and the stale handover duplicate.

**Confirmation:** active rule-bearing files now contain no Axis service pricing. Only retained references are (a) statutory regulatory fees, (b) rule-text describing the strip patterns, (c) historical changelog entries, (d) flagged files awaiting bulk treatment in the pricing phase.

---

## 2026-05-03 — Phase 3 Legacy Harvest #4 (CLIENT_WORKFLOWS.md → WORKFLOW_LIBRARY.md)

**Source harvested:** `D:\Wayne AI OS\business\CLIENT_WORKFLOWS.md` (legacy, marked LEGACY 2026-05-03)

**Workflows imported (4):**
- New Lead
- Active Client Work
- Weekly Review
- Follow-Up

Appended to `business/WORKFLOW_LIBRARY.md` in the strict template format (Purpose / Trigger / Steps / Outputs / Notes). Cross-references to v3 stores (`PIPELINE.md`, `EXECUTION_TRACKER.md`, `## Client Stage Vocabulary`) added; legacy "orchestrator" / "messaging" / "design-general" agent names removed; vague notes restructured into Notes lines.

**Not imported (deliberate):** Purpose / Rule / Final Rule preamble (generic); legacy "Done looks like" terminology adapted to "Outputs".

**Pricing scrub:** clean — source contained no pricing tokens.

**Note:** Legacy harvest Phase 3 — Unit #4.

---

## 2026-05-03 — Compliance Responsibility Model (active)

Aligns the system with the principle: *the client is responsible for their own GDPR / regulatory compliance. The system informs, flags, and guides — it does not take ownership.*

**Files patched (additive):**
- `.claude/agents/intake-capture.md` — escalation behaviour rewritten: halt + explain + inform + recommend (consult professional OR proceed knowingly). No auto-route to `gdpr`. No assumption of Wayne involvement.
- `.claude/agents/gdpr.md` — repositioned as compliance **advisor / template generator / process guide**. Explicit "do / do not" list. Outputs are guidance and templates, never execution on the client's behalf.
- `.claude/agents/dcos.md` — new "Compliance Responsibility Model" section: on compliance triggers, return explanation + options + next-step choices. Only route to `gdpr` on explicit user request.

**Why:** protects Wayne from liability creep, prevents the system from becoming a delegated compliance officer, keeps the client in the driver's seat.

**Not changed:** GDPR_LOG.md schema, GDPR.md schema, halt rules themselves, multi-client rules, Pricing Neutrality Rule. Logging discipline preserved.

---

## 2026-05-03 — Simple Onboarding Mode (intake-capture agent)

Reduces onboarding friction. Allows onboarding to start from conversation instead of requiring `INTAKE_TEMPLATE.md` to be completed first.

**Created:**
- `.claude/agents/intake-capture.md` — conversational intake extractor (Read-only, no file writes; produces a `## INTAKE DRAFT` block for `onboarding` Block A)

**Modified:**
- `.claude/agents/onboarding.md` — Block A intake-source rule rewritten to a 3-tier priority order: (1) conversation intake → (2) per-client `INTAKE.md` → (3) `INTAKE_TEMPLATE.md` fallback. Halt narrowed: only when all three are absent.
- `.claude/agents/dcos.md` — new "Conversational intake routing" rule: natural-language start phrases route to `intake-capture` first, then DCoS routes the draft to `onboarding`.

**Not changed:** GDPR flow, multi-client rules, `INTAKE_TEMPLATE.md` (still available as fallback), pricing rules, all other agents.

**Note:** intake-capture is a Read-only agent — does not write files, does not handle GDPR, does not assume unknowns.

---

## 2026-05-03 — Phase 3 Legacy Harvest #3 (CLIENT_INTAKE.md)

**Source harvested:** `D:\Wayne AI OS\business\CLIENT_INTAKE.md` (legacy, marked LEGACY 2026-05-03)

**Sections imported (adapted):**
- Business Overview → Section 1 (extended with Owner, Authorised signatory, Registered details)
- Current Setup → Section 2 (extended with automations probe)
- Key Problems → Section 3
- Lead & Client Flow → Section 4 (renamed Lead Flow & Growth)
- Admin & Workload → Section 5 (renamed Operations & Admin)
- Priorities → Section 6 (extended with 30–60 day focus)
- Notes → Section 7

**Targets written:**
- New: `business/HANDOVER/INTAKE_TEMPLATE.md` — client-facing intake form, completed before onboarding Block A
- Update: `.claude/agents/onboarding.md` — Block A now requires a completed intake (single-client or per-client) and halts if missing

**Not imported (deliberate):** Purpose / "Do not overcomplicate" preamble — already implicit in v3.

**Pricing scrub:** clean — source contained no pricing tokens (one false-positive grep on "feels" → "fee" disregarded). New template explicitly excludes pricing/budget fields per the Pricing Neutrality Rule.

**Note:** Legacy harvest Phase 3 — Unit #3. Purpose: standardise client intake before onboarding.

---

## 2026-05-03 — Pricing Neutrality Rule (active)

This is a new system build. Pricing is not yet defined and will be reviewed in a dedicated phase.

**Rule added:** existing prices are not active authority; legacy pricing must not be imported; placeholder `[PRICING TO BE DEFINED]` used until the pricing phase.

**Files patched (additive, no removals):**
- `business/EXECUTION_RULES.md` — new section `## Pricing Neutrality Rule`
- `.claude/agents/dcos.md` — new section `## Pricing Neutrality`
- `.claude/agents/onboarding.md` — new section `## Pricing Neutrality`
- `.claude/agents/deal-sourcing.md` — new section `## Pricing Neutrality`

**Note:** No active prices written. No legacy pricing imported. Pricing-strip discipline now substitutes the placeholder rather than silently dropping the field.

---

## 2026-05-03 — Phase 3 Legacy Harvest #2 (CLIENT_DELIVERY_PACK.md)

**Source harvested:** `D:\Wayne AI OS\business\CLIENT_DELIVERY_PACK.md` (legacy, marked LEGACY 2026-05-03)

**Sections imported:**
- 16-item pre-delivery checklist (System / Client Interface / Usability / QA Check) → new internal file
- Walkthrough handover checklist (4 items) → POST_LOCK_SUPPORT.md Stage 1 Actions
- Post-delivery first-week check (4 items) → POST_LOCK_SUPPORT.md Stage 2 Output

**Targets written:**
- New: `business/HANDOVER/DELIVERY_CHECKLIST.md` — internal quality gate before Day-7 lock
- Update: `business/HANDOVER/POST_LOCK_SUPPORT.md` — prose Actions/Output replaced with checkbox structure
- Update: `.claude/agents/handover.md` — Section 10 now requires Delivery Checklist as the 8th lock precondition

**Not imported (deliberate):** Purpose / Core Rule / Final Rule prose (already implicit in v3); Required/Optional file list (lines 21–37) — referenced legacy paths only.

**Pricing scrub:** clean — source file contained no pricing tokens (`£`, `GBP`, `$`, `EUR`, `2,500`, `497`, `1,500` — zero matches).

**Note:** Legacy harvest Phase 3 — Unit #2.

---

## 2026-05-03 — Phase 3 System Tightening (Post Harvest #1)

**Changes:**
- Linked `handover` agent to `POST_LOCK_SUPPORT.md` — Section 10 now ends at Day-7 lock and points to the post-lock file.
- Unified pipeline stage definitions in `PIPELINE.md` — deprecated the short-form client-stage sequence in `## Pipeline Stages Reference` in favour of the 8-stage canonical list in `## Client Stage Vocabulary`. Lead stages preserved.

**Files touched:**
- `.claude/agents/handover.md` — appended "After lock" subsection at the end of Section 10
- `business/PIPELINE.md` — replaced the duplicate client-stage line with a deprecation pointer (lead stages kept)

**Pricing scrub:** none required.

---

## 2026-05-03 — Phase 3 Legacy Harvest (CLIENT_ONBOARDING_FLOW.md)

**Source harvested:** `D:\Wayne AI OS\business\CLIENT_ONBOARDING_FLOW.md` (legacy, marked LEGACY 2026-05-03)

**Sections imported:**
- Stages 6 + 7 (walkthrough + early support) → adapted into a new file
- Pipeline status vocabulary (8 client stages) → appended to `PIPELINE.md`
- Review trigger phrases → appended to `EXECUTION_RULES.md`

**Targets written:**
- New: `business/HANDOVER/POST_LOCK_SUPPORT.md`
- Append: `business/PIPELINE.md` — new section `## Client Stage Vocabulary`
- Append: `business/EXECUTION_RULES.md` — new section `## Review Trigger Phrases`

**Not imported (deliberate):** legacy orchestrator routing, example prompts, retired agent names, Stages 1–5 (already covered by `onboarding.md` Blocks A–F + `gdpr` ack flow).

**Pricing scrub:** none required — source file contained no pricing.

**Note:** Legacy harvest Phase 3. Source file remains in place under `LEGACY.md` cover at `D:\Wayne AI OS\business\`.

---

## 2026-05-02 — v3 Initial Build

**Reason:** v2.1 had two limits:
1. Orchestrator-first routing was implicit — no execution trail of who owns what, status, or proof.
2. No revenue specialist — outreach and pipeline existed but no agent owned the find-the-deal step.

**Change:** Clean rebuild. Three-layer architecture.

**New layers:**
- Command — DCoS (sole user interface, routes + tracks)
- Thinking — 14 inherited specialists (do work + challenge)
- Revenue — Deal Sourcing OS (finds deals) + outreach + pipeline

**New files:**
- `.claude/agents/dcos.md`
- `.claude/agents/deal-sourcing.md`
- `business/EXECUTION_TRACKER.md`
- `business/DEAL_LOG.md`
- `docs/dcos/DIGITAL_CHIEF_OF_STAFF.md`
- `docs/deal-sourcing/NEW_DEAL_SOURCING_OS.md`
- `docs/ecosystem/AI_OS_ECOSYSTEM_MAP.md`
- `docs/ecosystem/ONBOARDING_NEW_OS.md`

**Rewritten:**
- `CLAUDE.md` — DCoS-first replaces orchestrator-first
- `START_HERE.md` — DCoS commands
- `business/EXECUTION_RULES.md`
- `business/AGENT_RESOLUTION.md`

**Inherited unchanged from v2.1:**
- 14 specialist agents
- All compliance protocols (`business/HANDOVER/`)
- Core context files (BRAND, OFFERS, MEMORY, CONTENT_THEMES, GDPR)
- Staggered onboarding model
- Hard limits on high-risk AI uses

**Active workstreams continued (no re-onboard):**
1. Axis OS deployment — Joseph (likely first)
2. Joseph Farodoye — awaiting call confirm
3. Mark Francis — youth mentoring concept
4. Anthony Lewis — estate agent prompts (post-session refinement)
5. Learning Out Loud — E2 draft after week 1 training

**Pricing:** Locked at memory level. Not stored in v3 docs.
# 2026-05-09

- Added `CORE/LEARNING/LESSONS_LEARNED_2026-05-09.md` capturing operational lessons from the website, product packaging, platform-build, pricing, compliance, and client-delivery workstream.
- Preserved new rules for platform confirmation before client builds, pricing authority checks, no fixed PDF page-count claims, professional document QA, and Wayne Francis brand positioning.
