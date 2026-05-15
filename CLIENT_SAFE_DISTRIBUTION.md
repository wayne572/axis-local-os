# Client-Safe Distribution

Status: active spec, updated 2026-05-11
Purpose: Define how to create a client-safe AXIS / Client OS copy without exposing Wayne's internal operating system, private strategy, prompts, logs, pricing review notes, or unrelated client data.

## Core Principle

Client distributions are generated from approved templates. They are not edited directly as the master source.

When the active system changes, regenerate or update the client copy from the approved template and run the client-safe checklist again.

## Active Source Paths

Current Codex optimisation copy:

`D:\Axis AI - ChatGPT OS\AXIS_OS_CODEX_CURRENT`

Master OS after reviewed sync:

`D:\Wayne AI OS\Axis OS_v3`

Current template pointers:

`PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/CURRENT_TEMPLATE_POINTERS.md`

Client version checklist:

`PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/CLIENT_VERSION_GENERATOR_CHECKLIST.md`

## Current Client Build Sources

Use the canonical templates in:

| Use Case | Source |
|---|---|
| Solo Operator OS | `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/LATEST_SELLABLE_BUILDS/01_SOLO_OPERATOR_OS_TEMPLATE_CLAUDE` |
| Client OS Build And Handover | `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/LATEST_SELLABLE_BUILDS/02_CLIENT_OS_BUILD_TEMPLATE_CLAUDE` |

Do not create new client builds from shipped folders, old live tests, duplicate ZIPs, or `_NOT_IN_USE_BUILDS_ARCHIVE_2026-05-09`.

## Platform Confirmation Rule

Before creating or packaging a client build, ask Wayne:

```text
Which platform will this client build run on first: Claude, ChatGPT, Codex, Telegram, WhatsApp, or another environment?
```

Then use the correct instruction layer:

| Platform | Instruction File / Layer |
|---|---|
| Claude | `CLAUDE.md` |
| Codex | `AGENTS.md` or `CODEX.md` |
| ChatGPT | Custom instructions / project instructions |
| Telegram | Channel access instructions and support boundary |
| WhatsApp | Channel access instructions and support boundary |

Telegram and WhatsApp must be described as planned or configured access channels only when they are actually built. Do not promise automation that has not been tested.

## Include Only Client-Relevant Files

Allowed content:

- client `README.md`
- client `START_HERE.md`
- platform-appropriate instruction file
- client workflow files
- client trackers
- client decision log
- client session log
- client usage notice if tracking is enabled
- human review policy
- data and usage boundaries
- AI risk register where relevant
- 30-day review file
- handover checklist
- client user guide
- client-specific context supplied by that client

## Governance Files To Include When Relevant

Use these where the client workflow touches AI use, personal data, staff, customers, guests, relationship memory, analytics, or usage tracking:

- `PROJECTS/SFW_PROJECT_SOLUTIONS/compliance/CLIENT_AI_GOVERNANCE_PACK/`
- `PROJECTS/SFW_PROJECT_SOLUTIONS/compliance/USAGE_TRACKING_POLICY_FOR_CLIENTS.md`
- `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/LATEST_SELLABLE_BUILDS/02_CLIENT_OS_BUILD_TEMPLATE_CLAUDE/COMPLIANCE/USAGE_TRACKING_NOTICE.md`
- `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/LATEST_SELLABLE_BUILDS/02_CLIENT_OS_BUILD_TEMPLATE_CLAUDE/COMPLIANCE/CLIENT_CONSENT_AND_ANALYTICS.md`
- human review policy / boundary notes included in the client template

## Exclude Always

Never include:

- Wayne's internal `CLAUDE.md`
- Wayne's internal `CODEX.md`
- `.claude/agents/`
- `business/EXECUTION_TRACKER.md`
- `business/DEAL_LOG.md`
- `business/PIPELINE.md`
- `business/ACTIVE_CLIENTS.md`
- `business/TRACKING/ACTIVE_WORKSTREAMS.md`
- `business/PRICING_AND_LEGAL_REVIEW_2026-05.md`
- Wayne's internal pricing review notes
- Wayne's lead generation strategy
- `ARCHIVE_NOTES/`
- `TESTING/`
- `TRACKER/`
- `SYNC_STATUS.md`
- `OPTIMISATION_SCAN_REPORT_2026-05-11.md`
- hidden system prompts
- internal DCoS source files unless rewritten as client-safe guidance
- Black Map material
- Hermes material
- unrelated client/test data
- API keys, tokens, passwords, credentials, or private account details

## Pricing Check

Before sending any client-facing file:

1. Check `business/PRICING_AUTHORITY.md`.
2. Remove superseded pricing.
3. Mark custom pricing as Wayne-approved.
4. Do not use old v2/v2.1 prices.
5. Do not quote Relationship Connector Mode as a separate old quarterly price; use current OS Care Plan positioning unless Wayne approves otherwise.

## Legal And Compliance Boundary

Client-facing compliance files are operational support, not legal advice.

For any client copy:

- include human review expectations
- include data boundaries
- include consent wording if usage tracking or relationship memory is enabled
- avoid guaranteed ROI, guaranteed bookings, guaranteed monetisation, or guaranteed revenue wording
- flag high-risk use cases before proceeding

## Build Process

1. Confirm client name, scope, target platform, and approved source template.
2. Copy only the relevant template and client-specific files.
3. Remove internal Wayne material.
4. Add client-specific context.
5. Add governance files where relevant.
6. Run pricing check.
7. Run client-safe exclusion check.
8. Run functional test.
9. Mark the build `in review`.
10. Lock only after Wayne signs off.

## Functional Test

Open the client copy and test:

```text
Read START_HERE.md and confirm what this Client OS is for.
```

Then test:

```text
Status
```

```text
Next action
```

```text
Review this workflow
```

If included:

```text
Run relationship pulse
```

## Failure Conditions

Stop the build if:

- any excluded file is present
- archive/test data is included
- another client's data is included
- old pricing appears
- usage tracking lacks consent wording
- the platform instruction file is wrong
- the client copy references Wayne's internal OS as if the client owns it
- the build makes unmeasured ROI or revenue guarantees

## Current Status

Spec updated against the current Client OS template on 2026-05-11.

Next required action:

Run one fake client distribution test and record it in `TESTING/LIVE_TEST_RESULTS_2026-05.md`.

