# Outcome Examples

Status: active draft
Purpose: Before / after proof examples for the Axis OS showcase.

## Example 1 - Messy Life Admin

### Input

```text
I need to pay the council tax, sort the car insurance, book the dentist, reply to school, and I still have not sent that form.
```

### Axis Output

Priority split:

| Priority | Item | Why |
|---|---|---|
| Today | Send the form | It may block something else |
| Today | Pay council tax | Deadline / consequence risk |
| This week | Car insurance | Renewal risk |
| This week | Reply to school | Relationship / admin clarity |
| Book next | Dentist | Important but less urgent |

Next action:

```text
Spend 20 minutes clearing the form and council tax first. Then add car insurance to the admin tracker with the renewal date.
```

## Example 2 - Missed Business Follow-Ups

### Input

```text
I spoke to three people last week and I think two asked for prices but I have not followed up.
```

### Axis Output

Suggested lead tracker:

| Lead | Context | Next Step | Follow-Up Date | State |
|---|---|---|---|---|
| Person 1 | Asked for prices | Send short pricing note | Today | active |
| Person 2 | Interested but unclear | Ask what outcome they want | Tomorrow | active |
| Person 3 | General chat | Park until they reply | Friday | waiting |

Draft follow-up:

```text
Hi [Name], just following up from our chat last week. You mentioned you wanted a rough idea of pricing. The best next step is a short call so I can understand what you actually need before suggesting anything. Would you be open to 15 minutes this week?
```

## Example 3 - Website Build

### Input

```text
I run a mobile beauty service and need a website that makes people trust me and book.
```

### Axis Output

- homepage structure
- trust section
- service menu
- booking CTA
- FAQ
- review request flow
- basic HTML page

Value:

```text
The customer moves from "I need a website" to a usable first version with copy, layout, and next launch steps.
```

## Example 4 - Audit To Build

### Input

```text
We keep losing job updates between the office, WhatsApp, and site teams.
```

### Axis Output

Risk:

```text
Job status depends on memory and fragmented messages.
```

Build opportunity:

```text
Create a Job Status Command Centre with owner, next action, blocker, client update, and review date.
```

First build:

```text
Start with a shared job tracker and weekly 20-minute ops review before automating anything.
```
