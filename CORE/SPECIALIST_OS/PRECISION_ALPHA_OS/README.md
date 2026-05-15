# Axis Precision Alpha OS

Status: active specialist OS bootstrap
Purpose: Institutional-style AI financial intelligence operating system for supervised crypto swing-trading research.
Platform: Codex-ready planning and implementation layer

## What This Is

Precision Alpha is a governed financial intelligence system.

It is designed to support:
- structured market reasoning
- BTC / ETH swing-trading research
- 4H and Daily timeframe analysis
- regime-aware trade thesis generation
- confidence scoring
- risk officer review
- paper-trading only execution records
- post-trade review and learning

## What This Is Not

Precision Alpha is not:
- a trading bot
- an autonomous execution system
- investment advice
- a signal-selling service
- a magic prediction engine
- HFT
- a replacement for professional financial, legal, tax, or regulatory advice

## Core Principle

```text
Decision quality > prediction hype
```

The system must optimise for governed decision process, evidence quality, risk discipline, and auditability before performance.

## MVP Scope

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

paper_trading_first: true
human_approval_required: true
no_autonomous_execution: true
no_self_modifying_agents: true
```

## Start Command

```text
AXIS: PRECISION ALPHA
```

## Working Commands

| Command | Use |
|---|---|
| `AXIS: PRECISION ALPHA` | Start the Precision Alpha specialist OS |
| `AXIS: PA STATUS` | Show current project state and next action |
| `AXIS: PA THESIS` | Create a structured trade thesis for BTC/ETH |
| `AXIS: PA REGIME` | Run regime classification |
| `AXIS: PA RISK REVIEW` | Apply Risk Officer protocol |
| `AXIS: PA JOURNAL` | Create or update trade journal record |
| `AXIS: PA POST-TRADE REVIEW` | Review a completed paper trade |
| `AXIS: PA BUILD NEXT` | Continue the implementation roadmap |

## File Map

```text
PRECISION_ALPHA_OS/
  README.md
  MASTER_CONTEXT.md
  GOVERNANCE_CONSTITUTION.md
  MVP_SCOPE.md
  IMPLEMENTATION_ROADMAP.md
  DATABASE_SCHEMA_MVP.md
  RISK_OFFICER_PROTOCOL.md
  REGIME_ENGINE_SPEC.md
  CONFIDENCE_ENGINE_SPEC.md
  TRADE_JOURNAL_SCHEMA.md
  REFLECTION_ENGINE_SPEC.md
  REAL_WORLD_DEPLOYMENT_PLAN.md
  OPEN_DECISIONS.md
```

## Current Build Priority

Build a supervised paper-trading intelligence OS first:

1. Governance constitution
2. Trade journal schema
3. Rule-based regime MVP
4. Confidence scoring MVP
5. Risk Officer MVP
6. Paper trading simulator
7. Reflection and learning loop

Do not build live execution until the system has passed review over a meaningful paper-trading sample.
