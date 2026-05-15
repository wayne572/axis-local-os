# Precision Alpha Trade Journal Schema

Status: active schema spec
Purpose: Define the canonical journal and audit memory structure.

## Core Rule

```text
Incomplete trades cannot enter memory.
```

## Required Lifecycle States

Allowed states:
- thesis_created
- risk_review_pending
- risk_vetoed
- human_approval_pending
- approved_for_paper
- paper_trade_open
- monitoring
- exited
- review_pending
- reviewed
- memory_update_pending
- memory_updated
- archived

## Trade Thesis Record

Required fields:
- trade_id
- created_at
- asset
- timeframe
- direction
- setup_type
- market_context
- regime_snapshot_id
- evidence_block
- contradiction_block
- confidence_score
- invalidation_level
- proposed_entry
- proposed_stop
- proposed_target
- risk_notes
- human_approval_status

## Risk Review Record

Required fields:
- risk_review_id
- trade_id
- reviewed_at
- decision
- veto_reason
- position_risk
- portfolio_risk
- regime_risk
- volatility_risk
- liquidity_risk
- event_risk
- confidence_integrity
- required_changes
- reviewer

## Paper Trade Record

Required fields:
- paper_trade_id
- trade_id
- opened_at
- entry_price
- stop_price
- target_price
- paper_size
- monitoring_notes
- exit_time
- exit_price
- exit_reason
- result_r_multiple
- pnl_paper

## Post-Trade Review Record

Required fields:
- review_id
- trade_id
- reviewed_at
- thesis_quality
- process_quality_score
- risk_discipline_score
- confidence_calibration
- regime_accuracy
- mistake_type
- lesson
- memory_update_allowed

## Audit Log

Every material action must create an audit log entry:
- created thesis
- changed thesis
- risk review
- human approval
- human override
- paper entry
- paper exit
- post-trade review
- memory update

No silent edits.

