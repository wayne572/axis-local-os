# Response Fidelity Policy

Status: capability spec — pending build
Date: 2026-05-15
Owner: Wayne Francis

## Purpose

Response Fidelity Policy is how Axis Local OS guarantees that automated client-facing responses match the client's own SOP and documentation. It is the governance layer that sits between a model draft and the outgoing reply, so a customer can deploy automation without worrying that the AI will invent, contradict, or exceed their own published rules.

It is not a guarantee that the model is always right. It is a guarantee that the system will not let a wrong reply leave the building.

## First Principle

The client's SOP is the source of truth. The model is fluency. The system enforces the rule that fluency does not override authority.

If the SOP does not cover the question, the system halts and escalates. It does not improvise.

## Four Tiers

Every outbound automated response is classified into one of four tiers, set per use case in a per-client policy file.

### Tier A — Canonical

Pre-written SOP responses. The model is allowed only to **select** the correct canned response from a small set. No paraphrasing, no synthesis. If no canned response fits, the system halts.

- Use for: FAQ acknowledgements, complaint receipts, GDPR replies, regulated wording, opt-out confirmations.
- Fidelity: 100% by construction.
- Failure mode: false negative (system refuses a question it could have answered). Acceptable.

### Tier B — Quote-Grounded

The reply must contain at least one direct quote from a retrieved SOP chunk, with citation. The model may surround the quote with brief framing but the substantive answer is the quoted text. The retrieval similarity score must exceed a configured threshold (default 0.75).

- Use for: policy questions, procedural answers, "what is your process for X" type queries.
- Fidelity: ~99%. Errors only via wrong-chunk selection.
- Failure mode: refusal on weak retrieval. Acceptable.

### Tier C — Synthesised And Verified

The model composes a reply from one or more retrieved SOP chunks. A second model pass (a verifier) reads the draft and the cited sources and answers a single question: *does this draft contradict, exceed, or invent anything not present in the cited source?* If yes, the draft is downgraded to Tier D or refused.

- Use for: personalised replies, tone-matched follow-ups, multi-source answers.
- Fidelity: ~95% after verifier pass.
- Failure mode: verifier misses subtle paraphrase drift. Mitigated by audit-trail review.

### Tier D — Draft Only

The model produces a draft. A human approves before the reply is sent. No automation past the draft step.

- Use for: complaints, regulated communications, high-value clients, anything Wayne or the operator flags sensitive.
- Fidelity: bounded by the human reviewer.
- Failure mode: latency. Acceptable for the use case.

## Per-Client Policy

Each client deployment has a policy file at `business/CLIENTS/<slug>/RESPONSE_POLICY.md` (or the multi-client equivalent) that maps use cases to tiers:

```text
support_faq            -> tier_b
complaint_acknowledge  -> tier_a
booking_change         -> tier_c
data_subject_request   -> tier_d
out_of_hours_holding   -> tier_a
escalation_to_owner    -> tier_d
```

Default tier for any unmapped use case is **Tier D** (human approval). Conservative by default.

## Required Retrieval Discipline

Before any reply tier above A is composed:

1. **SOP authority boost.** Documents flagged as SOP authority in the KB rank above general material.
2. **Similarity threshold check.** Top retrieved chunk must score above the configured floor. If not, halt.
3. **Source scope.** Only sources flagged as outbound-OK can be quoted in customer-facing replies. Internal-only notes are filtered out.
4. **Recency check.** If the top SOP chunk is older than the policy's freshness window (default 12 months), the reply is flagged and routed for human confirmation.

## Verifier Pass (Tier C)

The verifier runs as a second governed-loop call with a fixed prompt:

> Given the cited source(s) and the proposed draft, answer in JSON:
> `{ "contradicts": bool, "exceeds": bool, "invents": bool, "notes": "..." }`
>
> "contradicts" — the draft says something the source disagrees with.
> "exceeds" — the draft promises or asserts something the source does not support.
> "invents" — the draft contains facts that are not in the source.

Any `true` value forces a downgrade. The verifier's output is itself audited.

## Citation Requirement

Tier B and Tier C replies include a citation block visible to the customer's client. Citations are short and human-readable:

```text
Source: Your Refund Policy, section 3.2 (updated 2025-11-14)
```

