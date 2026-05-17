# FILE_OUTPUT_STANDARD.md

## 1. Status
Active - Build Rule (Non-Negotiable)

---

## 2. Purpose
This file defines the standard for how all files are created and updated during the Axis AI v4 build.

The goal is to prevent:
- partial updates
- fragmented logic
- missing sections
- inconsistent versions

---

## 3. Core Rule

Every time a file is created or updated:

The FULL file must be returned.

Never return:
- partial edits
- patches only
- "add this section" instructions without the full file

---

## 4. Why This Rule Exists

Partial updates create:

- version confusion
- missing logic
- broken system flow
- inconsistent structure

Returning the full file ensures:

- clarity
- reliability
- easy copy/paste
- consistent system state

---

## 5. Application Scope

This rule applies to ALL files:

- CORE files
- HERMES files
- UX files
- SPECIALIST OS files
- TRACKER files
- MARKETING files
- ANY future modules

---

## 6. Update Process

When updating a file:

1. Apply the change
2. Rebuild the full file
3. Return the entire updated file
4. Do not assume previous context is preserved

---

## 7. Exception Rule

There are NO exceptions.

Even small changes must return the full file.

---

## 8. Failure Condition

The rule is broken if:

- only part of a file is returned
- instructions are given without full file output
- sections are missing after update

---

## 9. Enforcement

All builders (ChatGPT, Claude, or any future agents) must follow this rule.

If a builder cannot return the full file:

The output is considered incomplete.

---

## 10. File Replacement Rule (NEW)

Every updated file must be clearly presented as a full replacement of the previous version.

The user must be able to:

- copy the file
- paste it directly
- overwrite the existing file completely

There must be NO requirement to:
- merge content manually
- compare versions
- reconstruct missing sections

Each returned file is treated as:

-> The new single source of truth

---

## 11. Output Clarity Rule (NEW)

When a file is returned:

- It must be complete
- It must be clean
- It must be ready to save

No surrounding explanation should be required to understand the file.

The file must stand alone.

---

## 12. End State

Every file in Axis AI v4 can be:

- copied
- pasted
- saved
- versioned

as a complete and final unit, without reconstruction.
