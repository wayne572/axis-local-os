# Axis OS v2 — Test Harness

End-to-end test scenarios the Handover Agent runs at Stage 6 to confirm a customer's stack actually works before sign-off.

**Rule of use:** Stage 6 cannot be marked complete until at least one test runs end-to-end with a green result. If the test fails, halt and troubleshoot using SETUP_SCRIPTS.md. Never sign off a broken handover.

---

## How the Handover Agent uses this file

1. Identify which stacks were deployed (from Stage 4 approval)
2. For each deployed stack, run its matching test scenario below
3. Walk the customer through each step — they perform the action, you watch the result
4. Confirm every checkpoint before moving to the next step
5. If any checkpoint fails, run the troubleshooting flow and re-test
6. Mark Stage 6 complete only when all tests for deployed stacks pass

---

## Test 01 — Lead Qualifier (Stack 01)

**What this proves:** a real enquiry flows from form to database to email draft to Slack ping without anything breaking.

**Setup**
- All Stack 01 tools must be set up and verified individually first
- The Lead Qualifier Zap must be turned ON in Zapier
- Slack channel `#axis-os-alerts` must exist and the customer must have it open
- Gmail must be open in another tab
- Airtable must be open in another tab

**Dummy data to use**
```
Name: Test Lead — Axis OS Setup
Email: [customer's own email — not the business email, ideally a personal one]
Phone: 07000 000000
Message: This is a test enquiry submitted during Axis OS v2 handover. Please ignore.
Source: Website
```

**Test steps**

| # | Action | Checkpoint |
|---|---|---|
| 1 | Open the live Typeform link in an incognito browser window | Form loads with the customer's branding |
| 2 | Fill in the dummy data and submit | Typeform shows "thank you" screen |
| 3 | Switch to Airtable tab and refresh | New row appears in the Leads table within 30 seconds, all fields populated correctly |
| 4 | Switch to Gmail tab and check Drafts | New draft appears with subject "New enquiry — Test Lead — Axis OS Setup" within 30 seconds |
| 5 | Switch to Slack `#axis-os-alerts` | New message reads: "New lead from Test Lead — Axis OS Setup — Website" |
| 6 | Open the Gmail draft and verify body content | Body uses the customer's voice (BRAND.md), greets the lead, signs off correctly |

**Pass criteria:** all 6 checkpoints green within 60 seconds of form submission.

**If it fails — troubleshooting order**
- Checkpoint 3 fails (Airtable) → Token expired or field mapping wrong. Re-run Airtable section of SETUP_SCRIPTS.md.
- Checkpoint 4 fails (Gmail draft) → Gmail account disconnected from Zapier. Reconnect and re-test.
- Checkpoint 5 fails (Slack) → Webhook URL wrong or Slack app not installed. Re-run Slack section of SETUP_SCRIPTS.md.
- Checkpoint 6 fails (voice wrong) → Update BRAND.md with stronger voice notes, regenerate the draft template.

**Cleanup after pass**
- Delete the test row in Airtable
- Delete the test draft in Gmail
- Leave the Slack message — useful as a reference for the customer

---

## Test 02 — Booking & Onboarding (Stack 02)

**What this proves:** a customer can book a slot, the booking lands in the calendar, and the onboarding email sequence kicks off.

**Setup**
- Calendly event type live, Airtable onboarding tracker built, Zap connecting them is ON

**Dummy data**
- Use the customer's own personal email to book a slot in the future (then cancel)

**Test steps**

