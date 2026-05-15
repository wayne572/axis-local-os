# Day 3 - Prospect List Brief
**UK Commercial Cleaning + Facilities - 200 Owner-Operators**
*v1.0 - 2026-04-30*

---

## Warning: Status

The Apollo MCP attempted the pull and returned:

> *"This endpoint is not accessible with this access token on a free plan."*

You will need to either:
1. **Upgrade Apollo** to a Basic or Professional plan (Basic ~GBP 39/mo, Professional ~GBP 79/mo per seat) - required to run programmatic API pulls and bulk-export contacts with verified emails, OR
2. **Run the search manually in the Apollo web UI** today using the exact filters below (the web UI works on free, with credit limits per month) and export a CSV.

Either route uses the same ICP definition. The MCP-driven approach becomes valuable once Apollo is upgraded - you'll be able to refresh the list weekly without manual work.

---

## ICP - Locked Definition (Phase 1)

| Filter | Value |
|---|---|
| Country | United Kingdom |
| Industry / Keyword | Commercial cleaning, Cleaning services, Facilities management, Janitorial services |
| Employee count | 11-200 |
| Revenue band | GBP 500,000 - GBP 5,000,000 |
| HQ region | UK only - exclude Ireland |
| Job titles | Owner, Founder, Managing Director, Director, CEO |
| Seniority | Owner, Founder, C-suite |
| Email status | Verified or Likely to engage |
| Sectors out of scope | Domestic cleaning (B2C), single-trader sole proprietors, franchises (head office handles BD) |

**Why these filters:**
- 11-200 staff = past survival stage, not yet so big they have an internal BDR team.
- GBP 500k-GBP 5m revenue = likely to feel the pain of inconsistent pipeline and have budget for a properly scoped service.
- Owner / MD / Director = decision-maker, not a gatekeeper.
- UK only = your compliance regime, your time zone, your case studies (Shimmer).

---

## Apollo Search String (paste into Apollo UI)

```
Location: United Kingdom
Headcount: 11-50, 51-200
Revenue: $650k - $6.5m  (approx. GBP 500k-GBP 5m, USD conversion at 1.30)
Keywords: "commercial cleaning" OR "facilities management" OR "janitorial"
Job titles: Owner, Founder, Managing Director, Director, CEO
Seniority: Owner, Founder, C-Suite
Email status: Verified
```

Save the search inside Apollo as **"PaaS - UK Cleaning - Phase 1"** so it can be re-run.

---

## Pull Plan - 200 Contacts

- Run the search above.
- Sort by Revenue (descending) - top of pipeline first.
- Export the first 200 contacts to CSV.
- Required fields: First name, Last name, Job title, Company, Domain, Verified email, LinkedIn URL, City, Employee count, Revenue band.
- Save export to the approved SF&W Project Solutions prospect-list location using the format: `YYYY-MM-DD_SECTOR_COUNT.csv`

---

## Compliance Pre-Flight (run before any contact is added to outreach)

- [ ] Confirm every record is a **business** email and a **business** address (no personal Gmail / personal phone).
- [ ] Confirm titles are role-relevant (cleaning company owner = relevant; their PA, accountant, or HR person = not).
- [ ] Cross-check against the master Suppression List - remove any matches.
- [ ] Cross-check against any client-supplied do-not-contact list.
- [ ] Document the legitimate interest assessment (LIA) - one paragraph saved alongside the CSV explaining why this list, this offer, this method.

---

## Segmentation (for outreach personalisation)

Split the 200 into 3 cohorts so the cold sequence can be lightly personalised without becoming bespoke:

| Cohort | Filter | Hook angle |
|---|---|---|
| A - Mid-market | 51-200 staff | "Replace the BDR you can't keep" |
| B - Growing | 11-50 staff, GBP 1m+ revenue | "Predictable contract pipeline" |
| C - Lean operators | 11-50 staff, sub-GBP 1m | "Win bigger contracts without hiring" |

---

## Next Action (Day 4 in the launch plan)

Write the cold-email sequence - 5 touches over 14 days - using the cohort hooks above. This is queued as Day 4.

---

## Notes for Wayne

- **Upgrade Apollo if you want this automated.** Without an upgrade, every list refresh is a manual 30-minute job.
- Free-plan Apollo gives ~25 verified email reveals per month - not enough for 200 contacts. Budget a one-month Professional plan (GBP 79) just to do the initial export, then drop back if you want.
- Alternative: **Cognism** or **Lusha** as data sources. Apollo is the recommendation because it's already wired into your stack and the MCP is live.
