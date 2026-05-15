# Axis OS v3 Enhancement Map

Status: active review document
Purpose: File-by-file map for improving the current working build without losing existing v3 functionality.
Source build: `D:\Axis AI - ChatGPT OS\AXIS_OS_CLAUDE_BUILD`
Target build: `D:\Wayne AI OS\Axis OS_v3`

Rule: v3 remains the master work OS. The latest Claude build contributes commercial packaging, product documentation, delivery templates, Solo Operator assets, and access-channel logic.

## Decision Key

| Status | Meaning |
|---|---|
| Import | Copy into v3 with light path and branding updates. |
| Rewrite | Use the source file as material, but adapt it to v3 rules and current brand structure. |
| Keep | Leave existing v3 file as authority. |
| Archive | Retain only as reference, not active system logic. |
| Exclude | Do not move into v3. |

## Core Control Files

| Source File | Target File | Decision | Reason |
|---|---|---|---|
| `AXIS_OS_CLAUDE_BUILD\CLAUDE.md` | `Axis OS_v3\CLAUDE.md` | Rewrite | Newer file has better Claude start behaviour, brand priority, access-channel rules, and commercial focus. Existing v3 has stronger DCoS and agent governance. Merge the best parts, do not replace. |
| `AXIS_OS_CLAUDE_BUILD\START_HERE.md` | `Axis OS_v3\START_HERE.md` | Rewrite | Newer version has better default priority, access-channel wording, trigger commands, and session close rules. Existing v3 has simpler DCoS entry. Merge into one cleaner v3 start page. |
| `AXIS_OS_CLAUDE_BUILD\README.md` | `Axis OS_v3\README.md` | Rewrite | Newer version explains the product better. Existing v3 README is too thin for handover or product understanding. |
| `AXIS_OS_CLAUDE_BUILD\LAUNCH_PROMPT.md` | `Axis OS_v3\LAUNCH_PROMPT.md` | Import | Useful quick-start launch instruction for Claude. Add as an operator aid, not as core constitution. |
| `AXIS_OS_CLAUDE_BUILD\OS_STARTUP_TEST.md` | `Axis OS_v3\TESTING\OS_STARTUP_TEST.md` | Import | Good functional test for whether Claude understands the build on startup. |
| `Axis OS_v3\DEVELOPER.md` | `Axis OS_v3\DEVELOPER.md` | Keep | Already added. It should remain the active copy, landing page, pricing language, and positioning standard. |

## Brand And Business Truth

| Source File | Target File | Decision | Reason |
|---|---|---|---|
| `BUSINESS\BRAND_ARCHITECTURE.md` | `Axis OS_v3\business\BRAND_ARCHITECTURE.md` | Import | Critical clarification: Wayne Francis is the brand, SF&W Project Solutions is the trading entity, AXIS is the product/system. |
| `BUSINESS\VENTURES\VENTURE_REGISTRY.md` | `Axis OS_v3\business\VENTURES\VENTURE_REGISTRY.md` | Import | Gives portfolio-level context and confirms consultancy-first priority. Black Map exclusion should remain unless Wayne reintroduces it. |
| `BUSINESS\VENTURES\SFW_PROJECT_SOLUTIONS.md` | `Axis OS_v3\business\VENTURES\SFW_PROJECT_SOLUTIONS.md` | Import | Stronger current truth for SF&W offer development, positioning, and active commercial priority. |
| `BUSINESS\TRACKING\ACTIVE_WORKSTREAMS.md` | `Axis OS_v3\business\TRACKING\ACTIVE_WORKSTREAMS.md` | Import | Adds cleaner workstream tracking than relying only on EXECUTION_TRACKER. Should complement, not replace, DCoS tracker. |
| `BUSINESS\TRACKING\INTRO_TRACKER.md` | `Axis OS_v3\business\TRACKING\INTRO_TRACKER.md` | Import | Supports Relationship Connector Mode and warm-intro tracking. |
| `BUSINESS\TRACKING\RELATIONSHIP_MEMORY.md` | `Axis OS_v3\business\TRACKING\RELATIONSHIP_MEMORY.md` | Import | Supports Boardy-style relationship intelligence with consent-aware memory. |
| `Axis OS_v3\business\BRAND.md` | Same | Keep with rewrite pass later | Keep the v3 business context file, but update language to match Wayne Francis / SF&W brand architecture. |
| `Axis OS_v3\business\OFFERS.md` | Same | Rewrite | Current offer set is outdated. Replace with the newer commercial stack after Wayne approves final pricing and offer names. |
| `Axis OS_v3\business\EXECUTION_TRACKER.md` | Same | Keep | This is v3 operational history. Do not overwrite. |
| `Axis OS_v3\business\DEAL_LOG.md` | Same | Keep | Existing revenue-layer log. Do not overwrite. |
| `Axis OS_v3\business\CLIENT_ACQUISITION_SYSTEM.md` | Same | Keep | Strong governance file. Can later be aligned with the newer outreach/audit funnel, but should not be replaced. |

