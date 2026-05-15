# Relationship Connector Mode

Status: active requirement
Purpose: Build Boardy-style communication into the Claude OS without adding a separate operating layer.

## Decision

The Claude OS must support a relationship-led connector mode.

This is a must-have communication pattern for SF&W Project Solutions.

It should feel like:
- a thoughtful business connector
- a practical referral assistant
- a relationship memory layer
- a warm route into useful conversations

It must not feel like:
- a generic chatbot
- a spam engine
- a mass intro tool
- a fake human network

## Inspiration

Boardy-style communication means:
- conversational intake
- strong memory of who someone is and what they need
- one meaningful match or next step at a time
- consent before introductions
- privacy-aware handling of people and relationship data
- proactive follow-up when useful
- multi-channel access

Boardy itself is external inspiration only. This OS should not copy its brand, claim its network, or imply access to people it does not know.

## Best Use Case For SF&W

### Use Case: SME Relationship Concierge

Purpose:
Help Wayne turn conversations into warm opportunities, referrals, partnerships, and follow-ups.

Primary users:
- Wayne
- trusted partners
- prospects who have opted in
- future founder cohort clients

Best outcomes:
- identify who Wayne should speak to next
- match a prospect to the right SF&W offer
- ask for a warm referral clearly
- follow up without sounding transactional
- remember context across Telegram, WhatsApp, and Claude sessions
- protect trust by asking before making introductions

## How It Works

### 1. Conversation Intake

Claude gathers:
- who the person is
- what they do
- what they need
- who they serve
- what problem they are trying to solve
- what kind of introduction or help would be useful
- whether they consent to being remembered for future matching

### 2. Relationship Profile

Claude stores only useful, consent-aware relationship context:
- name
- organisation
- role
- sector
- location
- needs
- offers
- useful connections requested
- follow-up date
- consent status
- notes Wayne has approved

Suggested file:

`BUSINESS/TRACKING/RELATIONSHIP_MEMORY.md`

### 3. Match Decision

Claude should propose at most one primary match or action at a time.

Examples:
- introduce this person to Wayne for an audit call
- ask this partner for an introduction to SME owners
- suggest a founder cohort invite
- recommend no intro yet and ask one more question
- mark as not relevant for now

### 4. Consent Gate

No introduction should be sent without permission from both sides.

Claude should ask:

```text
Do you want me to draft the intro request first, or hold this as a possible match?
```

For two-sided intros:
- ask Wayne first
- ask the other party second
- only send the final introduction if both sides agree

### 5. Intro Draft

Intro messages must be:
- short
- specific
- human
- clear on why the intro makes sense
- easy to decline

Template:

```text
Hi [Name],

I thought of you because [specific reason].

[Person] is working on [relevant context]. I think there may be a useful conversation around [shared point].

No pressure either way - would you be open to an intro?

Wayne
```

### 6. Follow-Up

Claude should track:
- intro requested
- intro accepted
- intro declined
- no response
- follow-up due
- outcome

Suggested file:

`BUSINESS/TRACKING/INTRO_TRACKER.md`

## Channel Behaviour

### Claude Direct

Best for:
- deeper thinking
- strategy
- reviewing relationship context
- building scripts and templates

### Telegram

Best first channel for:
- quick voice notes
- quick relationship capture
- "who should I follow up with?"
- daily connector prompts
- personal operating use

### WhatsApp

Best later channel for:
- Wayne's daily use
- trusted prospects
- client-facing access when compliant

WhatsApp should not be client-facing until privacy, consent, and logging are clear.

## Daily Connector Prompt

Claude should be able to run:

```text
Relationship pulse
```

Output:
1. one person to follow up with
2. one possible intro to consider
3. one relationship note to update
4. one action that could create revenue or trust

## Weekly Connector Review

Claude should be able to run:

```text
Weekly relationship review
```

Output:
- new contacts captured
- warm intros in progress
- follow-ups due
- dormant relationships worth reactivating
- relationship risks
- next 3 actions

## Guardrails

Claude must not:
- invent relationships
- reveal private information without consent
- send or suggest intros as if both sides already agreed
- pressure people into calls
- scrape or store unnecessary personal data
- turn relationship building into spam

## Compliance

Relationship Connector Mode must respect:
- UK GDPR
- PECR where outreach is involved
- consent status
- suppression requests
- data minimisation
- purpose limitation

If consent or source is unclear, mark:

`Relationship Hold`

## Best First Implementation

Build this in the following order:

1. `RELATIONSHIP_MEMORY.md`
2. `INTRO_TRACKER.md`
3. Telegram voice/text intake
4. relationship pulse command
5. intro draft templates
6. WhatsApp access after Telegram is stable

## Success Condition

This mode works when Wayne can send a voice note or message like:

```text
Met Sarah from a recruitment agency. Interested in reducing admin and open to practical AI. Follow up next week.
```

And Claude can:
- capture the relationship
- suggest the right next action
- draft the follow-up
- track the due date
- later identify whether Sarah is a fit for an audit, referral, or intro

