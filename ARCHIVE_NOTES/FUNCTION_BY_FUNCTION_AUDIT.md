# Function By Function Audit

Date: 2026-05-06
Build: AXIS OS Claude Build
Purpose: Confirm that existing functionality is preserved, enhanced, superseded, archived, or excluded.

## Audit Principle

No functionality should be lost.

Every existing function must be:
- preserved
- enhanced
- superseded by a stronger version
- archived as reference
- excluded only by explicit instruction

Black Map is excluded from this Claude build by user instruction. That is an exclusion rule, not deletion.

## Status Definitions

| Status | Meaning |
|---|---|
| Preserve | Keep the function substantially as-is |
| Enhance | Keep the function and improve it |
| Supersede | Replace active use with a stronger version while keeping old source as reference |
| Archive | Keep for reference, not active operation |
| Exclude | Deliberately leave out of this build |

## Executive Summary

The new Claude build preserves the current work OS functions and enhances most of them with AXIS v4 architecture.

Nothing material has been deleted.

Main enhancements:
- stronger Claude entry point
- clearer venture separation
- Claude-first routing
- full Specialist OS modules as playbooks
- stronger validation and testing
- active workstream tracking
- SF&W consultancy revenue layer
- generic SME delivery templates
- Relationship Connector Mode for Boardy-style communication

Main exclusions:
- Black Map context and workflows

Main archives:
- older Axis versions
- old deal-sourcing prototype
- WKS-specific client source files

## Function Audit Table

