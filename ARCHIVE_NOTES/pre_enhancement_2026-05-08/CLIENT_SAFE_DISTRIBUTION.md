# CLIENT-SAFE DISTRIBUTION

## STATUS
Spec — pending build approval

---

## PURPOSE

Defines a client-safe distribution of Axis OS that can be shared with a client without exposing the core system, agent prompts, validation logic, or orchestration internals.

Operationalises:

- LICENSE.md (legal scope)
- DISTRIBUTION_POLICY.md Tiers 1 + 2 (operational scope)

---

## CORE PRINCIPLE

The client-safe distribution is **generated from v3, never edited in place**.

When v3 changes, regenerate the distribution. Do not patch the distribution directly.

---

## TARGET LOCATION

Source: `D:\Wayne AI OS\Axis OS_v3\`
Generated distribution: `D:\Wayne AI OS\Axis OS_v3_CLIENT_SAFE\`

The client-safe folder is a **build artefact**, not part of the active system. Treated as output.

---

## INCLUDED FILES (whitelist)

The client-safe distribution contains only:

### Top-level
- `LICENSE.md`
- `DISTRIBUTION_POLICY.md` (Tier 1 + Tier 2 sections only; Tier 3 redacted)
- `START_HERE.md` (client-facing version — see Generation Rules below)
- `README.md`

### `business/`
- `BRAND.md` (per-client copy)
- `OFFERS.md` (per-client copy)
- `CONTENT_THEMES.md` (per-client copy)
- `MEMORY.md` (per-client copy)
- `GDPR.md` (per-client copy)
- `PIPELINE.md` (template only — no Wayne-specific entries)
- `ACTIVE_CLIENTS.md` — **excluded** (Wayne-side operational store)

### `business/HANDOVER/`
- `PLAYBOOK_TEMPLATE.md`
- `CLIENT_DATA_ACK.md`
- `INTAKE_TEMPLATE.md`
- `DELIVERY_CHECKLIST.md`
- `POST_LOCK_SUPPORT.md`
- `CLIENT_HANDOVER.md`
- `COMPLIANCE_PROTOCOL.md`
- `GDPR_PROTOCOL.md`
- `RISKS_AND_NOTES.md` (template, blank)
- `STACK_CATALOGUE.md` (Tier 2 only — pending pricing-phase rewrite; may be excluded until cleaned)

### `CLIENTS/<slug>/`
- The specific client's folder, intact (their own context).

---

## EXCLUDED FILES (blacklist — never distributed)

### Top-level
- `CLAUDE.md` (system constitution)
- `CHANGELOG.md` (full audit trail — internal)
- `SYSTEM_INSTANCE_TRACKING.md` (governance — internal)
- `CLIENT_SAFE_DISTRIBUTION.md` (this spec — internal)

### `.claude/agents/` — entire folder excluded
- `dcos.md`, `gdpr.md`, `onboarding.md`, `handover.md`, `deal-sourcing.md`, `intake-capture.md`, `audit.md`, `builder.md`, `context.md`, `design.md`, `linkedin.md`, `outreach.md`, `pipeline.md`, `qa.md`, `session-summary.md`, `social.md`, `workflow.md`

### `business/`
- `EXECUTION_TRACKER.md` (Wayne-side audit trail)
- `EXECUTION_RULES.md` (system rules — internal)
- `AGENT_RESOLUTION.md` (routing table — internal)
- `SYSTEM_REVIEW.md` (Wayne-side review)
- `DEAL_LOG.md` (revenue layer — internal)
- `WORKFLOW_LIBRARY.md` (canonical pattern source — internal)
- `CLIENT_ACQUISITION_SYSTEM.md` (Optional OS spec — internal)
- `OFFER_CONVERSION_FLOW.md` (Optional OS spec — internal)
- `ACTIVE_CLIENTS.md` (cross-client view — internal)

### `business/HANDOVER/`
- `SETUP_SCRIPTS.md` (operator-side)
- `TEST_HARNESS.md` (operator-side)

### `TRACKER/` — entire folder excluded
- `GDPR_LOG.md`, `INSTANCE_LOG.md`, `ACQUISITION_LOG.md`, `DELIVERY_LOG.md`, etc. — all logs are operator-side.

### `docs/` — entire folder excluded
- `POST_CREATION_VALIDATION.md` (validator prompt — internal)
- `POST_CREATION_VALIDATION_GATE.md` (gate spec — internal)
- `dcos/`, `deal-sourcing/`, `ecosystem/` — internal architecture

### `INPUTS/` — entire folder excluded

### `V3 Axis/` — internal audit framework
- excluded

### `Axis OS_v2/`, `Axis OS_v2.1/` — locked legacy, never distributed

### Per-client `INSTANCE_LOG` row, fingerprint references — never distributed

---

## GENERATION RULES

1. **Read-only of source.** The generation process never mutates `Axis OS_v3/`. It only reads + copies + redacts.
2. **Whitelist enforcement.** Anything not on the included list is excluded by default. New v3 files require an explicit decision before they appear in distributions.
3. **Per-client scoping.** Distributions are typically per-client; only that client's `CLIENTS/<slug>/` is included, not other clients' folders.
4. **`START_HERE.md` redaction.** The client-facing `START_HERE.md` excludes DCoS commands beyond `Status` (the four operator commands are operator-side); replaces internal references with client-friendly language.
5. **`DISTRIBUTION_POLICY.md` redaction.** Strip Tier 3 and Non-Distributable Components sections; client only sees their own tier.
6. **Pricing scrub.** Run the canonical pricing scan before any distribution build. Any token match halts the build until resolved (consistent with EXECUTION_RULES.md → Pricing Neutrality Rule).
7. **Validation Gate.** Each generated file passes the Post-Creation Validation Gate before inclusion.
8. **Instance registration.** Distribution builds register a new row in `TRACKER/INSTANCE_LOG.md` with the client_slug + tier + fingerprint hash of the included artefact set.
9. **Fingerprint embed.** Each generated `PLAYBOOK_TEMPLATE.md` carries an invisible per-instance fingerprint (e.g., a hash comment in the footer) to support leak detection.

---

## DELIVERY METHOD

Per `DISTRIBUTION_POLICY.md`:

- **Not** a zip dump.
- **Not** an unrestricted repository.
- Delivered via guided setup: staged file release, controlled onboarding, owner walks the client through what they have.

---

## UPDATE FLOW

When v3 is patched:

1. Patch `Axis OS_v3/` per the standard change-control rules.
2. Regenerate the client-safe distribution by re-running the generation rules.
3. Diff the new distribution against the prior one.
4. Notify the client only if a relevant Tier 1/2 file changed (e.g., a compliance protocol update).
5. Append a row to the client's `INSTANCE_LOG.md` entry referencing the new fingerprint.

---

## NEVER-INCLUDE RULE

Even with a Tier 3 (Full Restricted) recipient, the following are NEVER included in distributable form:

- DCoS source agent prompt (`dcos.md`)
- Post-Creation Validation prompt (`POST_CREATION_VALIDATION.md`)
- Internal orchestration prompts
- System enforcement logic

These are accessible only to the system owner. Tier 3 access means full *operational* visibility, not source-code access.

---

## FAILURE CONDITIONS

DCoS halts a distribution build if:

- A blacklisted file would be included
- A pricing token is detected in any included file
- The Validation Gate fails on any generated artefact
- `INSTANCE_LOG.md` is missing or the new instance row cannot be appended
- The fingerprint embed step fails or is missing

---

## END
