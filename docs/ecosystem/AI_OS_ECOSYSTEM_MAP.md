# AI OS Ecosystem Map — Axis OS v3

## Three layers, one user interface

```
                         USER
                          │
                          ▼
                    ┌──────────┐
                    │   DCoS   │   COMMAND LAYER
                    │ (router  │   (sole interface)
                    │ + tracker)│
                    └─────┬─────┘
                          │ routes
              ┌───────────┼────────────┐
              │           │            │
              ▼           ▼            ▼
       ┌──────────┐ ┌──────────┐ ┌──────────────┐
       │ THINKING │ │ REVENUE  │ │  COMPLIANCE  │
       │ LAYER    │ │ LAYER    │ │  (always on) │
       │ (Axis AI)│ │          │ │              │
       │          │ │ deal-    │ │ gdpr         │
       │ 14       │ │ sourcing │ │ HANDOVER/    │
       │ agents   │ │   ↓      │ │ COMPLIANCE_  │
       │          │ │ outreach │ │ PROTOCOL.md  │
       │          │ │   ↓      │ │              │
       │          │ │ pipeline │ │              │
       └──────────┘ └──────────┘ └──────────────┘
              │           │            │
              ▼           ▼            ▼
       MEMORY.md    DEAL_LOG.md   GDPR_LOG.md
       BRAND.md     PIPELINE.md   GDPR.md
       OFFERS.md    ACTIVE_       HANDOVER/
       CONTENT_     CLIENTS.md
       THEMES.md
                                 ↑
                                 │
                          EXECUTION_TRACKER.md
                          (DCoS owns)
```

## Layer 1 — Command (DCoS)

- **Agent:** dcos
- **Sole interface to the user**
- **Reads:** every user message, EXECUTION_TRACKER.md, PIPELINE.md, ACTIVE_CLIENTS.md, AGENT_RESOLUTION.md
- **Writes:** EXECUTION_TRACKER.md, routing decisions
- **Never:** executes specialist work, challenges output, runs audits

## Layer 2 — Thinking (Axis AI)

The 14 specialists. Each does its specialism AND challenges its own output before handing back.

Sub-groups:
- **Setup:** onboarding, handover
- **Content:** linkedin, social, outreach
- **Strategy:** audit, workflow
- **Build:** design, builder
- **Operations:** pipeline, qa, context, session-summary
- **Compliance:** gdpr

QA is the cross-cutting reviewer for client-facing work.

## Layer 3 — Revenue

Three-step chain:

1. **deal-sourcing** — finds and validates the deal → `DEAL_LOG.md`
2. **outreach** — drafts the message → `D:/Wayne Francis/Outreach/` or client folder
3. **pipeline** — tracks the lead through stages → `PIPELINE.md`, `ACTIVE_CLIENTS.md`

DCoS routes between steps. The user never chains manually.

## Compliance — always on

Sits underneath all three layers:
- `gdpr` agent handles SAR / erasure / breach / data map
- `business/HANDOVER/GDPR_PROTOCOL.md` — protocol
- `business/HANDOVER/COMPLIANCE_PROTOCOL.md` — PECR / CAP / EU AI / MLR / Equality
- Hard limits (high-risk AI uses) enforced by DCoS at routing

## Data flow — common task examples

**"Write me a LinkedIn post"**
```
User → DCoS → linkedin → qa → DCoS → User
        ↓                ↓
  tracker row        tracker row
  status: routed     status: done
```

**"Find me a client"**
```
User → DCoS → deal-sourcing → DEAL_LOG.md
                  ↓
              DCoS routes next step
                  ↓
              outreach → message draft → qa
                  ↓
              DCoS routes next step
                  ↓
              pipeline → PIPELINE.md
```

**"Onboard a new client"**
```
User → DCoS → handover (orchestrates: onboarding → audit → workflow → builder → qa → playbook)
        ↓
  tracker row tracks each stage
```

## How a new OS plugs in

See `ONBOARDING_NEW_OS.md`. Short version: a new OS becomes a new layer or a new agent inside an existing layer. DCoS routes to it via AGENT_RESOLUTION.md.