| Function | Current / Source Location | New Claude Build Location | Status | Notes |
|---|---|---|---|---|
| Session entry | `START_HERE.md`, `CHATGPT_OS.md` | `START_HERE.md`, `CLAUDE.md`, `README.md` | Enhance | Claude now has a native root instruction file and session sequence. |
| Claude compatibility | `D:\Wayne AI OS\CLAUDE.md`, AXIS v4 Claude DCoS files | `CLAUDE.md` | Enhance | Root Claude instructions are now specific to this build and SF&W priority. |
| ChatGPT folder OS behaviour | `CHATGPT_OS.md` | `CLAUDE.md`, `START_HERE.md` | Preserve | The read-order, practical output, and context-light behaviour are retained. |
| DCoS command layer | `docs/dcos/DIGITAL_CHIEF_OF_STAFF.md` | `CORE/DCoS`, `CLAUDE.md` | Enhance | Current DCoS logic preserved and upgraded with AXIS v4 protocols. |
| Orchestrator / routing | `roles/orchestrator.md`, `CHATGPT_OS.md`, AXIS v4 Hermes files | `CORE/CLAUDE_OPERATOR/CLAUDE_OPERATOR_MODEL.md`, `CORE/DCoS/DCOS_COMMAND_LAYER.md` | Enhance | Claude is now the active operator. Hermes is archived as reference only. |
| Fast / Deep mode | `CHATGPT_OS.md` | `CLAUDE.md` mode table | Enhance | Preserved as intent, upgraded into ORCHESTRATE / BUILD / LEAD / LEARN / REVIEW. |
| AXIS operating modes | user-provided AXIS spec | `CLAUDE.md` | Preserve | Modes are included as the main operating frame. |
| Workstream tracking | `projects/*/PROJECT_STATUS.md`, `business/PIPELINE.md` | `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md` | Enhance | New tracker gives lifecycle state, owner, next action, proof, blockers. |
| Lifecycle states | user-provided AXIS spec | `CLAUDE.md`, `ACTIVE_WORKSTREAMS.md` | Preserve | `active`, `in review`, `locked`, `archived` are active rules. |
| Business setup / onboarding | `roles/handover.md`, `roles/onboarding.md`, `business/SETUP_STATUS.md` | `START_HERE.md`, `VENTURE_REGISTRY.md`, future onboarding file needed | Preserve | Basic function preserved, but a dedicated Claude onboarding file should be added later. |
| Venture registry | implicit in business files and prompt | `BUSINESS/VENTURES/VENTURE_REGISTRY.md` | Enhance | Ventures are now separated. Black Map is excluded by rule. |
| SF&W consultancy context | scattered across prompt, `projects/sfw-consultancy`, `D:\Wayne Francis\Axis AI` | `BUSINESS/VENTURES/SFW_PROJECT_SOLUTIONS.md` | Enhance | SF&W now has a dedicated active venture file. |
| Black Map context | `business/OFFERS.md`, `business/WORKFLOWS.md`, Wayne Francis folders | no active location | Exclude | Excluded by user request. Not deleted from source locations. |
| Brand / voice | `business/BRAND.md`, user AXIS tone | `CLAUDE.md` | Preserve | Wayne voice rules are included. A fuller SF&W brand file can be added later. |
| Offer registry | `business/OFFERS.md`, `projects/sfw-consultancy/SME_AI_AUDIT_FUNNEL.md` | `PROJECTS/SFW_PROJECT_SOLUTIONS/offer`, `SFW_PROJECT_SOLUTIONS.md` | Enhance | Current offer is SF&W focused. Black Map offer content excluded. |
| SME AI Audit offer | `projects/sfw-consultancy/SME_AI_AUDIT_FUNNEL.md` | `PROJECTS/SFW_PROJECT_SOLUTIONS/offer/SME_AI_AUDIT_FUNNEL.md` | Preserve | Preserved as front-end consultancy offer. |
| Pipeline-as-a-Service offer | `D:\Wayne Francis\Axis AI\Pipeline-as-a-Service` | `PROJECTS/SFW_PROJECT_SOLUTIONS/offer` and `compliance` | Enhance | Preserved as secondary offer/source asset, not first general offer. |
| Pricing strategy | PaaS files, pricing page source | offer files; pricing not locked | Preserve | Pricing information exists in sources but should remain in review before client use. |
| Deal sourcing | `docs/deal-sourcing`, `projects/deal-sourcing`, AXIS v4 Deal Sourcing OS | `CORE/SPECIALIST_OS/DEAL_SOURCING_OS` | Supersede | AXIS v4 module is stronger and becomes active. Older deal-sourcing docs become reference. |
| 14-day profit sprint | `docs/deal-sourcing/14_DAY_PROFIT_SPRINT.md` | not yet active | Archive | Useful reference but not central to SF&W Claude build. Can be imported later if needed. |
| Lead identification | AXIS v4 Deal Sourcing OS | `DEAL_SOURCING_LEAD_IDENTIFICATION.md` | Enhance | Stronger with PSC filter, source order, compliance gates. |
| ICP definition | AXIS v4 Deal Sourcing OS | `DEAL_SOURCING_ICP.md` | Enhance | Preserved as specialist sub-file. |
| Outreach scripts | `roles/outreach.md`, `projects/deal-sourcing/OUTREACH_SCRIPTS.md`, daily runbook | `CORE/SPECIALIST_OS/SALES_OS`, `PROJECTS/.../outreach` | Enhance | Outreach now has Sales OS plus daily execution source. |
| Daily outreach workflow | `D:\Wayne Francis\Outreach\DAILY_RUNBOOK.md` | `PROJECTS/SFW_PROJECT_SOLUTIONS/outreach/DAILY_OUTREACH_RUNBOOK_SOURCE.md` | Preserve | Preserved as source; should be cleaned into active SME version. |
| Pipeline tracking | `business/PIPELINE.md`, deal pipeline docs | `ACTIVE_WORKSTREAMS.md`, `DEAL_SOURCING_TRACKING.md` | Enhance | Work tracking and lead tracking are separated. |
| Sales discovery | AXIS v4 Sales OS | `CORE/SPECIALIST_OS/SALES_OS/SALES_DISCOVERY.md` | Enhance | New dedicated sales capability. |
| Sales qualification | AXIS v4 Sales OS | `SALES_QUALIFICATION.md` | Enhance | New dedicated qualification logic. |
| Sales follow-up | AXIS v4 Sales OS | `SALES_FOLLOW_UP.md` | Enhance | Follow-up is now explicit. |
| Sales handoff to delivery | AXIS v4 Sales OS | `SALES_HANDOFF_TO_DELIVERY.md` | Enhance | Improves continuity from lead to client. |
| Client delivery | WKS modules, AXIS v4 Client Delivery OS | `CORE/SPECIALIST_OS/CLIENT_DELIVERY_OS`, `SME_DEPLOYMENT_MODULES.md` | Enhance | Delivery function strengthened and made generic. |
| Client onboarding | AXIS v4 Client Delivery OS | `CLIENT_DELIVERY_ONBOARDING.md` | Enhance | Dedicated onboarding logic active. |
| Delivery planning | AXIS v4 Client Delivery OS | `CLIENT_DELIVERY_PLAN.md` | Enhance | Dedicated delivery planning active. |
| Progress tracking | AXIS v4 Client Delivery OS | `CLIENT_DELIVERY_PROGRESS_TRACKING.md` | Enhance | Dedicated progress tracking active. |
| Client communication | AXIS v4 Client Delivery OS | `CLIENT_DELIVERY_COMMUNICATION.md` | Enhance | Dedicated communication layer active. |
| Completion / handoff | AXIS v4 Client Delivery OS | `CLIENT_DELIVERY_COMPLETION_HANDOFF.md` | Enhance | Dedicated completion handoff active. |
| WKS-specific delivery source | `D:\Wayne Francis\Axis AI\Client Builds` | `ARCHIVE_NOTES/SOURCE_CLIENT_BUILDS_WKS` | Archive | Preserved as source only; active reusable version is generic. |
| Generic SME delivery modules | source derived from WKS modules | `PROJECTS/.../client-templates/SME_DEPLOYMENT_MODULES.md` | Enhance | New clean template created to prevent client-specific leakage. |
| Compliance materials | PaaS compliance pack | `PROJECTS/SFW_PROJECT_SOLUTIONS/compliance` | Preserve | DPA, privacy notice, suppression policy, onboarding compliance form preserved. |
| GDPR awareness | `business/GDPR.md`, compliance files, Output Validation Engine | `compliance`, `OUTPUT_VALIDATION_ENGINE.md` | Enhance | Compliance exists at asset and validation level. |
| Suppression list policy | PaaS source files | `03_SUPPRESSION_LIST_POLICY.md` | Preserve | Preserved for outreach compliance. |
| Privacy notice addendum | PaaS source files | `02_PRIVACY_NOTICE_ADDENDUM.md` | Preserve | Preserved. |
| DPA template | PaaS source files | `01_DPA_TEMPLATE.md` | Preserve | Preserved. |
| Client onboarding compliance form | PaaS source files | `04_CLIENT_ONBOARDING_COMPLIANCE_FORM.md` | Preserve | Preserved. |
| Content creation | `roles/content.md`, AXIS v4 Marketing OS | `CORE/SPECIALIST_OS/MARKETING_OS` | Enhance | Marketing OS is stronger than simple role file. |
| Content planning | `business/CONTENT_THEMES.md`, Marketing OS | `MARKETING_CONTENT_PLAN.md` | Enhance | Current content function preserved, Black Map themes excluded from active use. |
| Positioning | `business/BRAND.md`, `AI OS Sales Copy.md`, Marketing OS | `MARKETING_POSITIONING.md`, SF&W files | Enhance | Needs future SF&W-specific brand/positioning file. |
| Inbound marketing handoff | AXIS v4 Marketing OS | `MARKETING_INBOUND_HANDOFF.md` | Enhance | New capability added. |
| Market intelligence / learning | user AXIS spec, AXIS v4 Market Operator OS | `CORE/SPECIALIST_OS/MARKET_OPERATOR_OS` | Enhance | Useful for LEARN/REVIEW mode. Not financial advice. |
| Market analysis | AXIS v4 Market Operator OS | `MARKET_ANALYSIS.md` | Preserve | Preserved as specialist function. |
| Market risk / scenario review | AXIS v4 Market Operator OS | `MARKET_RISK_ENGINE.md`, `MARKET_SCENARIO_ENGINE.md` | Preserve | Preserved as decision-support logic. |
| Memory | `business/MEMORY.md`, AXIS v4 Memory OS | `CORE/MEMORY/MEMORY_OPERATING_SYSTEM.md` | Enhance | Stronger memory rules added. Need future live memory log. |
| Relationship-led communication | Boardy-style requirement from Wayne | `CORE/CLAUDE_OPERATOR/RELATIONSHIP_CONNECTOR_MODE.md` | Enhance | New must-have mode for warm intros, referrals, follow-ups, and relationship memory. |
| Relationship memory | not explicit | `BUSINESS/TRACKING/RELATIONSHIP_MEMORY.md` | Enhance | New consent-aware relationship tracker. |
| Intro tracking | not explicit | `BUSINESS/TRACKING/INTRO_TRACKER.md` | Enhance | New tracker for permission-based introductions. |
| Telegram / WhatsApp access | requested by Wayne | `CORE/CLAUDE_OPERATOR/ACCESS_CHANNELS.md` | Enhance | Channels defined as access routes into Claude, not separate agents. |
| Client usage tracking | requested by Wayne | `COMPLIANCE/USAGE_TRACKING_NOTICE.md`, `CLIENT_CONSENT_AND_ANALYTICS.md`, `USAGE_LOG.md` | Enhance | New legal/ethical telemetry layer for support and improvement. |
| Session summary | `roles/session-summary.md`, `business/INPUTS/SESSION_SUMMARY.md` | `START_HERE.md`, `ACTIVE_WORKSTREAMS.md`; future session log needed | Preserve | Function is preserved in rule, but a dedicated session log file should be added. |
| QA / review | `roles/qa.md` | `CORE/VALIDATION/OUTPUT_VALIDATION_ENGINE.md` | Supersede | Validation Engine becomes active QA gate. |
| Audit role | `roles/audit.md` | `REVIEW` mode + Validation Engine + Market/Marketing modules | Enhance | Preserved through stronger review process. |
| Builder role | `roles/builder.md` | `BUILD` mode + Client Delivery / Build Rules | Enhance | Preserved and strengthened. |
| Workflow role | `roles/workflow.md` | Specialist OS + `SME_DEPLOYMENT_MODULES.md` | Enhance | Workflow design becomes part of delivery and build layer. |
| Pipeline role | `roles/pipeline.md` | Deal Sourcing Tracking + Active Workstreams | Enhance | Pipeline split into lead pipeline and workstream tracker. |
| Handover role | `roles/handover.md` | Client Delivery handoff + future onboarding file | Preserve | Function present but should be made more explicit later. |
| File output standard | AXIS v4 `FILE_OUTPUT_STANDARD.md`, current file update rule | `CORE/BUILD_RULES/FILE_OUTPUT_STANDARD.md` | Enhance | Adapted for Claude and live workspace editing. |
| Full-file copy/paste mode | AXIS v4 file rule | `FILE_OUTPUT_STANDARD.md` | Preserve | Preserved when Claude returns user-copyable files. |
| Workspace edit mode | current Codex/working folder behaviour | `FILE_OUTPUT_STANDARD.md` | Enhance | Explicitly allows direct edits with summary. |
| Governance | AXIS v4 governance files | `CORE/GOVERNANCE` | Enhance | System hierarchy, specialist control, build tracker active. |
| Specialist OS activation | AXIS v4 Hermes and governance files | `CORE/CLAUDE_OPERATOR/CLAUDE_OPERATOR_MODEL.md`, `CORE/SPECIALIST_OS/README.md` | Enhance | Specialist OS modules are now Claude playbooks, not separate agents. |
| Pause/resume specialist OS | AXIS v4 governance | `SPECIALIST_OS_CONTROL_LAYER.md` | Preserve | Preserved from AXIS v4. |
| Output assembly | AXIS v4 Hermes | `CLAUDE.md`, `CORE/VALIDATION/OUTPUT_VALIDATION_ENGINE.md` | Supersede | Claude now assembles and validates outputs directly. |
| Task handoff | AXIS v4 Hermes | `CORE/DCoS/DCOS_COMMAND_LAYER.md` | Supersede | Task handoff is simplified into Claude's DCoS discipline. |
| Conversation engine | AXIS v4 Hermes | `CLAUDE.md`, `CORE/CLAUDE_OPERATOR/CLAUDE_OPERATOR_MODEL.md` | Supersede | Claude is the direct conversation layer. |
| Testing | AXIS v4 testing files | `TESTING`, `FUNCTIONAL_TEST_PLAN.md` | Enhance | New build can be tested functionally. |
| Build testing workflow | AXIS v4 testing | `TESTING/BUILD_TESTING_WORKFLOW.md` | Preserve | Preserved. |
| System integration test | AXIS v4 testing | `TESTING/SYSTEM_INTEGRATION_TEST.md` | Preserve | Preserved. |
| Functional Claude test plan | newly created | `ARCHIVE_NOTES/FUNCTIONAL_TEST_PLAN.md` | Enhance | New test layer specific to this build. |
| SOPs | AXIS v4 SOP folder | `SOP` | Preserve | Preserved as operating reference. |
| Source manifest | new | `ARCHIVE_NOTES/SOURCE_MANIFEST.md` | Enhance | Adds traceability. |
| Structure review | new | `ARCHIVE_NOTES/STRUCTURE_AND_FUNCTION_REVIEW.md` | Enhance | Adds build review record. |
| D drive structure review | `projects/os-consolidation` | not copied into Claude build | Archive | Useful planning source, not active OS logic. |
| Older Axis versions | `D:\Wayne AI OS\Axis OS_v2`, `v2.1`, `v3` | no active location | Archive | Kept as reference only. |
| Deal Sourcing AI prototype | `D:\Deal Sourcing AI` | no active location | Archive | Superseded by AXIS v4 Deal Sourcing OS. |
| Backups | `D:\backup`, `D:\Backup 2026` | no active location | Archive | Untouched. |

