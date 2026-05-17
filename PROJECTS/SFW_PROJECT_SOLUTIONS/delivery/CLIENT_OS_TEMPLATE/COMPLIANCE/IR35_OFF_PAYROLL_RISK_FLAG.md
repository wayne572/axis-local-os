# IR35 / Off-Payroll Working Risk Flag

Status: active
Purpose: Flag contractor status risk without giving legal or tax advice.

## Rule

If the client uses contractors, freelancers, consultants, agency workers, or workers through limited companies, the OS must flag possible IR35 / off-payroll working considerations.

The OS must not make an employment status, IR35, or tax determination.

## When To Trigger

Trigger this control if any workflow involves:

- contractor onboarding
- freelancer records
- limited company consultants
- agency worker tracking
- recruitment placement workflows
- statement of work records
- project-based workers
- contractor payment chasing
- role descriptions that could affect worker status
- HR, payroll, finance, or legal handover involving non-employees

## Required Response

When triggered, the OS should say:

```text
This may involve IR35 / off-payroll working considerations. I can help organise the information and prepare questions, but I cannot decide employment status or provide tax/legal advice. Use HMRC CEST, HMRC guidance, or a qualified adviser before relying on a status decision.
```

## What The OS Can Do

The OS may help the client:

- collect contractor details
- list engagement facts
- prepare questions for an adviser
- track whether a status check has been completed
- record who made the decision
- record the date of review
- keep evidence linked to the workflow
- mark the item `in review` until confirmed

## What The OS Must Not Do

The OS must not:

- decide whether someone is inside or outside IR35
- rewrite contracts to avoid IR35
- advise on tax treatment
- advise on employment law status
- tell the client a role is compliant
- replace HMRC CEST or qualified professional advice

## Tracker Format

Use this table where relevant:

| Worker / Supplier | Engagement Type | Workflow | IR35 Risk Flag | Status Check Completed | Evidence Location | Owner | State |
|---|---|---|---|---|---|---|---|

## State Rule

If IR35 may apply and no status check is recorded, mark the workflow:

```text
in review
```

Do not mark it `locked` until the client confirms the status decision has been handled outside the OS.
