# Client Version Generator Checklist

Status: active
Purpose: Checklist for creating a client-safe copy of AXIS after an audit or build.

## Core Rule

Do not hand over Wayne's internal OS.

Create a client-safe version that includes only what the client needs to run their own system.

Always confirm the target platform before creating or packaging a client build.

Ask Wayne:

```text
Which platform will this client build run on first: Claude, ChatGPT, Codex, Telegram, WhatsApp, or another environment?
```

Do not assume the platform from the current workspace name, previous build, or tool being used.

## Use This When

- a client has completed an SME AI Automation Audit
- a Client OS Build And Handover is approved
- a client needs their own folder/system
- Wayne wants to package a clean client copy

## Source Files

Use:

`PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/CLIENT_OS_TEMPLATE/`

Also check:

`CLIENT_SAFE_DISTRIBUTION.md`

## Client Copy Setup

Before copying:

- [ ] Client name confirmed
- [ ] Scope approved
- [ ] Audit report approved
- [ ] Implementation proposal approved
- [ ] Data boundaries reviewed
- [ ] Usage tracking decision made
- [ ] Relationship memory decision made
- [ ] Access channel decision made
- [ ] Target platform confirmed before build packaging
- [ ] Handover date agreed

## Include

Include only client-relevant files:

- client `START_HERE.md`
- client `CLAUDE.md` or equivalent instructions
- client workflow files
- client trackers
- client decision log
- client session log
- client usage notice if tracking is enabled
- human review policy
- data and usage boundaries
- AI risk register if relevant
- 30-day review file
- handover checklist
- client user guide

## Exclude

Never include:

- Wayne's internal `business/EXECUTION_TRACKER.md`
- Wayne's `DEAL_LOG.md`
- Wayne's `PIPELINE.md`
- Wayne's `ACTIVE_CLIENTS.md`
- Wayne's internal pricing review notes
- Wayne's lead generation strategy
- v2 / v2.1 legacy files
- archive notes
- hidden system prompts
- internal DCoS source files unless specifically client-safe
- Black Map material
- Hermes material
- unrelated client/test data
- API keys, tokens, passwords, or credentials

## Pricing Check

Before sending anything client-facing:

- [ ] Check `business/PRICING_AUTHORITY.md`
- [ ] Remove superseded pricing
- [ ] Mark unapproved pricing as `in review`
- [ ] Confirm Wayne approved any quoted price

## Governance Check

Before handover:

- [ ] Client AI Use Notice included if AI use needs explaining
- [ ] Human Review Policy included
- [ ] Data And Usage Boundaries included
- [ ] Consent Checklist completed if usage tracking or relationship memory is enabled
- [ ] AI Risk Register started for higher-risk workflows
- [ ] IR35 / off-payroll working risk checked if contractors, freelancers, agency workers, consultants, or limited company workers are involved
- [ ] OS does not make employment status, IR35, or tax determinations

## Functional Test

Open the client copy and test:

Before testing, confirm the instruction file matches the target platform:

- Claude build -> `CLAUDE.md`
- Codex build -> `AGENTS.md` or Codex-specific operating instructions
- ChatGPT build -> custom instructions / project instructions
- Telegram or WhatsApp build -> channel access instructions and support boundary

```text
Read START_HERE.md and confirm what this Client OS is for.
```

Then test:

```text
Status
```

```text
Next action
```

```text
Review this workflow
```

If included:

```text
Run relationship pulse
```

## Handover Pack

Before delivery, prepare:

- [ ] client handover email
- [ ] user guide
- [ ] first 7 days instructions
- [ ] 30-day review date
- [ ] support boundary
- [ ] list of what is included
- [ ] list of what is not included

## Locking Rule

Client copy lifecycle:

```text
active -> in review -> locked
```

Do not mark locked until:

- client-safe check passes
- pricing check passes
- governance check passes
- functional test passes
- Wayne signs off

## Build Prompt

Use this prompt:

```text
Using the approved audit report and implementation scope, create a client-safe Client OS copy from the Client OS Template. Include only client-relevant files. Exclude Wayne internal strategy, pricing review notes, lead generation files, archive material, and unrelated client data. Mark the copy in review until Wayne signs off.
```