## Capability Coverage By Category

### Command And Routing

Status: enhanced

Covered by:
- `CLAUDE.md`
- `START_HERE.md`
- `CORE/DCoS`
- `CORE/CLAUDE_OPERATOR`
- `CORE/GOVERNANCE`

No loss identified.

### Business Context

Status: enhanced with one deliberate exclusion

Covered by:
- `BUSINESS/VENTURES/VENTURE_REGISTRY.md`
- `BUSINESS/VENTURES/SFW_PROJECT_SOLUTIONS.md`
- `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`

Excluded:
- Black Map context

No unintended loss identified.

### Revenue And Lead Generation

Status: enhanced

Covered by:
- `CORE/SPECIALIST_OS/DEAL_SOURCING_OS`
- `CORE/SPECIALIST_OS/SALES_OS`
- `PROJECTS/SFW_PROJECT_SOLUTIONS/outreach`
- `PROJECTS/SFW_PROJECT_SOLUTIONS/offer`

No loss identified.

### Delivery

Status: enhanced

Covered by:
- `CORE/SPECIALIST_OS/CLIENT_DELIVERY_OS`
- `PROJECTS/SFW_PROJECT_SOLUTIONS/client-templates/SME_DEPLOYMENT_MODULES.md`

Old client-specific source is archived, not removed.

