# Axis OS v2 — GDPR Protocol

UK GDPR + Data Protection Act 2018 controls baked into every Axis OS deployment.

**Read by:** handover agent (Stages 2, 4, 5, 7), gdpr agent (on demand), onboarding agent (Stage 5), all setup scripts touching personal data.

**Position:** Wayne is not a lawyer. This protocol gives sensible defaults that align with ICO guidance for UK SMEs. Customers handling high volumes of sensitive data should engage their own DPO or solicitor.

---

## The 9 Controls

### 1. Lawful basis declaration
Captured at Onboarding Stage 5. Stored in `business/GDPR.md`. Every customer must declare at least one lawful basis for processing personal data:

- **Consent** — explicit opt-in (marketing lists)
- **Contract** — necessary to deliver a service (clients)
- **Legitimate interest** — reasonable B2B contact (most SME outreach)
- **Legal obligation** — statutory requirement (HMRC, regulator)
- **Vital interest / public task** — rare for SMEs

If a customer can't declare a basis, halt and flag for Wayne — they need legal advice before deploying.

### 2. Data inventory (auto-generated at handover)
At Stage 4 of handover, the agent writes `business/GDPR_DATA_MAP.md`. Format:

```
| Tool | Personal data held | Lawful basis | Retention | Customer's role | International transfer? |
|------|--------------------|--------------|-----------|------------------|--------------------------|
| Airtable | Lead name, email, phone, notes | Legitimate interest | 12 months from last contact | Controller | US — DPF certified |
```

This file is what ICO ask for in any breach or audit. Keep it accurate.

### 3. Retention defaults (per stack)

| Stack | Default retention | Reason |
|---|---|---|
| 01 — Lead Qualifier | Unconverted leads: 12 months from last contact, then delete | Legitimate interest expires |
| 02 — Booking & Onboarding | Booking records: 12 months unless converted | Standard B2B retention |
| 03 — Content Engine | Audience interactions: indefinite (anonymised) | Not personal data once aggregated |
| 04 — Pipeline & Reporting | Active clients: indefinite while engaged + 6 years after last interaction | Statutory record-keeping |
| 05 — Cash Flow & Invoicing | Invoice records: 6 years | HMRC + Companies Act |
| 06 — Proposal & Contract | Proposals to non-clients: 12 months. Signed contracts: 6 years | Contract law statutory period |

Customers can override with documented reason. Defaults written to `business/GDPR.md` at handover.

### 4. Consent capture (form level)
Every Typeform/enquiry form set up by Axis OS must include a consent question:

> *"I'm happy to be contacted about my enquiry. (You can withdraw at any time by replying STOP or emailing us.)"* — checkbox required

Without this, lead processing relies on legitimate interest only — which is workable for B2B but risky for marketing follow-up beyond the original enquiry.

### 5. Subject Access Request (SAR) workflow
Customer types: `Run a Subject Access Request for [name or email]`

The **gdpr agent** searches:
- Airtable bases (all tables)
- Gmail (sent + drafts + inbox)
- Slack (any channel mentioning them)
- MEMORY.md and ACTIVE_CLIENTS.md
- Any HANDOVER logs that reference them

Returns a packaged `SAR_[name]_[date].md` report the customer reviews and sends to the data subject. **30-day statutory deadline** noted in the output.

### 6. Right to erasure ("delete my data")
Customer types: `Erase [name or email] from the system`

The gdpr agent:
1. Searches all data sources (same as SAR)
2. Lists every record found
3. Asks customer to confirm deletion (one chance — then it's gone)
4. Deletes records from Airtable
5. Adds to `business/GDPR_SUPPRESSION_LIST.md` so re-imports never restore the contact
6. Logs deletion in `TRACKER/GDPR_LOG.md` with date, record count, and reason

**Exception:** records required for legal/tax purposes (signed contracts, invoices) cannot be deleted before the statutory retention period. The gdpr agent flags these and explains to the customer.

### 7. Data Processing Agreements (DPAs)
At Stage 4, the handover agent reminds the customer:

> "Each tool you connect (Airtable, Zapier, Buffer, etc.) processes personal data on your behalf — they are 'processors', you are the 'controller'. UK GDPR requires a Data Processing Agreement (DPA) with each one. The links below take you to each tool's standard DPA — sign them within 7 days."

Standard DPA URLs are stored in this file (see Annex A).

### 8. Breach notification readiness
Generated at handover Stage 7: `business/GDPR_BREACH_PROTOCOL.md`

Pre-filled with the customer's data inventory. Includes:
- The 72-hour ICO notification rule
- Who to call first (their DPO or solicitor if any)
- ICO breach reporting URL: ico.org.uk/for-organisations/report-a-breach/
- Template breach notification email to affected data subjects
- Internal log section to record the incident

### 9. International transfers
Most listed tools (Airtable, Zapier, Buffer, Calendly) are US-headquartered. They are covered by the **EU-US Data Privacy Framework** as of July 2023, which UK ICO recognises (the UK Extension applies).

At Stage 4, the handover agent flags this and confirms each chosen tool is DPF-certified. If a tool is not DPF-certified, the agent halts and asks Wayne for direction.

---

## Annex A — Standard DPA Links

| Tool | DPA URL |
|---|---|
| Airtable | airtable.com/dpa |
| Zapier | zapier.com/legal/data-processing-addendum |
| Typeform | typeform.com/dpa |
| Calendly | calendly.com/dpa |
| Buffer | buffer.com/legal/dpa |
| Google Workspace (Gmail) | workspace.google.com/terms/dpa_terms.html |
| Slack | slack.com/legal/data-processing-addendum |
| Microsoft 365 | microsoft.com/licensing/docs/customer/dpa |

Verify links at quarterly review — vendors move pages.

---

## Annex B — Files this protocol creates per customer

| File | Created at | Purpose |
|---|---|---|
| `business/GDPR.md` | Onboarding Stage 5 + Handover Stage 4 | Master GDPR record per customer |
| `business/GDPR_DATA_MAP.md` | Handover Stage 4 | Tool-by-tool data inventory |
| `business/GDPR_SUPPRESSION_LIST.md` | First erasure request | Names that must never be re-imported |
| `TRACKER/GDPR_LOG.md` | First SAR or erasure | All GDPR-related actions logged |
| `business/GDPR_BREACH_PROTOCOL.md` | Handover Stage 7 | Pre-filled breach response template |

---

## Hard limits — what Axis OS does NOT do

- Does not give legal advice. Customers needing certainty must consult their DPO or solicitor.
- Does not register the customer with ICO. Most UK businesses processing personal data must register and pay an annual fee (£40–£60 for most SMEs) — flag this at handover Stage 4.
- Does not handle special category data (health, biometric, political, religious) without explicit Wayne sign-off. The handover agent halts if Onboarding reveals the customer processes special category data.
- Does not represent the customer in a regulator complaint or breach investigation.

---

## Maintenance

**Quarterly review checklist (Wayne to run):**
- Verify all DPA URLs in Annex A still resolve
- Check ICO guidance for any changes (ico.org.uk/for-organisations)
- Review the EU-US Data Privacy Framework status
- Update retention defaults if statutory periods change

**Last reviewed:** 2026-04-30
**Next review due:** 2026-07-30
