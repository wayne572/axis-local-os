# Axis OS v2 — Compliance Protocol

UK regulations beyond GDPR that affect Axis OS deployments. Sits alongside `GDPR_PROTOCOL.md`.

**Read by:** handover agent (Stages 2, 4, 7), qa agent (every content review), onboarding agent (Stage 6).

**Position:** Wayne is not a lawyer. This protocol gives sensible defaults for UK SME deployments. Customers in regulated sectors or handling complex cases should consult their own legal counsel.

---

## 1. PECR — Privacy and Electronic Communications Regulations

**What it covers:** marketing emails, SMS, phone calls, cookies. Sits alongside GDPR — GDPR is the data rule, PECR is the contact rule.

**Rules Axis OS enforces:**

### B2B vs B2C marketing
- Onboarding Stage 6 captures whether the business markets to B2B or B2C
- **B2B (corporate subscribers — companies, registered partnerships):** soft opt-in allowed. Cold email permitted with clear opt-out mechanism in every message.
- **B2C (individual consumers, sole traders):** explicit opt-in consent required before marketing email or SMS. Lead must have ticked a consent box.
- **Mixed:** treat as B2C by default for safety unless customer can prove B2B status of each contact.

### Cold outreach drafts
The Outreach Agent must:
- Always include a clear opt-out line ("Reply STOP to unsubscribe" or equivalent)
- Identify the sender (company name + registered address) in B2C messages
- Never email someone who has opted out (check `business/GDPR_SUPPRESSION_LIST.md` first)
- For SMS: identify the sender, include free opt-out

### Cookie banner reminder
If the customer embeds Typeform, Calendly, or any other widget on their website:
- Their website must have a cookie banner compliant with PECR + GDPR
- Banner must allow users to reject non-essential cookies (no pre-ticked boxes)
- The handover agent surfaces this at Stage 5 when a website-embedded widget is set up

### Suppression list discipline
Anyone who:
- Replies STOP to a marketing email
- Asks to be removed verbally or in writing
- Submits a right-to-erasure request

… is added to `business/GDPR_SUPPRESSION_LIST.md` immediately. The Outreach Agent must check this list before drafting any marketing message.

**ICO enforcement:** PECR fines run to £500,000 maximum. Most are £50–200k. Common breaches: marketing without consent, no opt-out, ignoring opt-outs.

---

## 2. CAP Code (Advertising Standards)

**What it covers:** UK Code of Non-broadcast Advertising and Direct & Promotional Marketing. Enforced by the ASA. Applies to anything Axis OS publishes — LinkedIn posts, social posts, website copy, ad copy, email marketing.

**Rules the QA Agent enforces on every public-facing content output:**