## Product Manual

| Source Folder/File | Target Folder/File | Decision | Reason |
|---|---|---|---|
| `PRODUCT_MANUAL\README.md` | `Axis OS_v3\PRODUCT_MANUAL\README.md` | Import | Needed so Wayne can explain the product clearly. |
| `PRODUCT_MANUAL\01_PRODUCT_OVERVIEW.md` | `Axis OS_v3\PRODUCT_MANUAL\01_PRODUCT_OVERVIEW.md` | Import | Useful plain-English explanation of what AXIS is. |
| `PRODUCT_MANUAL\02_CAPABILITY_MAP.md` | `Axis OS_v3\PRODUCT_MANUAL\02_CAPABILITY_MAP.md` | Import | Important capability reference. Should become the active product capability map. |
| `PRODUCT_MANUAL\03_PRODUCT_VERSIONS.md` | `Axis OS_v3\PRODUCT_MANUAL\03_PRODUCT_VERSIONS.md` | Import | Clarifies internal OS, client OS, and Solo Operator OS versions. |
| `PRODUCT_MANUAL\04_OPERATING_MODEL.md` | `Axis OS_v3\PRODUCT_MANUAL\04_OPERATING_MODEL.md` | Import | Explains how routing, tracking, review, and commands work. |
| `PRODUCT_MANUAL\05_USER_GUIDE.md` | `Axis OS_v3\PRODUCT_MANUAL\05_USER_GUIDE.md` | Import | Needed for Wayne and future client/user onboarding. |
| `PRODUCT_MANUAL\06_DEVELOPMENT_GUIDE.md` | `Axis OS_v3\PRODUCT_MANUAL\06_DEVELOPMENT_GUIDE.md` | Import | Helps future improvements stay controlled. |
| `PRODUCT_MANUAL\07_DOCUMENTATION_INDEX.md` | `Axis OS_v3\PRODUCT_MANUAL\07_DOCUMENTATION_INDEX.md` | Rewrite | Import structure but update paths to `D:\Wayne AI OS\Axis OS_v3`. |
| `PRODUCT_MANUAL\08_TESTING_AND_SIGNOFF.md` | `Axis OS_v3\PRODUCT_MANUAL\08_TESTING_AND_SIGNOFF.md` | Import | Strong signoff framework. |
| `PRODUCT_MANUAL\09_RISKS_AND_BOUNDARIES.md` | `Axis OS_v3\PRODUCT_MANUAL\09_RISKS_AND_BOUNDARIES.md` | Import | Important for legal/compliance boundaries and personal-life usage limits. |
| `PRODUCT_MANUAL\10_NEXT_ACTIONS.md` | `Axis OS_v3\PRODUCT_MANUAL\10_NEXT_ACTIONS.md` | Rewrite | Use as current roadmap, but refresh after migration. |

## Claude Operator And Access Channels

