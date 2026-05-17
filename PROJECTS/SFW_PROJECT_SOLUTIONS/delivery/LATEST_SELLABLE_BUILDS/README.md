# Latest Sellable Builds

Status: current source of truth
Last updated: 2026-05-17
Owner: Wayne Francis, trading under SF&W Project Solutions

## Purpose

This folder contains the current sellable build templates.

Use these before creating a new client copy.

All production builds must now use the Axis V4 operating logic:

```text
capture
-> structure
-> plan / operate
-> review
-> update tracker or memory
```

Functionality is the core of the build. Every production template must include:

- a clear start route
- active loops or workstream tracking
- decision capture
- weekly review
- 30-day review
- boundary/governance rules
- memory discipline
- acceptance tests
- shipping checklist

## Current Builds

### 01 - Solo Operator OS Template

Folder:

```text
01_SOLO_OPERATOR_OS_TEMPLATE_CLAUDE
```

Use this for a solo founder, consultant, freelancer, creator, or one-person business.

V4 production standard:

- `V4_OPERATING_LOGIC.md` must be included.
- `AXIS: IDEA TO MEMORY` must work.
- The build must distinguish temporary notes from durable memory.
- The user should always leave with a next action, tracker update, or reviewed memory decision.

### 02 - Client OS Build Template

Folder:

```text
02_CLIENT_OS_BUILD_TEMPLATE_CLAUDE
```

Use this after an SME audit or approved implementation scope when creating a client operating system.

V4 production standard:

- `V4_OPERATING_LOGIC.md` must be included.
- Workflow changes must pass review before becoming locked authority.
- Client memory must remain scoped to the client folder.
- Sensitive data and compliance boundaries must be visible before handover.

### 03 - Solo Operator OS Template - Codex

Folder:

```text
03_SOLO_OPERATOR_OS_TEMPLATE_CODEX
```

Use this when the Solo Operator OS will run inside Codex.

V4 production standard:

- `AGENTS.md` and `CODEX.md` are the platform authority.
- `V4_OPERATING_LOGIC.md` must be included.
- `AXIS: IDEA TO MEMORY` must work.
- `CLAUDE_REFERENCE.md` is retained only as a cross-platform reference.

## Platform Rule

Before creating any client build, ask:

```text
Which platform will this client build run on first: Claude, ChatGPT, Codex, Telegram, WhatsApp, or another environment?
```

Do not assume from the workspace being used.

## Compliance Rule

Current sellable builds include an IR35 / off-payroll working risk flag.

If a client uses contractors, freelancers, agency workers, consultants, or workers through limited companies, the OS must flag possible IR35 / off-payroll considerations.

The OS can organise facts, track whether a review has happened, and prepare questions. It must not decide employment status, IR35 status, or tax treatment.

## Shipped Builds

Client-specific builds that have already been prepared for sending live in:

```text
../SHIPPED/
```

## Do Not Use

Do not sell, ship, or copy from:

- live test folders
- Codex test folders
- old duplicate zips
- folders marked archive or not in use

Those are kept only for traceability.
