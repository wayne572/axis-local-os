# Axis Infrastructure Layer

Status: active - Axis OS v4 core layer
Owner: Wayne Francis
Purpose: Make the operating spine of Axis explicit, testable, and reusable.

## Why This Exists

Axis OS v4 is not a chatbot, prompt library, or random agent collection.

It is governed operational infrastructure:

- a core operating loop
- structured memory
- controlled specialist roles
- governance checkpoints
- one complete workflow from idea to execution to reflection

This folder consolidates behaviour that already existed across v3 and the AXIS AI v4 reference build, then adds the missing connective tissue.

## Canonical Files

Read these in order when reviewing or changing the core operating model:

1. `AXIS_CORE_LOOP.md`
2. `AXIS_MEMORY_ARCHITECTURE.md`
3. `AXIS_AGENT_SYSTEM.md`
4. `AXIS_GOVERNANCE_LAYER.md`
5. `AXIS_MVP_WORKFLOW_IDEA_TO_MEMORY.md`

## Relationship To Existing Files

This layer does not replace:

- `CLAUDE.md`
- `START_HERE.md`
- `CORE/DCoS/DCOS_COMMAND_LAYER.md`
- `CORE/SPECIALIST_OS/`
- `CORE/GOVERNANCE/`
- `CORE/VALIDATION/`

It sits above them as the plain-English operating map.

## Build Rule

Do not add new agent modules, product lanes, or automation layers until the core loop remains clear and one complete workflow still works end to end.
