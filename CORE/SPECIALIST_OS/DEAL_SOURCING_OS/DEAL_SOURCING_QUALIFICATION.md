# DEAL_SOURCING_QUALIFICATION.md

## 1. Status
Active - Execution Sub-File

---

## 2. Purpose
Define how leads and replies are filtered so only high-fit opportunities move toward Sales OS.

This file controls:

- qualification criteria
- scoring
- disqualification signals
- compliance hard stops

---

## 3. Core Principle

Not every lead is worth pursuing.

Focus only on good fit, real need, ability to pay - and drop the rest cleanly.

---

## 4. System Rules (Deep Logic)

### Qualification stages
1. **Lead Match** - does the person match the ICP one-pager? If no -> drop.
2. **Reply Quality** - did they reply with intent (question, interest, objection)? A "no thanks" is a clean close.
3. **Discovery Fit** - do their needs map to what the user offers? If no -> polite hand-off or close.
4. **Buying Conditions** - do they have the problem, a budget signal, decision power (or access), and a timeline?
   - 3 of 4 -> progress to Sales OS.
   - Fewer -> nurture or drop.

### Scoring
- YES -> proceed
- MAYBE -> nurture
- NO -> drop

### Disqualification signals
- Not the decision-maker and no path to one
- Timeline is "someday"
- Wants services outside scope
- Unrealistic expectations
- Poor communication
- Cold across three touches
- No budget signal at all

### UK Compliance hard stops (must drop)
- Target is in a high-risk vertical without sign-off (recruitment screening, credit, medical, biometric)
- AML-regulated activity without CDD in place
- Request involves special category data
- Prospect is B2C without opt-in

When a hard stop is hit -> flag and stop. No exceptions.

### Edge cases
- A "MAYBE" with strong ICP match but unclear timeline -> set 30-day nurture, not drop.
- A "YES" missing budget but strong problem and decision power -> still progress; budget surfaces in Sales OS.
- If user is uncertain -> ask one clarifying question; do not guess.

---

## 5. Execution Steps (User Layer)

1. Open the tracker.
2. For each replied lead, run the 4-stage check.
3. Apply YES / MAYBE / NO.
4. For YES: add discovery fit notes, set next action, hand off to Sales OS.
5. For MAYBE: set nurture follow-up date.
6. For NO: close cleanly, log reason in one line.
7. Confirm no compliance hard stop has been crossed.
8. Update tracker status.

---

## 6. Example

**Lead:** James, MD of a 6-person UK accountancy firm, replied to outreach asking about lead flow help.

- Lead Match: yes (UK, 1-10, owner, lead-flow problem)
- Reply Quality: yes (asked a question)
- Discovery Fit: yes (offer fits)
- Buying Conditions: problem PASS, budget PASS signal, decision-maker PASS, timeline PASS ("next quarter")
- **Compliance check:** AML-regulated sector -> CDD must be in place before pipeline activity. **HOLD.**
- Action: pause until CDD confirmed, then move to Sales OS.

---

## 7. Output Requirement

Each lead must be:

- clearly marked YES / MAYBE / NO
- tagged with discovery notes
- compliance-checked
- moved to the correct next stage with a date

---

## 8. Failure Conditions

Qualification has failed if:

- all leads are treated equally
- poor-fit prospects are pursued out of optimism
- compliance hard stops are missed
- no clear reason is logged when dropping a lead
- leads sit in MAYBE forever without a nurture date

---

## 9. End State

Qualification is working when:

- the user's time is on real opportunities
- conversion rates climb
- compliance risks are caught before they cost
- every lead has a status, a reason, and a next action
