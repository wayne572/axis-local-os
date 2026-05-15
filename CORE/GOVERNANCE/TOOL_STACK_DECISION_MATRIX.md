# Tool Stack Decision Matrix

Status: active
Purpose: Decide which tools AXIS should use, avoid, test, or defer.

## Core Rule

Do not add tools because they are fashionable.

Add a tool only when it improves:

- revenue
- delivery
- usability
- handover
- portability
- client trust
- measurable ROI

## Decision Statuses

| Status | Meaning |
|---|---|
| Use | Approved for active use |
| Test | Try on a small controlled workflow |
| Watch | Track, but do not use yet |
| Avoid | Do not use unless Wayne explicitly overrides |
| Client choice | Use if the client already works there |

## Current Matrix

| Tool / Platform | Status | Use Case | Reason | Boundary |
|---|---|---|---|---|
| Claude | Use | Main OS operator | Current working environment | Keep files portable |
| Codex | Use | Build/edit/test OS files | Strong for filesystem work | Not the client product brand |
| Markdown folders | Use | Portable OS storage | Simple, owned, transferable | Needs clean structure |
| CSV / spreadsheets | Use | Trackers and exports | Client-friendly | Avoid complex formulas unless needed |
| Notion | Client choice | Docs, trackers, shared workspace | Useful if client already uses it | Do not force it |
| Microsoft 365 | Client choice | Docs, email, Teams, SharePoint | Many SMEs already use it | Use client setup where possible |
| Google Workspace | Client choice | Docs, Gmail, Drive, Sheets | Many SMEs already use it | Need clear data boundaries |
| n8n | Test | Self-hosted / no-code automation | Good portability and automation | Test after manual workflow proof |
| Activepieces | Watch/Test | Open automation | Possible no-code alternative | Compare against n8n |
| Zapier | Client choice | Quick automation | Easy if client already pays | Can create subscription dependency |
| Make | Client choice | Visual automation | Useful for no-code clients | Watch complexity and lock-in |
| Airtable | Client choice | Lightweight database/CRM | Good for trackers | Can become paid dependency |
| Telegram | Test later | Quick capture / relationship notes | Lightweight capture route | Not built yet |
| WhatsApp | Watch/Test later | Client-friendly capture | Strong adoption | More compliance/platform friction |
| Apollo | Watch/Client choice | Prospect sourcing | Useful for lead generation | Check ToS, data basis, cost |
| Instantly / cold email tools | Watch | Outreach campaigns | Could support lead flow | Compliance and reputation risk |
| A2A | Watch | Agent interoperability | Emerging standard | Do not build on yet |
| MCP connectors | Watch/Use if available | Tool access | Useful when present | Never invent availability |

## Tool Approval Questions

Before adding a tool, ask:

- What problem does it solve?
- Can Wayne run it without coding?
- Can the client own it after handover?
- What happens if the provider changes price?
- Does it create lock-in?
- Does it touch personal data?
- Does it need a DPA or client consent?
- Can we prove ROI without it first?

## Preferred Order

1. Existing client tools
2. Markdown / folders / simple trackers
3. Open standards
4. Self-hosted or portable no-code tools
5. Proprietary tools only when justified

## Rejection Rule

Reject or defer a tool if:

- it solves a problem we have not proven
- it creates unclear data risk
- it requires coding Wayne cannot maintain
- it locks a client into a platform unnecessarily
- it is only impressive, not useful

## Review Prompt

```text
Review this proposed tool against the Tool Stack Decision Matrix. Recommend Use, Test, Watch, Avoid, or Client choice. Explain the reason in plain English.
```
