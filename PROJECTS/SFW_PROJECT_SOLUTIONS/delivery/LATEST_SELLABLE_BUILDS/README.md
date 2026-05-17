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
- AI OS control register
- workflow freeze protocol
- source trust / prompt injection check
- monthly memory audit
- usage and ROI tracking
- platform change watch
- tone and style profile
- care package review route
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
- The care package layer must support `AXIS: CARE REVIEW`.

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
- The care package layer must support `AXIS: CARE REVIEW`.

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
- The care package layer must support `AXIS: CARE REVIEW`.

## Care Package Standard

Every current build includes:

- `GOVERNANCE/AI_OS_CONTROL_REGISTER.md`
- `GOVERNANCE/AGENT_FREEZE_PROTOCOL.md`
- `GOVERNANCE/SOURCE_TRUST_AND_PROMPT_INJECTION_CHECK.md`
- `CARE_PACKAGE/CARE_PACKAGE_OPERATING_STANDARD.md`
- `CARE_PACKAGE/BUILD_UPDATE_LOG.md`
- `CARE_PACKAGE/MONTHLY_MEMORY_AUDIT.md`
- `CARE_PACKAGE/AI_USAGE_AND_ROI_TRACKER.md`
- `CARE_PACKAGE/PLATFORM_CHANGE_WATCH.md`
- `TEMPLATES/TONE_AND_STYLE_PROFILE.md`

This supports the ongoing care offer:

```text
keep the AI OS governed, current, safe, useful, and measurable as tools and workflows change
```

## Managed Shipped Build Standard

Treat every shipped build as a managed AI OS, not a one-off folder.

Use:

```text
../TEMPLATE_UPDATE_REGISTER.md
```

to decide whether a master template improvement should be applied to shipped builds.

Then record the exact shipped-build update in:

```text
CARE_PACKAGE/BUILD_UPDATE_LOG.md
```

Never overwrite a shipped build wholesale from the master template. Preserve client or user context, memory, trackers, decisions, and live workflows.

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
