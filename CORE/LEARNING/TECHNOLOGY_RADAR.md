# Technology Radar

Status: active
Owner: Wayne Francis
Purpose: Keep Axis OS v3 Enhanced current as AI tools, models, regulations, and automation patterns change.

## Core Rule

This radar exists to protect AXIS from becoming stale.

Do not chase every new tool. Track what matters, decide whether it is useful, then either:

- know
- watch
- test
- deploy
- reject

## Review Rhythm

Recommended cadence:

- weekly quick scan
- monthly deeper review
- immediate update when a major model, agent standard, compliance change, or access-channel change affects AXIS

## Radar Categories

| Category | Why It Matters |
|---|---|
| Open models | Determines what AXIS can run on without lock-in |
| Claude / Codex changes | Affects current operating environment |
| Open agent frameworks | Future multi-agent deployment options |
| Agent protocols | MCP, A2A, tool access, and agent-to-agent interoperability |
| No-code automation | Practical delivery route for Wayne and clients |
| SME AI adoption | Commercial timing and objection handling |
| UK AI / data regulation | Compliance and trust |
| Messaging and voice capture | Telegram, WhatsApp, voice notes, and quick capture |
| Client governance | Usage tracking, consent, review, and human oversight |
| Product packaging | Solo Operator OS, Client OS, audit offers, and relationship mode |

## Radar Statuses

| Status | Meaning |
|---|---|
| Know | Important context, no action yet |
| Watch | Monitor for maturity or relevance |
| Test | Run a small controlled test |
| Deploy | Approved for active use |
| Reject | Not useful or creates too much risk |

## Current Radar

| Item | Category | Status | Relevance | Next Action |
|---|---|---|---|---|
| Claude project/folder workflow | Claude / Codex changes | Deploy | Current primary operating route | Keep v3 Enhanced optimised for Claude |
| Codex folder workflow | Claude / Codex changes | Deploy | Useful for building and editing the OS | Maintain Codex-compatible Solo Operator build |
| MCP-style tool connectors | Agent protocols | Watch | Important for future tool access | Track available connectors before promising integrations |
| A2A protocol | Agent protocols | Watch | Agent interoperability is maturing | Track but do not build against it yet |
| n8n | No-code automation | Watch/Test | Strong candidate for self-hosted workflows | Test only after manual workflow is proven |
| Activepieces | No-code automation | Watch | Open automation option | Compare against n8n if needed |
| Telegram access | Messaging and voice capture | Test later | Useful for quick capture and relationship notes | Keep as planned access channel |
| WhatsApp access | Messaging and voice capture | Watch/Test later | Useful but more compliance and platform friction | Do not promise until scoped |
| UK SME AI adoption signals | SME AI adoption | Watch | Supports sales positioning | Use in LEARN briefs and offer updates |
| ICO AI guidance | UK AI / data regulation | Watch | Affects client governance and usage tracking | Review before client handover |
| AI ROI measurement | Client governance | Deploy | Commercial proof and trust builder | Use `AI_ROI_TRACKER.md` in audits and builds |

## Weekly Radar Prompt

Use this in LEARN mode:

```text
Activate Learn mode. Update the Technology Radar. Check open models, Claude/Codex changes, open agent frameworks, MCP/A2A, no-code automation, UK SME AI adoption, ICO/UK data guidance, Telegram/WhatsApp access, and product packaging. Return a one-page brief with: what changed, why it matters, what we should test, and what we should ignore.
```

## Output Format For Updates

Each update should include:

- date
- source or signal
- what changed
- why it matters to Wayne / SF&W
- risk
- recommended status
- next action

## Current Priority

The highest-value radar topics are:

1. AI ROI measurement for SMEs
2. Client governance and trust
3. Claude/Codex operating changes
4. Messaging/voice capture
5. Agent interoperability standards

## Boundary

Do not recommend a new platform simply because it is new.

Recommend only when it improves:

- revenue
- delivery
- client trust
- portability
- usability
- measurable ROI
