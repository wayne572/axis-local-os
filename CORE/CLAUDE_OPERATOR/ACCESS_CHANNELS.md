# Access Channels

Status: active planning file
Purpose: Defines how Wayne should access the Claude OS through chat channels without adding extra operating layers.

## Decision

Telegram and WhatsApp are access channels.

They are not separate agents.

They should send messages into the same Claude-backed OS and return responses from the same operating context.

## Target Experience

Wayne can message the OS from:
- Claude directly
- Telegram
- WhatsApp

Each channel should reach the same system:

```text
Telegram / WhatsApp / Claude
-> message intake
-> Claude operator
-> AXIS OS files
-> response
-> optional tracker update
```

## Required Communication Pattern

The access layer must support Relationship Connector Mode.

Source:

`CORE/CLAUDE_OPERATOR/RELATIONSHIP_CONNECTOR_MODE.md`

This means Telegram and WhatsApp should support:
- quick relationship capture
- voice-note or text intake
- follow-up reminders
- intro drafting
- consent-aware relationship memory
- daily relationship pulse

## Minimum Viable Build

### Phase 1 - Manual Claude Use

Use this folder directly in Claude.

No channel integration needed yet.

### Phase 2 - Telegram Access

Build a Telegram bot that:
- receives Wayne's message
- accepts short text notes and voice-note transcripts
- sends it to a Claude-compatible backend
- loads the needed OS files
- returns Claude's response
- logs important decisions or tasks
- updates relationship memory when Wayne confirms

Telegram is usually the simpler first channel.

### Phase 3 - WhatsApp Access

Add WhatsApp after Telegram works.

WhatsApp should use the official WhatsApp Business Platform or a compliant provider.

Do not build a fragile personal-phone workaround for client or business use.

WhatsApp should not become client-facing until:
- relationship memory rules are working
- consent capture is clear
- message logging is reliable
- suppression requests are respected

### Phase 4 - Unified Message Log

Add a shared message log so channel context is not scattered.

Suggested file:

`BUSINESS/TRACKING/CHANNEL_LOG.md`

Relationship files:

```text
BUSINESS/TRACKING/RELATIONSHIP_MEMORY.md
BUSINESS/TRACKING/INTRO_TRACKER.md
```

## Routing Rules

Channel messages should still follow AXIS rules:
- identify mode
- use relevant venture context
- read only needed files
- produce a clear next action
- update tracker when work changes

## Important Constraint

Do not create a new branded layer between Wayne and Claude.

The access layer should feel invisible.

## Open Build Questions

1. Where will the Claude backend run?
2. Which Claude API or compatible runtime will be used?
3. Where will message history be stored?
4. Should Telegram be personal-only or later client-facing?
5. Should WhatsApp be Wayne-only first, then client-facing later?
6. What data should be stored for relationship matching?
7. What consent wording should be used when someone is added to relationship memory?

## Recommendation

Start with:

1. Claude folder build
2. Telegram personal access
3. Relationship Connector Mode
4. shared channel log
5. WhatsApp only after Telegram is stable
