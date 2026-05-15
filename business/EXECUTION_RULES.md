# EXECUTION_RULES.md — Axis OS v3

## DCoS-first

Every task starts at DCoS. The user does not pick the agent.

## Mode classification

DCoS classifies every task before routing:

- **Fast** — short reply, single specialist, no review
- **Deep** — audit / workflow / system design / client deliverable. Mandatory QA or spec-review.

## Routing

DCoS picks the minimum agent set from `AGENT_RESOLUTION.md`.

- One specialist preferred. Chains only when the output quality requires it.
- Ambiguous request → DCoS asks one clarifying question, no guessing.

## Review enforcement

DCoS routes to QA when output is:
- client-facing
- external communication

DCoS routes to spec-review when output is:
- strategic
- structural (architecture, system, agent, workflow)

DCoS does not skip review. The specialist does the work; the reviewer signs it off; DCoS marks the tracker row `done` only after review passes.

## Tracking

Every routed task gets a row in `EXECUTION_TRACKER.md` at the moment of routing.

Status progression: `routed` → `in progress` → `awaiting review` → `done` (or `blocked` / `waiting`).

## Compliance gate

DCoS halts and flags if a request triggers any high-risk AI hard limit (recruitment screening, credit, medical, biometric, legal-effect decisions, education access).

GDPR triggers (SAR, erasure, data map, breach, GDPR status check) route to gdpr immediately.

## No bypass

DCoS-first cannot be skipped unless the user explicitly says so. If the user says "skip routing, just do X," DCoS still writes the bypass to the tracker so there's an audit trail.

## Review Trigger Phrases

Concrete signals that should fire the `qa` or `spec-review` route. These complement the broad rules in "Review enforcement" above by giving DCoS specific phrases to match.

**Route to `qa` when the output:**
- will be read by the client
- is part of the handover or playbook
- explains how to use the system
- contains instructions, recommendations, or guidance the client will act on

**Route to `spec-review` when:**
- onboarding or build feels overbuilt for the client's actual need
- the workflow is unclear or has too many branches
- the system map needs simplification
- the architectural decision affects multiple clients or future deployments

If the trigger is genuinely ambiguous, DCoS asks one clarification rather than running both reviews.

## Pricing Neutrality Rule

- Pricing is not defined during system build phases
- Do not write or store pricing in:
  `BRAND.md`, `OFFERS.md`, `CONTENT_THEMES.md`, `MEMORY.md`, `GDPR.md`
- Do not include pricing in workflows, SOPs, or playbooks
- If pricing appears, replace with:
  `[PRICING TO BE DEFINED]`
- Pricing will be defined in a separate post-build phase

**Audit discipline:** this rule applies to every agent and every harvest pass. Tracker rows for harvest tasks must record `Pricing scrub: <result>` so the audit trail is clear.

## Token discipline

- Load only the context files needed for the current task.
- Don't pre-fetch session summaries, dashboards, or calendars unless the task requires them.
- One workstream per session — DCoS flags workstream switches.
