# Axis Local OS Constitution And MVP Spec

Status: active foundation spec
Date: 2026-05-15
Owner: Wayne Francis
System name: Axis Local OS
Short name: AxisOS

## Mission

Axis Local OS is a local-first, memory-persistent AI operating system for governed agent workflows, retrieval-grounded execution, tool use, and controlled learning loops.

It is not just a chatbot. It is the operating layer that coordinates models, memory, tools, governance, audit records, and review.

## Strategic Principle

Axis Local OS does not start by training a custom model.

The first moat is:

- orchestration
- memory discipline
- retrieval quality
- governance
- auditability
- workflow control
- tool integration
- reflection and review

Model capability matters, but the system advantage comes from governed adaptive infrastructure.

## Non-Goals

Axis Local OS must not initially:

- train or fine-tune a custom model
- allow unsupervised self-modification
- trust model memory without retrieval
- create many autonomous agents before one governed loop works
- execute destructive actions without review
- convert unreviewed outputs into permanent memory
- claim project history without a retrievable source

## Constitution

```yaml
axis_local_os_constitution:
  no_claim_without_retrieval: true
  no_project_memory_from_model_guessing: true
  retrieved_context_requires_source_id: true
  stale_context_flag_required: true
  reviewed_memory_updates_only: true
  no_execution_without_review: true
  audit_every_action: true
  human_approval_for_external_effects: true
  self_modifying_models_disabled: true
```

## Core Architecture

```text
Axis Local OS
|
+-- Local Model Layer
+-- Agent Orchestration Layer
+-- RAG Memory Layer
+-- Tool Layer
+-- Governance Layer
+-- Reflection And Learning Layer
```

## MVP 0: Governed Local Assistant Loop

The first working loop is deliberately small:

```text
User request
-> retrieve relevant project memory
-> attach source IDs and stale-context flags
-> classify task and execution risk
-> propose the next action
-> require approval before any external effect
-> write an audit event
-> draft memory update only when requested
-> require human review before memory becomes permanent authority
```

This loop proves the spine of Axis Local OS before adding local model runtime, vector search, reranking, or multi-agent orchestration.

## Required Memory Rules

Every retrieved context item must include:

- source ID
- source path
- title
- chunk index
- modified date
- stale flag

Every answer or action that depends on project memory must be tied to retrieved context. If retrieval returns no useful context, the system must say so and proceed only as a fresh task or ask for more source material.

Memory writes are not automatic. The system may create a review draft, but permanent memory requires a reviewed update.

## Required Governance Rules

Actions are divided into three approval levels:

| Level | Meaning | Default |
|---|---|---|
| `none` | Read-only reasoning or status output | allowed |
| `review` | File edits, generated artifacts, proposed changes, memory drafts | requires review before becoming authority |
| `approval` | Commands, deletes, installs, external APIs, git mutation, database writes | requires explicit approval |

No execution path may bypass audit logging.

## Audit Event Minimum

Each governed-loop event must record:

- timestamp
- request
- task classification
- approval level
- approved or blocked status
- source IDs used
- stale source count
- proposed action
- memory proposal path, if one was created

## MVP Build Order

1. Constitution and governed loop
2. Local model runtime abstraction
3. Coding-agent workflow with command approval
4. Hosted model adapter (Claude, OpenAI) under per-request routing policy
5. Response Fidelity Policy (SOP-grounded automated replies, four-tier governance)
6. Command Centre Connectors (OAuth-secured integrations with Outlook, M365, Google Workspace, Drive, Teams, Slack, CRMs, finance tools)
7. Durable RAG memory store
8. Reranking and metadata discipline
9. Governance dashboard and review queue
10. LangGraph orchestration
11. Reflection and learning routines

The hosted model adapter (step 4) is what makes Axis Local OS hybrid rather than local-only. Local models stay the default for sensitive, fast, or offline work. Hosted frontier models (Claude, GPT) are routed in for hard reasoning, long context, and polish - under explicit policy, with redaction, source-scope filtering, and a full audit trail. Spec at `docs/modules/HOSTED_MODEL_ADAPTER.md`.

The Response Fidelity Policy (step 5) is what makes automated client-facing replies safe to deploy. Every outbound reply is classified into one of four tiers - canonical, quote-grounded, synthesised-and-verified, or draft-only - based on a per-client policy file. SOP is authority, model is fluency, and the system enforces the rule that fluency does not override authority. Spec at `docs/modules/RESPONSE_FIDELITY_POLICY.md`.

Command Centre Connectors (step 6) is the integration layer that turns Axis into the operator's command centre across Outlook, Microsoft 365, Google Workspace, Drive, Teams, Slack, CRMs, and finance tools. Security is the lead constraint: OAuth 2.0 with PKCE, OS-keychain credential storage, minimum-scope grants, per-client isolation, preview-and-approval writes, typed confirm phrases for destructive operations, and a full audit trail per connector call. Spec at `docs/modules/COMMAND_CENTRE_CONNECTORS.md`.

## Operator Binding

This Axis Local OS deployment is for Wayne Francis. The Wayne Copilot module binds the system to him specifically — operator profile at `CORE/OPERATOR_PROFILE.md`, KB ingest scope at `config/copilot_scope.json`, named workflows for audit-form response, daily / weekly / monthly cadence, teaching mode, and decision support mode. Single-operator deployment, not shareable. Spec at `docs/modules/WAYNE_COPILOT.md`.

## Current Implementation

The current local seed implementation lives in:

- `tools/rag/kb_ingest.py`
- `tools/rag/kb_search.py`
- `tools/rag/kb_capture.py`
- `tools/local_os/governed_loop.py`

This is not the final architecture. It is the smallest governed proof of the architecture.

