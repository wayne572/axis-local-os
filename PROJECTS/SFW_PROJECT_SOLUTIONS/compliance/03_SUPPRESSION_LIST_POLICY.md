# Suppression List Policy
**Pipeline-as-a-Service - Wayne Francis / SF&W Project Solutions**
*v1.0 - 2026-04-30*

---

## Purpose

The Suppression List is the single source of truth for "do not contact" across **all** Pipeline-as-a-Service engagements. Once an individual is on the list, they are not contacted again by Wayne Francis / SF&W Project Solutions on behalf of any client.

## What gets a contact added

A contact is added within 1 working day if any of the following occur:

1. They click the unsubscribe link in any outreach email.
2. They reply asking to be removed (any wording - "stop", "unsubscribe", "remove me", "not interested" stated firmly).
3. They submit a Subject Access Request requesting erasure or objection.
4. They report the message as spam.
5. The Controller (client) instructs removal.
6. We receive an ICO complaint reference.
7. The contact's email or phone hard-bounces twice.

## What we store

For each suppressed contact, the minimum:
- Email address (lower-cased, hashed for cross-client lookup)
- Phone number if SMS-suppressed (hashed)
- Date added
- Reason code (1-7 above)

We do **not** store the original outreach content alongside the suppression record - only enough to confirm "do not contact".

## Where it lives

- Primary: encrypted Airtable base, access restricted to Wayne + named sub-processors.
- Backup: encrypted file in the approved SF&W Project Solutions suppression-list location (offline copy, not shared with clients).
- API check: every outreach engine queries the Suppression List before sending, by hashed email.

## Retention

Indefinite. The whole point of the list is to remember forever.

## Audit

Reviewed weekly to confirm:
- New entries logged in the last 7 days are correctly tagged.
- No duplicates.
- Cross-client lookup is functioning.

A monthly export count goes into the client's monthly performance report (no contact details - just totals).

## Client visibility

Clients see:
- The total number of suppressed contacts blocked from their campaign that month.
- Reason-code breakdown.

Clients do **not** see:
- The contact details of suppressed individuals.
- The Suppression List from other client engagements.

## Owner

Wayne Francis is accountable. No outreach goes live without confirming the engine has Suppression List read access.

---

*Reviewed annually or after any material change to the outreach stack.*
