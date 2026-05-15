# Axis OS v2 Handover — Risks and Notes Log

Single source of truth for every risk flagged during the design, build, or deployment of the Handover system.

**Rule:** every risk flagged during a build review, a deployment, or a quarterly review gets logged here. No risks live only in conversation. If it isn't in this file, it isn't tracked.

**How to use this file:**
- Wayne reviews monthly — closes resolved risks, escalates unresolved ones
- Handover Agent reads this at Stage 1 of every deployment so the customer is aware of any open risks that affect them
- Quarterly maintenance run uses this to prioritise improvements to the catalogue, scripts, and tests

---

## Status key

- 🔴 OPEN — active risk, not yet mitigated
- 🟡 MONITORING — mitigation in place, watching first runs
- 🟢 CLOSED — fully resolved or proven non-issue
- ⚫ ACCEPTED — known risk, decision made not to fix

---

## Risks by source

### From handover.md (File 1) — 2026-04-30

**R1 — Stage 5 length and dropout** 🟡
- **Risk:** Stage 5 (guided setup) is 60–90 mins. If the customer disengages, the system needs to resume cleanly.
- **Mitigation:** pause/resume logic writes progress to MEMORY.md.
- **Watch:** first 3 real deployments — confirm resume actually works.

**R2 — Stack Catalogue staleness** 🔴
- **Risk:** Stage 4 is opinionated and locked to STACK_CATALOGUE.md. If the catalogue isn't kept current, recommendations get stale.
- **Mitigation:** quarterly review schedule built into STACK_CATALOGUE.md (next due 2026-07-30).
- **Owner:** Wayne. Calendar reminder needed.

**R3 — No QA Agent in Handover chain** ⚫
- **Risk:** Playbook isn't QA'd before handing to customer.
- **Decision:** accepted. Playbook is internal-only, low brand risk.

### From STACK_CATALOGUE.md (File 2) — 2026-04-30

**R4 — Tool price drift** 🔴
- **Risk:** Tool prices change 2–4 times a year. Stale prices look unprofessional in customer-facing recommendations.
- **Mitigation:** quarterly review.
- **Owner:** Wayne.

**R5 — Stack 01/02 overlap** 🟡
- **Risk:** Both use Airtable + Zapier + Gmail. Double-counting cost when both are deployed.
- **Mitigation:** handover.md Stage 4 must detect overlap before presenting cost.
- **Watch:** test on first dual-stack deployment.

**R6 — No enterprise-tier stacks** ⚫
- **Risk:** Salesforce/HubSpot Pro not covered. Limits up-market reach.
- **Decision:** accepted for now. Axis OS v2 targets SMEs not on enterprise platforms. Tier 2 catalogue is a future build.

**R7 — Stack 03 margin opportunity** 🟢
- **Note (not a risk):** Stack 03 has a low monthly tooling cost — could anchor a low-entry starter offer. Pricing `[PRICING TO BE DEFINED]`. Tagged for product roadmap; defer to the pricing phase.

### From SETUP_SCRIPTS.md (File 3) — 2026-04-30

**R8 — UI drift in tool menus** 🔴
- **Risk:** Airtable/Typeform/Zapier change menu names regularly. Scripts break silently for new customers until updated.
- **Mitigation:** quarterly walkthrough by Wayne to refresh menu paths and screenshots.
- **Owner:** Wayne.

**R9 — Gmail step is light** 🟡
- **Risk:** Customers may expect more from "Gmail setup" than just labels. Could feel underwhelming.
- **Mitigation:** agent reassures with explicit message: "That's all we need from Gmail directly — drafts come from Zapier."

**R10 — Only Stack 01 has a sample Zap walkthrough** 🟡
- **Risk:** Customers running Stacks 02–06 need their own Zap recipes. Currently hand-built each time.
- **Mitigation:** add Zap recipes per stack after first 3 deployments validate the pattern.
- **Owner:** Wayne, after data from real handovers.

