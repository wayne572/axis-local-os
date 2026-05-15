# DEAL_SOURCING_OUTREACH.md

## 1. Status
Active - Logic File (Balanced)

---

## 2. Purpose
Define how outreach is executed in a structured, compliant, and effective way.

This ensures:

- conversations are started correctly
- compliance is maintained
- messaging is consistent
- prospects are respected

---

## 3. Core Principle

Start conversations, don't overwhelm.

---

## 4. System Rules

- keep messages short
- personalise lightly but meaningfully
- avoid pressure
- move toward conversation, not explanation

---

## 4A. Contact Route Lookup - FIRST STEP (NEW)

Before any message is drafted, Claude must locate the prospect's contact route.

The lookup order is fixed:

1. **Company website FIRST** - confirms the business is real, shows what they actually do, often lists the team and direct LinkedIn links.
2. **LinkedIn company page** - used to verify or when no website exists.
3. **Google `site:linkedin.com/in` search** - last-resort fallback for the named director.
4. **Verify the profile** matches (role, location, active in last 90 days).
5. **Log the contact route** in the tracker.
6. **If unconfirmed within 2 minutes** -> mark "LinkedIn unconfirmed" and move on. Do not draft outreach to an unconfirmed contact.

Why website-first:

- confirms the business is operating, not dormant
- shows their actual service offering (sharper personalisation)
- About / Team pages often link directly to LinkedIn
- skips LinkedIn search noise entirely when the website does the work

Claude must always provide direct deep links - Google search URL for the website, LinkedIn company URL, and the Google `site:linkedin.com/in` fallback - in that order, automatically.

When presenting any lead, Claude must always show:

- **Companies House registered name** (exact legal name)
- **SIC code(s)**
- **Director name**

This prevents confusion when multiple businesses share similar trading names. The Companies House identity is the source of truth.

---

## 5. Outreach Structure

Each message should include:

1. Observation (specific to them)
2. Relevant problem
3. Simple idea or angle
4. Soft invitation

---

## 6. Channel Rules (STRICT)

Allowed:

- LinkedIn (primary)
- Email (direct, personalised)
- Website contact forms (targeted use)

NOT allowed:

- WhatsApp cold outreach
- SMS cold outreach
- mass-blast email tools
- scraped personal contact lists

---

## 7. Compliance Rules (UK GDPR / PECR)

Every outreach must:

- clearly identify the sender
- include a simple opt-out line
- avoid misleading claims
- avoid special category data

B2C:

- requires explicit consent -> DO NOT contact

B2B:

- must have legitimate interest
- must be relevant to role/business

You must:

- record lawful basis in tracking
- respect opt-outs immediately
- avoid sensitive data use

---

## 8. Personalisation Rules

Personalisation must be:

- specific (real observation)
- relevant (linked to problem)
- honest (no guessing or fabrication)

Avoid:

- fake familiarity
- generic templates
- forced personalisation

---

## 9. Tone Rules

All outreach must be:

- calm
- professional
- clear

Avoid:

- hype
- urgency pressure
- "guaranteed results"
- aggressive sales language

---

## 10. Length Constraints

- LinkedIn: <100 words
- Email: <150 words

Shorter is better.

---

## 11. Follow-Up Rules

- wait 2-5 days between follow-ups
- maximum 2-3 follow-ups
- tone stays relaxed

Final close example:

"Will leave it here - happy to pick this up if it becomes relevant."

---

## 12. Response Handling

### Positive Reply
-> move to Sales OS

---

### Neutral Reply
-> ask ONE clarifying question

---

### Info-Only Reply

If asked:

"Send more info"

Do NOT send long explanations.

Instead:

- give short context
- ask ONE diagnostic question

Goal:
-> move conversation forward

---

### No Reply
-> follow-up -> then close

---

### Opt-Out
-> stop immediately
-> record in tracker

---

## 13. Edge Cases

### AML / High-Risk Signals
-> do NOT proceed
-> mark Compliance Hold

---

### High-Risk Verticals
-> apply stricter filtering
-> avoid borderline outreach

---

## 14. Example Outreach (Email)

Subject: Quick thought on lead flow

Hi [Name],

Noticed you're running [business type] - a lot of businesses in that space struggle with consistent leads.

There's usually a simple way to improve that without changing everything.

Would it be useful to share a quick idea?

- Wayne

(Just let me know if not relevant)

---

## 15. Failure Conditions

Outreach fails if:

- messages are too long
- compliance rules are ignored
- tone is pushy
- conversations stall in "info loops"
- personalisation is fake

---

## 16. End State

Outreach is working when:

- conversations start naturally
- responses are relevant
- compliance is maintained
- pipeline progresses cleanly

The goal is:

Conversation -> Qualification -> Next Step
