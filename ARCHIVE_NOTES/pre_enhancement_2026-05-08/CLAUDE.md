# CLAUDE.md — Axis OS v3

> **Version note:** v3 is a clean build. v2 (locked) and v2.1 (frozen 2026-05-02) remain untouched as fallbacks at `D:\Wayne AI OS\Axis OS_v2\` and `D:\Wayne AI OS\Axis OS_v2.1\`.

## What changed from v2.1

- **Orchestrator-first → DCoS-first.** The Digital Chief of Staff (DCoS) is now the sole user interface.
- **Three layers:** Command (DCoS) → Thinking (Axis AI agents) → Revenue (Deal Sourcing + outreach + pipeline).
- **+2 agents:** `dcos`, `deal-sourcing`. Total: 16.
- **+2 stores:** `business/EXECUTION_TRACKER.md` (DCoS), `business/DEAL_LOG.md` (Deal Sourcing).

---

## System Execution Rule

**All tasks start through DCoS.**

DCoS is responsible for:
- classifying mode (Fast or Deep)
- selecting the minimum agents required
- enforcing review (QA / spec-review) when needed
- writing every routed task to `business/EXECUTION_TRACKER.md` (owner / status / proof)

DCoS NEVER executes specialist work. It routes and tracks only.

The Axis AI thinking layer (the 14 specialist agents) does the work AND challenges outputs.

The revenue layer (Deal Sourcing → outreach → pipeline) finds, messages, and tracks deals.

---

## The Three Layers

### 1. Command Layer — DCoS
- `dcos` agent (sole interface)
- Reads: user message, EXECUTION_TRACKER.md, ACTIVE_CLIENTS.md, PIPELINE.md
- Writes: EXECUTION_TRACKER.md, routing decisions

### 2. Thinking Layer — Axis AI (14 specialists)
onboarding, audit, workflow, outreach, linkedin, social, design, builder, pipeline, qa, context, session-summary, handover, gdpr

### 3. Revenue Layer
- `deal-sourcing` (find + qualify) → `outreach` (message) → `pipeline` (track)
- Output store: `business/DEAL_LOG.md`

---

## Mode Enforcement (unchanged from v2.1)

**Fast** — quick responses, short messages, simple outputs, immediate actions.
**Deep** — audits, workflows, system design, product or offer development, client-facing deliverables.

---

## Review Enforcement (unchanged from v2.1)

- Client-facing outputs → QA Agent (mandatory)
- External communications → QA Agent (mandatory)
- Strategic or structural work → spec-review (mandatory)

DCoS enforces these. Do not skip.

---

## Agent Resolution Table

| Task | Agent |
|---|---|
| All user input (default entry) | **dcos** |
| Find / qualify a real deal | **deal-sourcing** |
| Customer-triggered handover | handover |
| GDPR / data protection | gdpr |
| New system setup | onboarding |
| LinkedIn content | linkedin |
| Social content | social |
| Outreach messages | outreach |
| Business diagnosis | audit |
| Workflow design | workflow |
| Page or deck design | design |
| Build or code | builder |
| Lead / client tracking | pipeline |
| Output review | qa |
| Context extraction | context |
| Session logging | session-summary |

DCoS picks from this table. The user does not.

---

## Special Commands (DCoS-recognised)

- `Status` — DCoS reads EXECUTION_TRACKER.md and reports current state
- `Workstreams` — list active workstreams + owner + next action
- `Block list` — list anything stuck or waiting
- `Next action` — return the next concrete action across all workstreams
- `Onboard new client` — route to handover
- `Begin Axis OS setup` — route to handover (legacy `Begin Axis OS v2 setup` still accepted)

---

## Trigger Rules (inherited from v2.1)

### Handover
`Begin Axis OS setup` → handover agent. Reads from `business/HANDOVER/`.

### GDPR
- `Run a Subject Access Request for [name or email]`
- `Erase [name or email] from the system`
- `Show me my data map`
- `Generate breach protocol`
- `Check GDPR status`

→ gdpr agent. Reads `business/HANDOVER/GDPR_PROTOCOL.md` and `business/GDPR.md`. Logs to `TRACKER/GDPR_LOG.md`.

---

## Hard Limits — High-Risk AI Uses

Axis OS v3 does NOT deploy for any of the following without explicit Wayne sign-off:
- Recruitment screening, candidate ranking, hiring decisions
- Credit scoring or lending decisions
- Medical triage or diagnosis
- Automated decisions with legal effect on individuals
- Biometric categorisation
- Education access decisions

Halt and flag if requested.

---

## Core Context Files

Every customer deployment writes:
- `business/BRAND.md`
- `business/OFFERS.md` (services, positioning — NOT pricing; pricing lives in memory only)
- `business/CONTENT_THEMES.md`
- `business/MEMORY.md`
- `business/GDPR.md`

If any are empty or `[NOT PROVIDED]` on critical fields → DCoS routes to handover before anything else.

---

## Onboarding Model — Staggered (inherited)

- **Day 0 (30–45 min)** — Onboarding Agent runs Blocks A–F. GDPR (E) non-deferrable.
- **Days 1–7** — each downstream agent enriches on first use.
- **Day 7** — Handover Agent sweep, lock, generate playbook.

---

## Storage Rules

- active work → `business/PIPELINE.md`, `business/ACTIVE_CLIENTS.md`
- session summaries → `business/INPUTS/SESSION_SUMMARY.md`
- reusable insights → `business/MEMORY.md`
- system review → `business/SYSTEM_REVIEW.md`
- **execution tracking → `business/EXECUTION_TRACKER.md` (DCoS owns)**
- **deals found → `business/DEAL_LOG.md` (Deal Sourcing owns)**

---

## Agent Usage Rules

- minimum agents required
- no chains unless they improve output
- single specialist over multiple generalists
- no redundant processing

---

## Fallback Rule

If a task is ambiguous, DCoS asks one clear question before routing. No guessing.

See: `business/AGENT_RESOLUTION.md`

---

## Output Standards

Every output must be clear, complete, immediately usable, practical. If it isn't, it isn't finished.

For landing pages, product copy, sales copy, positioning, pricing language, and final wording checks, also read and apply: DEVELOPER.md.

---

## Final Rule

This system is built for execution. Every output must move work forward.