**R11 — No screenshots in setup scripts** 🟡
- **Risk:** Pure text works for Claude-driven instructions but is harder for customers if exported as a self-serve PDF.
- **Mitigation:** add visual annexes only if/when self-serve handover becomes a product.

**R12 — Off-catalogue WebFetch source quality** 🔴
- **Risk:** Off-catalogue fallback may pull from outdated blogs. Bad source = bad setup.
- **Mitigation:** "prefer official sources" rule in fallback flow; Wayne sanity-checks first 3–5 off-catalogue runs.
- **Owner:** Wayne.

### From TEST_HARNESS.md (File 4) — 2026-04-30

**R13 — Test 03 actually publishes a real post** 🔴
- **Risk:** Content Engine test schedules a live post. If cleanup is missed, real post goes out.
- **Mitigation:** cleanup step is explicit in test instructions. Agent must prompt customer to confirm "kept" or "unscheduled".
- **Owner:** Handover Agent — needs strong prompt at end of Test 03.

**R14 — Zap fast-forward not perfect** 🟡
- **Risk:** Test 06 uses Zapier's test feature — doesn't perfectly simulate live day 3 / day 7 delays.
- **Mitigation:** sanity-check timing manually after first deployment running Stack 06.

**R15 — No load testing** ⚫
- **Risk:** Tests are functional, not volume. SME volumes are fine; scale-ups would need different testing.
- **Decision:** accepted for v1. Out of scope for SME deployments.

**R16 — Owner Test is subjective** 🟡
- **Risk:** "Does this report tell you what you need to know?" is a judgement call. Different customers give different answers.
- **Mitigation:** agent uses explicit yes/no confirmation prompt. Repeated "no" triggers MEMORY.md improvements before sign-off.

### From PLAYBOOK_TEMPLATE.md (File 5) — 2026-04-30

**R17 — Open risks section may overwhelm customers** 🟢
- **Risk:** "Open risks for your deployment" section pulls from RISKS_AND_NOTES.md and could surface internal-feeling items that worry the customer.
- **Mitigation:** Handover Agent must filter — only include risks where status is OPEN and relevance is "customer-facing". Internal risks (e.g. R8 UI drift) should not be shown.
- **Status:** Closed by R24 fix on 2026-04-30 — filter rule now in handover.md Stage 7.

**R18 — Regenerate my playbook command not implemented** 🟡
- **Risk:** Playbook footer promises a `Regenerate my playbook` command, but no agent currently handles it.
- **Mitigation:** add this as a recognised command in the Handover Agent or a small dedicated playbook agent in v2.1.
- **Owner:** Wayne. Track in product backlog.

**R19 — Login URLs and costs go stale** 🔴
- **Risk:** Tool URLs change, plans get renamed, costs shift. Playbook becomes inaccurate within 6–12 months.
- **Mitigation:** quarterly playbook refresh option for active customers; add a "last verified" date to each tool row.
- **Owner:** Wayne for active customer reviews.

**R20 — Customer self-edit could break MEMORY rules** 🟡
- **Risk:** Playbook tells customers to edit BRAND.md and MEMORY.md directly. Heavy edits could fragment the file structure.
- **Mitigation:** add a one-line note to the playbook recommending small additive edits, not bulk rewrites. Major rewrites should re-run Onboarding.
- **Owner:** PLAYBOOK_TEMPLATE.md edit pending.

### From Live Test (v2.1) — 2026-04-30

**R21 — START_HERE.md missing handover trigger** 🟢
- **Risk:** Customer opening v2.1 fresh had no way to know to type `Begin Axis OS v2 setup`. START_HERE.md still pointed only to `Onboard new client`.
- **Mitigation:** Fixed in v2.1 START_HERE.md edit on 2026-04-30. Handover trigger is now Step 3, with Onboarding kept as a secondary path for context-only setups.
- **Status:** Closed at first edit. Logged for traceability.