| Source File | Target File | Decision | Reason |
|---|---|---|---|
| `CORE\CLAUDE_OPERATOR\CLAUDE_OPERATOR_MODEL.md` | `Axis OS_v3\CORE\CLAUDE_OPERATOR\CLAUDE_OPERATOR_MODEL.md` | Import | Defines Claude as operator, not separate product. Useful for live use. |
| `CORE\CLAUDE_OPERATOR\ACCESS_CHANNELS.md` | `Axis OS_v3\CORE\CLAUDE_OPERATOR\ACCESS_CHANNELS.md` | Import | Captures Telegram/WhatsApp as future channels, not separate systems. |
| `CORE\CLAUDE_OPERATOR\TRIGGER_COMMANDS.md` | `Axis OS_v3\CORE\CLAUDE_OPERATOR\TRIGGER_COMMANDS.md` | Import | Adds `AXIS: NEW CLIENT`, `AXIS: SOLO START`, and related startup triggers. |
| `CORE\CLAUDE_OPERATOR\RELATIONSHIP_CONNECTOR_MODE.md` | `Axis OS_v3\CORE\CLAUDE_OPERATOR\RELATIONSHIP_CONNECTOR_MODE.md` | Import | Must-have relationship/Boardy-style communication layer. |
| `Axis Claude Build Test\telegram_*.py` | No active target | Archive | Useful experiment only. Do not include as active no-code system because Wayne wants no-code first. |
| `Axis Claude Build Test\TELEGRAM_BOT_SETUP.md` | `Axis OS_v3\ARCHIVE\TELEGRAM_EXPERIMENTS\TELEGRAM_BOT_SETUP.md` | Archive | Keep as future technical reference, not active promise. |

## DCoS And Governance

| Source File | Target File | Decision | Reason |
|---|---|---|---|
| `CORE\DCoS\DCOS_COMMAND_LAYER.md` | `Axis OS_v3\CORE\DCoS\DCOS_COMMAND_LAYER.md` | Import | Newer DCoS playbook aligns with the commercial/product build. Existing v3 agent DCoS remains authority for agent routing. |
| `CORE\GOVERNANCE\BUILD_PHASE_TRACKER.md` | `Axis OS_v3\CORE\GOVERNANCE\BUILD_PHASE_TRACKER.md` | Import | Useful for product build status. |
| `CORE\GOVERNANCE\SPECIALIST_OS_CONTROL_LAYER.md` | `Axis OS_v3\CORE\GOVERNANCE\SPECIALIST_OS_CONTROL_LAYER.md` | Import | Helps explain specialist OS access and boundaries. |
| `CORE\GOVERNANCE\SYSTEM_RULE_HIERARCHY.md` | `Axis OS_v3\CORE\GOVERNANCE\SYSTEM_RULE_HIERARCHY.md` | Import | Useful for preventing conflicting instructions. |
| `CORE\VALIDATION\OUTPUT_VALIDATION_ENGINE.md` | `Axis OS_v3\CORE\VALIDATION\OUTPUT_VALIDATION_ENGINE.md` | Import | Strengthens QA before deliverables are treated as final. |
| `Axis OS_v3\.claude\agents\*` | Same | Keep | Current 16-agent structure is v3's strongest operational layer. Do not replace with newer playbook-only files. |
| `Axis OS_v3\business\AGENT_RESOLUTION.md` | Same | Keep | Existing v3 agent resolution table remains useful. Later add references to imported Specialist OS playbooks. |

## Specialist OS Playbooks

