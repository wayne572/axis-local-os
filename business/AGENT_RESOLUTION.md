# AGENT_RESOLUTION.md — Axis OS v3

DCoS uses this table to route every task. Pick the minimum agents required.

## Default routing table

| Task signal | Agent | Layer |
|---|---|---|
| Default entry — every user message starts here | **dcos** | Command |
| "Find me a deal", "who can I sell to", "where are the leads" | **deal-sourcing** | Revenue |
| "Begin Axis OS setup", new client deployment | handover | Thinking |
| "Run a SAR", "erase X", "data map", "breach", "GDPR status" | gdpr | Thinking |
| "Onboard new client" (skip full handover) | onboarding | Thinking |
| Write a LinkedIn post / article / carousel | linkedin | Thinking |
| Write Instagram / X / TikTok / Facebook post | social | Thinking |
| Write outreach email / cold message / follow-up | outreach | Revenue (chain after deal-sourcing) |
| Diagnose a business / find inefficiencies / readiness review | audit | Thinking |
| Design a workflow / SOP / process | workflow | Thinking |
| Design a page / deck / wireframe / visual | design | Thinking |
| Build / spec / code | builder | Thinking |
| Track a lead / move pipeline stage / next-action | pipeline | Revenue |
| Review output before send | qa | Thinking |
| Extract context from a doc or session | context | Thinking |
| Capture session summary | session-summary | Thinking |

## Chain rules

- **Deal-finding chain:** deal-sourcing → outreach → pipeline (DCoS routes each step in turn, never in parallel)
- **Client deployment chain:** handover (handover orchestrates onboarding → audit → workflow → builder → qa internally)
- **Content chain:** topic intake → linkedin/social/outreach → qa (before send)

## Tie-break rules

If two agents fit:

1. Prefer the more specialised agent.
2. Prefer the agent closer to revenue (deal-sourcing > outreach > pipeline).
3. Prefer the agent with explicit trigger phrasing in the user message.
4. If still tied, ask the user one question.

## When to halt instead of route

- High-risk AI use (recruitment, credit, medical, biometric, legal-effect, education access) → halt, flag to user.
- Core context missing (BRAND, OFFERS, CONTENT_THEMES, MEMORY, GDPR empty) → route to handover before anything else.
- Compliance flag (B2C marketing without consent, special category data, regulated financial promotion) → halt, flag.
