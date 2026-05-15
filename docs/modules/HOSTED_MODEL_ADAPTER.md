# Hosted Model Adapter

Status: capability spec — pending build
Date: 2026-05-15
Owner: Wayne Francis

## Purpose

The Hosted Model Adapter extends Axis Local OS so that the governed loop can call frontier hosted models (Claude, OpenAI, others) when the work needs more capability than a local model can give — without breaking governance, audit, or data discipline.

Local-only is the right default for sensitive, fast, or offline work. Hosted is the right call for hard reasoning, long context, polished drafting, and complex code. Axis should be able to choose, per request, under rules Wayne sets.

## First Principle

Axis governance does not change when the model lives somewhere else.

A hosted call is still:

- classified and approval-gated
- retrieved-grounded (no claim without sources)
- audited (request, model, sources, response — recorded locally)
- bounded by per-client routing rules
- reversible at the level the action operates on

The model provider is an adapter. The governance is the building.

## Architecture

The existing `tools/local_os/model_runtime.py` already takes a `provider_type`. Today only `ollama` is wired. The hosted adapter adds:

- `provider_type: "claude"` — Anthropic Messages API
- `provider_type: "openai"` — OpenAI Chat Completions API

Both are registered in `config/local_model_runtime.json` alongside the existing local provider. Selection is per-request, with a default and an override flag:

```text
axis_answer.py --model gemma:local        # on-device
axis_answer.py --model claude-opus-4-7    # hosted, audited
axis_answer.py --model gpt-5              # hosted, audited
axis_answer.py                            # uses policy default
```

## Routing Policy

A small policy file (`config/model_routing.json`) controls when hosted calls are allowed:

```json
{
  "default": "local",
  "allow_hosted_for": ["reasoning", "long_context", "polish"],
  "always_local_for": ["client_data", "regulated", "personal_memory"],
  "per_client": {
    "<client_slug>": "local_only"
  }
}
```

Routing rules apply before the call is made. A request tagged `client_data` or scoped to a client marked `local_only` cannot escape to a hosted provider, even if the user asks.

## Secrets Handling

Hosted providers need API keys. Rules:

- Keys live in `.env` (gitignored), never in config files.
- Keys are loaded once at process start. Never logged. Never echoed.
- The audit event records the provider name and the model ID, never the key.
- If a key is missing, the adapter halts with a clear message and does not fall back silently.

## Data Discipline

Before any hosted call, Axis enforces three checks:

1. **Redaction sweep** — strips known sensitive markers (client names tagged private, personal data fields, GDPR-flagged content) from the prompt unless explicitly allowed by routing policy.
2. **Source scoping** — only retrieved sources that are flagged hosted-OK are included in the prompt. Sources marked local-only are filtered out.
3. **Consent gate** — if any retrieved source belongs to a client marked `local_only`, the call halts.

These checks are non-bypassable. They run inside the governed loop, not inside the adapter.

## Audit Event Extension

Hosted calls add these fields to the existing model runtime audit event:

- `provider` — claude / openai / etc.
- `model_id` — exact model string (e.g. `claude-opus-4-7`)
- `endpoint` — base URL the call was sent to
- `prompt_tokens` / `completion_tokens` — reported by the provider where available
- `redaction_applied` — true / false
- `sources_filtered_by_scope` — count of sources excluded for hosted-OK reasons
- `policy_decision` — which rule allowed the call
- `cost_estimate` — optional, based on published per-token rates

## Failure Modes

The adapter halts and routes to Wayne if:

- API key is missing or rejected
- Routing policy forbids hosted for this request
- A retrieved source is local-only and the request requires it
- The provider returns an error or times out (default 60s)
- Redaction fails to complete
- The selected model is not on the allowed model list

No silent fallback to local. If a hosted call fails, Axis says so and asks Wayne what to do.

## MVP Build Order

1. Spec + module registration (this file + entry in `axis_modules.py`).
2. `provider_type: "claude"` adapter in `model_runtime.py` — health check, generate, audit.
3. `provider_type: "openai"` adapter — same shape.
4. `config/model_routing.json` + routing decision function.
5. Redaction sweep + source scope filter in the governed loop pre-call hook.
6. Per-client routing rules (reads from `business/CLIENTS/<slug>/MODEL_POLICY.md`).
7. `axis_answer.py --model <id>` flag.
8. Cost-estimate field in audit events.
9. Hosted-call governance dashboard view (read-only summary).

## First CLI Surface

```powershell
python tools/local_os/model_runtime.py health --provider claude
python tools/local_os/model_runtime.py generate --provider claude --model claude-opus-4-7 --prompt "..."
python tools/local_os/axis_answer.py "Explain the Axis governance model" --model claude-opus-4-7
```

## Governance Rules

- Hosted calls are opt-in per request or per client, never global by default.
- A request flagged with regulated client data cannot reach a hosted provider.
- Every hosted call writes an audit event before the response is shown.
- API keys are never written to any file the user can see, including audit logs.
- The user can revoke hosted access at any time by editing the routing policy.
- Hosted responses are still subject to the same retrieval-grounding rule — model fluency does not override source authority.

## Success Condition

Wayne can ask Axis a hard question, route it to Claude or GPT under explicit policy, get a frontier-grade answer grounded in his own sources, and see a full audit trail of which provider was called, what was sent, what came back, and which routing rule allowed it.
