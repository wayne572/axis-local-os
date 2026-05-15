# Wayne Francis / SF&W Project Solutions - Pipeline-as-a-Service (PaaS)
**Launch Plan - v1.0**
Owner: Wayne Francis
Date: 2026-04-30

---

## 1. The Offer

**Name:** Pipeline-as-a-Service
**Tagline:** *"You don't buy leads. You own a pipeline we run for you."*

**What the client gets:**
- A branded lead engine (their domain, their CRM, their data).
- 30-60 qualified B2B leads per month in their target vertical + region.
- Booked discovery calls direct to their calendar.
- Monthly performance report.

**What Wayne Francis / SF&W Project Solutions keeps:**
- The engine itself (Apollo + outreach stack + qualification agents).
- The right to run identical engines for non-competing clients.

---

## 2. Pricing

| Tier | Setup | Monthly | What's included |
|---|---|---|---|
| **Starter** | in review | in review | 30 qualified leads, 1 vertical, 1 region |
| **Growth** | in review | in review | 60 leads, 2 verticals OR 2 regions |
| **Scale** | in review | in review | 120 leads, multi-region, dedicated review call |

Pricing is not locked. The old Deployment and Live pricing is superseded and must not be used.

**Target:** commercial target to be recalculated after Wayne approves pricing.

---

## 3. The Stack (what gets built)

| Layer | Tool | Purpose |
|---|---|---|
| Sourcing | Apollo (your existing MCP) | ICP-matched contact discovery |
| Enrichment | Apollo + Common Room | Verify, enrich, score |
| Outreach | Gmail / Instantly / Apollo sequences | Multi-step email + LinkedIn |
| Qualification | Claude API agent (System 01 base) | Reply triage, intent scoring, objection handling |
| Booking | Calendly / Cal.com | Direct to client's calendar |
| CRM | Airtable or client's existing CRM | Lead record + activity log |
| Reporting | Looker Studio / Notion dashboard | Monthly performance |

Reuse 80% of System 01 - Lead Qualifier. Only new build is the per-client config layer.

---

## 4. Vertical Pick (start here)

**Phase 1 vertical: UK commercial cleaning + facilities companies, GBP 500k-GBP 5m revenue.**

Why:
- You already have Shimmer in this lane - domain knowledge.
- Owner-operators reachable via Apollo.
- Buy cycle is short.
- Clear pain (winning B2B contracts).
- Easy referral loops.

Phase 2 verticals (after 3 paying clients): trades, accountants, IT MSPs.

---

## 5. UK Compliance Checklist (do before client #1)

- [ ] **Register with ICO as a data controller** (GBP 40-GBP 60/yr) - declare "lead generation services for B2B clients" as a processing purpose
- [ ] **Draft a Data Processing Agreement (DPA)** template - you act as a *processor* for the client (clean position; client is the controller)
- [ ] **Privacy Policy update** on waynefrancis.co.uk - disclose PaaS processing
- [ ] **Lawful basis statement:** Legitimate interest for B2B contact, role-relevant only, business addresses only
- [ ] **Suppression list** - every contact who opts out is added to a master suppression file shared across all clients
- [ ] **Apollo ToS check** - confirm reseller/processor use is permitted under your plan
- [ ] **PECR-compliant unsubscribe** in every outbound message
- [ ] **No B2C** - refuse consumer leads; B2B only, full stop
- [ ] **No special-category data** (health, finance role-targeting requires extra review)

Deliverables to draft:
1. DPA template (client signs at onboarding)
2. Privacy notice addendum
3. Suppression list policy
4. Onboarding compliance form (client confirms their lawful basis to contact leads)

---

## 6. The 90-Day Build

### Days 1-14 - Foundation
- ICO registration submitted
- DPA + privacy docs drafted (use the gdpr agent in Axis OS v2.1)
- One-page sales sheet built
- Pricing locked (above)
- Outreach engine v1 spec written (reuse System 01)

### Days 15-30 - Pilot client #1
- Sign one pilot client only after Wayne approves pilot pricing and compliance wording
- Build engine, deliver 30 leads, document everything
- Capture results: leads, calls booked, deals closed
- Get a written testimonial + permission to use logo

### Days 31-60 - Productise + sell
- Convert pilot results into a one-pager + a 90-second video
- Outreach to 200 cleaning company owners via Apollo
- Target: 3 paying clients at full price by day 60

### Days 61-90 - Scale to 8 clients
- Add Growth tier
- Hire/contract 1 VA for inbox triage (GBP 300/mo)
- Onboard clients 4-8
- Revenue target to be recalculated after pricing approval

---

## 7. Sales Funnel

```
Apollo prospect list (200 owners)
        down
Cold email sequence (5 touches over 14 days)
        down
Short diagnosis call
        down
PaaS proposal (Starter / Growth / Scale)
        down
Sign DPA + invoice setup fee
        down
14-day build -> engine live
        down
Monthly retainer + quarterly review
```

---

## 8. Unit Economics

**Per Starter client:**
- Apollo seat cost share: ~GBP 60/mo
- Email infra (Instantly/SendGrid): ~GBP 40/mo
- VA inbox triage: ~GBP 60/mo
- Compute (Claude API): ~GBP 30/mo
- Gross margin to be calculated after pricing approval

8-client scenario to be calculated after pricing approval.

---

## 9. Risks + Mitigations

| Risk | Mitigation |
|---|---|
| ICO complaint from a contacted lead | Suppression list + clean opt-out + only role-relevant B2B |
| Client churn after month 3 | Quarterly review call + lead quality SLA |
| Apollo throttling / ToS breach | Diversify sourcing; add LinkedIn Sales Nav by month 6 |
| Reputational risk (bad outreach copy) | Every sequence reviewed by qa agent before launch |
| Wayne becomes the bottleneck | VA + SOPs by client #4 |

---

## 10. Immediate Next Actions (this week)

1. **Today** - Approve this plan / amend
2. **Day 1** - Draft DPA + privacy addendum (gdpr agent)
3. **Day 2** - Build PaaS one-pager (design + qa agents)
4. **Day 3** - Pull 200-prospect Apollo list (cleaning, UK, owner-operator)
5. **Day 4** - Write outreach sequence (outreach + qa agents)
6. **Day 5** - Submit ICO registration
7. **Day 7** - Launch first cold sequence

---

## 11. Success Metrics (90-day scoreboard)

- Pilot client signed by day 30
- 3 paying clients by day 60
- 8 paying clients by day 90
- MRR target approved by Wayne after pricing review
- Zero compliance complaints
- 1 documented case study with results

---

**Status:** Draft v1.0 - awaiting Wayne approval to begin Day 1.