Citations are mandatory for the customer's audit, not optional. They are also what makes wrong replies discoverable — if the cited source does not say what the reply says, someone sees that fast.

## Audit Event

Every outbound reply writes an event with:

- `policy_tier` — A / B / C / D
- `use_case` — mapped key (e.g. `support_faq`)
- `sources_used` — list of source IDs with chunk indexes
- `top_similarity_score` — float
- `retrieval_threshold` — the policy floor at decision time
- `verifier_result` — for Tier C only
- `human_approver` — for Tier D only
- `reply_text_hash` — sha256 of the exact text sent
- `recipient_scope` — channel + recipient ID (not the body, just the address)
- `policy_version` — sha256 of the active policy file
- `sop_version` — sha256 of the cited SOP document(s)

The `policy_version` and `sop_version` hashes are the key to drift detection: when a SOP is updated, every prior reply that depended on the old version can be identified and reviewed.

## Drift And Replay

When a SOP document is replaced:

1. Axis computes the new sha256.
2. The audit log is scanned for replies that cited the old hash.
3. A drift report is generated listing affected reply IDs and recipients.
4. Wayne or the operator decides whether to issue a correction, a follow-up, or no action.

This makes "wrong reply" recoverable in the way a regulator or a serious client will respect.

## Outbound Channel Hooks

The policy is enforced at the channel boundary, not at the model boundary. Concretely: any module that sends an outbound reply (Gmail, Outlook, web chat, SMS, voice) must call the response-fidelity gate before send. Channels that do not call the gate are not allowed to send automated replies.

## Failure Modes

The gate halts and escalates if:

- No SOP chunk passes the similarity threshold
- The matched SOP is older than the freshness window
- The verifier flags contradicts / exceeds / invents
- The use case is unmapped (default Tier D)
- A source flagged internal-only would be required to answer
- The recipient is on an escalation list
- The reply text length exceeds the policy maximum
- The reply contains a forbidden phrase pattern (e.g. "guaranteed", "no risk", numbers that look like a price commitment)

## MVP Build Order

1. Spec + module registration (this file + entry in `axis_modules.py`).
2. SOP-authority flag in the KB ingest pipeline.
3. Per-client `RESPONSE_POLICY.md` reader + tier router.
4. Tier A — canonical-response selector.
5. Tier B — quote-and-cite generator with similarity threshold.
6. Verifier prompt + Tier C path.
7. Tier D — drafts-only with explicit approval surface.
8. Channel-side gate hook (Gmail first, then others).
9. Drift report (`axis_drift.py report --since <sop_change>`).
10. Audit dashboard view filtered by `policy_tier`.

## First CLI Surface

```powershell
python tools/local_os/axis_reply.py classify --use-case support_faq --question "What are your opening hours?"
python tools/local_os/axis_reply.py draft --client acme --use-case booking_change --input msg.txt
python tools/local_os/axis_reply.py verify --draft draft.txt --sources s1,s2
python tools/local_os/axis_drift.py report --client acme --since 2026-04-01
```

## Governance Rules

- The client's SOP is authority. The model is not.
- Default tier is D. No automated send without an explicit policy mapping.
- A retrieval below threshold is a halt, not a "best effort."
- Every outbound reply is audited with policy and SOP version hashes.
- A wrong reply must be traceable to a specific source chunk within one audit query.
- Citations are part of the reply, not optional metadata.
- Forbidden phrase patterns and outbound length caps are policy, not suggestions.
- Stale SOP citations require human confirmation before send.
- Internal-only sources never appear in customer-facing replies.

## What This Lets Axis Promise

> *Every automated reply is either word-for-word from the client's SOP, a direct quote from the client's documentation with citation, or held back for the team to approve. Every reply is logged with the exact source it came from. If the SOP is right, the AI replies will be right. If a reply is ever wrong, the system can show exactly which document let it through, and the SOP can be fixed — not the AI.*

This is the promise Axis can make and keep. It is not "100% accurate AI." It is "100% governed output, with the SOP as the source of truth."

## Success Condition

A customer can deploy Axis to automate replies for a chosen use case, see the policy file in plain English, watch every reply be cited back to their own SOP, and trust that anything the SOP does not cover will be escalated, not invented.
