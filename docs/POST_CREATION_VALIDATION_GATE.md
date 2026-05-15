# POST-CREATION VALIDATION GATE (MANDATORY)

## PURPOSE

Ensure that every file created within Axis OS is:

- structurally correct
- pricing-neutral
- correctly placed
- activation-compliant
- logging-consistent

This gate prevents invalid system components from entering the OS.

---

## TRIGGER

This validation MUST run immediately after:

- any new file creation
- any file overwrite or version upgrade

---

## EXECUTION

DCoS must:

1. Call:
   `Axis OS_v3/docs/POST_CREATION_VALIDATION.md` (the validator prompt)

2. Provide:
   - FILE_PATH
   - FILE_CONTENT

---

## DECISION LOGIC

If STATUS = PASS:

→ File is accepted
→ System execution continues

If STATUS = FAIL:

→ File is rejected
→ Execution HALTS immediately

---

## FAILURE HANDLING

On FAIL:

DCoS must:

1. Output validation results
2. Highlight violations
3. Block downstream steps
4. Require correction before retry

No automatic fixes allowed.

---

## ENFORCEMENT RULES

- This gate is NON-BYPASSABLE
- Applies to ALL system files (core + optional OS)
- Applies regardless of phase (build, harvest, update)

---

## SYSTEM IMPACT

Prevents:

- pricing contamination
- incorrect file placement
- duplicate structures
- invalid activation states
- broken logging schemas

---

## INTEGRATION NOTE

This gate operates BEFORE:

- Archivist recording
- System progression
- Any downstream agent execution