**R22 — CLAUDE.md First-Time Setup Rule conflicted with Handover** 🟢
- **Risk:** First-Time Setup Rule said "route to Onboarding Agent" when context files are empty. With v2.1, empty-state should route to Handover (which calls Onboarding as Stage 2). Logic conflict.
- **Mitigation:** Fixed in v2.1 CLAUDE.md edit on 2026-04-30. Empty state now routes to Handover. Direct-to-Onboarding only fires when user explicitly says "Onboard new client".
- **Status:** Closed at first edit. Logged for traceability.

**R23 — Cost overlap not previously specified in handover.md Stage 4** 🟢
- **Risk:** Stage 4 told the agent to cross-check existing tools but didn't define how to deduplicate costs across stacks (e.g. shared Zapier subscription).
- **Mitigation:** Cost overlap rule added to handover.md Stage 4 on 2026-04-30 with a worked example. Agent now presents deduplicated total and explicitly calls out shared tools.
- **Status:** Closed at first edit. Logged for traceability.

**R24 — Risks filter logic for playbook not previously specified** 🟢
- **Risk:** Playbook template referenced `[OPEN_RISKS_AFFECTING_THIS_CUSTOMER]` but handover.md never told the agent how to filter customer-facing vs internal risks (R17 mitigation gap).
- **Mitigation:** Risks filter rule added to handover.md Stage 7 on 2026-04-30. Defines include/exclude logic, requires plain-English phrasing, hides internal IDs.
- **Status:** Closed at first edit. R17 also closed by this fix.

### From Dry-Run 2 (Financial Services) — 2026-04-30

**R25 — Audit Agent had no regulated industry awareness** 🟢
- **Risk:** Stage 3 of handover could recommend content workflows to FCA/legal/medical firms without surfacing the compliance sign-off requirement.
- **Mitigation:** Onboarding now has a Stage 6 GDPR baseline that captures regulated-industry status. Handover.md Stage 2 reads this and surfaces compliance reminders at Stages 3, 4, 5, 7.
- **Status:** Closed on 2026-04-30.

**R26 — Off-limits substitution logic missing** 🟢
- **Risk:** Stage 4 told the agent to respect off-limits but didn't define substitutes. Customers could end up with degraded stacks.
- **Mitigation:** Substitution table added to STACK_CATALOGUE.md (Slack→Gmail digest, Zapier→Make.com, etc.). Handover halts if no substitute exists.
- **Status:** Closed on 2026-04-30.

**R27 — Regulated industry notes not in STACK_CATALOGUE** 🟢
- **Risk:** FCA/regulated context only existed in Use Case Guide. Stage 4 couldn't surface compliance risk per stack.
- **Mitigation:** Per-stack regulated industry notes added to STACK_CATALOGUE.md, including FCA financial promotions rule.
- **Status:** Closed on 2026-04-30.

**R28 — Off-catalogue tools may have feature limits affecting workflow** 🔴
- **Risk:** Off-catalogue fallback handles setup but doesn't check capability fit (e.g. HubSpot Free has no API access).
- **Mitigation:** Defer until first 3 real off-catalogue runs reveal common feature-limit patterns. Then add capability checks.
- **Status:** Open. Tracked for post-deployment review.

### From GDPR Framework Build — 2026-04-30

**R29 — DPF certification status changes per tool** 🔴
- **Risk:** Tools can lose Data Privacy Framework certification. Out-of-date status puts customer in non-compliant state for international transfer.
- **Mitigation:** Quarterly review checks DPF status per tool. gdpr agent uses WebSearch to verify on each `Show me my data map` request.
- **Owner:** Wayne for quarterly review.

**R30 — Customer skips DPA signing** 🟡
- **Risk:** Customers told to sign DPAs within 7 days but no enforcement. Non-compliance risk.
- **Mitigation:** GDPR.md tracks DPA signed status. `Check GDPR status` command flags unsigned DPAs as red. Add reminder in monthly system review.

