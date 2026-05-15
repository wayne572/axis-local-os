# Latest Sellable Builds

Status: current source of truth
Last updated: 2026-05-09
Owner: Wayne Francis, trading under SF&W Project Solutions

## Purpose

This folder contains the current sellable build templates.

Use these before creating a new client copy.

## Current Builds

### 01 - Solo Operator OS Template

Folder:

```text
01_SOLO_OPERATOR_OS_TEMPLATE_CLAUDE
```

Use this for a solo founder, consultant, freelancer, creator, or one-person business.

### 02 - Client OS Build Template

Folder:

```text
02_CLIENT_OS_BUILD_TEMPLATE_CLAUDE
```

Use this after an SME audit or approved implementation scope when creating a client operating system.

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
