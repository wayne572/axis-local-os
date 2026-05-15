# Mobile-Friendly Shipping Standard

Status: active standard
Owner: Wayne Francis
Applies to: Solo Operator OS, Client OS Build, Audit packs, handover packs, and any client-facing Axis delivery

## Purpose

Every shipped Axis build should include a mobile-friendly HTML guide.

Clients often open delivery files from email, phone, WhatsApp, or cloud storage before they ever inspect the full folder. A clear mobile guide makes the delivery feel professional, easy to use, and less intimidating.

## Standard Rule

No client-facing Axis OS should be shipped with Markdown files only.

Every shipped build must include:

- the working OS folder
- the zipped OS folder
- a mobile-friendly HTML guide
- email setup instructions
- a clear start command
- a first-session walkthrough

## Required Mobile Guide File

Use this naming pattern:

```text
[CLIENT_OR_BUILD_NAME]_MOBILE_START_GUIDE.html
```

Examples:

```text
TIANNA_MULTI_PROJECT_SOLO_OS_MOBILE_START_GUIDE.html
SCC_HOMES_CLIENT_OS_MOBILE_START_GUIDE.html
```

## What The Mobile Guide Must Include

### 1. Welcome

Explain what the client has received in plain English.

### 2. What To Do First

Tell the client:

- download the zip
- unzip it
- keep the folder together
- open the startup guide
- use the start command

### 3. Start Command

Show the exact command the client should use.

Example:

```text
AXIS: TIANNA START
```

### 4. First Setup Session

Tell the client what to set up first:

- active projects or workflows
- open loops
- follow-ups
- admin
- decisions
- weekly priorities

### 5. Core Files

List the key files in the package and what each one is for.

### 6. First 7 Days

Give the client a simple first-week plan.

### 7. Boundaries

Explain what the OS does not do.

At minimum:

- no medical advice
- no legal advice
- no financial advice
- no employment or safety decisions
- AI suggestions require human judgement

### 8. Support / Next Step

Tell the client what to do if they get stuck.

## Design Standard

The mobile guide should be:

- readable on phone
- single HTML file
- plain English
- no heavy technical language
- short sections
- sticky or simple navigation where useful
- printable if possible
- visually consistent with Axis documentation

## Shipping Checklist

Before sending a build, confirm:

- OS folder is complete
- zip file has been rebuilt
- mobile start guide exists
- mobile start guide is included inside the folder
- mobile start guide is available beside the zip
- email draft tells the client to open the mobile guide first
- setup guide is included
- handover notes are included
- start command is correct
- no private internal notes are included

## Completion Rule

A client build is not shipping-ready until the mobile guide exists and has been checked.