| Rule | Check |
|---|---|
| No misleading claims | Every factual claim must be supportable by evidence the customer can produce |
| No unsubstantiated comparisons | "We're the best" needs proof; "We're the only" needs verification |
| Testimonials must be real and verifiable | Cannot generate fake testimonials. If a testimonial is used, customer must be able to produce the source |
| Disclose paid partnerships | If content features a partner, sponsor, or affiliate link, it must be disclosed (#ad, #sponsored, "in partnership with") |
| No misleading urgency | "Only 2 left" / "expires today" must be true. Generated urgency without basis fails |
| Price claims must be accurate | "Save 50%" requires a recent and genuine higher price reference |
| Health/wellbeing/financial claims | Higher bar — Axis OS adds a flag for the customer's review, never auto-approves |
| No discrimination | See Equality Act section below |

**ASA enforcement:** Public adjudications. No fine, but reputational damage. ASA can require ads to be removed and the customer to publicly accept the ruling.

---

## 3. EU AI Act (transparency baseline)

**What it covers:** EU regulation in force from 2024, fully effective 2026. Classifies AI systems by risk. Affects UK SMEs serving EU customers.

**Where Axis OS sits:** Most use cases (content drafting, lead routing, calendar booking) are **minimal/limited risk** — only transparency obligations apply.

**Rules Axis OS enforces:**

### Transparency
- The QA Agent flags content as "AI-assisted" if it goes out without human edit
- The Playbook (Stage 7) tells the customer: "Anything sent without your edit should disclose AI assistance to comply with EU transparency rules. Most messages get a human edit, so this rarely applies."

### Hard limits — high-risk AI uses
Axis OS does NOT deploy for:
- Recruitment screening, candidate ranking, or hiring decisions about people
- Credit scoring or lending decisions
- Medical triage or diagnosis
- Automated decisions with legal effects on individuals
- Biometric categorisation
- Education access decisions

If a customer asks Axis OS to do any of these, halt and flag for Wayne. These would require a separate compliance regime, regulatory registration, and likely human review at every step.

**Severity for SME deployments today:** Low — most Axis OS work is limited risk. High if scope ever expands.

---

## 4. Money Laundering Regulations 2017 (MLR / AML)

**What it covers:** UK anti-money-laundering rules. Applies to:
- Accountants and auditors
- Tax advisers
- Solicitors and legal advisers
- Estate agents (residential and commercial)
- Lettings agents (rent ≥ €10,000/month)
- Casinos and high-value dealers
- Trust and company service providers
- Crypto-asset businesses

**Rules Axis OS enforces if Onboarding Stage 6 flags AML-regulated vertical:**

### Customer Due Diligence (CDD) gating
- Stack 04 (Pipeline) requires a "CDD complete" status field for each client
- The Pipeline Agent must not progress a client to "active" status until CDD is marked complete
- This is a workflow rule the Builder Agent applies at handover for AML-regulated customers

### Record retention
- AML records must be kept **5 years** from the end of the business relationship (already aligns with our 6-year default for active clients)
- Stack 04 retention rules are stricter under MLR — never auto-purge below 5 years

### Suspicious Activity Reports (SARs to NCA)
- SARs are confidential and must NOT be discussed in client-facing communications
- Axis OS hard limit: the Outreach Agent and Content Agents must never write about SARs, suspicious activity, or anything implying a tip-off
- If a customer references a SAR in conversation with the system, the agent acknowledges privately and does not record details in MEMORY.md

### Politically Exposed Persons (PEP)
- Enhanced Due Diligence required for PEPs
- The Pipeline Agent flags PEP status if marked, and surfaces it to the customer at every interaction with that record

**HMRC and FCA enforcement:** Significant fines for AML breaches. Personal liability for officers in some cases.

---

## 5. Equality Act 2010

**What it covers:** Anti-discrimination across employment, services, and education. Protected characteristics: age, disability, gender reassignment, marriage/civil partnership, pregnancy/maternity, race, religion/belief, sex, sexual orientation.

**Rules the QA Agent enforces on every content output:**

| Check | Rule |
|---|---|
| Inclusive language | Default to gender-neutral terms unless the brand voice deliberately specifies otherwise |
| No exclusionary phrasing | Avoid age/ability assumptions ("young dynamic team", "must be physically fit" unless genuine occupational requirement) |
| Image/example diversity | When suggesting visuals or examples in content, default to diverse representation |
| Targeting | Marketing must not exclude protected groups except where law permits (e.g. women's health products) |

### Hard limits — recruitment and HR
Axis OS does NOT:
- Screen, rank, score, or filter candidates
- Generate "ideal candidate" criteria that could indirectly discriminate
- Write rejection letters that imply a protected characteristic was a factor
- Make any decision about a person's employment

If the customer wants Axis OS to assist with recruitment, scope is limited to: writing job adverts (which the QA Agent reviews for inclusive language) and tracking applications in a pipeline. **Decisions stay human.**

**Enforcement:** Civil claims by individuals. Damages uncapped in some cases. EHRC can investigate.

---

## What this means for the QA Agent

The QA Agent now runs every public-facing content output through these checks in sequence:

1. **Brand check** (existing) — voice, tone, language alignment
2. **CAP Code check** — claims supportable, no misleading urgency, testimonials real, partnerships disclosed
3. **PECR check** (for outreach/marketing) — opt-out present, sender identified, suppression list checked
4. **Equality Act check** — inclusive language, no exclusionary phrasing
5. **EU AI transparency** — flag as AI-assisted if no human edit
6. **Regulated industry check** — if MEMORY.md REGULATED_INDUSTRY is set, flag for compliance sign-off

If any check fails, return specific edits with reason. Never block silently — always tell the customer why and what to change.

---

## Maintenance

**Quarterly review checklist (Wayne to run):**
- Check ICO PECR enforcement actions for new patterns
- Check ASA recent rulings — any new patterns for SMEs?
- Check EU AI Act implementation status — any new obligations triggered?
- Check HMRC/NCA AML guidance updates
- Check EHRC Equality Act guidance updates

**Last reviewed:** 2026-04-30
**Next review due:** 2026-07-30
