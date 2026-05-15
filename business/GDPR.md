# GDPR Record — [BUSINESS_NAME]

This file is the customer's master GDPR record. Populated at Onboarding Stage 5 and Handover Stage 4. Read by the gdpr agent on every request.

**Status:** [DRAFT — to be populated at handover]

---

## 1. Lawful basis for processing

**Primary basis:** [Legitimate interest / Consent / Contract / Legal obligation]

**Reasoning:** [One paragraph from the customer explaining why this basis applies]

**Date declared:** [DATE]

---

## 2. Special category data

Does the business process special category data (health, biometric, political, religious, sexual orientation, race)?

- [ ] No
- [ ] Yes — type: [specify]

If yes, the customer has been advised to consult their own DPO or solicitor before deploying. Additional safeguards required.

---

## 3. ICO registration

- [ ] Registered. Reference: [ICO REF]
- [ ] Not yet registered. Will register within 14 days of handover.

ICO registration URL: ico.org.uk/registration

---

## 4. Data Processing Agreements (DPAs)

For each connected tool, the customer must sign the standard DPA. Track here:

| Tool | DPA signed | Date | Reference |
|---|---|---|---|
| [Tool 1] | [Y/N] | [date] | [ref] |
| [Tool 2] | [Y/N] | [date] | [ref] |

DPA links are in `business/HANDOVER/GDPR_PROTOCOL.md` Annex A.

---

## 5. Retention schedule (defaults)

[Pulled from GDPR_PROTOCOL.md based on stacks deployed. Customer can override with documented reason.]

| Data type | Retention | Source |
|---|---|---|
| [e.g. Unconverted leads] | [12 months] | [Stack 01 default] |

---

## 6. International transfers

| Tool | Country | DPF certified | Notes |
|---|---|---|---|
| [Tool] | [Country] | [Y/N] | [verified date] |

---

## 7. Data subject rights — operational readiness

- SAR workflow: handled by gdpr agent — type `Run a Subject Access Request for [name]`
- Right to erasure: handled by gdpr agent — type `Erase [name] from the system`
- Right to rectification: customer edits records directly in Airtable; the gdpr agent can guide
- Right to data portability: gdpr agent exports a JSON or CSV on request
- Right to object: customer adds the data subject to `GDPR_SUPPRESSION_LIST.md`

---

## 8. DPO / privacy point of contact

**Designated person:** [Name and role within customer's business]
**Contact email:** [email]

If the customer has no formal DPO (most SMEs don't need one), the owner is the default privacy point of contact.

---

## 9. Last review

**Date:** [DATE]
**Next review due:** [DATE + 6 months]

The customer should review this file every 6 months or whenever:
- A new tool is added to the stack
- The business changes structure (sale, merger)
- ICO guidance changes materially
- A breach occurs

---

*This file lives in the customer's own folder and is owned by them. Axis OS does not transmit it externally.*
