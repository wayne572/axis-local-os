# Current Template Pointers

Status: active
Last reviewed: 2026-05-17
Purpose: Identify the canonical delivery templates so archived, shipped, and test folders are not edited by mistake.

## Core Rule

Use `LATEST_SELLABLE_BUILDS` as the source for current sellable templates.

Do not create new client work from:

- shipped client folders
- `_NOT_IN_USE_BUILDS_ARCHIVE_2026-05-09`
- live test folders
- old duplicate ZIPs
- folders marked archive, test, backup, or not in use

## Current Canonical Templates

| Product / Use Case | Canonical Folder | Platform Default | Status |
|---|---|---|---|
| Solo Operator OS | `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/LATEST_SELLABLE_BUILDS/01_SOLO_OPERATOR_OS_TEMPLATE_CLAUDE` | Claude | production V4 template; includes `V4_OPERATING_LOGIC.md`, idea-to-memory workflow, memory discipline, simple user guide, first 7 days guide, acceptance tests, shipping checklist, and platform notes |
| Client OS Build / Growth Template | `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/LATEST_SELLABLE_BUILDS/02_CLIENT_OS_BUILD_TEMPLATE_CLAUDE` | Claude | production V4 template; includes `V4_OPERATING_LOGIC.md`, Growth blueprint, role map, owner command centre example, acceptance tests, adoption plan, handover script, change control, shipping checklist, and sample records |

## V4 Template Rule

All production AI OS builds must be created from the V4 templates above.

Minimum required operating loop:

```text
Capture -> Structure -> Operate -> Review -> Memory Update
```

Do not ship a production build until the relevant acceptance tests confirm:

- one full workflow loop works end-to-end
- `AXIS: IDEA TO MEMORY` is available
- memory updates are scoped, useful, and approved
- governance and human review boundaries are clear

## Current Business And Delivery Authority

Use these documents for current offer catalogue, delivery SOP, and operator training:

- `final-docs-drafts/AXIS_AI_OS_BUSINESS_BIBLE.md`
- `final-docs-drafts/AXIS_AI_OS_BUSINESS_BIBLE_MOBILE.html`
- `final-docs-drafts/AXIS_BUILD_DELIVERY_MASTER_SOP.md`
- `launch-control/CLIENT_OS_GROWTH_TEST_SME_EXAMPLE/`

SME AI Automation Audit remains the front-door offer for SME work. Client OS Growth should be sold after Audit proves scope, team readiness, value, and manageable risk.

## Current Shipped Builds

Shipped builds are proof and client history, not starting templates.

| Client | Folder | Use |
|---|---|---|
| Joseph / Bluxe | `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/SHIPPED/03_JOSEPH_BLUXE_SOLO_OS_CLAUDE_CLIENT_BUILD` | shipped client reference |
| Savannah / SCC Homes | `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/SHIPPED/04_SAVANNAH_SCC_HOMES_SOLO_OS_CODEX_CLIENT_BUILD` | shipped client proof and reference |

## Platform Confirmation Rule

Before creating any client build, ask:

```text
Which platform will this client build run on first: Claude, ChatGPT, Codex, Telegram, WhatsApp, or another environment?
```

Then adjust the instruction file:

| Platform | Instruction File |
|---|---|
| Claude | `CLAUDE.md` |
| Codex | `AGENTS.md` or `CODEX.md` |
| ChatGPT | custom instructions / project instructions |
| Telegram | channel access instructions and support boundary |
| WhatsApp | channel access instructions and support boundary |

## Archive Handling

The bulky `_NOT_IN_USE_BUILDS_ARCHIVE_2026-05-09` folder should not be used for current work. It can be moved to an external archive after Wayne approves the cleanup.
