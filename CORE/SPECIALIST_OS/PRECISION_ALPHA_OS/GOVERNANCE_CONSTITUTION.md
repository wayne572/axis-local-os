# Precision Alpha Governance Constitution

Status: active
Purpose: Non-negotiable safety and operating rules.

## Immutable Safety Constitution

```yaml
no_trade_without_risk_review: true
no_memory_update_without_review: true
no_confidence_without_evidence: true
no_execution_during_system_failure: true
no_unlogged_human_override: true
no_strategy_auto_deployment: true
no_autonomous_execution: true
paper_trade_only_in_mvp: true
human_approval_required: true
```

## Authority Hierarchy

1. Governance Constitution
2. Risk Officer Protocol
3. Data Validation Rules
4. Regime Detection
5. Confidence Scoring
6. Trade Thesis
7. Reflection Engine

If layers conflict, the higher layer wins.

## Risk Officer Authority

```yaml
risk_officer_authority: highest
risk_officer_can_veto_all_trades: true
```

The Risk Officer does not need to find a better trade. It only needs to decide whether the proposed trade should be blocked, reduced, deferred, or sent for human review.

## Human Approval Rule

No trade can progress to paper execution unless a human explicitly approves it.

Every human approval or override must be logged.

## Memory Integrity Rule

Incomplete trades cannot enter learning memory.

Memory updates require:
- completed trade record
- post-trade review
- process quality score
- audit validation

## Confidence Integrity Rule

Confidence is not probability of profit.

Confidence means:
- evidence strength
- alignment quality
- historical validation
- contradiction handling
- environmental clarity

Any confidence score without evidence is invalid.

## Commercial / Compliance Boundary

Precision Alpha is for internal research and supervised paper-trading development unless separately reviewed.

It must not be presented as:
- investment advice
- a managed trading service
- a signal service
- guaranteed returns
- financial promotion material

Any external use, client use, public content, or monetisation requires a compliance review first.

