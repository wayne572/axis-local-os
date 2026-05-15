# CLIENT_ACQUISITION_SYSTEM

## STATUS
Optional OS — Inactive by default

Activation:
- Controlled via Onboarding Block G
- Must be explicitly enabled per client

If not activated:
- DCoS blocks all acquisition routing
- System remains dormant

---

## PURPOSE

The Client Acquisition System defines how potential clients are:

- Identified
- Approached
- Captured
- Routed into the Axis onboarding pipeline

This system operates strictly as a **top-of-funnel layer**.

It does NOT:
- Sell
- Convert
- Price
- Close

---

## SYSTEM FLOW

Channel → Message → Capture → Qualification → Routing → Intake

---

## BLOCK A — CHANNEL DEFINITION

Channels must be explicitly declared during onboarding.

No default channels exist.

Allowed channel types (non-exhaustive):

- Network-led (referrals, partnerships)
- Outbound (direct outreach)
- Inbound (content, organic discovery)
- Platform-based (directories, marketplaces)

Each channel must define:

- source type
- interaction method
- expected lead format

---

## BLOCK B — MESSAGE LAYER

Defines how prospects are engaged.

Constraints:

- No pricing references
- No offer structures
- No guarantees requiring compliance validation

Allowed structure:

- Problem articulation
- Audience relevance
- Outcome framing (non-quantified)

This is a **pre-offer communication layer only**.

---

## BLOCK C — LEAD CAPTURE

All leads must enter the system through one of the following:

- Direct conversation → routed to intake-capture
- Form submission → mapped to INTAKE_TEMPLATE.md
- Call booking → triggers intake conversation
- Manual entry → logged and routed

Hard rule:

- ALL leads must pass through intake-capture
- No direct onboarding entry allowed

---

## BLOCK D — QUALIFICATION (LIGHT FILTER)

Purpose:
Prevent misaligned leads entering onboarding.

Allowed signals:

- Problem clarity
- Engagement readiness
- Fit with client profile

Constraints:

- No pricing qualification
- No automated rejection systems
- No scoring models tied to revenue

Outcome options:

- Proceed to intake
- Discard (manual)
- Defer

---

## BLOCK E — ROUTING LOGIC

All captured leads must be routed as follows:

Default:
→ intake-capture

Alternative:
→ discard
→ defer

Blocked routes:

- Direct to onboarding
- Direct to sales systems
- Direct to delivery

---

## BLOCK F — TRACKING (ACQUISITION_LOG)

Append-only logging required.

Log file:
TRACKER/ACQUISITION_LOG.md

Each entry must include:

- timestamp
- channel
- source
- lead_type (inbound / outbound / referral)
- action (captured / routed / discarded / deferred)
- destination (intake / discard / defer)
- client_slug (if created)

Strict exclusions:

- pricing
- revenue
- deal value
- conversion metrics

---

## BLOCK G — ACTIVATION CONTROL

This system is OFF by default.

Activation rules:

- Enabled only via Onboarding Block G
- Must be explicitly selected per client
- Cannot auto-activate

DCoS responsibilities:

- Prevent routing if inactive
- Enforce system boundaries
- Confirm activation before execution

---

## BLOCK H — SYSTEM BOUNDARIES

This system is strictly separated from:

- Sales OS (conversion logic)
- Offer Conversion Flow (offer design + pricing)
- Delivery systems

Relationship:

Acquisition → Intake → Onboarding → (Optional Systems)

No backward routing allowed.

---

## COMPLIANCE + LIABILITY

- Messaging must remain non-committal and non-contractual
- No claims requiring regulatory validation
- No representation of outcomes as guaranteed

Axis AI provides structure only.

Client is fully responsible for:
- outreach actions
- communication content
- regulatory compliance

---

## FAILURE CONTROLS

DCoS must intervene if:

- Pricing language appears
- Leads bypass intake-capture
- System activates without onboarding approval
- Routing skips defined flow

---

## INTEGRATION POINTS

Feeds into:
- intake-capture agent

Uses:
- INTAKE_TEMPLATE.md (indirect mapping)

Creates:
- CLIENTS/<slug>/ (only after intake completion)

Logs to:
- TRACKER/ACQUISITION_LOG.md

---

## END STATE

A lead is considered successfully acquired when:

- It has passed through intake-capture
- A CLIENTS/<slug>/ directory is created
- It transitions into onboarding
