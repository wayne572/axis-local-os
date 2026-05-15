# Audit To Client OS Workflow

Status: active
Purpose: Defines how SF&W turns an SME AI Automation Audit into a client-ready AI OS.

## Principle

The SF&W Claude OS is the factory.

The client OS is the product.

Do not hand over the internal SF&W build.

## Inputs From Audit

After an audit, collect:

- client name
- business summary
- key pain points
- tools currently used
- workflows reviewed
- agreed priority workflows
- data involved
- risks or compliance notes
- usage tracking / analytics preference
- contractor, freelancer, agency worker, consultant, or limited company worker use
- IR35 / off-payroll working risk flag, if relevant
- client tone and preferences
- assistant name preference
- success criteria
- agreed scope
- out-of-scope items

## Build Sequence

### Step 0 - Confirm Target Platform

Before creating the client copy, ask Wayne:

```text
Which platform will this client build run on first: Claude, ChatGPT, Codex, Telegram, WhatsApp, or another environment?
```

Record the answer in the client handover checklist.

Do not assume the platform from the current working folder, previous client build, or the AI tool being used to prepare the files.

### Step 1 - Create Client Copy

Copy:

`PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/CLIENT_OS_TEMPLATE`

Rename:

`[CLIENT_NAME]_AI_OS`

### Step 2 - Fill Client Context

Complete:

`BUSINESS/CLIENT_CONTEXT.md`

Use only confirmed facts from:
- audit notes
- client answers
- agreed proposal
- signed scope

During first-time client setup, ask:

```text
Would you like to give your AI PA a name, or should we keep the default name Axis?
```

Record the answer as `Assistant Name`.

### Step 3 - Select Modules

Use:

`CORE/WORKFLOW_MODULES/SME_DEPLOYMENT_MODULES.md`

Select only modules included in scope:
- enquiry follow-up
- quote or proposal generator
- standard email handler
- invoice and payment chaser
- job, client, or pipeline tracker

### Step 4 - Build Workflow Index

Complete:

`WORKFLOWS/WORKFLOW_INDEX.md`

Each workflow must have:
- owner
- status
- source module
- next action
- proof required

### Step 5 - Populate Trackers

Complete:

- `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`
- `BUSINESS/TRACKING/DECISION_LOG.md`
- `BUSINESS/TRACKING/SESSION_LOG.md`

Optional, if in scope:
- `BUSINESS/TRACKING/RELATIONSHIP_MEMORY.md`
- `BUSINESS/TRACKING/INTRO_TRACKER.md`

### Step 6 - Add Templates

Update:

- `TEMPLATES/EMAIL_TEMPLATES.md`
- `TEMPLATES/PROMPT_LIBRARY.md`

Only include templates that match the client's voice and scope.

### Step 7 - Review Compliance

Review:

`COMPLIANCE/DATA_HANDLING_NOTES.md`
`COMPLIANCE/USAGE_TRACKING_NOTICE.md`
`COMPLIANCE/CLIENT_CONSENT_AND_ANALYTICS.md`

Mark `in review` if:
- personal data is involved
- outreach is involved
- sensitive data appears
- client wants WhatsApp or Telegram
- data moves into a new tool
- usage tracking is enabled
- analytics or improvement learning is requested
- contractors, freelancers, agency workers, consultants, or limited company workers are involved

If IR35 / off-payroll working may be relevant, include:

`COMPLIANCE/IR35_OFF_PAYROLL_RISK_FLAG.md`

### Step 7A - Set Usage Tracking

Complete:

`BUSINESS/TRACKING/USAGE_LOG.md`

Decide with the client:
- essential operational tracking
- optional improvement analytics
- anonymised learning
- public case study or example use

Do not use identifiable client material for public examples without explicit approval.

### Step 8 - Handover

Run:

`HANDOVER/HANDOVER_CHECKLIST.md`

Then give the client:
- folder walkthrough
- daily prompt
- weekly review prompt
- workflow update example
- support route
- 30-day review date

## Output

The final client OS should include:

```text
[CLIENT_NAME]_AI_OS/
  CLAUDE.md or target-platform instruction file
  START_HERE.md
  BUSINESS/
  CORE/
  WORKFLOWS/
  TEMPLATES/
  TRAINING/
  COMPLIANCE/
  CHANNELS/
  HANDOVER/
```

## Locking Rule

The client OS can move to `locked` only when:

- client context is complete
- target platform is confirmed and reflected in the instruction file
- assistant name is confirmed or default `Axis` accepted
- workflows match agreed scope
- data handling is reviewed
- IR35 / off-payroll working risk is flagged where relevant
- usage tracking is explained and recorded
- handover checklist is complete
- Wayne has reviewed the copy
- client has received the walkthrough

## Failure Conditions

Do not hand over if:
- placeholders remain
- internal SF&W files are included
- other client details are included
- compliance is unclear
- contractor or worker status is being decided by the OS
- workflow ownership is missing
- the client does not know how to use it
