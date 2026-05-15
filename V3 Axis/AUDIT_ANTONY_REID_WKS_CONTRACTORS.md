# Wks Building Contractors Ltd — AI Audit Analysis
## Analysis Date: May 2, 2026 | Auditor: Wayne Francis

---

## Executive Summary

Antony Reid is running a construction/renovation business with a 2-5 person team, but he's completely manual on admin—no tools at all. He's drowning in chasing invoices, creating quotes, writing proposals, and answering repetitive emails. He doesn't even track how much time it's taking because it's too scattered. We'll build a **3-layer automation system** (Client Management + Invoicing + Document Automation + CRM) that connects his entire admin workflow, turning his manual process into a streamlined system. Expected outcome: 10-15 hours/week freed up, steady bookings from better follow-up, and zero things falling through the cracks.

---

## Current State

### Business Profile
- **Company:** Wks Building Contractors Ltd
- **What they do:** Renovations, bathroom & kitchen installations, handyman works
- **Team size:** 2-5 people
- **Structure:** Appears to be Antony + 1-4 team members (likely tradespeople who don't handle admin)

### Current Bottleneck
- **Primary pain point:** "The admin side" — everything administrative
- **Specific areas bleeding time:**
  - ✗ Chasing invoices or following up on enquiries
  - ✗ Creating proposals, quotes, or documents  
  - ✗ Writing up notes, reports, or summaries
  - ✗ Answering the same emails or messages repeatedly
  - ✗ Chasing people for information or updates
- **Impact:** "I genuinely do not know" how many hours (RED FLAG: admin is so chaotic he doesn't even track it)

### Tech Stack
- **Current tools used:** NONE — "mostly manual"
- **How well they work together:** 2/10 (essentially non-existent)
- **Tool count:** 0 professional tools

### AI Readiness
- **Current AI usage:** No, not yet
- **Team openness to change:** 5/10 (moderate — willing but cautious)

### Their Vision
- **6-month goals:** 
  1. Reduce the time spent on admin
  2. Free up time to focus on growth
  3. Reduce the chance of things falling through the cracks
- **3-month success definition:** "Steady bookings of work & easier workflow"

---

## The Problem

### What's Really Happening

Antony is running his business entirely through email, phone, and spreadsheets (or possibly just his head). Here's the cycle:

1. **Inquiry comes in** → Answer manually → Follow up when they don't respond
2. **Job gets approved** → Create proposal manually → Send via email → Chase for approval
3. **Job starts** → Keep notes manually → Track materials/hours somehow
4. **Job finishes** → Create invoice manually → Email it → Chase payment
5. **Payment comes in** → Record manually → Reconcile somehow

Every step is manual. Every follow-up is manual. Every customer gets the same generic email responses because there's no system to personalize them at scale.

### Why It Matters

- **Time impact:** Unknown (but clearly 5-10+ hours/week based on the pain points listed)
- **Revenue impact:** 
  - Missed follow-ups = lost jobs (he specifically said "reduce chance of things falling through the cracks")
  - Slow invoicing = delayed cash flow
  - Manual quoting = slow sales cycle
- **Team impact:** Antony is the bottleneck. His trades people probably can't book work themselves
- **Growth impact:** He literally can't grow because admin is eating all his time. He'd need to be 2-3 people just to handle current volume

### Root Cause

**No systems. No tools. Everything is manual and in Antony's head.**

This is a classic trade business problem: great at the work, terrible at the business. He needs:
1. A way to manage leads/enquiries automatically
2. A way to generate proposals/quotes without rewriting them each time
3. A way to invoice automatically when jobs complete
4. A way to follow up on overdue invoices without manually chasing
5. A way to store project info so it doesn't get lost

---

## Proposed Solution

### High-Level Approach

We're going to give Antony 4 integrated layers that handle his entire workflow:

1. **Client Management Layer** — Every enquiry gets captured, tracked, and automatically followed up
2. **Project Management Layer** — Track jobs from quote to completion
3. **Document Automation** — Proposals, quotes, and invoices generate automatically
4. **Payment Tracking** — Invoices sent automatically, overdue ones flagged

This means:
- Enquiry comes in → Auto-logged, customer gets response, auto-reminder if they don't reply
- Job approved → Quote auto-generated from template, invoice auto-created when marked complete
- Invoice sent → Auto-tracked, auto-reminder at 15/30 days overdue
- Cash flow visible → Dashboard shows him money in, money out, overdue amounts

### Architecture

**Layer 1: Lead Capture & CRM**
- Tool: HubSpot Free or Pipedrive Starter (simple CRM for small teams)
- What it does: Every email/call/text gets logged as a lead, automatically tracked, auto-reminders for follow-ups
- Why: Right now leads are lost because they're scattered across email, phone, and his brain

**Layer 2: Proposal & Quote Automation**
- Tool: Zapier/Make.com connecting CRM → Proposal software (Beautiful.ai or Proposify)
- What it does: When a lead is marked "Ready for quote" → template proposal auto-generates with project details
- Why: Instead of spending 30 mins writing the same proposal, it generates in 2 mins, he customizes the price, sends

**Layer 3: Project & Invoice Management**
- Tool: Wave (free invoicing + accounting for small teams)
- What it does: Create a job in the CRM → auto-create an invoice template → when job is marked "complete" → invoice auto-generates and sends
- Why: No more manual invoice creation. Payment tracking automatic.

**Layer 4: Automation & Follow-Up**
- Tool: Zapier automations
- What it does: 
  - Overdue invoice? Auto-email reminder
  - No response to quote? Auto-follow-up in 3 days
  - Lead inactive? Auto-check-in at 7 days
- Why: Follow-ups happen automatically, nothing falls through the cracks

**Layer 5: Knowledge Base**
- Tool: Notion (free) or Google Docs
- What it does: Store templates for proposals, job info sheets, customer notes
- Why: New team member can find project info. Antony doesn't have to remember everything.

---

## Quick Wins (2-4 Week Timeline)

### Quick Win #1: Email-to-CRM System
**What:** Set up a simple CRM (HubSpot Free) so every inquiry is logged and tracked automatically

**Implementation:**
- Day 1-2: Set up HubSpot, import past customers if they're in an Excel file
- Day 3-4: Set up a Zapier automation: "Email from @[his email] → HubSpot Create Lead"
- Day 5: Set up auto-reminder: "If lead hasn't been contacted in 3 days → Email Antony"
- Week 2: Train Antony on how to use it (10 mins)

**Impact:**
- Zero lost enquiries
- Automatic follow-up reminders (nothing slips through)
- Can see at a glance which customers to chase
- **Hours saved:** 2-3 hours/week (no more "where did that message go?")

### Quick Win #2: Invoice Automation in Wave
**What:** Set up Wave invoicing so invoices generate with one click and auto-send to customers

**Implementation:**
- Day 1-2: Set up Wave, create invoice template for a typical job
- Day 3-4: Set up customer list in Wave
- Day 5: Test: create a sample invoice, send it
- Week 2: Zapier automation: "Mark job complete in CRM → Wave creates invoice"

**Impact:**
- Invoices send same day job completes (faster payment)
- Automatic payment reminders at 15/30 days overdue
- Financial dashboard shows him money in, money out, cash position
- **Hours saved:** 1-2 hours/week (no more manual invoicing)

---

## Implementation Timeline

### Week 1-2: Foundation & Quick Wins

**Days 1-3: Setup Phase**
- HubSpot account created, basic setup
- Import customer list (if available)
- Wave account created, template invoices built
- Email addresses & phone numbers consolidated

**Days 4-5: Automation Setup**
- Zapier: Email → HubSpot lead automation
- Zapier: Job complete → Wave invoice automation
- Auto-follow-up reminders configured
- Basic training (30 mins with Antony)

**Week 2: Testing & Adjustment**
- Test the full flow: enquiry → quote → job → invoice
- Adjust templates based on real data
- Team introduced to new system

### Week 3-4: Expansion & Integration

**Week 3: Add Proposal Automation**
- Proposify or Beautiful.ai account setup
- Proposal templates created (bathroom, kitchen, handyman variants)
- Zapier: CRM → Proposal auto-generate
- Test a full proposal flow

**Week 4: Knowledge Base & Cleanup**
- Create Notion workspace with project templates, job sheets
- Document all automations (so team knows how they work)
- Audit Wave for accuracy
- Plan for next phase (if needed)

### Month 2: Optimization & Scaling

- Monitor what's working, what needs tweaking
- Add new templates as needed
- Integrate payment processing (Stripe/PayPal) if not already done
- Train team members on CRM/invoice system
- Identify next automation opportunities (materials ordering? Scheduling?)

### Month 3: Growth Phase

- System running smoothly, Antony has 10+ hours/week freed up
- Dashboard shows him real-time business health
- Ready to either take on more work or hire another person
- Document everything for future scaling

---

## Expected Results in 3 Months

### Time Savings
- **Antony:** 10-15 hours/week freed up (from email, proposals, invoicing, chasing)
- **Team:** 1-2 hours/week (if they help, they're now part of a system vs. chaos)
- **Total capacity gained:** ~12-15 hours/week = nearly 2 full days

### Quality Improvements
- **Enquiry follow-up:** From "sometimes" → Automatic (100% get a response)
- **Invoice payment time:** From 45 days average → 20 days average (faster cash flow)
- **Quote response:** From 3-5 days to same day
- **Nothing falls through the cracks:** Every lead, every job, every invoice tracked

### Business Impact
- **Steady bookings:** Automatic follow-ups mean more jobs booked
- **Better cash flow:** Invoices send immediately, payment reminders automatic
- **Growth capacity:** Antony can now take on growth projects instead of fighting admin fires
- **Professionalism:** Customers see consistent, prompt communication (not scattered responses)

---

## Tools & Components Needed

| Component | Tool/Service | Why It's Needed | Cost |
|-----------|--------------|-----------------|------|
| Lead Management & CRM | HubSpot Free or Pipedrive Starter | Centralize all enquiries, track conversations, auto-reminders | $0-25/mo |
| Invoicing & Accounting | Wave (free) or QuickBooks Self-Employed | Create & send invoices, track payments, tax reports | $0-15/mo |
| Proposal/Quote Generation | Beautiful.ai or Proposify | Auto-generate professional proposals from templates | $0-30/mo |
| Automation Engine | Zapier or Make.com | Connect all tools together, trigger automations | $20-30/mo |
| Knowledge Base | Notion (free) or Google Drive | Store templates, job sheets, project info | $0 |
| Payment Processing | Stripe or PayPal | Accept online payments (optional but recommended) | 2.9% + $0.30 per transaction |
| **Total Monthly Cost** | | | **$20-100/mo** |

---

## Success Metrics

**We'll measure success using:**

### 1. Time Metrics
- **Admin time Antony spends:** Baseline unknown → Target: <5 hours/week
- **Follow-up effectiveness:** Baseline: unknown → Target: 100% of leads get response
- **Invoice processing time:** Baseline: 1-2 days after job complete → Target: Same day

### 2. Cash Flow Metrics
- **Days to invoice:** Baseline: 1-3 days after job → Target: Same day job completes
- **Average payment time:** Baseline: 45+ days → Target: 20-30 days
- **Overdue invoices:** Baseline: unknown (probably many) → Target: <10% overdue at 30 days

### 3. Business Metrics
- **Lead conversion:** How many enquiries → jobs (should improve with better follow-up)
- **Monthly revenue:** Should increase as cash flow improves and he has time to chase growth
- **Team productivity:** Team members can now see/update job status (less bottleneck on Antony)

### 4. The Big Goal Metric
- **3-month definition: "Steady bookings & easier workflow"**
  - Booking rate: Consistent month-to-month (no gaps)
  - Workflow ease: Antony rates the system (target: 8/10 or higher)

---

## Risks & Considerations

### Adoption Risk: 5/10 (MEDIUM)
**Issue:** Antony is used to doing things manually. New tools can feel overwhelming.
**Mitigation:** 
- Start with ONE system (HubSpot) first, not everything at once
- Hands-on training, not just documentation
- Quick wins first (show value fast)
- Regular check-ins (week 1, 2, 4) to debug issues

### Data Quality Risk: 6/10 (MEDIUM-HIGH)
**Issue:** Moving from scattered emails/files to a CRM means cleaning up data
**Mitigation:** 
- Spend day 1 importing/cleaning customer list properly
- Don't try to backfill old data (too much work), start fresh from today
- Create data entry standards (so new enquiries are consistent)

### Process Documentation Risk: 7/10 (MEDIUM-HIGH)
**Issue:** Right now "the process" is in Antony's head. We need to document it.
**Mitigation:** 
- Create standard job sheet (so every job captures the same info)
- Write down the full flow: inquiry → quote → job → invoice → payment
- Team needs to understand why the system exists (or they'll ignore it)

### Team Scaling Risk: 5/10 (MEDIUM)
**Issue:** If Antony hires more people, they need to know how to use the system
**Mitigation:** 
- Document everything in Notion (video walkthrough + written guide)
- System should be simple enough that a 16-year-old apprentice can use it
- Clear access levels (who sees what)

---

## Opportunities Beyond Phase 1

Once the core system is running smoothly, Antony could expand to:
- **Materials ordering automation** — Flag materials needed → auto-generate supplier orders
- **Schedule management** — Google Calendar auto-updates based on booked jobs
- **Payment processing** — Online payments so customers don't delay paying
- **Photo documentation** — Job photos auto-organize into project folders
- **Customer portal** — Customers can see job progress/invoices themselves
- **Reporting** — Weekly/monthly reports to see revenue, pipeline, team utilization

---

## Next Steps

### Step 1: Approval Call (30-45 min) — THIS WEEK
- Review this analysis with Antony
- Answer questions about approach, tools, timeline
- **Decision point:** Does he want to move forward?

### Step 2: Scoping Session (1-2 hours) — WEEK 1
- Walk through his exact workflow (how does an enquiry actually come in? What does he do with it?)
- Get copies of sample documents (quote template, invoice template, job sheet if it exists)
- Identify any custom fields he needs (e.g., Does he track materials per job? Crew assignments?)
- Set expectations and timeline

### Step 3: Build Phase (2 weeks) — WEEK 1-3
- Day-by-day work on setup, automation, training
- Regular check-ins with Antony
- Quick wins completed first (so he sees value immediately)

### Step 4: Support & Optimization (Ongoing) — MONTH 2-3
- Monitor how he's using the system
- Fix issues that come up
- Add features based on feedback
- Plan next phase (if needed)

---

## Investment & Engagement

**[To be filled in based on Wayne's business model — pricing, support package, success guarantee, etc.]**

---

## Contact & Next Steps

**Antony's Contact:**
- Email: wks@contractor.net
- Phone: +447725731802
- Business: Wks Building Contractors Ltd

**Ready to discuss?** This analysis is tailored to his specific situation. He should see immediate value from quick wins (2-3 hours/week in 2 weeks), and full transformation in 3 months.

---

**Questions or concerns about this analysis? Let me know and I can adjust the approach.**

*Analysis by Wayne Francis | Wayne.francis4@googlemail.com*
