# DEAL_SOURCING_LEAD_IDENTIFICATION.md

## 1. Status
Active - Workflow File (Production v3)

---

## 2. Purpose
Define how leads are identified, filtered, and prepared for outreach.

This ensures:

- high-signal lead discovery
- compliant targeting
- consistent pipeline input
- efficient execution

---

## 3. Core Principle

Find real businesses first -> verify second.

---

## 4. System Rules

- prioritise active, visible businesses
- avoid registry-first discovery
- apply compliance and quality checks before outreach
- enforce speed + clarity (2-minute rule)

---

## 5. Approved Lead Sources

Use:

- LinkedIn (company search - primary)
- Google Maps (service intent searches)
- industry directories (Yell, Trustpilot, Bark, etc.)
- referrals

---

## 5A. Country Default Rule

Default to official registries based on user location:

- UK -> Companies House
- US -> State registries
- CA -> Federal / Provincial registries
- AU -> ASIC
- IE -> CRO
- NZ -> Companies Office
- SG -> ACRA

Used for **verification only**, not discovery.

---

## 5B. Lookup Default Order (2-Min Rule)

For each lead:

1. Website (FIRST)
2. LinkedIn company page
3. LinkedIn person (fallback)

Hard cap:

- 2 minutes per lead
- if unclear -> move on

---

## 5C. Source Ordering Rule (NEW - CORE LOGIC)

Default discovery order:

1. LinkedIn company search (primary)
2. Google Maps / industry directories
3. Companies House (verification only)

Companies House must NOT be used for lead discovery.

Reason:

- registries contain inactive / PSC / non-operational entities
- real businesses exist where customers find them

---

## 6. Avoid Sources

DO NOT use:

- scraped personal data
- purchased B2C lists
- unknown/unverified databases
- registry-only discovery

---

## 7. Verification Checks

Each lead must pass:

- correct business type
- correct role (decision-maker or relevant)
- active business (website or LinkedIn presence)
- ICP match
- valid contact route
- no compliance red flags

---

## 7A. Compliance Checks (UK GDPR / PECR)

Before outreach:

- confirm B2B context
- confirm relevance
- record lawful basis
- avoid special category data
- flag risks early

If unclear:

-> mark Compliance Hold

---

## 7B. Personal Service Company (PSC) Filter

Identify and reject contractor-style entities.

If LinkedIn shows the named director:

- "Open to work" or actively job-seeking
- working across multiple companies in a contractor pattern
- primarily identified as an employee/contractor
- no clear business presence (no website, no service offering)

-> Reject

Reason:
Personal Service Company (PSC), not an active business serving clients.

---

## 8. Volume Rule

Do NOT identify only the number you plan to contact.

Instead:

- identify 15-20% MORE leads

Reason:

- compliance filtering
- PSC filtering
- invalid leads

---

## 9. Daily / Weekly Targets

Suggested baseline:

- Daily: 10 leads identified
- Weekly: 50 leads
- Monthly: 200 leads

Adjust based on:

- response rate
- qualification rate

---

## 10. Execution Steps

1. search LinkedIn companies (primary)
2. search Maps/directories (secondary)
3. select potential leads
4. run website-first lookup
5. verify LinkedIn presence
6. apply verification checks
7. apply compliance checks
8. apply PSC filter
9. verify legal entity via registry (if needed)
10. add to tracker
11. assign initial status

---

## 11. DCoS Roles

ChatGPT DCoS:
- generates lead ideas
- structures identification workflows

Claude DCoS:
- checks compliance risks
- validates logic

Claude controls execution.

---

## 12. Output Requirement

Leads must be:

- real (visible in market)
- active
- contactable
- compliant
- business-operated (not contractor-based)

---

## 13. Failure Conditions

- registry-first discovery used
- too many rejects (signal too low)
- poor ICP fit
- missing verification
- compliance ignored
- PSC leads included

---

## 14. End State

Lead identification is working when:

- leads are high quality from the start
- outreach conversion improves
- reject rate drops
- time per lead decreases

The system produces:

High-signal input -> predictable pipeline output
