# Voice And Message Capture Plan

Status: active plan
Purpose: Define how AXIS should later capture notes, tasks, relationship updates, and decisions from Telegram, WhatsApp, and voice without overbuilding too early.

## Core Rule

Manual workflow first. Automation second.

Do not build Telegram, WhatsApp, or voice automation until the capture categories and review flow work manually in Claude.

## Why This Matters

Wayne and clients will not always open a full folder/project to capture useful context.

The likely real-world capture routes are:

- quick message
- voice note
- WhatsApp
- Telegram
- email forwarded into the system
- meeting note pasted after a call

## Capture Categories

Every captured item should be classified as one of:

- task
- decision
- idea
- relationship note
- client note
- project note
- follow-up
- risk
- knowledge note
- review item

## Minimum Manual Workflow

Before any automation, test this in Claude:

```text
AXIS: CAPTURE THIS
```

Then paste the note.

AXIS should return:

- category
- summary
- destination file
- next action
- whether review is needed

## Message Capture Format

Use this simple format:

```text
Capture:
Source:
Person / project:
Note:
Action needed:
By when:
Sensitivity:
```

## Voice Note Handling

If a voice note is transcribed, AXIS should:

1. clean obvious transcription errors
2. summarise the note
3. classify the item
4. identify any action
5. ask before storing sensitive personal data
6. write to the correct tracker or context file

## Relationship Capture

For relationship notes, AXIS should use:

`CORE/CLAUDE_OPERATOR/RELATIONSHIP_CONNECTOR_MODE.md`

and:

`business/TRACKING/RELATIONSHIP_MEMORY.md`

Capture:

- who
- context
- relevance
- last contact
- next useful action
- consent or sensitivity note

## Telegram Plan

Potential first use:

- quick capture
- relationship notes
- daily command
- follow-up reminders

Do not use Telegram for:

- sensitive client data
- passwords
- confidential contracts
- regulated decisions
- large client handovers

## WhatsApp Plan

Potential first use:

- client-friendly capture
- relationship follow-up
- quick voice notes

Risks:

- platform setup complexity
- business API limitations
- personal data exposure
- client expectation creep

Do not promise WhatsApp access until tested and scoped.

## Future Automation Path

1. Manual capture in Claude
2. Define capture categories
3. Test with Wayne's own notes
4. Add Telegram quick capture
5. Review data and consent risks
6. Test WhatsApp only if the use case is strong
7. Add no-code automation if required

## Capture Routing Table

| Capture Type | Destination |
|---|---|
| task | active workstream or project tracker |
| decision | decision log |
| idea | idea tracker |
| relationship note | relationship memory |
| warm intro | intro tracker |
| client note | client folder |
| risk | risk register |
| product improvement | product manual or active workstream |
| pricing note | pricing authority or offer file, in review |

## Test Prompt

```text
AXIS: CAPTURE THIS

Source: voice note
Person / project: SF&W Project Solutions
Note: I need to follow up with the accountant I spoke to about the audit. They were worried about data privacy and wanted a simple example.
Action needed: Draft a follow-up and log the concern.
By when: Friday
Sensitivity: normal business context
```

Expected result:

- category: relationship note / follow-up
- destination: relationship memory and active workstream
- next action: draft follow-up
- risk: data privacy concern should be addressed with governance pack

## Boundary

Capture should reduce friction, not create hidden surveillance.

Always be clear about what is stored, why, and where.
