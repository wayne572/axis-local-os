# Axis Core Loop

Status: active - v4 operating spine
Purpose: Define how every meaningful Axis task moves from intake to outcome.

## Core Principle

Every task must move through one controlled loop.

```text
Intake
-> classify
-> retrieve context
-> choose mode
-> apply specialist support if needed
-> produce output or plan
-> validate
-> update tracker if work state changed
-> propose memory update if durable learning exists
```

The loop must stay visible enough for governance and simple enough for Wayne to use without managing the machinery.

## Lifecycle Stages

Every work item is in one lifecycle state:

| State | Meaning | Rule |
|---|---|---|
| active | Work is live or being shaped | Requires owner and next action |
| in review | Output, commitment, or decision needs checking | Cannot be treated as locked |
| locked | Shipped, signed off, or current authority | Supersede instead of casual editing |
| archived | Retained for history only | Not active authority unless explicitly revived |

## Handoffs

Handoffs must be structured, not casual.

Each handoff includes:

- objective
- current lifecycle state
- owner
- relevant context
- output required
- validation required
- next action
- blocker or risk, if any

## Governance Checkpoints

Run governance checks when a task affects:

- pricing
- legal wording
- compliance
- client commitments
- public positioning
- external communications
- memory authority
- Precision Alpha financial research
- system architecture

If a checkpoint is triggered, route to `REVIEW` before locking.

## Memory Update Timing

Memory updates happen only after useful learning is identified.

Memory may be proposed after:

- a decision is made
- a repeated pattern is confirmed
- Wayne corrects the system
- a workflow produces a reusable lesson
- a client or project state changes

Memory must not be updated just because a conversation happened.

## Failure Conditions

The core loop fails if:

- work has no lifecycle state
- a client-facing output bypasses review
- a tracker-changing task is not tracked
- memory is updated without durable value
- specialist playbooks conflict
- Wayne receives fragmented internal routing instead of one clear answer

## Success Condition

Axis OS v4 is working when Wayne can give a messy real-world request and receive:

- the right mode
- the right context
- a usable output
- clear validation
- tracked next action
- memory update only when useful
