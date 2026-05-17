# MARKET_JOURNAL.md

## 1. Status
Active - Execution Sub-File

---

## 2. Purpose
Track trades and behaviour.

---

## 3. Core Principle

Track discipline, not just profit.

---

## 4. Required Data

- asset
- entry
- stop
- target
- result
- emotion
- rules followed
- risk amount (must be pulled from MARKET_RISK_ENGINE output before logging)

---

## 5. Discipline Score

Score 0-5:

- correct setup
- valid rules
- risk respected
- emotional control
- plan followed

---

## 6. Output

Discipline score per trade

---

## 7. Failure Conditions

- not logging trades
- dishonest tracking
- ignoring patterns
- logging without the risk amount from MARKET_RISK_ENGINE

---

## 8. End State

You learn from every trade.