### Marketing And Content

Status: enhanced

Covered by:
- `CORE/SPECIALIST_OS/MARKETING_OS`

Note:
A dedicated SF&W brand and content file should be added later to replace reliance on mixed older brand files.

### Review And QA

Status: enhanced / superseded

Covered by:
- `CORE/VALIDATION/OUTPUT_VALIDATION_ENGINE.md`
- `TESTING`
- `ARCHIVE_NOTES/FUNCTIONAL_TEST_PLAN.md`

The old QA role is superseded by stronger validation.

### Memory And Continuity

Status: enhanced, but needs a live memory file

Covered by:
- `CORE/MEMORY/MEMORY_OPERATING_SYSTEM.md`
- `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`

Recommended addition:
- `BUSINESS/TRACKING/SESSION_LOG.md`
- `BUSINESS/TRACKING/DECISION_LOG.md`

### Governance

Status: enhanced

Covered by:
- `CORE/GOVERNANCE`
- `SOP`
- `CORE/BUILD_RULES`

No loss identified.

## Gaps To Close Before Locking

These are not lost functions. They are functions that should be made more explicit in the new build.

1. Add `BUSINESS/TRACKING/SESSION_LOG.md`
2. Add `BUSINESS/TRACKING/DECISION_LOG.md`
3. Add `BUSINESS/VENTURES/SFW_BRAND.md`
4. Add `PROJECTS/SFW_PROJECT_SOLUTIONS/outreach/DAILY_OUTREACH_RUNBOOK.md` as a cleaned active version
5. Add `PROJECTS/SFW_PROJECT_SOLUTIONS/offer/SME_AI_AUDIT_CHECKLIST.md`
6. Add `PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/CLIENT_ONBOARDING_FLOW.md`
7. Clean copied AXIS v4 encoding issues - complete on 2026-05-06
8. Review consent wording for Relationship Connector Mode
9. Review usage tracking wording before first client handover

## Audit Conclusion

The Claude build does not remove core functionality.

It enhances the work OS by adding:
- stronger routing
- stronger validation
- specialist systems
- cleaner venture separation
- workstream tracking
- SF&W revenue assets
- test workflows
- Claude-first access model for Telegram and WhatsApp planning
- relationship-led communication with consent gates

Functions that are not active are either:
- archived because they are superseded
- source-only because they contain client-specific details
- excluded because Wayne requested it

Recommended status:
in review

Next action:
Close the remaining open gaps above, then run the functional test plan.
