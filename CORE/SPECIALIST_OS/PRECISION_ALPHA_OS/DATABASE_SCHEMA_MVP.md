# Precision Alpha Database Schema MVP

Status: active implementation spec
Purpose: Define the first PostgreSQL schema for Precision Alpha journal, governance, audit, and paper-trading memory.

## Design Principle

The database exists to preserve decision quality.

It must record:
- what the system saw
- what the system believed
- what evidence supported the belief
- what risk review decided
- what the human approved or overrode
- what happened in paper trading
- what was learned after review

## Non-Negotiable Rules

```yaml
no_trade_without_risk_review: true
no_memory_update_without_review: true
no_confidence_without_evidence: true
no_unlogged_human_override: true
no_silent_edits: true
paper_trade_only_in_mvp: true
```

## MVP Tables

Core tables:

1. `market_candles`
2. `regime_snapshots`
3. `trade_theses`
4. `risk_reviews`
5. `human_approvals`
6. `paper_trades`
7. `trade_reviews`
8. `memory_updates`
9. `audit_log`

Do not add vector memory yet. Reviewed relational memory comes first.

---

## 1. market_candles

Purpose:
Store validated BTC/ETH market candles for 4H and 1D timeframes.

```sql
CREATE TABLE market_candles (
    candle_id BIGSERIAL PRIMARY KEY,
    asset TEXT NOT NULL CHECK (asset IN ('BTC', 'ETH')),
    timeframe TEXT NOT NULL CHECK (timeframe IN ('4H', '1D')),
    source TEXT NOT NULL,
    opened_at TIMESTAMPTZ NOT NULL,
    closed_at TIMESTAMPTZ NOT NULL,
    open_price NUMERIC(18, 8) NOT NULL,
    high_price NUMERIC(18, 8) NOT NULL,
    low_price NUMERIC(18, 8) NOT NULL,
    close_price NUMERIC(18, 8) NOT NULL,
    volume NUMERIC(28, 8),
    data_quality_score NUMERIC(5, 2) NOT NULL DEFAULT 100,
    validation_notes TEXT,
    ingested_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE (asset, timeframe, source, opened_at)
);
```

Validation rules:
- no duplicate candles
- no missing timestamps without validation note
- high must be greater than or equal to open, close, and low
- low must be less than or equal to open, close, and high
- `closed_at` must be after `opened_at`

---

## 2. regime_snapshots

Purpose:
Record the market regime used at the point of thesis creation.

