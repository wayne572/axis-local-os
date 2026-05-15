# Precision Alpha Open Decisions

Status: active
Purpose: Track unresolved choices without losing assumptions.

## Open Decisions

```yaml
confidence_weight_values: unresolved
regime_thresholds: unresolved
vector_db_choice: unresolved
dashboard_architecture: unresolved
portfolio_correlation_model: unresolved
adaptive_sizing_formulas: unresolved
reflection_update_logic: unresolved
market_data_storage_granularity: unresolved
event_calendar_source: unresolved
paper_trade_execution_model: unresolved
```

## Decision Rules

Do not resolve these by assumption.

Each decision needs:
- options
- trade-offs
- recommendation
- risk
- MVP impact
- decision owner
- review date

## Current Recommendation

Resolve in this order:

1. Database schema and journal fields
2. Market data source and storage rules
3. Regime thresholds
4. Confidence weight placeholders
5. Risk Officer hard limits
6. Dashboard approach
7. Reflection update rules
8. Vector memory choice

## Deferred Until After Paper-Trading Evidence

Do not finalise yet:
- adaptive sizing formulas
- agent performance weights
- advanced portfolio correlation model
- live execution gateway
- external-facing product model

