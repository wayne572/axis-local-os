# Precision Alpha Reflection Engine Spec

Status: active design spec
Purpose: Define how the system learns without corrupting itself.

## Core Principle

Reflection may recommend change.

Reflection may not self-deploy strategy changes during MVP.

```yaml
self_modification_disabled_in_mvp: true
no_memory_update_without_review: true
process_quality_weighted_higher_than_pnl: true
```

## Reflection Inputs

Reflection uses only reviewed records:
- completed trade thesis
- risk review
- paper trade record
- post-trade review
- process quality score
- confidence calibration note
- regime accuracy note

## Mistake Classification

Allowed mistake types:
- bad data
- weak evidence
- regime mismatch
- confidence overstated
- ignored contradiction
- risk rule violation
- emotional override
- late entry
- poor exit discipline
- thesis was good but market invalidated normally
- no mistake / acceptable process

## Learning Updates

Reflection can recommend:
- confidence weight adjustment
- regime rule review
- risk rule tightening
- setup archive
- setup watchlist
- journal template improvement
- data quality improvement

Reflection cannot:
- auto-deploy a new strategy
- increase live risk
- bypass Risk Officer
- overwrite historical audit records

## Memory Compression

Memory should store:
- concise setup pattern
- context
- mistake
- process lesson
- confidence calibration insight
- rule implication

Memory should not store:
- bloated reasoning chains
- repeated market commentary
- unreviewed opinions
- unvalidated claims

## Reflection Output Format

```text
Reflection Summary:

Trade ID:
Process Quality:
Result:
Mistake Type:
Confidence Calibration:
Regime Accuracy:
Lesson:
Recommended Rule Change:
Memory Update Allowed:
Needs Human Review:
```

