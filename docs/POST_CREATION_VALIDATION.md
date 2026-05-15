# POST CREATION VALIDATION PROMPT

## PURPOSE

This prompt is used immediately after any file is created within Axis OS.

It verifies that the file complies with:
- system architecture rules
- pricing neutrality
- correct placement
- activation logic
- logging consistency

---

## USAGE

Run this prompt after creating or updating any system file.

Provide:
- File path
- File content

---

## PROMPT

You are validating a newly created Axis OS file.

Your task is to confirm whether the file passes all required system checks.

---

### INPUT

File Path:
{{FILE_PATH}}

File Content:
{{FILE_CONTENT}}

---

### VALIDATION CHECKS

1. Path Validation
- Confirm the file exists at the correct path
- Confirm it is NOT placed inside CLIENTS/ unless explicitly required

2. Pricing Neutrality
- Confirm NO pricing language exists
- This includes:
  - prices
  - fees
  - packages
  - implied pricing structures

If found, mark as FAIL

3. Duplication Check
- Confirm the file is NOT duplicated inside CLIENTS/
- Confirm it exists only in its intended system location

4. Activation State (if applicable)
- If the file is an Optional OS:
  - Confirm default state is OFF
  - Confirm activation requires onboarding trigger

5. Logging Consistency (if applicable)
- If ACQUISITION_LOG or similar logs are referenced:
  - Confirm path = TRACKER/<LOG_NAME>.md
  - Confirm append-only structure is implied or stated
  - Confirm NO pricing or revenue fields exist

---

### OUTPUT FORMAT

Return:

STATUS: PASS / FAIL

DETAILS:

- Path: PASS / FAIL
- Pricing Neutrality: PASS / FAIL
- Duplication: PASS / FAIL
- Activation State: PASS / FAIL / N/A
- Logging Consistency: PASS / FAIL / N/A

ISSUES:

- List any violations clearly
- Reference exact lines or sections where possible

---

### RULES

- Be strict
- Do not assume compliance
- If uncertain → mark as FAIL
- Do not fix the file
- Only validate
