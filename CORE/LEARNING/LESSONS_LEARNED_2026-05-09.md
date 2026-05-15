# Lessons Learned — 2026-05-09

**Context:** Website, product packaging, client builds, platform readiness, and Axis AI market positioning.

**Owner:** Wayne Francis  
**Trading under:** SF&W Project Solutions  
**Product system:** Axis AI

---

## 1. Platform Must Be Confirmed Before Every Client Build

**Lesson:** We nearly created the wrong platform version for Joseph by treating a Codex build as acceptable when the client needed Claude.

**System rule to preserve:** Before creating any client OS build, ask:

> Which platform will this build be used on first: Claude, ChatGPT, Codex, or another agreed platform?

**Operational impact:** Prevents rework, broken handover, and client confusion.

**Status:** Preserve as a mandatory build-control rule.

---

## 2. Wayne Francis Is The Brand; Axis AI Is The Product

**Lesson:** The market-facing structure is clearer when Wayne Francis leads the site, with SF&W Project Solutions as the trading entity and Axis AI as the product system.

**Correct wording:**

> Wayne Francis · Trading under SF&W Project Solutions · Creator of Axis AI

**Avoid:**

- Founder, Axis AI
- Treating Axis AI as the whole company
- Hiding Wayne behind the product too early

**Operational impact:** Better trust, clearer personal positioning, stronger partner/client explanation.

**Status:** Preserve in all website, proposal, documentation, and client-facing material.

---

## 3. The Website Needs A Funnel, Not A Single Product Page

**Lesson:** A polished Solo OS page is useful, but it creates confusion if the homepage and offer structure are weaker.

**Improved site structure:**

1. Homepage — Wayne Francis positioning and high-level offer routes
2. Axis AI overview — explains both core builds
3. Solo Operator OS page — detailed page for individuals
4. Client OS Build page — detailed page for SMEs and teams
5. Readiness Review — first conversion point

**Operational impact:** Visitors understand who Wayne is, what Axis AI is, and which offer fits them.

**Status:** Enhance website documentation and sales pathway.

---

## 4. Both Builds Need To Be Explained Together

**Lesson:** Selling only the Solo Operator OS makes the offer feel smaller than the actual product ecosystem.

**Core builds to present:**

- **Solo Operator OS** — personal AI operating system for one-person operators.
- **Client OS Build** — business AI operating system for SMEs and small teams.

**Supporting route:**

- **AI Readiness Review** — confirms fit before any paid build.

**Operational impact:** Makes the product architecture easier to understand and sell.

**Status:** Preserve in website, sales docs, and partner materials.

---

## 5. Pricing Needs A Single Source Of Truth

**Lesson:** Pricing conflicts appeared across older files and website copy. The HTML page had the right pricing, but older OS files still surfaced outdated figures.

**Pricing authority:** `business/PRICING_AUTHORITY.md`

**Locked pricing to preserve:**

- Solo Operator OS: Starter £1,495, Standard £2,495, Premium £3,995
- SME AI Automation Audit: Lite £2,500, Core £4,500, Deep Dive £6,500
- Client OS Build: Foundation £6,500, Growth £9,500, Enterprise £12,500
- Launch/Scale/Transform bundles: £9,995 / £12,995 / £15,995
- OS Care Plan: £750 / £995 / £1,495 per month

**Operational impact:** Any pricing output must check the pricing authority before being sent externally.

**Status:** Preserve as a review-control rule.

---

## 6. Client Documentation Must Be Professional, Not Just Complete

**Lesson:** PDFs and manuals cannot just contain the right words. They must look professional enough to hand to a paying client without apology.

**Quality standard:**

- Titles must sit correctly inside designed areas.
- Page hierarchy must be clear.
- Branded colours must be consistent.
- Images must be chosen deliberately.
- No broken formatting, awkward spacing, or placeholder content.

**Operational impact:** Add visual QA before any shipped documentation pack.

**Status:** Preserve in file output and delivery rules.

---

## 7. Do Not Use Fixed PDF Page Counts In Marketing

**Lesson:** Fixed page-count claims create avoidable accuracy risk because documentation packs may vary by client and build.

**Preferred wording:**

