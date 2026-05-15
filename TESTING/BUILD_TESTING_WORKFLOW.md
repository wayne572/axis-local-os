# BUILD_TESTING_WORKFLOW.md

## 1. Status
Active - Build Testing Rule

---

## 2. Purpose
This file defines how file and logic testing must happen throughout the Axis AI v4 build.

The goal is to:

- catch issues early
- prevent system drift
- avoid broken logic
- maintain consistency
- ensure all components work together

Testing is continuous, not delayed.

---

## 3. Core Principle

Testing happens during the build, not at the end.

Every part of the system must be:

- checked
- validated
- aligned

before moving forward.

---

## 4. Test Ownership (NEW)

Claude is responsible for:

- triggering tests
- coordinating test execution
- validating results
- deciding whether to proceed

DCoS systems support testing by:

- generating test outputs
- reviewing files
- identifying issues

Claude always controls the final decision.

---

## 5. What Must Be Tested

Every test cycle must check:

- file completeness
- file location
- naming consistency
- logic consistency
- rule alignment
- duplicate or conflicting rules
- missing dependencies
- broken handoffs
- Specialist OS activation rules
- DCoS parity
- Claude routing logic
- memory rules
- validation rules

---

## 6. Testing Frequency

Testing must occur:

- after every 3-5 new files
- after any core rule change
- after any Claude file change
- after any DCoS file change
- before adding a Specialist OS
- before completing a build phase

Testing is mandatory at these checkpoints.

---

## 7. Test Modes (NEW)

### A. Light Test
Used during rapid build.

Checks:
- file completeness
- naming
- structure
- basic logic alignment

---

### B. Full System Test
Used at key checkpoints.

Checks:
- full Claude flow
- DCoS parity
- memory behaviour
- validation engine
- Specialist OS rules
- full execution path

---

Claude must choose the correct test mode based on task importance.

---

## 8. File Test Checklist

Each file must be checked for:

- correct file name
- correct folder location
- full file present
- replacement-ready format
- no missing sections
- no partial patches
- follows FILE_OUTPUT_STANDARD.md

If any check fails:

-> file must be corrected immediately

---

## 9. Logic Test Checklist

System logic must be checked for:

- no contradictions between files
- no bypass of Claude
- no bypass of validation
- no silent Specialist OS activation
- no conflict between ChatGPT DCoS and Claude DCoS
- no memory misuse
- no unclear next steps
- no broken execution flow

If any issue exists:

-> logic must be fixed before continuing

---

## 10. DCoS Parity Test

Both DCoS systems must be checked for:

- matching file categories
- shared rule alignment
- intentional differences only
- no missing logic on either side
- consistent structure

If parity is broken:

-> rebuild alignment before proceeding

---

## 11. Claude Flow Test

Test the full system flow:

User request
-> Claude interprets
-> routes correctly
-> structures task
-> hands off
-> receives output
-> validates
-> assembles response
-> returns final output

If any step is unclear or broken:

-> system fails test

---

## 12. Specialist OS Test

Each Specialist OS must be tested for:

- OFF by default
- user-approved activation only
- clear purpose
- no scope creep
- safe deactivation
- no interference with Claude core rules

---

## 13. Memory Test

Memory system must be checked for:

- only useful information stored
- no irrelevant memory
- no outdated memory reused incorrectly
- corrections properly captured
- structured format maintained

---

## 14. Validation Test

Every test cycle must confirm:

OUTPUT_VALIDATION_ENGINE.md is:

- applied correctly
- not bypassed
- still aligned with system outputs

---

## 15. Test Output Format

Each test must produce:

- Test Name
- Files Checked
- Test Type (Light / Full)
- Result: PASS / FAIL
- Issues Found
- Required Fixes
- Next Action
- Timestamp

This ensures traceability and consistency.

---

## 16. Test Tracking Rule (NEW)

Claude should track:

- last test run
- last test result
- unresolved issues

This prevents:

- repeated mistakes
- silent failures
- forgotten issues

---

## 17. Failure Rule

If any test fails:

- stop new file creation
- fix the issue immediately
- return the full corrected file
- re-run the test
- only continue once passed

No progress is allowed on a failing system.

---

## 18. Build Phase Gate

A build phase is complete only when:

- all required files exist
- all tests pass
- all logic is aligned
- all handoffs are clear
- no critical issues remain

---

## 19. End State

The build testing workflow is working when:

- the system stays clean as it grows
- files remain consistent
- logic remains aligned
- new features integrate smoothly
- no major fixes are needed later

Axis AI v4 becomes:

- stable
- scalable
- reliable
