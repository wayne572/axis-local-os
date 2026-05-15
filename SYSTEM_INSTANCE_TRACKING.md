# SYSTEM INSTANCE TRACKING

## STATUS
Active

---

## PURPOSE

Assigns a unique `instance_id` to every Axis OS deployment.

Provides:

- traceability across deployments
- leak detection if system content surfaces outside an authorised instance
- enforcement support for the LICENSE and DISTRIBUTION_POLICY

---

## CORE PRINCIPLE

No client deployment proceeds without an instance registration.

Every `CLIENTS/<slug>/` creation must be preceded by an instance row.

---

## INSTANCE RECORD SCHEMA

Each instance is recorded as one append-only row in:

`TRACKER/INSTANCE_LOG.md`

| Field | Description |
|---|---|
| `instance_id` | UUID v4. Unique. Never reused. |
| `client_slug` | The per-client slug (lowercase, hyphenated, ASCII). |
| `client_display_name` | Human-readable client name. |
| `created_date` | UTC date of registration (YYYY-MM-DD). |
| `tier` | LICENSE/DISTRIBUTION tier — `view` / `operator` / `full-restricted`. |
| `device` | Device or environment where the instance was created (e.g. `Windows Desktop`). |
| `responsible_operator` | The Axis-side operator who registered the instance (typically Wayne). |
| `fingerprint_ref` | Optional path to a fingerprint artefact (hash of artefact subset) used for leak comparison. `pending` until first artefact is generated. |
| `status` | `active` / `archived` / `revoked`. |
| `notes` | One-line free text. |

---

## REGISTRATION FLOW

1. Operator triggers a new client deployment.
2. DCoS halts at `CLIENTS/<slug>/` creation step until an instance is registered.
3. Operator generates a UUID v4 and appends a row to `TRACKER/INSTANCE_LOG.md`.
4. DCoS verifies the row exists and the `client_slug` matches.
5. DCoS proceeds with `CLIENTS/<slug>/` creation, onboarding, and downstream flow.

---

## DCoS ENFORCEMENT

DCoS must:

- Halt any deployment that lacks an instance row.
- Halt if `instance_id` is duplicated (UUID collision — vanishingly unlikely but enforced).
- Halt if `client_slug` does not match the registered slug.
- Refuse to proceed with onboarding, handover, or post-lock support until an instance is active.

DCoS does not register instances itself. Registration is a deliberate operator action.

---

## LEAK DETECTION

If content from Axis OS surfaces outside an authorised instance:

1. Compare the surfaced artefact against `fingerprint_ref` entries in `INSTANCE_LOG.md`.
2. If the fingerprint matches a known instance → suspected source identified; trigger LICENSE enforcement (access termination / usage revocation).
3. If no fingerprint matches → the leak is from an unregistered or pre-tracking source; flag for investigation.

Fingerprints should be hashes (SHA-256) of stable artefact subsets — typically a per-client subset that includes the slug, the playbook header, and a non-trivial random nonce embedded at registration time.

---

## INSTANCE_LOG.md PATH

Canonical path: `TRACKER/INSTANCE_LOG.md`

This file does **not** exist yet. Per the never-auto-create rule, the first instance registration must be authorised by Wayne, who creates the file with the schema header before the first row is appended.

Until the file exists, any `CLIENTS/<slug>/` creation halts and routes to Wayne for setup.

---

## STATUS RULES

- `active` — current deployment, in use
- `archived` — deployment locked (post-handover) but instance retained for traceability
- `revoked` — license violation, leak, or other enforcement event; access terminated

Status transitions are append-only — never mutate an existing row. To change status, append a new row referencing the same `instance_id` with the new status, or maintain a separate state table.

---

## SYSTEM RULES

- No pricing tracked.
- No revenue tracked.
- No personally identifiable data beyond what's already in the client name / slug.
- No tracking of client business performance.

Instance tracking is for **deployment integrity**, not for analytics.

---

## INTEGRATION POINTS

- LICENSE.md — instance tier maps to license tier.
- DISTRIBUTION_POLICY.md — instance tier maps to distribution tier.
- ACTIVE_CLIENTS.md — `instance_id` may be referenced in the live deployment row.
- DCoS — enforces registration gate.
- Validation Gate — does not run on `INSTANCE_LOG.md` appends (logging is exempt).

---

## FAILURE CONDITIONS

DCoS halts and flags if:

- `INSTANCE_LOG.md` is missing
- A `CLIENTS/<slug>/` creation is requested without a registered instance
- Duplicate `instance_id` detected
- `client_slug` mismatch between instance row and folder
- Fingerprint mismatch on leak-detection comparison

---

## END
