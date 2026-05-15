# SYSTEM DISTRIBUTION POLICY

## STATUS
Active

---

## PURPOSE

This document defines how Axis OS may be distributed, shared, and deployed.

It protects the integrity of the system and prevents unauthorised replication.

---

## CORE PRINCIPLE

Axis OS is not distributed as a complete system.

It is delivered as a controlled, guided implementation.

---

## DISTRIBUTION TIERS

### TIER 1 — VIEW ACCESS

User receives:

- high-level documents
- read-only materials

User does NOT receive:

- prompts
- agent logic
- system orchestration

---

### TIER 2 — OPERATOR ACCESS

User receives:

- selected working files (e.g. intake, checklist)
- limited workflow visibility

User does NOT receive:

- DCoS logic
- validation prompts
- internal system rules

---

### TIER 3 — FULL SYSTEM (RESTRICTED)

Access granted only if:

- explicitly approved
- controlled by the system owner

Includes:

- full file structure
- all system logic

Restrictions still apply under LICENSE.md.

---

## NON-DISTRIBUTABLE COMPONENTS

The following must NEVER be shared externally:

- DCoS (Digital Chief of Staff)
- POST_CREATION_VALIDATION_PROMPT.md
- internal orchestration prompts
- system enforcement logic

---

## DELIVERY METHOD

Axis OS must NOT be distributed as:

- full file dumps
- zip archives
- unrestricted repositories

Axis OS must be delivered via:

- guided setup
- staged file release
- controlled onboarding

---

## CLIENT INSTANCES

Each client must have:

CLIENTS/<slug>/

No shared environments.

---

## TRACEABILITY

Each deployment should include:

- client identifier
- instance reference

This ensures traceability if system leakage occurs.

---

## CHANGE CONTROL

Users may not:

- alter core system files
- redefine system logic

All structural changes must:

- be approved
- follow version control

---

## VIOLATION RESPONSE

If unauthorised use or distribution is detected:

- access is revoked
- system usage is terminated

---

## END
