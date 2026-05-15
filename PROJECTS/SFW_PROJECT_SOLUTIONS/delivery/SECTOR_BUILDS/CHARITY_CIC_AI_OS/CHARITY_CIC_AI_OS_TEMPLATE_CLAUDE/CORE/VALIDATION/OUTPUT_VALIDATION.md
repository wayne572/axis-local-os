# Charity And CIC Output Validation

Status: active
Purpose: Final quality gate for charity/CIC client outputs.

## Checks

Before delivering an output, confirm:

1. It answers the request.
2. It is clear.
3. It is complete enough to use.
4. It fits agreed scope.
5. It has a next action.
6. It flags risks or blockers.
7. It does not invent organisation facts.
8. It handles personal data and sensitive data carefully.
9. It does not make safeguarding, eligibility, legal, clinical, financial, or trustee decisions.
10. It marks sensitive or public-facing outputs `in review`.

## Stop Conditions

Stop and ask for clarification if:
- organisation facts are missing
- scope is unclear
- legal/compliance wording is being changed
- personal data use is unclear
- safeguarding concerns are present
- the organisation asks the OS to decide support eligibility, risk level, legal position, medical advice, financial advice, or board approval
- the organisation asks for something outside agreed scope

## Review States

Use:
- draft
- in review
- locked
- superseded

