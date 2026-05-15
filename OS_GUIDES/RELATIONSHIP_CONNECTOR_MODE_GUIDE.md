# Relationship Connector Mode Guide

Status: active draft
Purpose: Guide for using Relationship Connector Mode.

## What It Is

Relationship Connector Mode is the AXIS relationship memory and follow-up layer.

It helps track:

- warm introductions
- referrals
- useful contacts
- follow-up dates
- relationship context
- possible opportunities
- consent around introductions

It is Boardy-style in the sense that it is not just a contact list. It helps identify useful relationship actions.

## Best First Use Case

SME Relationship Concierge for SF&W Project Solutions.

Use it to manage:

- partner conversations
- warm intros
- prospects
- referral sources
- existing client follow-ups
- people who may know potential clients

## Core Commands

| Command | What It Does |
|---|---|
| `Run relationship pulse` | Reviews who needs attention |
| `Capture relationship note` | Records useful context |
| `Track warm intro` | Logs a possible introduction |
| `Draft follow-up message` | Writes a follow-up |
| `Review intro consent` | Checks if an intro should be made |
| `Who should I follow up with?` | Produces a follow-up shortlist |
| `Who could help with this?` | Looks for useful relationship connections |

## Relationship Pulse Flow

Use:

```text
Run relationship pulse
```

The OS should check:

1. Who is active
2. Who needs follow-up
3. Which intro opportunities exist
4. Which relationships are going cold
5. Which conversations may support current work
6. What should happen next

## Capture Flow

Use:

```text
Capture relationship note
```

The OS should capture:

- person
- organisation if relevant
- relationship type
- context
- last contact
- next useful action
- consent or sensitivity notes

## Warm Intro Flow

Use:

```text
Track warm intro
```

The OS should capture:

- who might introduce who
- why the intro may be useful
- whether consent is needed
- proposed message
- next action

## Follow-Up Flow

Use:

```text
Draft follow-up message
```

The OS should write a message that is:

- warm
- specific
- low pressure
- clear on why you are getting in touch
- not over-salesy

## Consent Rule

Do not assume people want to be introduced.

Before making an introduction, check:

- Is the reason clear?
- Would both people benefit?
- Has consent been given or should it be requested first?
- Is any personal or sensitive information being shared?

## Good Example Prompts

```text
I spoke to Naomi about a possible intro to a community cycling partner. Capture this and suggest the next action.
```

```text
Who should I follow up with this week for SF&W?
```

```text
Draft a low-pressure follow-up to someone who asked about the SME audit.
```

```text
Review whether this intro is appropriate before I send it.
```

## Files To Use

Relationship memory:

`business/TRACKING/RELATIONSHIP_MEMORY.md`

Intro tracker:

`business/TRACKING/INTRO_TRACKER.md`

Access-channel planning:

`CORE/CLAUDE_OPERATOR/ACCESS_CHANNELS.md`

Relationship mode:

`CORE/CLAUDE_OPERATOR/RELATIONSHIP_CONNECTOR_MODE.md`

## Boundary

Relationship Connector Mode should be helpful, not invasive.

It should not secretly track people, expose private notes, or create introductions without care.
