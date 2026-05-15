# Precision Alpha Real-World Deployment Plan

Status: active
Purpose: Keep implementation practical and safe.

## Recommended Stack For MVP

```yaml
backend: Python
database: PostgreSQL
dashboard: Streamlit
market_data: Binance public market data
macro_data_later: FRED
simulation_later: Freqtrade
orchestration_later: LangGraph
vector_memory_later: TBD
```

## Why This Stack

Python:
Best fit for data, scoring, backtesting, and financial tooling.

PostgreSQL:
Best first memory layer for auditability, relational journal records, JSON fields, and queryable history.

Streamlit:
Fastest route to a human approval dashboard without overbuilding.

Binance market data:
Practical source for BTC/ETH candle data.

FRED:
Useful later for macro context.

Freqtrade:
Useful later for backtesting and dry-run simulation after governance exists.

LangGraph:
Useful later for human-in-the-loop agent workflows once the process is proven.

## Deployment Stages

### Stage 1 - Local Research OS

Runs locally.

No API keys for execution.

Data only.

### Stage 2 - Local Paper Trading OS

Adds paper trade records and dashboard.

Still no live execution.

### Stage 3 - Backtesting Integration

Adds Freqtrade or equivalent for historical simulation.

Still supervised.

### Stage 4 - Human-In-The-Loop Workflow

Adds LangGraph or equivalent if manual workflow becomes hard to manage.

### Stage 5 - Live Execution Review

Do not proceed without:
- legal / compliance review
- risk review
- technical security review
- extended paper-trading evidence
- strict human approval gateway

## Compliance Reminder

This OS must remain internal research infrastructure unless separately reviewed.

Do not market as:
- investment advice
- trade signal service
- managed trading product
- guaranteed return system

