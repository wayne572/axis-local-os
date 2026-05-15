# Wayne Copilot

Status: capability spec — partially active (profile and scope filed; workflow build pending)
Date: 2026-05-15
Owner: Wayne Francis

## Purpose

This Axis Local OS deployment is Wayne Francis's. The Wayne Copilot capability binds the system to him specifically — his identity, his offers, his pricing, his clients, his brand, his cadence, his teaching preferences — so Axis acts as a copilot from the first interaction rather than a generic system waiting to be configured.

The Wayne Copilot is not a separate agent. It is a configuration of the existing governed loop: an operator profile that informs every prompt, a KB scope that brings in everything Wayne has built across Axis, and a small set of named workflows (audit-form response, daily command centre, weekly review) that wire the standard Axis surfaces into Wayne's actual operating cadence.

## First Principle

The copilot is for Wayne. It is not a multi-tenant feature. It is not a shareable persona. The profile, the ingest scope, the client folders, and the audit trail belong to this one deployment. If Wayne later needs a copilot for someone else, that is a separate deployment with its own profile, its own scope, its own audit.

## Components

### 1. Operator Profile

Filed at `CORE/OPERATOR_PROFILE.md`. The canonical description of who Wayne is, how to communicate with him, how to teach him when he is learning, how to support decisions when he is choosing, and what the system will not do on his behalf.

The governed loop reads the profile on every interaction. Prompts to local or hosted models include the profile's communication-style and teaching-mode rules so output is consistent across sessions and across providers.

### 2. Copilot Scope

Filed at `config/copilot_scope.json`. The list of folders the KB should index for Wayne:

