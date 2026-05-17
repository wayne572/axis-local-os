# Apollo Lead Enrichment Session — Work in Progress

**Date Started**: 2026-05-06  
**Status**: Paused — Free-plan API blocker discovered  
**Next Session**: Claude Code (CLI)

---

## Objective
Enrich 10 Companies House accounting firms with decision-maker contact information (Finance Directors, CFOs, Financial Controllers) using Apollo's free plan.

## Target Companies (10)
1. LEXDEN RELIANCE LTD
2. CLARITY THROUGH NUMBERS LIMITED
3. FINANCIAL LITERACY AND EDUCATION CONSULTING LIMITED
4. SKG ACCOUNTANT LTD
5. CRYSTAL ACCOUNTANCY SERVICES LTD
6. OC ACCOUNTANCY LTD
7. ZINSIGHTS ACCOUNTING & CONSULTANCY LTD
8. SURE ELMA TRUSTEE LTD
9. M.A.J BOOKKEEPING LIMITED
10. IMEC SQUARED LIMITED

**Company Profile**: All incorporated Dec 30-31, 2023; Active status; Primary SIC codes in accounting/tax/bookkeeping

---

## Apollo Free-Plan Limitation Discovered

**Critical Finding**: Apollo's free-tier access token blocks ALL enrichment and search APIs, not just discovery:

| API | Free Plan Status |
|---|---|
| `apollo_companies_search` | ❌ API_INACCESSIBLE |
| `apollo_people_api_search` | ❌ API_INACCESSIBLE |
| `apollo_people_match` | ❌ API_INACCESSIBLE |
| `apollo_organizations_enrich` | ❌ API_INACCESSIBLE |
| Enrich-Lead skill | ❌ Requires unavailable APIs |
| Prospect skill | ❌ Requires unavailable APIs |
| Sequence-Load skill | ❌ Requires leads to exist |

**Implication**: Systematic enrichment workflow cannot proceed with free plan. Free-tier access is limited to manual web platform interaction only.

---

## Decision Points for Tomorrow

### Option 1: Upgrade to Paid Plan
- **Pros**: Full API access, systematic enrichment of all 10 companies, scalable workflow
- **Cons**: Cost
- **Action**: Contact Apollo sales or upgrade account at https://app.apollo.io/

### Option 2: Focus on Warm Prospects
- **Context**: 2 warm prospects identified (Savannah, Cole)
- **Pros**: Build on existing interest, no API requirements
- **Action**: Verify status in Notion database, prepare personalized outreach

### Option 3: Alternative Enrichment Tool
- **Options**: LinkedIn Sales Navigator, Hunter.io, ZoomInfo, RocketReach
- **Pros**: May have free tier or trial access
- **Action**: Evaluate available tools

### Option 4: Manual Research + Apollo
- **Approach**: Manually look up company websites for the 10 firms, use domain-based enrichment if available
- **Blocker**: Web search currently restricted in Cowork; may work in Claude Code

---

## Files Created in This Session
- `apollo-enrichment-session.md` (this file) — Session notes and decision points
- Context saved to memory for next session

---

## Next Steps for Claude Code Session
1. Read this file to understand context
2. Choose a direction from the Decision Points above
3. If upgrading to paid plan: Test Apollo enrichment workflow on the 10 companies
4. If focusing on warm prospects: Verify Savannah & Cole status in Notion
5. If alternative tool: Evaluate and set up enrichment
6. If manual research: Research company websites and domains for the 10 firms

---

**Notes for Tomorrow**:
- User confirmed: "lets use the free plan, so keep within those limits" — but free plan APIs are too restrictive for this workflow
- User has 2 warm prospects (Savannah, Cole) that may be higher priority
- Cowork web search is blocked; Claude Code may have different network access
- Apollo skills available: enrich-lead, prospect, sequence-load (all blocked by API access)