| Source Folder | Target Folder | Decision | Reason |
|---|---|---|---|
| `CORE\SPECIALIST_OS\DEAL_SOURCING_OS` | `Axis OS_v3\CORE\SPECIALIST_OS\DEAL_SOURCING_OS` | Import | Stronger deal sourcing workflow than current v3 alone. Supports consultancy revenue. |
| `CORE\SPECIALIST_OS\SALES_OS` | `Axis OS_v3\CORE\SPECIALIST_OS\SALES_OS` | Import | Needed for discovery, follow-up, qualification, and handoff. |
| `CORE\SPECIALIST_OS\CLIENT_DELIVERY_OS` | `Axis OS_v3\CORE\SPECIALIST_OS\CLIENT_DELIVERY_OS` | Import | Critical for turning audits into implemented client systems. |
| `CORE\SPECIALIST_OS\MARKETING_OS` | `Axis OS_v3\CORE\SPECIALIST_OS\MARKETING_OS` | Import | Supports landing pages, positioning, posts, and offer copy. |
| `CORE\SPECIALIST_OS\MARKET_OPERATOR_OS` | `Axis OS_v3\CORE\SPECIALIST_OS\MARKET_OPERATOR_OS` | Import | Useful for learning, research, and strategic market checks. |
| `CORE\SPECIALIST_OS\SPECIALIST_OS_ACCESS_GUIDE.md` | `Axis OS_v3\CORE\SPECIALIST_OS\SPECIALIST_OS_ACCESS_GUIDE.md` | Import | Helps clients and Wayne understand how specialist OS files are accessed. |
| `CORE\SPECIALIST_OS\README.md` | `Axis OS_v3\CORE\SPECIALIST_OS\README.md` | Import | Index for the specialist playbook layer. |

## SF&W Project Solutions Assets

| Source Folder/File | Target Folder/File | Decision | Reason |
|---|---|---|---|
| `PROJECTS\SFW_PROJECT_SOLUTIONS\README.md` | `Axis OS_v3\PROJECTS\SFW_PROJECT_SOLUTIONS\README.md` | Import | Creates a clear project space for the revenue engine. |
| `audit\SME_AI_AUDIT_CHECKLIST_TEMPLATE.md` | Same under v3 project | Import | Core audit delivery asset. |
| `audit\DISCOVERY_CALL_NOTES_TEMPLATE.md` | Same under v3 project | Import | Needed for repeatable audit workflow. |
| `audit\AUDIT_REPORT_TEMPLATE.md` | Same under v3 project | Import | Needed to convert discovery into a professional report. |
| `proposals\IMPLEMENTATION_PROPOSAL_TEMPLATE.md` | Same under v3 project | Import | Needed for paid implementation proposal. |
| `proposals\IMPLEMENTATION_SCOPE_TEMPLATE.md` | Same under v3 project | Import | Needed for delivery control and client clarity. |
| `delivery\CLIENT_HANDOVER_EMAIL_TEMPLATE.md` | Same under v3 project | Import | Useful for client-ready delivery. |
| `offer\PRICING_AND_VALUE_GUIDE.md` | Same under v3 project | Import in review | Important commercial work, but pricing stays in review until Wayne approves. |
| `offer\SOLO_OPERATOR_OS_OFFER.md` | Same under v3 project | Import in review | Important Solo Operator positioning asset. |
| `offer\SOLO_OPERATOR_OS_LANDING_PAGE_COPY.md` | Same under v3 project | Import in review | Useful but should go through `DEVELOPER.md` before public use. |
| `offer\SME_AI_AUDIT_FUNNEL.md` | Same under v3 project | Import | Strong front-end commercial funnel. |
| `offer\PIPELINE_AS_A_SERVICE_*` | Same under v3 project | Archive or in review | Useful idea, but secondary to SME Audit and Solo Operator OS. Do not make active offer yet. |

## Outreach And Lead Generation

| Source Folder/File | Target Folder/File | Decision | Reason |
|---|---|---|---|
| `outreach\SME_AUDIT_OUTREACH_PACK\README.md` | Same under v3 project | Import | Good repeatable outreach pack. |
| `outreach\SME_AUDIT_OUTREACH_PACK\01_CORE_OUTREACH_MESSAGES.md` | Same under v3 project | Import in review | Useful but should be checked against no-hype and compliance rules. |
| `outreach\SME_AUDIT_OUTREACH_PACK\02_SECTOR_VARIANTS.md` | Same under v3 project | Import in review | Useful for broad SME targeting without limiting to estate agents. |
| `outreach\SME_AUDIT_OUTREACH_PACK\03_AUDIT_LANDING_PAGE_COPY.md` | Same under v3 project | Import in review | Needs Developer final pass before public use. |
| `outreach\SME_AUDIT_OUTREACH_PACK\04_LEAD_TRACKER_TEMPLATE.md` | Same under v3 project | Import | Supports manual/no-code lead tracking. |
| `outreach\SME_AUDIT_OUTREACH_PACK\05_DAILY_OUTREACH_ROUTINE.md` | Same under v3 project | Import | Gives Wayne a repeatable daily routine. |
| `outreach\DAILY_OUTREACH_RUNBOOK_SOURCE.md` | Same under v3 project | Rewrite | Merge into outreach routine if not duplicative. |
| `outreach\TEST_SENDS` | Same under v3 project archive | Archive | Useful proof/testing history, not active standard. |