**R31 — Special category data flagged but not enforced** 🟡
- **Risk:** Customer says "yes" to special category data, agent halts at Stage 2, but if they say "I understand", the agent continues. They might not actually consult a DPO.
- **Mitigation:** Strong wording in Stage 2 prompt. Cannot remove halt without legal advice — handover keeps the gate but accepts customer accountability.

**R32 — ICO registration not auto-checked** 🟡
- **Risk:** Customer answers "Don't know" to ICO registration. System logs it but doesn't verify.
- **Mitigation:** `Check GDPR status` command surfaces unregistered status as amber. Customer responsible for completing registration.

**R33 — gdpr agent SAR coverage limited to Axis OS-known sources** 🟡
- **Risk:** SAR searches Airtable, Gmail, Slack, local files. If customer has personal data elsewhere (their own CRM, accounting software), SAR misses it.
- **Mitigation:** SAR report includes a section "Records NOT included" — customer must manually search their other systems and add to the SAR before sending.

### From Compliance Sweep (PECR + CAP + EU AI + MLR + Equality) — 2026-04-30

**R34 — PECR B2C consent enforcement relies on customer honesty** 🟡
- **Risk:** System can block sends to suppression list, but if a customer adds B2C contacts they sourced without consent, the system has no way to verify.
- **Mitigation:** Onboarding Stage 6 captures B2B/B2C status. Outreach Agent flags B2C marketing without consent reference. Customer attestation in GDPR.md covers them but liability still sits with them.

**R35 — Cookie banner is customer responsibility** 🟡
- **Risk:** Stage 5 reminds customer to install a cookie banner, but no enforcement. If they skip it, embedded Typeform/Calendly puts them in PECR breach.
- **Mitigation:** Stage 5 prompt is firm and lists free options. Add to monthly system review: "Cookie banner check — still in place?"

**R36 — CAP Code claim verification depends on customer evidence** 🟡
- **Risk:** QA Agent flags unverifiable claims, but can't independently check whether the customer has the evidence to back a claim.
- **Mitigation:** QA Agent forces a "Can you produce evidence for this claim?" prompt. Customer attestation captured in MEMORY.md when they confirm.

**R37 — EU AI Act transparency disclosure may not be needed in UK** 🟢
- **Risk:** Some customers operate UK-only and don't sell into EU. Forcing transparency disclosure on every unedited message is overkill.
- **Mitigation:** Disclosure is conditional — only attached when content goes out without human edit. Most messages get edited, so it rarely lands. Acceptable as-is.
- **Status:** Closed — operating as designed.

**R38 — AML CDD gating depends on customer flagging vertical correctly** 🟡
- **Risk:** If onboarding misses or mis-answers AML question, CDD gating won't apply and customer could process clients without due diligence.
- **Mitigation:** Onboarding Stage 6 lists every AML-regulated sector explicitly. Quarterly review prompts customer to re-confirm.

**R39 — Equality Act check is rule-based, not deep semantic** 🟡
- **Risk:** QA Agent catches obvious exclusionary phrasing but may miss subtle indirect discrimination.
- **Mitigation:** Hard limits prevent recruitment use entirely. For other content, customer review is the safety net. Document this as accepted scope.

**R40 — Compliance protocol added late — existing customers (when they exist) not migrated** ⚫
- **Risk:** Once Axis OS v2.1 has live customers, retroactive compliance changes need a migration path.
- **Decision:** Accepted. v2.1 has no live customers yet. First customer deployment goes through the full compliance flow from day one.

---

## Standing rules going forward

1. **Every risk flagged during file build, code review, or deployment gets logged here.** No exceptions. The agent reads this file at Stage 1 of every handover.
2. **Status updates happen at:** monthly Wayne review, quarterly catalogue review, after every real deployment.
3. **New entries follow the format above:** ID, status, risk, mitigation, owner.
4. **CHANGELOG.md references this file** when risks are closed or escalated — keep both in sync.

---

**Last reviewed:** 2026-04-30
**Next review due:** 2026-05-30 (monthly)