| # | Action | Checkpoint |
|---|---|---|
| 1 | Open the Calendly booking link in incognito | Page loads with available slots |
| 2 | Book a slot for tomorrow morning | Confirmation page shows |
| 3 | Check the customer's calendar (Google or Outlook) | Event appears at the correct time with correct title |
| 4 | Check Airtable onboarding tracker | New row appears with the booking details |
| 5 | Check Gmail inbox | Calendly confirmation email received |
| 6 | Check Gmail Drafts | Welcome email draft created (Axis OS-generated, not Calendly's default) |

**Pass criteria:** all 6 checkpoints green within 60 seconds.

**Cleanup:** cancel the test booking, delete test row in Airtable, delete welcome draft.

---

## Test 03 — Content Engine (Stack 03)

**What this proves:** the agent can produce a brand-aligned post batch and the customer can schedule it through Buffer.

**Setup**
- BRAND.md and CONTENT_THEMES.md are populated
- Buffer is connected to LinkedIn (and any other approved platform)
- Airtable content log exists

**Test steps**

| # | Action | Checkpoint |
|---|---|---|
| 1 | Run the LinkedIn agent: "Draft 3 posts for this week based on CONTENT_THEMES" | 3 posts produced |
| 2 | Run the QA agent on the output | QA returns a pass or specific edits |
| 3 | Apply edits if any, then copy the final post into Buffer | Buffer shows the post in the queue |
| 4 | Schedule for tomorrow morning | Buffer confirms scheduled time |
| 5 | Add a row to Airtable content log | Row created with post text, platform, scheduled date |

**Pass criteria:** all 5 checkpoints green. Customer can see the scheduled post in Buffer.

**Cleanup:** unschedule the test post in Buffer (it was a real post that would have gone out — better to keep it scheduled if the customer is happy with the content).

---

## Test 04 — Pipeline & Reporting (Stack 04)

**What this proves:** the customer can get a real status report and the data is accurate.

**Setup**
- Airtable pipeline has at least 3 sample rows (use real data from Onboarding interview if available, or dummy data with a clear "TEST" tag)

**Test steps**

| # | Action | Checkpoint |
|---|---|---|
| 1 | Customer types: `What is the current status?` | Agent returns a status report within 30 seconds |
| 2 | Compare report numbers to Airtable manually | Numbers match exactly |
| 3 | Check the report includes: open leads, active clients, next 3 actions | All three sections present |
| 4 | Customer types: `Let's do the monthly system review` | Agent runs the review flow |
| 5 | Confirm the review opens SYSTEM_REVIEW.md and walks the prompts | Yes |

**Pass criteria:** all 5 checkpoints green. Numbers must be exact — if they're off, the data layer is broken.

---

## Test 05 — Cash Flow & Invoicing (Stack 05)

**What this proves:** an overdue invoice triggers a chase email draft and a Slack ping.

**Setup**
- Invoice tracker in Airtable has at least one row with a due date in the past (manually set for the test)
- Zap connecting Airtable to Gmail and Slack is ON

**Test steps**

| # | Action | Checkpoint |
|---|---|---|
| 1 | Add a test invoice in Airtable with due date 8 days ago | Row created |
| 2 | Wait for the next Zap run (or manually trigger) | Zap fires |
| 3 | Check Gmail Drafts | Chase email draft created with correct invoice details |
| 4 | Check Slack | Overdue alert posted in `#axis-os-alerts` |

**Pass criteria:** all 4 checkpoints green.

**Cleanup:** delete the test invoice row, delete the draft, leave Slack message.

---

## Test 06 — Proposal & Contract (Stack 06)

**What this proves:** a proposal sent today triggers a follow-up draft at day 3 and day 7.

**Setup**
- Proposal tracker in Airtable
- Zap with delays for day 3 and day 7 follow-ups

**Test steps**

| # | Action | Checkpoint |
|---|---|---|
| 1 | Add a test proposal row with sent date = today | Row created |
| 2 | Use the Zap test feature to fast-forward both delay branches | Both delay branches fire successfully |
| 3 | Check Gmail Drafts for day 3 follow-up | Draft created with appropriate copy |
| 4 | Check Gmail Drafts for day 7 follow-up | Draft created with appropriate copy |

**Pass criteria:** all 4 checkpoints green. Day 7 draft must be more direct in tone than day 3 (Zap should be configured this way).

---

## Universal final test — The Owner Test

After all stack-specific tests pass, run this one regardless of stack:

**Test:** the customer types `What is the current status?` cold, with no other context.

**Expected:** within 30 seconds, they see a clear, accurate, useful snapshot of their business.

If the customer cannot make sense of the output, the handover is not complete. Improve MEMORY.md and re-run before sign-off.

---

## Failure escalation

If any test fails three times in a row after troubleshooting:

1. Halt Stage 6
2. Save state to `business/MEMORY.md`: "Stage 6 paused — Test [#] failed at checkpoint [#]. Reason: [diagnosis]."
3. Tell the customer: "Let's pause here. I want Wayne to look at this directly before we sign off — the system isn't ready until this passes."
4. Add a CHANGELOG.md entry: "Handover paused at Stage 6 — [customer] — [test] — [reason]"
5. Email Wayne the failure summary

Do not sign off a handover with a failing test. Sign-off implies the system works. If it doesn't work, it isn't signed off.

---

## Maintenance

**Quarterly review checklist (Wayne to run):**
- For each test, confirm checkpoints still match the actual tool behaviour
- Add new tests as new stacks are added to the catalogue
- Capture any new failure modes seen during real handovers
- Tighten timing thresholds (60-second pass criteria) if tools have got faster or slower

**Last reviewed:** 2026-04-30
**Next review due:** 2026-07-30
