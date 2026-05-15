# Relationship Connector OS

Status: active module spec
Date: 2026-05-15
Owner: Wayne Francis

## Purpose

Relationship Connector OS is the Axis Local OS module for relationship memory, warm introductions, follow-up discipline, and consent-aware networking.

It is inspired by Boardy-style superconnector behaviour, PingCRM-style personal networking CRM patterns, and OpenVolo-style local-first social CRM patterns, but it must remain Axis-native: local-first, governed, source-backed, and approval-led.

## What This Module Should Do

Relationship Connector OS should help Wayne:

- remember useful relationship context
- identify people who need follow-up
- surface warm intro opportunities
- draft low-pressure follow-up messages
- track intro consent before anyone is connected
- protect private notes from becoming public or client-safe copy
- produce weekly relationship digests
- keep the relationship workflow human, specific, and trust-building

## Best Practices To Bring In

### From PingCRM

Use these patterns:

- unified timeline per contact
- relationship scoring based on recency, frequency, reciprocity, and breadth
- identity resolution across channels
- weekly digest of people worth reaching out to
- contextual AI follow-up drafts
- self-hosted/open ownership of relationship data

Axis adaptation:

- relationship scores must be explainable, not mysterious
- follow-up drafts require human review
- no message should be sent automatically
- relationship context must be source-backed

### From OpenVolo

Use these patterns:

- local-first contact data
- unified contacts across social/email channels
- workflow types such as sync, enrich, search, prune, sequence, and agent
- analytics and sync-health thinking
- AI assistant over the CRM data
- encrypted credentials when external accounts are connected

Axis adaptation:

- start with local Markdown/JSON trackers before OAuth integrations
- keep credentials out of repo
- add sync only after governance and consent rules are stable
- treat AI as a drafting and reasoning layer, not an autonomous outreach engine

## First Data Model

```yaml
contacts:
  - contact_id
  - name
  - organisation
  - role
  - sector
  - location
  - relationship_type
  - consent_status
  - source_id
  - sensitivity

interactions:
  - interaction_id
  - contact_id
  - date
  - channel
  - summary
  - source_id
  - follow_up_due

relationship_scores:
  - contact_id
  - recency
  - frequency
  - reciprocity
  - breadth
  - explanation

intro_opportunities:
  - intro_id
  - person_a
  - person_b
  - reason
  - consent_a
  - consent_b
  - status
  - next_action

message_drafts:
  - draft_id
  - contact_id
  - purpose
  - draft_text
  - approval_status
  - source_ids
```

## First Commands

```text
AXIS: RELATIONSHIP PULSE
AXIS: CAPTURE RELATIONSHIP
AXIS: TRACK INTRO
AXIS: DRAFT FOLLOW-UP
AXIS: REVIEW INTRO CONSENT
AXIS: WEEKLY RELATIONSHIP REVIEW
```

## Governance Rules

- Do not invent relationships.
- Do not imply consent where consent is unknown.
- Do not send messages automatically.
- Do not create two-sided introductions without both sides agreeing.
- Do not expose private relationship notes in client-safe outputs.
- Do not scrape, enrich, or store unnecessary personal data.
- Mark unclear source or consent as `needs confirmation`.
- Keep outreach warm, specific, and low pressure.

## Current Axis Source Files

Use these existing files as the starting authority:

- `CORE/CLAUDE_OPERATOR/RELATIONSHIP_CONNECTOR_MODE.md`
- `OS_GUIDES/RELATIONSHIP_CONNECTOR_MODE_GUIDE.md`
- `business/TRACKING/RELATIONSHIP_MEMORY.md`
- `business/TRACKING/INTRO_TRACKER.md`

## MVP Build Order

1. Register Relationship Connector OS as a module.
2. Add relationship-specific routing.
3. Add local relationship pulse over existing trackers.
4. Add capture draft flow that creates review-only memory proposals.
5. Add intro consent review command.
6. Add follow-up drafting with source IDs.
7. Add weekly digest.
8. Add integrations only after the local workflow is proven.

## Success Condition

Wayne can write:

```text
Met Sarah from a recruitment agency. Interested in reducing admin and open to practical AI. Follow up next week.
```

Axis should:

- capture the relationship note for review
- identify consent status
- suggest the next action
- draft a warm follow-up if asked
- track the due date
- later surface Sarah in a relationship pulse

