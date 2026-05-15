# BUILD_PHASE_TRACKER.md

## 1. Status
Active - Build Tracking Layer

---

## 2. Purpose
This file tracks Axis AI v4 build progress across phases so no files, dependencies, or validation steps are missed.

It is the live record of what has been built, what has been tested, and what remains.

---

## 3. Core Principle

No phase is complete unless:

- all required files exist
- dependencies resolve
- tests pass
- no critical issues remain

---

## 4. Phase Structure

The Axis AI v4 build runs in controlled phases:

- Phase 1 - UX + Build Rules
- Phase 2 - Claude Core
- Phase 3 - DCoS Layer
- Phase 4 - Governance + Testing
- Phase 5 - Specialist OS Modules
- Phase 6 - Integration + Live Testing
- Phase 7 - Deployment Preparation

---

## 5. Phase Tracking Table

| Phase | Purpose | Required Files | Status | Test Status |
|---|---|---|---|---|
| Phase 1 - UX + Build Rules | Define how the system feels and how files are produced | SOLO_USER_EXPERIENCE.md, USER_MODE_LAYER.md, FILE_OUTPUT_STANDARD.md | Complete | Light Test PASS |
| Phase 2 - Claude Core | Build the user-facing interface layer | CLAUDE_OPERATOR_CONVERSATION_ENGINE, CLAUDE_OPERATOR_ROUTING_ENGINE, CLAUDE_OPERATOR_SPECIALIST_OS_ACTIVATION, CLAUDE_OPERATOR_TASK_HANDOFF_PROTOCOL, CLAUDE_OPERATOR_RESPONSE_ASSEMBLY, MEMORY_OPERATING_SYSTEM | Complete | Light Test PASS, Validation Integration Test PASS |
| Phase 3 - DCoS Layer | Build silent execution layer (ChatGPT + Claude DCoS) | DCoS_PARITY_BUILD_MAP, DCOS_INTERACTION_PROTOCOL, 4 ChatGPT DCoS files, 4 Claude DCoS files | Complete | FULL DCOS SYSTEM TEST - RUN 2 PASS |
| Phase 4 - Governance + Testing | Lock rules, hierarchy, validation, test workflow | SYSTEM_RULE_HIERARCHY, SPECIALIST_OS_CONTROL_LAYER, BUILD_PHASE_TRACKER, OUTPUT_VALIDATION_ENGINE, BUILD_TESTING_WORKFLOW, CLAUDE_OPERATOR_CORE_TESTING_WORKFLOW, SYSTEM_INTEGRATION_TEST | In Progress | Pending re-run after BUILD_PHASE_TRACKER resolved |
| Phase 5 - Specialist OS Modules | Build domain-focused modules | DEAL_SOURCING_OS (complete), Sales OS (planned), Marketing OS (planned), Client Delivery OS (planned), Precision Alpha OS (active specialist) | In Progress | Deal Sourcing OS - Integration scenarios PASS |
| Phase 6 - Integration + Live Testing | Run live behaviour tests across the full system | DEAL_SOURCING_LIVE_TEST, future live tests | Not Started | - |
| Phase 7 - Deployment Preparation | Prepare for real-world rollout | TBD | Not Started | - |

---

## 6. File Tracking Rule

Every build file must be:

- listed under a phase
- marked complete only when saved
- marked valid only after passing the relevant tests

If a file is built but not tested, the phase remains "In Progress."

---

## 7. Dependency Rule

If a file is referenced by another file or test, it must exist.

If a required file is missing:

- stop new build work
- create the missing file
- rerun the relevant test

This rule is non-negotiable.

---

## 8. Testing Requirement

Before marking any phase complete:

- run the relevant test from BUILD_TESTING_WORKFLOW.md
- confirm PASS
- record the result in the tracking table

If FAIL:

- the phase remains incomplete
- fixes are applied
- the test is re-run

---

## 9. Progress Control Rule

Claude must check this tracker before suggesting new build files.

Claude must prevent:

- duplicate work
- skipped dependencies
- phase jumps without test approval

If a phase has unresolved issues, no later phase may advance.

---

## 10. Phase Completion Rule

A phase is complete only when:

- all required files are saved
- all dependencies resolve
- relevant tests pass
- no unresolved critical issues remain

The phase status moves to "Complete" only after the test status confirms PASS.

---

## 11. Current Build State

Snapshot at this point:

- Core UX created (SOLO_USER_EXPERIENCE.md, USER_MODE_LAYER.md)
- Claude Core created and validated
- DCoS layer created and passed FULL DCOS SYSTEM TEST - RUN 2
- Deal Sourcing OS created, consolidated to one-concept-one-file
- System Integration Test scenarios passed behaviour checks
- BUILD_PHASE_TRACKER now resolves the missing dependency that surfaced during integration testing
- Phase 4 (Governance + Testing) ready to be re-tested for completion

---

## 12. Failure Conditions

The tracker has failed if:

- files are missing but a phase is marked complete
- tests are skipped
- phases are skipped out of order
- duplicate files are created
- broken dependencies are ignored
- the tracker is not updated after a build or test event

---

## 13. End State

The tracker is working when:

- build progress is visible at a glance
- missing dependencies are caught early
- phases are controlled and ordered
- no work is duplicated
- Axis AI v4 grows cleanly, phase by phase, test by test