- The Axis Local OS repo (this folder)
- Axis OS v3 at `D:\Wayne AI OS\Axis OS_v3\` — the operator system, agents, governance, handover protocols, locked offers
- `LATEST_SELLABLE_BUILDS` — current delivery templates
- `D:\Wayne Francis\Axis AI\` — sales assets, sector builds, system specs
- The Axis pricing and sales master HTML files — pricing authority (boosted in retrieval)
- `D:\Wayne Francis\Profiles & Content\` and `Outreach\` — Wayne's voice and prior content
- `D:\Wayne Francis\Clients\` — per-client subfolders, scoped per-client at retrieval

Each ingest root carries a `scope_tag` (`internal_only`, `always_local`, etc.) that the hosted-model adapter's source-scope filter respects. Client data is tagged `always_local` — it never reaches a hosted provider.

### 3. Audit-Form Workflow

When Wayne forwards a completed AI Readiness Review or any other prospect intake to Axis, the copilot runs a structured workflow rather than ad-hoc reasoning.

```text
form submission
-> parse into intake-capture schema
-> compliance check (special category data, B2C consent, MLR, high-risk AI)
-> ICP fit score with one-line reason
-> offer match (Readiness Review only / Solo OS / SME Audit / Client OS Build / Bundle), middle tier as the default quote
-> first three automation candidates with intake citations
-> Tier C draft reply in Wayne's voice (RFP verifier pass)
-> file artefacts under D:\Wayne Francis\Clients\<prospect>\
-> hand back to Wayne for approval before send
```

The workflow is reusable. Audit form schemas live at `business/HANDOVER/INTAKE_TEMPLATE.md` in v3 plus any custom forms Wayne uses. Each form maps to the same five output fields: fit score, offer match, automation candidates, reply draft, file plan.

### 4. Daily / Weekly / Monthly Cadence

The copilot exposes three named workflows that match Wayne's stated cadence (see profile):

- `axis: daily command` — calendar pull, inbox triage view, today's open loops, follow-ups due
- `axis: weekly review` — Friday review of deals progressed, content shipped, what slipped, focus for next week
- `axis: 30 day pulse` — revenue, pipeline, content engagement, what to change

All three are read-only by default. None run on a schedule until Wayne explicitly turns scheduled execution on. Each draws from the connector layer once that is built; until then, they accept structured input from Wayne and produce the view from local data.

### 5. Teaching Mode

When Wayne asks how something works, the copilot uses the five-step structure from the profile:

1. One-sentence plain-English summary
2. Why it matters
3. The simple version of how it works
4. What he needs to do next
5. Source ID for deeper reading

Teaching mode is triggered by phrases like "how does this work," "what is this," "explain," "I do not understand," and by retrieval surfacing material Wayne has not previously touched. Wayne can also trigger it explicitly with `axis: teach me about <topic>`.

### 6. Decision Support Mode

When Wayne is choosing between options, the copilot uses the four-line structure from the profile:

- Recommendation (one line, one biggest reason)
- The tradeoff
- The alternative
- What you would need to know to be more certain

Triggered by phrases like "what do you think," "should I," "which should I pick," or explicit `axis: decide between A and B`.

## Per-Client Routing

When Wayne mentions a client by name or runs an audit-form workflow, the routing layer scopes the active context to `D:\Wayne Francis\Clients\<name>\`. Within that scope:

- Retrieval pulls client material first
- Outputs save to that client's folder
- Audit events tag the active client scope
- Hosted-model calls respect the client's always-local flag if set
- Session prompts reference the client by name without Wayne having to repeat the context

The client-mention rule in Wayne's global CLAUDE.md is honoured: if Wayne references a client and the session has not been client-scoped, the copilot prompts him to confirm the scope rather than guessing.

## Compliance Guardrails (Always On)

The UK compliance rules from Wayne's global CLAUDE.md apply to every copilot interaction:

- GDPR / UK data protection — never blast personal data without lawful basis; respect SARs; populate `business/GDPR.md` for client deployments
- PECR — opt-out lines on outreach; flag missing cookie banners
- CAP Code — never invent testimonials, never make unsubstantiated claims, always disclose paid partnerships
- EU AI Act transparency — append AI-assisted note if content goes out unedited
- Equality Act — inclusive language by default, flag exclusionary phrasing
- MLR / AML — CDD before active status for regulated clients; never reference SARs publicly
- High-risk AI hard limits — no recruitment screening, credit scoring, medical triage, or automated decisions with legal effect

These do not need to be repeated per request. The system holds them.

## Session Efficiency Rules (Always Enforced)

From Wayne's global rules:

- `/load` only at session start. No automatic Notion dashboard pulls.
- One workflow per session. Flag a workstream switch.
- Plain text drafts before HTML email rendering.
- Batch confirmed before execution.
- No speculative fetches.
- Anansi Island goes to Gemma, never Claude.

The copilot enforces these without being asked.

## What Is Live Today

- `CORE/OPERATOR_PROFILE.md` exists and is read by any future prompt-builder that includes it.
- `config/copilot_scope.json` defines the ingest plan. Actual KB ingest from these roots is pending (requires extension to `tools/rag/kb_ingest.py` to read the scope file).
- The audit-form workflow, daily / weekly / monthly cadence commands, teaching mode trigger, and decision support trigger are specified here. They get built once the underlying capabilities they depend on are stable (Response Fidelity Policy for the Tier C reply draft, Command Centre Connectors for the calendar / inbox view).

## MVP Build Order

1. Profile + scope filed (this commit).
2. Extend `kb_ingest.py` to read `copilot_scope.json` and ingest from configured roots with the right scope tags.
3. Wire the profile into the grounded-prompt builder so every model call includes the operator-style rules.
4. Build `axis_audit_form.py` — accepts a form file, runs the audit-form workflow, files artefacts, hands draft to Wayne.
5. Build `axis_daily.py` / `axis_weekly.py` / `axis_30day.py` cadence commands.
6. Wire teaching mode trigger into the answer renderer.
7. Wire decision support trigger.

## Governance Rules

- The copilot is for Wayne only. Profile, scope, audit are not shareable artefacts.
- Profile content is internal-only. Never sent to a hosted model unless Wayne explicitly approves.
- Pricing is authoritative from the master HTML files. Never restated from model memory.
- Client material is always_local by default. Never sent to a hosted provider without explicit per-client approval.
- Every audit-form workflow run writes an audit event including the form file hash, the fit score, the offer match, and the path to the filed artefacts.
- Compliance halts route to the compliance protocol. The copilot does not improvise around them.
- Session efficiency rules are enforced by the system, not by Wayne having to remind it.

## Success Condition

Wayne forwards an AI Readiness Review response to Axis. Within one approval cycle, Axis returns: a parsed intake, a fit score with reason, an offer match at the right tier, three automation candidates with intake citations, a Tier C draft reply in Wayne's voice with the brand block and signature, and a filed artefact set under the prospect's client folder. Wayne reviews the draft, approves the send, and the reply goes out via the Outlook or Gmail connector with a full audit trail. No part of that round trip required Wayne to repeat his offers, his brand, his pricing, his cadence, his compliance rules, or his client folder convention. The system already knew.