## No-Code Delivery Plans

| Source Folder/File | Target Folder/File | Decision | Reason |
|---|---|---|---|
| `delivery\NO_CODE_DELIVERY_PLANS\README.md` | Same under v3 project | Import | Essential because Wayne is not a programmer. |
| `01_SOLO_OPERATOR_OS_DELIVERY_PLAN.md` | Same under v3 project | Import | Makes Solo Operator deliverable without code. |
| `02_SME_AI_AUTOMATION_AUDIT_DELIVERY_PLAN.md` | Same under v3 project | Import | Makes the front-end audit repeatable. |
| `03_CLIENT_OS_BUILD_HANDOVER_DELIVERY_PLAN.md` | Same under v3 project | Import | Turns audit into implementation without code. |
| `04_RELATIONSHIP_CONNECTOR_MODE_DELIVERY_PLAN.md` | Same under v3 project | Import | Defines the Boardy-style relationship use case and quarterly value. |

## Client OS Template

| Source Folder/File | Target Folder/File | Decision | Reason |
|---|---|---|---|
| `delivery\CLIENT_OS_TEMPLATE` | `Axis OS_v3\PROJECTS\SFW_PROJECT_SOLUTIONS\delivery\CLIENT_OS_TEMPLATE` | Import in review | Stronger practical handover template than v3 client-safe spec alone. Must be reviewed for client-safe boundaries. |
| `CLIENT_OS_TEMPLATE\CLAUDE.md` | Same under v3 project | Rewrite | Must not expose internal Wayne strategy or hidden system logic. |
| `CLIENT_OS_TEMPLATE\START_HERE.md` | Same under v3 project | Import in review | Good client startup page. Needs client-safe pass. |
| `CLIENT_OS_TEMPLATE\COMPLIANCE\*` | Same under v3 project | Import in review | Useful, but legal wording should be reviewed before paid client use. |
| `CLIENT_OS_TEMPLATE\CHANNELS\ACCESS_CHANNELS.md` | Same under v3 project | Import | Helps explain Telegram/WhatsApp as optional future channels. |
| `CLIENT_OS_TEMPLATE\HANDOVER\*` | Same under v3 project | Import | Strong client handover workflow. |
| `CLIENT_OS_TEMPLATE\TEMPLATES\*` | Same under v3 project | Import | Useful reusable client templates. |
| `CLIENT_OS_TEMPLATE\TRAINING\USER_GUIDE.md` | Same under v3 project | Import | Client needs plain user guidance. |
| `CLIENT_SAFE_DISTRIBUTION.md` in v3 | Same | Keep and update later | Existing v3 client-safe spec is stronger governance. Update it to reference the newer Client OS Template. |

## Solo Operator OS

