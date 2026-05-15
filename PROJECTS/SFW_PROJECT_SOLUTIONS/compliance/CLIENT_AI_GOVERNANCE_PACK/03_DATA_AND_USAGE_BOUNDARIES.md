# Data And Usage Boundaries

Status: client-facing draft
Purpose: Define what data should and should not be used in the Client OS.

## Data Principle

Use the minimum information needed to complete the task.

## Usually Safe To Include

- business process notes
- workflow steps
- public company information
- non-sensitive project notes
- general client communication drafts
- internal task lists
- meeting summaries with no sensitive details

## Be Careful With

- names and contact details
- personal circumstances
- HR information
- financial details
- health information
- safeguarding information
- legal disputes
- complaints
- confidential commercial information

## Do Not Include Unless Approved

- special-category personal data
- criminal offence data
- medical details
- biometric data
- children's data
- passwords
- API keys
- bank details
- full identity documents

## Usage Tracking Boundary

Usage tracking should focus on system improvement, not surveillance.

Appropriate usage tracking:

- which workflows are used
- where users get stuck
- which templates need improvement
- what outcomes are being measured

Avoid tracking:

- private personal notes without consent
- sensitive employee behaviour
- hidden monitoring
- unnecessary personal detail

## Deletion And Correction

If data is wrong, outdated, or no longer needed, it should be corrected or removed from the active Client OS.

## Prompt To Use

```text
Review this data before I add it to the Client OS. Tell me what should be removed, anonymised, or handled carefully.
```
