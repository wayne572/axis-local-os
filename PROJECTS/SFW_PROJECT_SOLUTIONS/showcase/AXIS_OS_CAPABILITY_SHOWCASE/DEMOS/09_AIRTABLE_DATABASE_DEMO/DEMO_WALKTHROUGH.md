# Airtable Database Demo Walkthrough

Status: demo walkthrough
Command: `AXIS: AIRTABLE DATABASE DEMO`

## What This Demonstrates

AXIS AI OS can turn a scattered client delivery process into a database structure that supports forms, audit capture, opportunity mapping, build scope, delivery tracking, and handover.

This is a controlled demo. It does not touch Wayne's current Airtable base.

## Demo Setup

Have open:

- `AIRTABLE_DEMO_TABLE_SPEC.md`
- `CLAUDE_AIRTABLE_DEMO_PROMPT.md`
- Airtable, if Wayne wants to create the test base live

Reference only:

```text
https://airtable.com/appgAvB8R0sNnhTps/tblUd1ajHmKozINu2/viwMFEW4Flfa7rPTa?blocks=hide
```

## 5-Minute Demo Flow

### 1. Start With The Boundary

Say:

```text
This is my existing Airtable. For the demo, AXIS does not touch it. It reads the context and sets a safety boundary first.
```

Show:

- existing base ID
- note that it is reference only
- new demo base name

### 2. Explain The Business Problem

Say:

```text
Most small businesses do not have one joined-up place for lead capture, audit notes, build priorities, delivery tasks, and review. AXIS turns that mess into a controlled delivery database.
```

### 3. Show The Demo Table Plan

Open `AIRTABLE_DEMO_TABLE_SPEC.md`.

Show the four tables:

- Demo Clients
- Demo Audit Capture
- Demo Opportunities
- Demo Delivery Tasks

### 4. Show The Fictional SME

Use:

```text
Harbour & Holt Kitchens Ltd
Client code: HHK-TEST
```

Say:

```text
This fictional client lets us test the complete Audit to Client OS Growth pathway without exposing real client data.
```

### 5. Paste The Prompt Into Claude

Open `CLAUDE_AIRTABLE_DEMO_PROMPT.md`.

Paste into Claude AI OS.

Expected result:

- Claude confirms the live base is read-only
- Claude names the new demo base
- Claude produces the table structure
- Claude produces fictional sample records
- Claude gives forms/views to create

### 6. Optional Live Airtable Build

Only do this if Wayne has created a new empty demo base.

Do not use:

```text
appgAvB8R0sNnhTps
```

Use only the new demo base.

### 7. Close With The Value

Say:

```text
The important thing is not Airtable itself. Airtable is only the capture layer. The value is that AXIS knows what needs to be captured, why it matters, how it connects to delivery, and how it becomes a controlled client handover.
```

## Prospect-Friendly Explanation

```text
This is the part clients often cannot design for themselves. They know the work is scattered, but they do not know what the operating structure should be. AXIS maps the work, creates the capture system, tests it with real scenarios, and turns it into a working delivery rhythm.
```

## Demo Boundary

Do not claim:

- that AXIS has modified Airtable unless it actually has
- that forms were created automatically if they were only planned
- that the demo uses real client data

Say instead:

```text
Suggested database structure
```

or:

```text
Demo table plan
```

unless a new test base was actually built.