| Source Folder/File | Target Folder/File | Decision | Reason |
|---|---|---|---|
| `delivery\SOLO_OPERATOR_OS_TEMPLATE` | `Axis OS_v3\PROJECTS\SFW_PROJECT_SOLUTIONS\delivery\SOLO_OPERATOR_OS_TEMPLATE` | Import | Core Solo Operator product template. |
| `delivery\SOLO_OPERATOR_OS_LIVE_TEST` | `Axis OS_v3\PROJECTS\SFW_PROJECT_SOLUTIONS\delivery\SOLO_OPERATOR_OS_LIVE_TEST` | Import as test artefact | Useful tested Claude version. Keep separate from clean template. |
| `delivery\SOLO_OPERATOR_OS_CODEX_LIVE_TEST` | `Axis OS_v3\PROJECTS\SFW_PROJECT_SOLUTIONS\delivery\SOLO_OPERATOR_OS_CODEX_LIVE_TEST` | Import as test artefact | Useful Codex version. Keep separate from Claude live-test. |
| `delivery\SOLO_OPERATOR_OS_DELIVERY_CHECKLIST.md` | Same under v3 project | Import | Needed for repeatable setup. |
| `delivery\SOLO_OPERATOR_OS_TEST_PLAN.md` | Same under v3 project | Import | Needed before selling or handing over. |
| `delivery\SOLO_OPERATOR_OS_LIVE_TEST.zip` | No active target | Exclude or archive outside v3 | Zips are output artefacts, not active source files. |

## Compliance And Usage Tracking

| Source Folder/File | Target Folder/File | Decision | Reason |
|---|---|---|---|
| `compliance\01_DPA_TEMPLATE.md` | Same under v3 project | Import in review | Useful for client legal/data setup, should get legal review before use. |
| `compliance\02_PRIVACY_NOTICE_ADDENDUM.md` | Same under v3 project | Import in review | Useful but not legal advice. |
| `compliance\03_SUPPRESSION_LIST_POLICY.md` | Same under v3 project | Import | Useful for outreach compliance. |
| `compliance\04_CLIENT_ONBOARDING_COMPLIANCE_CHECKLIST.md` | Same under v3 project | Import | Useful before client deployment. |
| `compliance\USAGE_TRACKING_POLICY_FOR_CLIENTS.md` | Same under v3 project | Import in review | Needed for legal/ethical usage tracking. Should be client-consent first. |
| `Axis OS_v3\business\GDPR.md` | Same | Keep | Existing v3 GDPR context remains active. |
| `Axis OS_v3\business\HANDOVER\GDPR_PROTOCOL.md` | Same | Keep | Existing v3 GDPR protocol remains active. |

## Testing And Archive Notes

| Source Folder/File | Target Folder/File | Decision | Reason |
|---|---|---|---|
| `TESTING\BUILD_TESTING_WORKFLOW.md` | `Axis OS_v3\TESTING\BUILD_TESTING_WORKFLOW.md` | Import | Useful validation workflow. |
| `TESTING\SYSTEM_INTEGRATION_TEST.md` | `Axis OS_v3\TESTING\SYSTEM_INTEGRATION_TEST.md` | Import | Useful for checking upgraded v3 works. |
| `TESTING\PHASE6_VIRTUAL_LIFECYCLE_TEST.md` | `Axis OS_v3\TESTING\PHASE6_VIRTUAL_LIFECYCLE_TEST.md` | Archive or import in review | Useful, but may be too build-phase specific. |
| `ARCHIVE_NOTES\FUNCTION_BY_FUNCTION_AUDIT.md` | `Axis OS_v3\ARCHIVE_NOTES\FUNCTION_BY_FUNCTION_AUDIT.md` | Import as reference | Important audit proof. |
| `ARCHIVE_NOTES\FUNCTIONAL_TEST_PLAN.md` | `Axis OS_v3\ARCHIVE_NOTES\FUNCTIONAL_TEST_PLAN.md` | Import as reference | Useful validation source. |
| `ARCHIVE_NOTES\STRUCTURE_AND_FUNCTION_REVIEW.md` | `Axis OS_v3\ARCHIVE_NOTES\STRUCTURE_AND_FUNCTION_REVIEW.md` | Import as reference | Useful rationale for current architecture. |
| `ARCHIVE_NOTES\HERMES_REFERENCE` | `Axis OS_v3\ARCHIVE_NOTES\HERMES_REFERENCE` | Archive only | Hermes is not active. Keep for reference only. |
| `ARCHIVE_NOTES\AXIS_V4_REFERENCE` | `Axis OS_v3\ARCHIVE_NOTES\AXIS_V4_REFERENCE` | Archive only | Keep for source history, not active authority. |
| `SOP\HERMES_CORE_SYSTEM_SOP.md` | No active target | Exclude or archive | Hermes not active. |
| `TESTING\HERMES_CORE_TESTING_WORKFLOW.md` | No active target | Exclude or archive | Hermes not active. |

