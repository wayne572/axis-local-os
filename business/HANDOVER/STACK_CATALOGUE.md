# Axis OS v2 — Stack Catalogue

Pre-tested tool combinations the Handover Agent recommends from.

**Rule:** The Handover Agent must recommend a stack from this catalogue only. Never invent combinations. If a customer needs something not covered, halt and flag for Wayne.

**Currency:** All prices in £ GBP, monthly, exc. VAT, based on UK pricing as of April 2026. Prices change — review quarterly.

---

## How the Handover Agent uses this file

1. After Stage 3 (Diagnose), read this file
2. Match the customer's priority workflows to the closest stack below
3. Cross-check against:
   - Tools they already pay for (don't double-up)
   - Their monthly budget cap
   - Their off-limits list
4. Recommend the matched stack to the customer in plain English
5. If they want alternatives, offer the stack's listed alternatives
6. Never go off-catalogue

---

## Stack 01 — Lead Qualifier (Universal Core)

**Use when:** the priority workflow is lead capture and follow-up. This is the most common entry stack — applies to roughly 80% of SME deployments.

**What it builds:**
- Public enquiry form on the website
- Leads land in a structured database
- Auto-acknowledgement to the lead
- Owner gets a Slack/email ping with qualification status
- Auto-draft follow-up emails at day 2 and day 5

**Tools:**
| Tool | Purpose | Cost |
|---|---|---|
| Typeform (Basic) | Enquiry form on website | £25/mo |
| Airtable (Free) | Lead database | £0 |
| Zapier (Starter) | Connector between tools | £20/mo |
| Gmail (existing) | Outreach drafts land here | £0 |
| Slack (Free) | Ping owner on new lead | £0 |

**Total:** £45/month

**Alternatives:**
- Replace Typeform with Tally (£0) — saves £25/mo, slightly less polished
- Replace Airtable with Google Sheets (£0) — works but loses structured views
- Replace Zapier with Make.com (£10/mo) — saves £10/mo, steeper learning curve

**What it doesn't include:**
- A full CRM (HubSpot, Salesforce) — out of scope
- Calendar booking — see Stack 02
- Payment collection — out of scope

---

## Stack 02 — Booking & Onboarding

**Use when:** the priority workflow is converting enquiries into bookings, and onboarding new clients consistently.

**What it builds:**
- Calendar booking link customers can self-serve
- Auto-confirmation and reminder emails
- Standard onboarding email sequence (welcome, document checklist, kickoff)
- Onboarding tasks tracked in Airtable

**Tools:**
| Tool | Purpose | Cost |
|---|---|---|
| Calendly (Standard) | Self-serve booking | £10/mo |
| Airtable (Free) | Onboarding task tracker | £0 |
| Zapier (Starter) | Connect Calendly → Airtable → Gmail | £20/mo |
| Gmail (existing) | Onboarding emails | £0 |

**Total:** £30/month

**Alternatives:**
- Replace Calendly with Cal.com (£0) — open-source, saves £10/mo
- Replace Calendly with Microsoft Bookings (included with M365) — £0 if already on M365

**What it doesn't include:**
- Payment processing — out of scope
- Contract/e-signature — see Stack 06

---

## Stack 03 — Content Engine

**Use when:** the priority is consistent content output (LinkedIn + social) and the owner has no time to post manually.

**What it builds:**
- Weekly content draft batch (4–8 posts)
- Brand-checked through QA Agent
- Scheduled posts via Buffer or Notion calendar
- Performance log in Airtable for monthly review

**Tools:**
| Tool | Purpose | Cost |
|---|---|---|
| Buffer (Essentials) | Scheduling LinkedIn + 1 other platform | £5/mo |
| Airtable (Free) | Content log and performance tracker | £0 |
| Canva (Free) | Lightweight visuals if needed | £0 |

**Total:** £5/month

**Alternatives:**
- Replace Buffer with native LinkedIn scheduling (£0) — works for LinkedIn only
- Upgrade Canva to Pro (£11/mo) — only if they need heavy design assets

**What it doesn't include:**
- Paid ads — out of scope
- Video editing — out of scope

---

## Stack 04 — Pipeline & Reporting

**Use when:** the priority is visibility — owner can't see their pipeline, can't run a monthly review.

**What it builds:**
- Live pipeline in Airtable (leads, proposals, active clients)
- Status snapshot via the `What is the current status?` command
- Monthly review using `Let's do the monthly system review`

**Tools:**
| Tool | Purpose | Cost |
|---|---|---|
| Airtable (Free, upgrade if >1k records) | Pipeline database | £0–£20/mo |
| Slack (Free) | Optional weekly digest | £0 |

**Total:** £0–£20/month

**Alternatives:**
- None recommended. Airtable is the canonical Axis OS v2 pipeline tool.

**What it doesn't include:**
- Forecasting tools — out of scope
- Accounting integration — see Stack 05

**AML-regulated customer extension (auto-applied if GDPR.md flags AML-regulated vertical):**
- Add `CDD_Complete` (yes/no) and `CDD_Date` fields to the pipeline
- Add `PEP_Status` (yes/no) field — flag in views
- Pipeline Agent rule: never set client status to "Active" if `CDD_Complete = no`
- Retention rule: keep all records minimum 5 years from end of business relationship (we default to 6 — already aligned)
- Hard limit: Outreach Agent and Content Agents must never write about SARs or suspicious activity for these clients

---

## Stack 05 — Cash Flow & Invoicing

**Use when:** the priority workflow is invoice follow-up and payment chasing (common in trades, construction, agencies).

**What it builds:**
- Invoice tracker in Airtable (synced from accounting tool)
- Auto-draft chase emails at day 7 and day 14
- Slack ping when invoice goes overdue

**Tools:**
| Tool | Purpose | Cost |
|---|---|---|
| Existing accounting (Xero/QuickBooks/FreeAgent) | Source of invoice data | varies — often already paid |
| Zapier (Starter) | Sync invoices to Airtable | £20/mo |
| Airtable (Free) | Tracker | £0 |
| Gmail (existing) | Chase email drafts | £0 |

**Total:** £20/month (assuming accounting already exists)

**Alternatives:**
- Use Make.com instead of Zapier (£10/mo)
- For solo traders without accounting: skip this stack and recommend they pick an accounting tool first

**What it doesn't include:**
- Direct debit collection — out of scope
- Credit checking — out of scope

---

## Stack 06 — Proposal & Contract

**Use when:** the priority is proposal follow-up (professional services, agencies, consultants).

**What it builds:**
- Proposal tracker in Airtable
- Auto-draft follow-up at day 3, 7, 14
- Optional: e-signature via existing tool

**Tools:**
| Tool | Purpose | Cost |
|---|---|---|
| Airtable (Free) | Proposal tracker | £0 |
| Zapier (Starter) | Trigger follow-up sequences | £20/mo |
| Gmail (existing) | Follow-up drafts | £0 |
| Existing e-sign (DocuSign/PandaDoc) | If they have one | varies |

**Total:** £20/month (using existing e-sign if any)

**Alternatives:**
- For low volume: skip Zapier, run manually via the Outreach Agent (£0)

**What it doesn't include:**
- Proposal generation — handled by Outreach Agent inside Axis OS v2

---

## Off-limits substitution table

When a customer puts a tool on their off-limits list, the Handover Agent must offer a substitute, not silently drop the tool. Use this table:

| Off-limits tool | Substitute | Trade-off |
|---|---|---|
| Slack | Gmail (digest emails) or Microsoft Teams | Slower notifications, more email noise |
| Zapier | Make.com, n8n, or manual workflow | More setup time, possibly cheaper |
| Airtable | Google Sheets, Notion, or HubSpot Free | Less structured views, may hit feature limits |
| Typeform | Tally, Google Forms, or Microsoft Forms | Less polished UX |
| Buffer | Native LinkedIn scheduling, Hootsuite Free | Single-platform only |
| Calendly | Cal.com, Microsoft Bookings (M365) | Different UI, similar function |
| Gmail | Outlook (M365) | Same function, different platform |

If a customer lists a tool as off-limits and the table doesn't have a substitute, halt and ask Wayne. Do not skip a tool's function silently — that produces a degraded stack the customer doesn't realise they have.

---

## Regulated industry notes per stack

If MEMORY.md has REGULATED_INDUSTRY set, the Handover Agent surfaces these notes per stack:

| Stack | Regulated industry note |
|---|---|
| 01 — Lead Qualifier | All auto-reply and follow-up email drafts must be reviewed for compliance language before sending. Acknowledgement emails are usually fine; anything that mentions services or pricing needs sign-off. |
| 02 — Booking & Onboarding | Confirmation and onboarding emails are operational — usually low compliance risk. Welcome content that describes services needs review. |
| 03 — Content Engine | **High compliance risk.** Every LinkedIn or social post must go through compliance sign-off before posting. Build the review step into the workflow. |
| 04 — Pipeline & Reporting | Internal-only. No client-facing content. Compliance not engaged. |
| 05 — Cash Flow & Invoicing | Invoice chase emails are operational and follow standard wording — usually low risk. Have compliance approve the template once. |
| 06 — Proposal & Contract | **High compliance risk.** All proposals must be reviewed by compliance. Follow-up emails should reference the proposal but not introduce new claims. |

For FCA-regulated firms specifically: financial promotions rules under the FCA Handbook require approval by an authorised person. The Axis OS QA Agent is not an authorised person.

---

## Combining stacks

Most customers will run 2 stacks in parallel after the 14-day sprint. The Handover Agent should recommend the **2 priority stacks only** at handover. Additional stacks layer in during month 2–3.

**Common combinations:**

| Vertical | Recommended starting stacks |
|---|---|
| Professional services | Stack 01 + Stack 06 |
| Trades & home services | Stack 01 + Stack 05 |
| Health & wellness | Stack 01 + Stack 02 |
| Property | Stack 01 + Stack 04 |
| Retail & e-commerce | Stack 03 + Stack 04 |
| Hospitality | Stack 01 + Stack 03 |
| Education & training | Stack 01 + Stack 03 |
| Creative agencies | Stack 06 + Stack 03 |
| Construction | Stack 01 + Stack 05 |
| Non-profits / CICs | Stack 03 + Stack 04 |
| Recruitment | Stack 01 + Stack 04 |
| Financial services | Stack 04 + Stack 06 |

---

## Off-catalogue requests

If a customer says "I want to use [tool not listed]", the Handover Agent must:

1. Check whether the tool is functionally equivalent to a listed alternative (e.g. Pipedrive instead of Airtable for pipeline). If equivalent, accept it and flag in CHANGELOG.md as "off-catalogue substitution".
2. If not equivalent but the customer still wants to use it, route to the **Off-Catalogue Tool Fallback** flow in SETUP_SCRIPTS.md. The agent uses WebSearch and WebFetch to pull official setup guidance, walks the customer through it, and logs the steps for future catalogue review.
3. If the tool involves regulated data (financial accounts, medical records, legal contracts), halt and flag for Wayne — never proceed on regulated tooling without explicit sign-off.
4. Always log off-catalogue tools to `business/HANDOVER/_OFF_CATALOGUE_LOG.md` so patterns can feed the quarterly catalogue review. If the same tool appears 3+ times, it becomes a candidate for full inclusion.

Stability still matters — but the customer is never blocked just because their preferred tool isn't on our list.

---

## Maintenance

**Quarterly review checklist (Wayne to run):**
- Confirm all listed tools still exist and at quoted prices
- Check for new tools that should be added to the catalogue
- Remove tools that have been deprecated or have had major UX regressions
- Update the "common combinations" table based on real deployment data

**Last reviewed:** 2026-04-30
**Next review due:** 2026-07-30
