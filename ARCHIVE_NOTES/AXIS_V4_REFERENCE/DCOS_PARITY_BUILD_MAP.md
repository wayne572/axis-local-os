# DCoS_PARITY_BUILD_MAP.md

## 1. Status
Active - DCoS Build Control Layer

---

## 2. Purpose
This file ensures both ChatGPT DCoS and Claude DCoS are:

- built together
- aligned structurally
- consistent in behaviour
- complete with no missing components

It is the master control file for the DCoS layer inside Axis AI v4.

---

## 3. Core Principle

Both DCoS systems must:

- follow the same structure
- serve the same purpose
- operate under Hermes control
- never act as user interfaces

They are execution engines only.

---

## 4. System Roles

### ChatGPT DCoS Role
- builder
- generator
- system creator
- structured output producer

### Claude DCoS Role
- critic
- reviewer
- logic checker
- risk identifier
- consistency validator

---

## 5. Shared Behaviour Rules

Both DCoS systems must:

- follow SOLO_USER_EXPERIENCE.md
- follow HERMES_CONVERSATION_ENGINE.md
- follow HERMES_ROUTING_ENGINE.md
- follow MEMORY_OPERATING_SYSTEM.md
- follow OUTPUT_VALIDATION_ENGINE.md
- follow FILE_OUTPUT_STANDARD.md

They must:
- return full files
- be clear and structured
- provide actionable outputs
- never expose internal system complexity

---

## 6. Structural Parity Rule

Both DCoS systems must contain the same file categories.

Required files for BOTH:

- SYSTEM_PROMPT.md
- TASK_ROLE.md
- OUTPUT_RULES.md
- LIMITS.md

No system is considered complete unless both sides have matching files.

---

## 7. Directory Structure

```
AXIS_AI_v4/CORE/DCoS/
|
+-- DCoS_PARITY_BUILD_MAP.md
|
+-- CHATGPT_DCoS/
|   +-- CHATGPT_DCOS_SYSTEM_PROMPT.md
|   +-- CHATGPT_DCOS_TASK_ROLE.md
|   +-- CHATGPT_DCOS_OUTPUT_RULES.md
|   +-- CHATGPT_DCOS_LIMITS.md
|
+-- CLAUDE_DCoS/
    +-- CLAUDE_DCOS_SYSTEM_PROMPT.md
    +-- CLAUDE_DCOS_TASK_ROLE.md
    +-- CLAUDE_DCOS_OUTPUT_RULES.md
    +-- CLAUDE_DCOS_LIMITS.md
```

---

## 8. Build Synchronisation Rule

Whenever a file is created for one DCoS:

-> the equivalent file MUST be created for the other

Example:

If:
CHATGPT_DCOS_SYSTEM_PROMPT.md is created

Then:
CLAUDE_DCOS_SYSTEM_PROMPT.md must also be created

---

## 9. Update Synchronisation Rule

Whenever a file is updated:

- both versions must be reviewed
- both must be aligned structurally
- differences must be intentional, not accidental

---

## 10. Difference Control Rule

Differences between ChatGPT and Claude DCoS must be:

- intentional
- documented
- role-based

Allowed differences:

- tone
- depth of analysis
- response style
- task emphasis

Not allowed:

- missing logic
- missing sections
- inconsistent rules

---

## 11. Task Routing Relationship

Hermes decides:

- which DCoS handles the task
- when both are used
- when outputs are merged

DCoS systems do NOT decide routing.

---

## 12. Output Merge Rule

If both DCoS systems are used:

Hermes must:

- combine outputs
- remove duplication
- resolve conflicts
- present one unified response

The user must never see:

- conflicting outputs
- multiple voices
- system-level complexity

---

## 13. Failure Conditions

The DCoS system has failed if:

- one DCoS has missing files
- structure is inconsistent
- outputs contradict each other
- roles overlap incorrectly
- Hermes routing is bypassed

---

## 14. Validation Rule

Before considering DCoS build complete:

Check:

- all required files exist for both systems
- structure is identical
- differences are intentional
- outputs follow validation rules

---

## 15. End State

The DCoS layer is working when:

- ChatGPT builds effectively
- Claude critiques effectively
- Hermes controls both
- outputs are consistent and reliable
- the user experiences one seamless system