## Existing v3 Files To Keep Untouched

| Current v3 File/Folder | Decision | Reason |
|---|---|---|
| `.claude\agents\` | Keep | Active v3 agent structure. |
| `business\EXECUTION_TRACKER.md` | Keep | Operational history and DCoS proof. |
| `business\DEAL_LOG.md` | Keep | Existing deal history. |
| `business\ACTIVE_CLIENTS.md` | Keep | Active client state. |
| `business\PIPELINE.md` | Keep | Active pipeline state. |
| `business\HANDOVER\*` | Keep | Strong onboarding, compliance, and handover layer. Update only after review. |
| `CLIENT_SAFE_DISTRIBUTION.md` | Keep | Strong governance rule for client copies. Should be updated, not replaced. |
| `DISTRIBUTION_POLICY.md` | Keep | Existing distribution boundary. |
| `LICENSE.md` | Keep | Existing license/legal boundary. |
| `SYSTEM_INSTANCE_TRACKING.md` | Keep | Instance tracking remains useful. |
| `CHANGELOG.md` | Keep | Historical record. |
| `V3 Axis\` | Keep as internal reference | Contains active/history audit work. Do not merge blindly. |

## Files/Folders To Exclude From The Upgrade

| Source | Decision | Reason |
|---|---|---|
| Any Black Map material | Exclude | Wayne explicitly excluded Black Map unless reintroduced. |
| Any active Hermes instruction | Exclude | Wayne found Hermes hard to work with and chose Claude/Codex route instead. |
| Generated zips | Exclude | Output artefacts, not canonical source. |
| Temporary scripts used only for cleanup | Exclude | Not part of active OS. |
| Telegram bot Python scripts | Archive only | Future technical experiment; no-code product should not depend on them. |
| Old v2/v2.1 files | Exclude from active logic | Locked/frozen fallback only. |

## Migration Order

1. Clean v3 punctuation/encoding in active visible files.
2. Add folder structure: `CORE`, `PRODUCT_MANUAL`, `PROJECTS\SFW_PROJECT_SOLUTIONS`, `TESTING`, `ARCHIVE_NOTES`.
3. Import brand architecture and SF&W venture files.
4. Rewrite `CLAUDE.md`, `START_HERE.md`, and `README.md` using v3 governance plus newer commercial clarity.
5. Import Product Manual.
6. Import Specialist OS playbooks.
7. Import SF&W audit, outreach, proposal, delivery, and compliance assets.
8. Import Client OS Template and Solo Operator OS Template as `in review`.
9. Update `business\OFFERS.md` to the new commercial stack once Wayne approves the offer/pricing wording.
10. Run startup, client OS, Solo Operator, Relationship Connector, and output validation tests.
11. Mark upgraded v3 as `in review` until Wayne signs off.
12. Lock only after live Claude test passes.

## Priority Recommendation

Do not upgrade everything at once.

Start with the files that make v3 more useful immediately:

1. `BUSINESS\BRAND_ARCHITECTURE.md`
2. `BUSINESS\VENTURES\SFW_PROJECT_SOLUTIONS.md`
3. `PRODUCT_MANUAL\README.md` and capability map
4. `CORE\CLAUDE_OPERATOR\TRIGGER_COMMANDS.md`
5. `CORE\CLAUDE_OPERATOR\RELATIONSHIP_CONNECTOR_MODE.md`
6. `PROJECTS\SFW_PROJECT_SOLUTIONS\delivery\NO_CODE_DELIVERY_PLANS`
7. `PROJECTS\SFW_PROJECT_SOLUTIONS\delivery\SOLO_OPERATOR_OS_TEMPLATE`
8. `PROJECTS\SFW_PROJECT_SOLUTIONS\delivery\CLIENT_OS_TEMPLATE`

That gives Wayne the biggest functional improvement without risking the working v3 control layer.