```sql
CREATE TABLE regime_snapshots (
    regime_id UUID PRIMARY KEY,
    asset TEXT NOT NULL CHECK (asset IN ('BTC', 'ETH')),
    timeframe TEXT NOT NULL CHECK (timeframe IN ('4H', '1D')),
    evaluated_at TIMESTAMPTZ NOT NULL,
    trend TEXT NOT NULL CHECK (trend IN ('bullish_trend', 'bearish_trend', 'range', 'transition', 'unclear')),
    volatility TEXT NOT NULL CHECK (volatility IN ('low', 'normal', 'high', 'extreme')),
    liquidity TEXT NOT NULL CHECK (liquidity IN ('acceptable', 'thin', 'unstable', 'poor')),
    regime_confidence NUMERIC(5, 2) NOT NULL CHECK (regime_confidence >= 0 AND regime_confidence <= 100),
    regime_match BOOLEAN NOT NULL,
    no_trade_reason TEXT,
    evidence JSONB NOT NULL,
    data_quality_score NUMERIC(5, 2) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

Rule:
If `regime_confidence` is below 70, `regime_match` should normally be false unless explicitly justified and reviewed.

---

## 3. trade_theses

Purpose:
Store the structured trade thesis before risk review.

```sql
CREATE TABLE trade_theses (
    trade_id UUID PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    asset TEXT NOT NULL CHECK (asset IN ('BTC', 'ETH')),
    timeframe TEXT NOT NULL CHECK (timeframe IN ('4H', '1D')),
    direction TEXT NOT NULL CHECK (direction IN ('long', 'short', 'no_trade')),
    setup_type TEXT NOT NULL,
    lifecycle_state TEXT NOT NULL CHECK (
        lifecycle_state IN (
            'thesis_created',
            'risk_review_pending',
            'risk_vetoed',
            'human_approval_pending',
            'approved_for_paper',
            'paper_trade_open',
            'monitoring',
            'exited',
            'review_pending',
            'reviewed',
            'memory_update_pending',
            'memory_updated',
            'archived'
        )
    ),
    regime_id UUID REFERENCES regime_snapshots(regime_id),
    market_context JSONB NOT NULL,
    evidence_block JSONB NOT NULL,
    contradiction_block JSONB NOT NULL,
    confidence_score NUMERIC(5, 2) NOT NULL CHECK (confidence_score >= 0 AND confidence_score <= 100),
    confidence_reason TEXT NOT NULL,
    invalidation_level NUMERIC(18, 8),
    proposed_entry NUMERIC(18, 8),
    proposed_stop NUMERIC(18, 8),
    proposed_target NUMERIC(18, 8),
    proposed_risk_r NUMERIC(8, 4),
    expected_holding_period TEXT,
    thesis_summary TEXT NOT NULL,
    created_by TEXT NOT NULL DEFAULT 'Precision Alpha',
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

Rules:
- `evidence_block` cannot be empty.
- `confidence_score` above 90 requires historical validation evidence.
- `direction = no_trade` is valid and should be logged when appropriate.
- Thesis edits must create `audit_log` records.

---

## 4. risk_reviews

Purpose:
Store Risk Officer review and veto authority.

```sql
CREATE TABLE risk_reviews (
    risk_review_id UUID PRIMARY KEY,
    trade_id UUID NOT NULL REFERENCES trade_theses(trade_id),
    reviewed_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    decision TEXT NOT NULL CHECK (
        decision IN (
            'veto',
            'approve_for_paper_only',
            'reduce_risk',
            'defer_pending_data',
            'request_human_review',
            'reject_incomplete_thesis'
        )
    ),
    veto_reason TEXT,
    position_risk JSONB NOT NULL,
    portfolio_risk JSONB NOT NULL,
    regime_risk JSONB NOT NULL,
    volatility_risk JSONB NOT NULL,
    liquidity_risk JSONB NOT NULL,
    event_risk JSONB NOT NULL,
    confidence_integrity JSONB NOT NULL,
    required_changes TEXT,
    reviewed_by TEXT NOT NULL DEFAULT 'Risk Officer',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

Rule:
No trade can move to `human_approval_pending` or `approved_for_paper` without a risk review decision.

---

## 5. human_approvals

Purpose:
Record Wayne's approval, rejection, or override.

```sql
CREATE TABLE human_approvals (
    approval_id UUID PRIMARY KEY,
    trade_id UUID NOT NULL REFERENCES trade_theses(trade_id),
    risk_review_id UUID NOT NULL REFERENCES risk_reviews(risk_review_id),
    approval_status TEXT NOT NULL CHECK (approval_status IN ('approved', 'rejected', 'override')),
    approved_by TEXT NOT NULL,
    approved_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    reason TEXT NOT NULL,
    override_flag BOOLEAN NOT NULL DEFAULT FALSE,
    override_reason TEXT,
    paper_trade_only BOOLEAN NOT NULL DEFAULT TRUE
);
```

Rules:
- Overrides must include `override_reason`.
- MVP must keep `paper_trade_only = true`.
- No unlogged human override is allowed.

---

## 6. paper_trades

Purpose:
Track supervised paper execution and outcome.

```sql
CREATE TABLE paper_trades (
    paper_trade_id UUID PRIMARY KEY,
    trade_id UUID NOT NULL REFERENCES trade_theses(trade_id),
    approval_id UUID NOT NULL REFERENCES human_approvals(approval_id),
    opened_at TIMESTAMPTZ,
    entry_price NUMERIC(18, 8),
    stop_price NUMERIC(18, 8),
    target_price NUMERIC(18, 8),
    paper_size NUMERIC(18, 8),
    current_state TEXT NOT NULL CHECK (current_state IN ('not_opened', 'open', 'monitoring', 'exited', 'cancelled')),
    monitoring_notes JSONB NOT NULL DEFAULT '[]'::jsonb,
    exit_time TIMESTAMPTZ,
    exit_price NUMERIC(18, 8),
    exit_reason TEXT,
    result_r_multiple NUMERIC(10, 4),
    pnl_paper NUMERIC(18, 8),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

Rules:
- This table is paper only.
- A trade must be `exited` or `cancelled` before post-trade review.
- Monitoring notes should be concise.

---

## 7. trade_reviews

Purpose:
Force post-trade reflection before memory update.

```sql
CREATE TABLE trade_reviews (
    review_id UUID PRIMARY KEY,
    trade_id UUID NOT NULL REFERENCES trade_theses(trade_id),
    paper_trade_id UUID NOT NULL REFERENCES paper_trades(paper_trade_id),
    reviewed_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    thesis_quality NUMERIC(5, 2) NOT NULL CHECK (thesis_quality >= 0 AND thesis_quality <= 100),
    process_quality_score NUMERIC(5, 2) NOT NULL CHECK (process_quality_score >= 0 AND process_quality_score <= 100),
    risk_discipline_score NUMERIC(5, 2) NOT NULL CHECK (risk_discipline_score >= 0 AND risk_discipline_score <= 100),
    confidence_calibration TEXT NOT NULL,
    regime_accuracy TEXT NOT NULL,
    mistake_type TEXT NOT NULL CHECK (
        mistake_type IN (
            'bad_data',
            'weak_evidence',
            'regime_mismatch',
            'confidence_overstated',
            'ignored_contradiction',
            'risk_rule_violation',
            'emotional_override',
            'late_entry',
            'poor_exit_discipline',
            'normal_invalidation',
            'no_mistake_acceptable_process'
        )
    ),
    lesson TEXT NOT NULL,
    memory_update_allowed BOOLEAN NOT NULL DEFAULT FALSE,
    reviewed_by TEXT NOT NULL DEFAULT 'Reflection Agent'
);
```

Rules:
- Process quality is more important than PnL.
- Memory update is blocked unless `memory_update_allowed = true`.

---

## 8. memory_updates

Purpose:
Store reviewed learning only.

```sql
CREATE TABLE memory_updates (
    memory_update_id UUID PRIMARY KEY,
    trade_id UUID NOT NULL REFERENCES trade_theses(trade_id),
    review_id UUID NOT NULL REFERENCES trade_reviews(review_id),
    update_type TEXT NOT NULL CHECK (
        update_type IN (
            'setup_pattern',
            'risk_rule',
            'confidence_calibration',
            'regime_rule',
            'strategy_decay',
            'data_quality',
            'journal_improvement'
        )
    ),
    summary TEXT NOT NULL,
    rule_implication TEXT,
    approved_for_memory BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

Rules:
- No reviewed trade, no memory update.
- No bloated reasoning.
- Store the lesson, not the whole argument.

---

## 9. audit_log

Purpose:
Immutable audit trail for governance and trust.

```sql
CREATE TABLE audit_log (
    audit_id BIGSERIAL PRIMARY KEY,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    actor TEXT NOT NULL,
    action TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    entity_id TEXT NOT NULL,
    previous_state JSONB,
    new_state JSONB,
    reason TEXT,
    source TEXT NOT NULL DEFAULT 'Precision Alpha'
);
```

Rules:
- No silent edits.
- Every lifecycle state change must be logged.
- Every human override must be logged.
- Every memory update must be logged.

---

## Suggested Indexes

```sql
CREATE INDEX idx_market_candles_asset_timeframe_opened
ON market_candles(asset, timeframe, opened_at);

CREATE INDEX idx_regime_snapshots_asset_timeframe_time
ON regime_snapshots(asset, timeframe, evaluated_at);

CREATE INDEX idx_trade_theses_asset_timeframe_state
ON trade_theses(asset, timeframe, lifecycle_state);

CREATE INDEX idx_risk_reviews_trade_id
ON risk_reviews(trade_id);

CREATE INDEX idx_paper_trades_trade_id
ON paper_trades(trade_id);

CREATE INDEX idx_trade_reviews_trade_id
ON trade_reviews(trade_id);

CREATE INDEX idx_memory_updates_trade_id
ON memory_updates(trade_id);

CREATE INDEX idx_audit_log_entity
ON audit_log(entity_type, entity_id);
```

---

## Implementation Notes

Use UUIDs for decision-linked records:
- trade thesis
- regime snapshot
- risk review
- approval
- paper trade
- trade review
- memory update

Use `BIGSERIAL` for high-volume append-only records:
- market candles
- audit log

Use `JSONB` where the evidence or risk structure may evolve.

Do not use JSONB to avoid designing core fields. Core governance fields must stay queryable.

---

## First Build Target

The first implementation should support this manual flow:

```text
Create thesis
-> attach regime snapshot
-> score confidence
-> run risk review
-> log human approval
-> open paper trade
-> exit paper trade
-> complete post-trade review
-> approve memory update
-> write audit log
```

If that flow works, Precision Alpha has a trustworthy foundation.

