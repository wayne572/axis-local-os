# Precision Alpha Regime Engine Spec

Status: active MVP spec
Purpose: Classify market environment before trade thesis generation.

## Core Rule

```yaml
no_trade_without_regime_match: true
minimum_regime_confidence: 70
```

## Full Target Regime Dimensions

```yaml
trend:
volatility:
liquidity:
macro:
sentiment:
structural_behavior:
```

## MVP Dimensions

Start with:
- trend
- volatility
- liquidity

Defer:
- macro
- sentiment
- structural behaviour

## Trend Classifications

Allowed values:
- bullish trend
- bearish trend
- range
- transition
- unclear

Suggested rule inputs:
- 20 EMA
- 50 EMA
- 200 EMA
- higher high / lower low structure
- 4H and 1D alignment

## Volatility Classifications

Allowed values:
- low
- normal
- high
- extreme

Suggested rule inputs:
- ATR percentile
- recent candle range
- volatility expansion vs rolling baseline
- gap / wick anomaly

## Liquidity Classifications

Allowed values:
- acceptable
- thin
- unstable
- poor

Suggested rule inputs:
- volume vs rolling average
- spread proxy
- exchange stability notes
- abnormal candle / volume behaviour

## Regime Output

```yaml
asset:
timeframe:
timestamp:
trend:
volatility:
liquidity:
regime_confidence:
regime_match:
no_trade_reason:
evidence:
data_quality:
```

## No-Trade Conditions

No trade if:
- regime confidence below 70
- data validation failed
- trend is unclear and setup requires trend
- volatility is extreme and setup is not volatility-specific
- liquidity is poor
- risk officer vetoes

