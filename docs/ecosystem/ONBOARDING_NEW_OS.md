# Onboarding a New OS into Axis v3

How to plug a new operating system (or new specialist agent) into the v3 ecosystem without breaking the architecture.

## Decide: new layer or new agent in an existing layer?

| If the new OS... | Then... |
|---|---|
| Is the new sole user interface | (no — DCoS is locked as the sole command layer) |
| Adds a new revenue or specialist function | Add as an agent inside an existing layer |
| Adds a whole new domain (e.g. "Recruiting OS", "Finance OS") | Add as a new sub-group inside Thinking layer |
| Adds a new tracker / log | Add the file in `business/` and document in CLAUDE.md storage rules |

## Steps

### 1. Define the agent

Create `.claude/agents/[name].md` with the standard frontmatter:

```
---
name: [name]
description: [one paragraph — what triggers it, what it does, what it doesn't do]
---
```

Body must cover:
- Inputs required
- Outputs structure
- Reject filters (when not to act)
- Hand-offs (which agent picks up next)
- What it does NOT do (boundary statement)

### 2. Add to AGENT_RESOLUTION.md

Add a row to the routing table with:
- Task signal phrase(s)
- Agent name
- Layer

If the new agent chains with others, document the chain rule.

### 3. Create the output store (if needed)

If the new agent produces structured output, create the log file in `business/` and define the schema in the agent definition.

### 4. Update CLAUDE.md

Add the agent to the resolution table in `CLAUDE.md`. Update layer descriptions if a new sub-group is created.

### 5. Update CHANGELOG.md

Log the addition with reason, files added, files modified, and inheritance from existing agents.

### 6. Update DCoS spec

If the new agent introduces new routing logic (e.g. compliance halt for a new high-risk use), update `docs/dcos/DIGITAL_CHIEF_OF_STAFF.md`.

### 7. Test the routing

Run a test message that should trigger the new agent. DCoS should:
- Pick the new agent without ambiguity
- Write a tracker row
- Hand off cleanly
- Receive the output back
- Mark the row done

If routing is ambiguous, refine the task signal phrasing in `AGENT_RESOLUTION.md`.

## What NOT to do

- Don't add an agent that bypasses DCoS — DCoS-first is non-negotiable.
- Don't duplicate an existing specialism — extend the existing agent instead.
- Don't hardcode pricing into the new agent's definition (memory only).
- Don't skip the compliance review — if the new agent could touch high-risk AI, GDPR, or PECR, document the halt rules first.

## Inheritance check

Before shipping the new agent, confirm it inherits:
- UK compliance rules (GDPR / PECR / CAP / EU AI / MLR / Equality)
- Hard limits on high-risk AI uses
- DCoS-first routing
- QA / spec-review enforcement for client-facing or structural work

If any of those don't apply, document the exception explicitly in the agent definition.
