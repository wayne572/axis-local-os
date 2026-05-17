# Agent Freeze Protocol

Status: template
Purpose: Pause a client AI workflow when quality, safety, scope, permission, or data risk appears.

## Freeze Triggers

Freeze a workflow if:

- it produces incorrect or risky output twice
- it touches data outside agreed client scope
- it creates client-facing communication without required approval
- it makes or implies legal, tax, HR, safeguarding, medical, or regulated advice
- a user reports loss of trust
- permissions, tools, data sources, or connected systems changed unexpectedly
- the workflow no longer matches signed scope

## Freeze Steps

1. Mark the workflow status as `frozen` in `GOVERNANCE/AI_OS_CONTROL_REGISTER.md`.
2. Record the issue in `BUSINESS/TRACKING/DECISION_LOG.md` or the relevant workstream.
3. Stop using the workflow for live client decisions.
4. Review the instruction, memory source, workflow file, permissions, and recent outputs.
5. Define the fix and acceptance test.
6. Restart only after client owner or SF&W owner approval.

## Restart Checklist

- [ ] Cause identified
- [ ] Fix applied
- [ ] Test prompt passed
- [ ] Memory checked
- [ ] Data boundary checked
- [ ] Owner approved restart
- [ ] Control register updated

