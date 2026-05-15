# Client Data & Compliance Acknowledgement

> **Use:** Lightweight client-facing acknowledgement step during Axis OS deployment. Owned by the `handover` agent. Issued before any client data is processed. Not a substitute for a Data Processing Agreement, DPIA, or formal contract — those are separate documents triggered by `business/HANDOVER/COMPLIANCE_PROTOCOL.md`.

---

## Quick note before we begin

As part of your AI system setup, we may:

- Process limited business data
- Structure workflows involving client or operational data
- Store basic system context to make your setup work effectively

---

## What this means (plain English)

- We use only the data needed to deliver your system
- We don't sell, share, or repurpose your data
- You stay in control of your data at all times
- Our lawful basis for processing is **legitimate interest** for B2B setup work, or **contract performance** once you're an active client. We confirm the basis with you before any new processing activity.

---

## When this matters

This step is relevant if your system:

- Handles customer or client information
- Automates communication (email, SMS, messaging)
- Stores or processes identifiable data

If none of the above apply, this step is minimal and can be passed quickly.

---

## Your rights

At any point you can:

- Request a copy of the data we hold for you (Subject Access Request)
- Ask us to correct or erase your data
- Withdraw consent for any optional processing
- Raise a concern with the ICO (ico.org.uk)

We respond to data requests within statutory timeframes per UK GDPR.

---

## Your confirmation

By continuing, you confirm that:

- You understand your system may involve basic data processing
- You're happy to proceed with setup on the lawful basis above
- You can request changes or deletion at any time

---

### Use & Responsibility

This system is designed to support your business operations, workflows, and decision-making.

Once deployed, you remain fully responsible for how the system is used within your organisation.

Axis AI provides structure and guidance, but does not assume responsibility for how the system is operated after deployment.

You are responsible for ensuring all usage complies with applicable laws, regulations, and internal policies.

---

## Action

Type:

**"Agree and continue"**

to proceed with your setup.

---

## Optional — extended setup

If your system involves any of the following, we'll complete a more detailed compliance step before processing begins:

- Special category data (health, ethnicity, religion, biometric, sexual orientation, political/trade union)
- Children's data
- Large-scale automated decision-making
- Cross-border transfers outside the UK/EEA
- MLR-regulated activity (accounting, legal, estate agency, lettings, tax advice, crypto, high-value dealing)

Most clients will not need this.

---

## Summary

This is not a legal barrier — it's a quick confirmation so we can build your system properly.

For the full handling rules, see `business/HANDOVER/COMPLIANCE_PROTOCOL.md` and `business/HANDOVER/GDPR_PROTOCOL.md`. Once accepted, the `gdpr` agent populates `business/GDPR.md` with the lawful basis and data map for your deployment.

---

## Internal — handover agent notes

When this template is issued to a client:

1. Replace nothing — issue verbatim or with branded wrapper only.
2. Wait for client to type **"Agree and continue"** (or signed equivalent).
3. If client triggers the "Optional — extended setup" path → halt deployment, run extended compliance step before any processing.
4. Never combine this with a marketing opt-in — keep PECR consent separate and explicit.

## Trigger — on "Agree and continue"

When the client confirms, the `handover` agent (or `gdpr` agent if invoked directly) must:

### Step 1 — Append to `TRACKER/GDPR_LOG.md`

One row, append-only:

```
| YYYY-MM-DD | data_ack | <Client name> | <Owner name or n/a> | onboarding | "Agree and continue" via <channel> | <reference path or msg id> |
```

Required fields:
- **Date** — UTC date the confirmation was received
- **Event type** — `data_ack`
- **Client** — registered business name
- **Subject** — name of the person who confirmed (the business owner or designated rep)
- **Stage** — `onboarding` (first acknowledgement) or `handover` (Day-7 reconfirm) or `live` (renewal)
- **Confirmation / Detail** — exact phrase + channel (chat / email / signed PDF)
- **Reference** — path to supporting artefact (email thread, screenshot, signed file) or `pending`

### Step 2 — Update `business/GDPR.md` (only if needed)

Update GDPR.md only when the acknowledgement provides new information. Do not touch sections that are unchanged.

Update if:
- **Section 1 (Lawful basis):** if not yet declared → set primary basis (`Legitimate interest` for B2B setup; `Contract` once active client) and `Date declared`
- **Section 2 (Special category data):** only if the client triggered the extended setup path
- **Section 3 (ICO registration):** if the client supplied ICO ref during the ack, record it
- **Section 8 (DPO / privacy point of contact):** record the confirming person if not already present
- **Section 9 (Last review):** set `Date` to today, `Next review due` to today + 6 months

If GDPR.md is still in `[DRAFT — to be populated at handover]` state and the ack is the first GDPR event, mark Status as `Active — onboarding ack received` instead.

### Step 3 — Tracker row via DCoS

DCoS appends a single row to `business/EXECUTION_TRACKER.md`:

```
| YYYY-MM-DD | <Client> data ack received | Fast | gdpr | Wayne | done | TRACKER/GDPR_LOG.md |
```

### Step 4 — Halt conditions

Do not log and do not proceed if any of these apply:
- Confirmation came from someone other than the registered business owner / designated rep
- Client declined or asked questions instead of confirming
- Client triggered the extended setup path (special category, children's data, automated decisions, cross-border transfer, MLR-regulated activity) — halt and run extended compliance step first
- Marketing consent was bundled into the same reply — halt and request a separate PECR opt-in
