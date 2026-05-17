# DCOS_INTERACTION_PROTOCOL.md

## 1. Status
Active - DCoS Collaboration Layer

---

## 2. Purpose
This file defines how ChatGPT DCoS and Claude DCoS interact during execution.

It is the rulebook for collaboration between the two DCoS systems and ensures they work together cleanly under Hermes control.

---

## 3. Core Principle

ChatGPT DCoS builds.
Claude DCoS reviews.
Hermes controls both.

No overlap. No confusion.

---

## 4. Role Separation

### ChatGPT DCoS
Responsible for:
- creating files
- generating workflows
- producing structured outputs
- building implementation-ready assets

### Claude DCoS
Responsible for:
- reviewing outputs
- detecting risks
- checking logic
- improving clarity and consistency

---

## 5. Interaction Flow

Hermes -> ChatGPT DCoS -> Claude DCoS -> Hermes -> Validation -> Final Response

The user only sees Hermes. Every step in between is invisible.

---

## 6. Build-Review Loop

When both DCoS systems are used:

1. Hermes structures the task
2. Hermes sends the build task to ChatGPT DCoS
3. ChatGPT DCoS returns a complete output
4. Hermes sends the output to Claude DCoS for review
5. Claude DCoS returns structured feedback or a full revised file
6. Hermes merges and resolves any issues
7. Hermes runs validation
8. Hermes returns the final response

---

## 7. Review Output Types

Claude DCoS may return:

- structured feedback
- risk notes
- correction notes
- full revised file if requested

If a full revised file is returned, it must follow FILE_OUTPUT_STANDARD.md.

---

## 8. Conflict Resolution

If ChatGPT DCoS and Claude DCoS conflict:

Hermes must:
- identify the conflict
- choose the safer and clearer path
- preserve system rules
- avoid exposing internal disagreement to the user

Claude feedback should be considered, but not blindly applied.

---

## 9. Single Voice Rule

The final output must feel like one system.

The user must not see:
- multiple voices
- internal disagreement
- fragmented outputs
- unresolved contradictions

---

## 10. Iteration Control

Hermes must prevent endless review loops.

Maximum:
2 build-review iterations per task.

If unresolved after 2 iterations:
- simplify the task
- ask the user for clarification
- or pause the task

---

## 11. Scope Control

Both DCoS systems must stay inside their assigned task.

They must not:
- expand scope
- introduce unrelated ideas
- redesign the system unless explicitly instructed
- activate Specialist OS modules

---

## 12. Validation Requirement

After DCoS interaction, Hermes must run:

AXIS_AI_v4/CORE/VALIDATION/OUTPUT_VALIDATION_ENGINE.md

No output reaches the user without validation.

---

## 13. Specialist OS Interaction

If a Specialist OS is involved:

- Hermes must activate it first with user approval
- ChatGPT DCoS may build within the active Specialist OS scope
- Claude DCoS may review within the active Specialist OS scope

Neither DCoS may activate a Specialist OS.

---

## 14. Folder Path Rule

The canonical DCoS folder path is:

AXIS_AI_v4/CORE/DCoS/

All DCoS references must use this exact folder casing.

Do not use:

AXIS_AI_v4/CORE/DCOS/

---

## 15. Failure Conditions

The DCoS interaction has failed if:

- roles overlap
- Claude builds without instruction
- ChatGPT reviews as final authority
- Hermes is bypassed
- validation is skipped
- outputs conflict without resolution
- the final answer feels fragmented
- incorrect folder casing causes broken references

---

## 16. Recovery Rule

If failure occurs:

1. Hermes pauses
2. identifies the issue
3. fixes the dependency or role conflict
4. reruns the relevant test
5. continues only after PASS

---

## 17. End State

The DCoS interaction layer is working when:

- ChatGPT DCoS builds clean outputs
- Claude DCoS improves quality
- Hermes controls the process
- validation runs before final delivery
- the user receives one clear final result

The process is invisible.
The output is consistent.
The system feels unified.
