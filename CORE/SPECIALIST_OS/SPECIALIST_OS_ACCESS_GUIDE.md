# Specialist OS Access Guide

Status: active
Purpose: Explains how Wayne and Claude access specialist capabilities in the new build.

## Plain-English Rule

Specialist OS modules are capability playbooks.

They are not separate agents.

Claude reads and applies the right playbook when the work needs it.

## How Wayne Accesses Them

Wayne can ask naturally:

```text
Use Lead mode.
```

```text
Use Sales OS to draft the follow-up.
```

```text
Use Client Delivery OS for this onboarding.
```

```text
Review this using the validation layer.
```

```text
Run the weekly relationship review.
```

Claude should then read the relevant module and produce the output.

## Access By Mode

| Mode | Specialist Module | Use For |
|---|---|---|
| LEAD | Deal Sourcing OS | finding, filtering, and qualifying prospects |
| LEAD | Sales OS | outreach, replies, discovery, follow-up, handoff |
| BUILD | Client Delivery OS | onboarding, delivery, progress, completion |
| BUILD / LEAD | Marketing OS | positioning, content, inbound handoff |
| LEARN / REVIEW / BUILD | Precision Alpha OS | governed BTC/ETH crypto research, trade thesis generation, regime/risk review, paper-trading journal |
| REVIEW | Output Validation | final checks, risk, readiness |
| ORCHESTRATE / LEAD | Relationship Connector Mode | warm intros, referrals, follow-ups, relationship memory |

## Access By Trigger

| Trigger / Request | Claude Should Use |
|---|---|
| `AXIS: NEW CLIENT` | Audit-to-client workflow + Client OS template |
| `What is the current status?` | Active Workstreams + DCoS Command Layer |
| `Build the next asset` | Current active workstream + BUILD mode |
| `Activate Lead mode` | Deal Sourcing OS + Sales OS |
| `Run relationship pulse` | Relationship Connector Mode |
| `Run weekly review` | Active Workstreams + Validation |
| `AXIS: PRECISION ALPHA` | Precision Alpha OS |
| `AXIS: PA THESIS` | Precision Alpha OS - thesis + confidence + risk review |
| `AXIS: PA RISK REVIEW` | Precision Alpha Risk Officer Protocol |
| `AXIS: PA JOURNAL` | Precision Alpha Trade Journal Schema |

## How Claude Should Respond

Claude may say:

```text
Mode: LEAD
Using: Deal Sourcing OS + Sales OS
```

Then provide the working output.

Claude should not over-explain the internal architecture unless Wayne asks.

## Specialist File Locations

Deal Sourcing:
`CORE/SPECIALIST_OS/DEAL_SOURCING_OS`

Sales:
`CORE/SPECIALIST_OS/SALES_OS`

Client Delivery:
`CORE/SPECIALIST_OS/CLIENT_DELIVERY_OS`

Marketing:
`CORE/SPECIALIST_OS/MARKETING_OS`

Precision Alpha:
`CORE/SPECIALIST_OS/PRECISION_ALPHA_OS`

Relationship Connector:
`CORE/CLAUDE_OPERATOR/RELATIONSHIP_CONNECTOR_MODE.md`

Validation:
`CORE/VALIDATION/OUTPUT_VALIDATION_ENGINE.md`

## Client Version

Clients should not see the full internal Specialist OS language unless they need it.

In client copies, explain them as:

`Capability Modules`

Example:

- Enquiry Follow-Up
- Quote Builder
- Email Handler
- Invoice Chaser
- Job Tracker
- Relationship Memory
- Weekly Review
