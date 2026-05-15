# GDPR_LOG.md

Append-only log of every GDPR-relevant event in the system. Owned by the `gdpr` agent. DCoS routes; gdpr writes.

**Canonical path:** `Axis OS_v3/TRACKER/GDPR_LOG.md` (relocated from `Axis OS_v3/business/GDPR_LOG.md` 2026-05-03).

## Event types

- `data_ack` — client confirmed Data & Compliance Acknowledgement
- `sar` — Subject Access Request raised / fulfilled
- `erasure` — Right to Erasure request raised / fulfilled
- `rectification` — data correction performed
- `portability` — data export issued
- `objection` — data subject added to suppression list
- `breach` — breach detected, contained, reported
- `dpa_signed` — Data Processing Agreement signed for a connected tool
- `review` — 6-monthly GDPR.md review completed
- `escalation` — compliance trigger fired; halt logged

## Format

| Date | Event type | Client | Subject | Stage | Confirmation / Detail | Reference |
|---|---|---|---|---|---|---|

## Rules

1. Append-only. Never edit, never delete.
2. One row per event. No batching.
3. `Subject` = the data subject's name or email when relevant; `n/a` when not (e.g., DPA signing).
4. `Stage` = `onboarding` / `handover` / `live` / `offboarding`.
5. `Confirmation / Detail` = the exact phrase or short description (e.g., `"Agree and continue" via email 2026-05-03`).
6. `Reference` = file path to supporting artefact (signed doc, email thread ID, etc.) or `pending`.
7. SAR / breach events must include statutory deadline tracking — see `business/HANDOVER/GDPR_PROTOCOL.md`.

---

## Events

| Date | Event type | Client | Subject | Stage | Confirmation / Detail | Reference |
|---|---|---|---|---|---|---|
| 2026-05-03 | data_ack | __TEST__ | Jane Doe | onboarding | "Agree and continue" via email | thread-12345 |
| 2026-05-03 | data_ack | greenfield_ops | [TEST owner] | onboarding | Client confirmed: Axis AI provides structure only; client owns data responsibility; no compliance guarantees. Test simulation. | `CLIENTS/greenfield_ops/ONBOARDING.md` |
| 2026-05-03 | escalation | __TEST_HEALTH__ | Jane Doe | onboarding | Halted — patient health records (special category, Art. 9) — extended setup required before data_ack | thread-health-001 |
| 2026-05-03 | escalation | unknown-clinic | unknown | onboarding | Halted at intake-capture — patient health records ~200/week (special category, UK GDPR Art. 9). Extended compliance setup required before any further intake. | conversation 2026-05-03 |
