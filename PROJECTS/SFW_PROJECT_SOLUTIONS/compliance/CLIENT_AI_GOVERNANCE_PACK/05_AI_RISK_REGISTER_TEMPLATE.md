# AI Risk Register Template

Status: client-facing draft
Purpose: Simple register for AI-related risks, controls, and review actions.

## Risk Register

| ID | Risk | Area | Likelihood | Impact | Control | Owner | Status | Review Date |
|---|---|---|---|---|---|---|---|---|
| R001 | AI output used without review | Human review | medium | high | Human Review Policy | | active | |
| R002 | Sensitive data added unnecessarily | Data protection | medium | high | Data And Usage Boundaries | | active | |
| R003 | Old or wrong information used | Accuracy | medium | medium | Regular context review | | active | |
| R004 | Client expects automation that was not scoped | Delivery | medium | medium | Scope and handover review | | active | |
| R005 | Usage tracking feels like monitoring | Trust | low/medium | high | Consent checklist and clear notice | | active | |

## Risk Ratings

Likelihood:

- low
- medium
- high

Impact:

- low
- medium
- high

Status:

- active
- in review
- controlled
- closed

## Review Prompt

```text
Review this Client OS against the AI Risk Register. Identify new risks, weak controls, and the next action to reduce risk.
```
