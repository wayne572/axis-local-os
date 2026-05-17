# Functional Test Plan

Status: active
Purpose: Prove the Claude build works as an operating system, not just a folder.

## Test 1 - Session Start

Prompt:
What is the current status?

Expected behaviour:
- Claude reads `CLAUDE.md`
- Claude reads `START_HERE.md`
- Claude reads `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`
- Claude gives a Priority Pulse and next action

Pass condition:
Output names SF&W Project Solutions as the priority and does not route to excluded ventures.

## Test 1A - Claude-First Operator

Prompt:
How does this OS route work?

Expected behaviour:
- Claude explains that Claude is the direct operator.
- Claude explains that Specialist OS files are playbooks.
- Claude does not present Hermes as an active layer.

Pass condition:
Output is simple, direct, and Claude-first.

## Test 2 - Build Mode

Prompt:
Activate BUILD mode for SF&W and build the SME audit checklist.

Expected behaviour:
- Claude reads SF&W context
- Claude reads the SME Audit Funnel
- Claude creates a usable checklist
- Claude marks the asset as draft or in review

Pass condition:
Checklist is practical, SME-wide, and not limited to one sector.

## Test 3 - Lead Mode

Prompt:
Activate LEAD mode and create a 30-minute outreach workflow for SME prospects.

Expected behaviour:
- Claude uses Deal Sourcing OS and Sales OS
- Claude produces a prospecting and outreach flow
- Claude includes compliance and suppression-list awareness

Pass condition:
Output is action-ready and does not overcomplicate sourcing.

## Test 4 - Review Mode

Prompt:
Review the SME AI Audit Funnel and tell me if it is ready to lock.

Expected behaviour:
- Claude uses Output Validation Engine
- Claude checks clarity, completeness, actionability, risks, and missing proof
- Claude gives sign-off or remediation list

Pass condition:
Claude does not lock the file unless proof assets exist.

## Test 5 - Client Delivery

Prompt:
A prospect agreed to the SME Audit. Build the onboarding flow.

Expected behaviour:
- Claude uses Client Delivery OS
- Claude creates onboarding steps, data requirements, timeline, and next action
- Claude flags compliance if personal or client data is involved

Pass condition:
Output is structured and client-ready.

## Test 6 - Exclusion Rule

Prompt:
What should we do next for Black Map?

Expected behaviour:
- Claude states Black Map is excluded from this build
- Claude asks whether Wayne wants to reintroduce it
- Claude does not read or route Black Map files automatically

Pass condition:
Exclusion is respected.

## Test 7 - Access Channel Rule

Prompt:
Can I use this through Telegram or WhatsApp?

Expected behaviour:
- Claude explains that Telegram and WhatsApp are access channels.
- Claude does not create a new operating layer.
- Claude points to `CORE/CLAUDE_OPERATOR/ACCESS_CHANNELS.md`.
- Claude recommends Telegram first, then WhatsApp.

Pass condition:
Channel access is framed as a simple route into the same Claude OS.

## Test 7A - New Client Trigger

Prompt:
AXIS: NEW CLIENT

Expected behaviour:
- Claude switches to BUILD mode.
- Claude recognises this as client OS setup.
- Claude reads the audit-to-client workflow and client OS template instructions.
- Claude asks for missing client setup facts.
- Claude includes the one-time AI PA naming question.
- Claude does not invent client details.

Pass condition:
Claude starts the client setup workflow, includes the AI PA naming step, and lists the missing facts needed to create the client copy.

## Test 8 - Relationship Connector Mode

Prompt:
Met Sarah from a recruitment agency. She is interested in reducing admin and open to practical AI. Follow up next week.

Expected behaviour:
- Claude recognises this as relationship capture.
- Claude asks whether Wayne wants to add Sarah to relationship memory if consent is unclear.
- Claude suggests one next action.
- Claude can draft a follow-up.
- Claude does not invent extra personal details.

Pass condition:
Relationship is captured or held for confirmation, with a clear next action and consent status.

## Test 9 - Intro Consent Gate

Prompt:
Introduce Sarah to James because both work in recruitment.

Expected behaviour:
- Claude does not assume permission.
- Claude drafts an intro request first.
- Claude tracks the intro as `idea` or `ask party`.

Pass condition:
No final intro is drafted as if both sides already agreed.

## Overall Pass Standard

The OS passes if:
- it starts cleanly
- it prioritises SF&W
- it routes correctly
- it validates outputs
- it tracks lifecycle state
- it avoids excluded venture context
- it produces usable assets
- it keeps Claude as the operator
- it treats Telegram and WhatsApp as access channels
- it supports relationship-led communication with consent gates
