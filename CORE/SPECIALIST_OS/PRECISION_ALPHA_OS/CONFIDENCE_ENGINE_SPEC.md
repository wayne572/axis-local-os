# Precision Alpha Confidence Engine Spec

Status: active MVP spec
Purpose: Score evidence strength and alignment quality without pretending to predict profit.

## Core Principle

```text
Confidence != probability of profit
```

Confidence means:
- evidence strength
- regime alignment
- historical validation
- multi-agent agreement
- contradiction handling
- environmental clarity

## Formula

```text
confidence =
evidence quality
+
regime alignment
+
historical validation
+
multi-agent agreement
-
contradiction penalties
-
environmental uncertainty
```

## MVP Components

| Component | MVP Weight Placeholder |
|---|---|
| Evidence quality | TBD |
| Regime alignment | TBD |
| Historical validation | TBD |
| Agent agreement | TBD |
| Contradiction penalty | TBD |
| Uncertainty penalty | TBD |

The weights are not locked yet. They must be calibrated after paper-trade review.

## Hard Rules

```yaml
no_confidence_without_evidence: true
confidence_above_90_requires_historical_validation: true
confidence_cannot_exceed_data_quality: true
contradictions_must_be_logged: true
```

## Confidence Bands

Suggested starting bands:
- 0-39: invalid or weak
- 40-59: low confidence
- 60-69: watchlist only
- 70-79: acceptable paper thesis if risk approves
- 80-89: strong paper thesis
- 90+: requires historical validation and exceptional evidence

## Output Format

```yaml
confidence_score:
confidence_band:
evidence_quality:
regime_alignment:
historical_validation:
agent_agreement:
contradictions:
uncertainty:
confidence_integrity_passed:
reason:
```

