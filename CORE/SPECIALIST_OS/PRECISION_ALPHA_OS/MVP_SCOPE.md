# Precision Alpha MVP Scope

Status: locked
Purpose: Prevent complexity drift.

## Market Scope

```yaml
assets:
  - BTC
  - ETH

market:
  crypto

execution_style:
  swing_trading

timeframes:
  - 4H
  - 1D
```

## MVP Restrictions

```yaml
no_autonomous_execution: true
human_approval_required: true
paper_trading_first: true
no_self_modifying_agents: true
self_modification_disabled_in_mvp: true
data_validation_required: true
process_quality_weighted_higher_than_pnl: true
```

## MVP Agent Limit

```yaml
mvp_agent_limit: 5
```

Allowed MVP agents:
- Market Data Agent
- Regime Agent
- Thesis Agent
- Risk Officer
- Reflection Agent

Deferred agents:
- Sentiment Agent
- Macro Agent
- Onchain Agent
- Advanced Liquidity Agent
- Execution Supervisor beyond paper-trade logging

## MVP Success Criteria

The MVP is successful when:
- every trade thesis is complete
- no thesis bypasses risk review
- no confidence score exists without evidence
- the system can say no trade clearly
- all human approvals and overrides are logged
- all paper trades receive post-trade review
- memory only updates after review
- audit trail is complete

MVP success is not measured by profit first.

## Do Not Build Yet

Do not build:
- live exchange execution
- autonomous trade placement
- self-modifying strategies
- complex multi-agent orchestration
- advanced ML regime classifier
- sentiment-triggered trades
- external client-facing signal product

