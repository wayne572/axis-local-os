# Client Module Guide

Status: active
Purpose: Explains the client's available AI OS modules in plain English.

## What Modules Are

Modules are the jobs this AI OS can help with.

They are not separate bots.

The client talks to the same assistant, and the assistant uses the right module in the background.

Each module should still follow the V4 loop:

```text
Capture -> Structure -> Operate -> Review -> Memory Update
```

## Available Modules

### 1. Enquiry Follow-Up

Use for:
- new enquiries
- missed replies
- follow-up reminders
- lead status updates

Example prompt:

```text
Log this new enquiry and draft a follow-up.
```

### 2. Quote Or Proposal Builder

Use for:
- quote drafts
- proposal outlines
- scope summaries
- quote follow-up emails

Example prompt:

```text
Build a draft quote from these notes.
```

### 3. Standard Email Handler

Use for:
- repeat email replies
- customer questions
- internal messages
- tone checks before sending

Example prompt:

```text
Draft a reply to this email in our usual tone.
```

### 4. Invoice And Payment Chaser

Use for:
- payment reminders
- overdue invoice emails
- payment tracker updates
- polite escalation messages

Example prompt:

```text
Draft a polite payment reminder for this overdue invoice.
```

### 5. Job, Client, Or Pipeline Tracker

Use for:
- current work status
- active jobs
- quotes pending
- follow-ups due
- weekly review

Example prompt:

```text
Update the tracker from these notes.
```

### 6. Relationship Memory

Use for:
- follow-ups
- warm contacts
- referrals
- relationship notes

Example prompt:

```text
Add this contact to relationship memory and remind me to follow up next week.
```

### 7. Weekly Review

Use for:
- what happened this week
- overdue tasks
- blockers
- decisions needed
- next week priorities

Example prompt:

```text
Run the weekly review.
```

### 8. Idea To Memory

Use for:
- new improvement ideas
- workflow changes
- future opportunities
- useful operating lessons

Example prompt:

```text
AXIS: IDEA TO MEMORY
```

This should create a structured plan, workflow update, decision, or backlog item with a clear owner and next action.

## Module Access

The client can ask naturally.

They do not need to say the module name unless they want to.

Examples:

```text
What needs my attention today?
```

```text
Draft the follow-up.
```

```text
Review this before I send it.
```

```text
What is overdue?
```

## Scope Rule

Only modules listed in `WORKFLOWS/WORKFLOW_INDEX.md` are active for this client.

If the client asks for a module outside scope, Claude should say it needs to be added by SF&W before use.

Do not add new durable memory from a module unless it is useful beyond the current session and allowed by the client's data rules.
