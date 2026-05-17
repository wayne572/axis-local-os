# Agent Freeze Protocol

Status: template
Purpose: Pause an AI workflow when quality, safety, scope, or data risk appears.

## Freeze Triggers

Freeze a workflow if:

- it produces incorrect or risky output twice
- it touches data outside agreed scope
- it makes or implies legal, tax, medical, HR, safeguarding, or regulated advice
- the user reports loss of trust
- permissions, tools, or connected systems changed unexpectedly
- the workflow is no longer aligned with the user's goals

## Freeze Steps

1. Mark the workflow status as `frozen` in `GOVERNANCE/AI_OS_CONTROL_REGISTER.md`.
2. Record the issue in the relevant tracker or decision log.
3. Stop using the workflow for live decisions.
4. Review the instruction, memory source, workflow file, and recent outputs.
5. Define the fix and acceptance test.
6. Restart only after the user approves.

## Restart Checklist

- [ ] Cause identified
- [ ] Fix applied
- [ ] Test prompt passed
- [ ] Memory checked
- [ ] User approved restart
- [ ] Control register updated