> Branded client documentation pack

**Avoid:**

> 26-page documentation pack

**Operational impact:** Safer marketing and fewer inconsistencies when documents change.

**Status:** Preserve in website, proposal, and sales copy.

---

## 8. The Product Should Be Described As More Than An AI Assistant

**Lesson:** “AI assistant” undersells the value. The stronger framing is “AI operating system” because the product includes structure, memory, workflows, review, commands, documentation, and handover.

**Better positioning:**

> Axis AI is not another chatbot. It is a practical operating layer built around how you work, what you are building, and what must not get dropped.

**Operational impact:** Use “operating system” and “operating layer” language in sales pages, guides, and proposals.

**Status:** Preserve as positioning rule.

---

## 9. Boardy-Type Communication Is A Product Requirement

**Lesson:** Relationship-aware, proactive communication is not optional. Wayne wants the system to help track people, promises, context, replies, and next steps.

**Required capability:**

- Relationship memory
- Follow-up tracking
- Context summaries
- Suggested outreach
- Conversation history awareness where legally and technically available

**Operational impact:** Relationship Connector logic should appear in Solo OS and Client OS builds, with data handling controls.

**Status:** Preserve as must-have capability.

---

## 10. Compliance Needs To Be A Workflow Control, Not A Footnote

**Lesson:** GDPR, usage tracking, client consent, IR35/off-payroll risk, and platform/data handling must appear as active checks in the OS.

**Controls to preserve:**

- Usage tracking notice before client handover
- GDPR-aware data handling wording
- IR35/off-payroll risk flag for relevant client work
- Platform confirmation before build
- No invented claims, fake testimonials, or unsupported guarantees

**Operational impact:** Add compliance checks into review and handover stages.

**Status:** Preserve and enhance.

---

## 11. Website Design Needs Offer Logic And Visual Quality Together

**Lesson:** A page can have good copy and still feel weak if the design hierarchy, image crop, spacing, and CTA flow are poor.

**Quality checks used today:**

- Hero image not over-cropped
- Price/platform details displayed as intentional UI elements
- Page has a route, not just blocks of information
- No placeholder testimonials
- Clear distinction between homepage, product overview, and product detail page

**Operational impact:** Web outputs require both content review and visual review.

**Status:** Add to developer/design rules.

---

## 12. The Readiness Review Is The Best First Conversion Point

**Lesson:** The safest commercial pathway is not “buy now”; it is “start with a readiness review.” This reduces pressure, qualifies the lead, and confirms the right build.

**Recommended funnel:**

Homepage → Axis AI page → Readiness Review → Discovery call → Proposal → Build

**Operational impact:** Website CTAs should prioritise the Readiness Review unless the page is a direct product page.

**Status:** Preserve as sales funnel rule.

---

## 13. Archive Non-Shipped Builds To Reduce Confusion

**Lesson:** Too many versions make the system hard to trust. The latest sellable builds should be easy to find, and everything else should be clearly filed as not in use.

**Current principle:**

- Latest sellable builds live in one named folder.
- Shipped client builds live separately.
- Old builds are archived as not in use.

**Operational impact:** Maintain build hygiene after every client packaging session.

**Status:** Preserve as delivery-control rule.

---

## 14. What To Improve Next

Recommended next system enhancements:

1. Create a dedicated Client OS Build landing page.
2. Create a Squarespace merge guide for the new homepage and Axis AI overview page.
3. Add a website QA checklist to `DEVELOPER.md`.
4. Add platform confirmation to the client build startup workflow.
5. Add a “pricing authority check” to all sales and proposal workflows.
6. Add a “no placeholder content” rule to final document and website review.
7. Build a simple client handover checklist covering platform, docs, consent, usage tracking, and review date.

---

## Summary

Today confirmed that Axis AI is strongest when presented as a product ecosystem:

- Wayne Francis is the human brand.
- SF&W Project Solutions is the trading entity.
- Axis AI is the operating system product.
- Solo Operator OS and Client OS Build are the two core commercial builds.
- The Readiness Review is the first conversion step.

The key improvement is discipline: one source of truth, one clean build structure, platform confirmed before build, and professional QA before anything goes to a client.

