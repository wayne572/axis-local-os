# Charity And CIC Module Guide

Status: active
Purpose: Explains the organisation's available AI OS modules in plain English.

## What Modules Are

Modules are the jobs this AI OS can help with.

They are not separate bots.

The organisation talks to the same assistant, and the assistant uses the right module in the background.

## Available Modules

### 1. Command Centre

Use for:
- today's priorities
- overdue follow-ups
- blockers
- decisions needed
- weekly focus

Example prompt:

```text
Run today's command centre and show me what needs attention.
```

### 2. Referral And Enquiry Tracker

Use for:
- new enquiries
- partner referrals
- follow-up dates
- non-sensitive status tracking
- next-action reminders

Example prompt:

```text
Log this referral without unnecessary sensitive detail and draft the next follow-up.
```

### 3. Grants And Funding Pipeline

Use for:
- grant opportunities
- funder fit checks
- eligibility notes
- grant deadlines
- funder reporting dates
- renewal dates
- application task lists

Example prompt:

```text
Add this funder opportunity and create the next actions before the deadline.
```

### 4. Grant Application Support

Use for:
- application question breakdown
- draft answers
- evidence checklists
- project need statements
- budget narrative prompts
- final review lists

Example prompt:

```text
Break down this grant application and draft answers using only the evidence we have.
```

### 5. Fundraising Campaign Tracker

Use for:
- fundraising appeals
- campaign goals
- event fundraising
- supporter messages
- sponsor asks
- campaign follow-up

Example prompt:

```text
Build a fundraising campaign plan for this project with messages, dates, and follow-up actions.
```

### 6. Donor And Sponsor Stewardship

Use for:
- donor thank-you messages
- sponsor updates
- relationship follow-up
- renewal reminders
- supporter journeys

Example prompt:

```text
Create a donor follow-up plan and draft thank-you messages for these supporters.
```

### 7. Impact Evidence And Funder Reporting

Use for:
- outputs
- outcomes
- anonymised stories
- evidence gaps
- funder updates
- reporting deadlines

Example prompt:

```text
Create an anonymised funder update from these notes and flag any missing evidence.
```

### 8. Income Risk And Continuation Review

Use for:
- funding gaps
- grant end dates
- over-reliance on one funder
- missed reporting deadlines
- next funding actions

Example prompt:

```text
Run an income risk review and show the next funding actions for the next 90 days.
```

### 9. Social Media And Content Engine

Use for:
- post ideas
- image prompts
- Canva/design briefs
- captions
- comment replies
- donor thank-you posts
- volunteer recruitment posts
- fundraising campaign posts
- impact story posts
- short video/reel scripts
- weekly content calendars

Example prompt:

```text
Create a week of social posts for this campaign with image prompts, captions, comment replies, and human-review flags.
```

### 10. Volunteer And Partner Memory

Use for:
- volunteer notes
- partner relationships
- meeting context
- introductions
- follow-up reminders

Example prompt:

```text
Add this partner note and remind us what to follow up on next week.
```

### 11. Service Delivery Tracker

Use for:
- programme activity
- sessions and events
- operational blockers
- internal actions
- non-sensitive support updates

Example prompt:

```text
Update the service delivery tracker and flag anything blocked or overdue.
```

### 12. Governance And Board Reporting

Use for:
- trustee updates
- board summaries
- decision logs
- risk notes
- monthly progress reports

Example prompt:

```text
Turn these updates into a board-ready summary with decisions, risks, and next actions.
```

### 13. Communications Drafting

Use for:
- volunteer messages
- partner updates
- donor thanks
- standard replies
- newsletter drafts
- fundraising appeals
- funder updates
- social captions
- comment replies
- image prompts

Example prompt:

```text
Draft this message in a warm, clear charity-sector tone.
```

### 14. Weekly Review

Use for:
- what happened this week
- overdue actions
- blockers
- decisions needed
- next week priorities

Example prompt:

```text
Run the weekly review.
```

## Module Access

The organisation can ask naturally.

They do not need to say the module name unless they want to.

Examples:

```text
What needs our attention today?
```

```text
Draft the follow-up.
```

```text
Review this before we send it.
```

```text
What is overdue?
```

## Scope Rule

Only modules listed in `WORKFLOWS/WORKFLOW_INDEX.md` are active for this organisation.

If the organisation asks for a module outside scope, Claude should say it needs to be added by SF&W before use.

## Funding Integrity Rule

Claude can help organise, draft, review, and track funding work.

Claude must not invent impact, inflate numbers, fabricate stories, submit applications, or publish fundraising messages without human review.

## Social Media Integrity Rule

Claude can help create image prompts, captions, comments, campaign posts, and content plans.

Claude must not identify beneficiaries without permission, exploit sensitive stories, fabricate quotes or outcomes, or publish public posts without human review.
