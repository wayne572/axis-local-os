# Agent Interoperability Watch

Status: active watch
Purpose: Track agent interoperability standards and decide when AXIS should support them.

## Why This Exists

AI agents are moving from isolated tools toward systems that can communicate, delegate, and coordinate across vendors and runtimes.

AXIS should stay aware of this without becoming dependent on any one standard too early.

## Current Standards To Watch

| Standard / Pattern | Status | Why It Matters | AXIS Position |
|---|---|---|---|
| MCP-style tool access | Active ecosystem | Gives models structured access to tools and data | Useful now where connectors are available |
| A2A / Agent-to-Agent protocol | Maturing | May allow agents from different systems to communicate | Watch, do not depend on yet |
| OpenAI-compatible endpoints | Stable practical pattern | Supports portability across runtimes | Prefer where possible |
| Webhooks / OpenAPI | Mature | Practical for no-code and client integrations | Use before proprietary lock-in |
| IMAP/SMTP | Mature | Email interoperability | Prefer over locked email tools where suitable |
| CalDAV/CardDAV | Mature | Calendar/contact portability | Consider for future client systems |

## Decision Rule

AXIS should support interoperability only when it improves one of:

- portability
- client handover
- tool access
- auditability
- reduced vendor lock-in
- practical no-code delivery

Do not add complexity just to appear current.

## When To Test A2A

Test A2A only when:

- Claude/Codex workflow is stable
- Client OS template is tested
- Solo Operator OS is tested
- there is a real need for agents across tools or providers to communicate
- implementation does not create vendor lock-in

## Practical Near-Term Use

For now, AXIS should treat interoperability as:

1. folder-based context
2. structured Markdown
3. CSV/spreadsheet trackers
4. generic webhooks
5. MCP/tool connectors where available
6. no-code automation after manual workflow proof

## Watch Items

| Item | Status | Next Action |
|---|---|---|
| MCP availability in Claude/Codex | Watch | Note which connectors are actually available before promising them |
| A2A adoption | Watch | Review monthly in Technology Radar |
| n8n/Activepieces connector support | Watch | Test with one low-risk internal workflow |
| WhatsApp Business API access | Watch | Assess compliance and setup complexity before client use |
| Telegram bot capture | Test later | Useful for relationship notes and quick capture |

## Interoperability Risk Questions

Before adding any standard, ask:

- Does Wayne understand how to run it?
- Can it be explained to a client?
- Does it keep data portable?
- Can the client own it after handover?
- What happens if the provider changes pricing or access?
- Does it increase compliance risk?

## Output Rule

If asked whether AXIS supports a protocol or connector, answer based on the current host and actual files/tools available.

Never invent tool availability.
