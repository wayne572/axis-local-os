# Client OS Build And Handover - No-Code Delivery Plan

Status: active draft
Price: GBP 9,995, in review
Owner / brand: Wayne Francis
Trading entity: SF&W Project Solutions
Purpose: Build and hand over a client AI operating system without programming.

## Who This Is For

Clients who have completed an audit or already know which workflow needs a structured operating system.

Best fit:
- SME with 5-20+ staff
- small agency or consultancy
- professional services firm
- property business
- recruitment agency
- accountancy firm
- local service business

## Client Outcome

The client receives a working, documented operating system for the agreed workflow or business area.

It may include:
- client context
- workflow modules
- active workstream tracker
- decision log
- session log
- email templates
- prompt library
- handover pack
- user guide
- 30-day review checklist

## What You Need

No-code tools:
- Claude
- client OS template folder
- implementation scope
- client examples
- shared folder or documents
- email
- review calls

Source files:
- `delivery/CLIENT_OS_TEMPLATE`
- `proposals/IMPLEMENTATION_SCOPE_TEMPLATE.md`
- `delivery/CLIENT_HANDOVER_EMAIL_TEMPLATE.md`

## Delivery Timeline

Recommended:
10-20 working days for first version.

## Stage 1 - Confirm Scope

Use:

`proposals/IMPLEMENTATION_SCOPE_TEMPLATE.md`

Confirm:
- workflow being improved
- in scope
- out of scope
- inputs needed
- outputs
- acceptance criteria
- change control

No-code rule:
If it is not in the scope, do not build it.

## Stage 2 - Create Client OS Copy

Use trigger:

```text
AXIS: NEW CLIENT
```

No-code action:
Copy:

`delivery/CLIENT_OS_TEMPLATE`

Rename:

```text
CLIENT_OS_[CLIENT_NAME]
```

Mark:

```text
Status: in review
```

## Stage 3 - Fill Client Context

Update:
- `BUSINESS/CLIENT_CONTEXT.md`
- `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`
- `BUSINESS/TRACKING/DECISION_LOG.md`
- `WORKFLOWS/WORKFLOW_INDEX.md`

Prompt:

```text
Using the approved scope and audit report, configure this Client OS copy. Include only client-facing workflow details. Do not include SF&W internal strategy.
```

## Stage 4 - Build The Workflow Modules

Use the template modules as the base.

For each workflow, create:
- purpose
- inputs
- steps
- owner
- output
- review rule
- failure points
- prompt the client can use

No-code examples:
- enquiry tracker
- quote follow-up process
- candidate follow-up tracker
- document chase workflow
- onboarding checklist
- weekly status report

## Stage 5 - Create Templates

Depending on scope, create:
- email templates
- prompt templates
- checklist
- tracker
- report format
- handover notes

Keep everything editable by the client.

No code.

## Stage 6 - Test With Sample Data

Use 3-5 realistic examples.

Test:
- Does Claude understand the workflow?
- Does the tracker capture the right fields?
- Does the output match the client's tone?
- Does the handover make sense?
- Are any steps missing?

Record issues in:

`BUSINESS/TRACKING/SESSION_LOG.md`

## Stage 7 - Handover

Use:

`delivery/CLIENT_HANDOVER_EMAIL_TEMPLATE.md`

Show the client:
- where to start
- main commands
- workflows included
- how to add new work
- how to review output
- what is out of scope
- how to request changes

## Stage 8 - 30-Day Review

Use:

`HANDOVER/30_DAY_REVIEW_CHECKLIST.md`

Review:
- usage
- workflow fit
- missed steps
- time saved
- adoption
- what to simplify
- what to build next

## Deliverables

Client receives:
- configured Client OS
- workflow modules
- trackers
- templates
- prompt library
- handover pack
- user guide
- 30-day review

## What Is Not Included

Not included unless agreed:
- custom coding
- API integrations
- automatic email sending
- WhatsApp/Telegram bot setup
- CRM migration
- legal/compliance advice
- ongoing optimisation

## Completion Criteria

Move to locked when:
- client has tested the OS
- issues have been resolved
- handover is complete
- boundaries are explained
- 30-day review is booked
