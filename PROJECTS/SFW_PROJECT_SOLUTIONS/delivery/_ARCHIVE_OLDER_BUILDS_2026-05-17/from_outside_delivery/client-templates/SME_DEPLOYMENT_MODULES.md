# SME Deployment Modules

Status: active template
Purpose: Generic delivery modules for SF&W Project Solutions client work.

## Use Rule

This file is the reusable template.

Old client-specific source files are stored in:

`ARCHIVE_NOTES/SOURCE_CLIENT_BUILDS_WKS`

Do not use old client files directly with a new client.

## Module 1 - Enquiry Follow-Up

Purpose:
Make sure every new enquiry is captured, acknowledged, and followed up.

Typical inputs:
- enquiry source
- customer name
- email or phone
- service requested
- urgency
- preferred contact method
- next action

Typical outputs:
- acknowledgement message
- follow-up reminder
- lead status update
- owner assignment

Best for:
- trades
- property services
- recruitment
- care providers
- professional services
- cleaning and facilities companies

## Module 2 - Quote Or Proposal Generator

Purpose:
Turn repeat quote or proposal work into a structured process.

Typical inputs:
- customer details
- requested service
- scope
- exclusions
- timeline
- pricing assumptions
- terms

Typical outputs:
- draft quote
- proposal outline
- follow-up email
- internal review checklist

Best for:
- trades
- consultants
- agencies
- service firms

## Module 3 - Standard Email Handler

Purpose:
Reduce time spent answering repeat questions.

Typical inputs:
- common email scenarios
- tone of voice
- approved answers
- escalation rules

Typical outputs:
- reusable response bank
- draft replies
- escalation prompts
- client communication checklist

Best for:
Any SME that answers the same questions repeatedly.

## Module 4 - Invoice And Payment Chaser

Purpose:
Improve cash flow by making payment follow-up consistent and professional.

Typical inputs:
- invoice date
- due date
- amount
- client name
- payment terms
- reminder schedule

Typical outputs:
- reminder email
- overdue follow-up
- escalation notice
- payment tracker update

Best for:
Any SME with unpaid invoices or manual payment chasing.

## Module 5 - Job, Client, Or Pipeline Tracker

Purpose:
Create a simple operating view of active work, enquiries, quotes, clients, and next actions.

Typical fields:
- contact
- opportunity or job
- status
- owner
- value
- next action
- due date
- notes

Typical outputs:
- live tracker
- weekly status view
- overdue action list
- handoff notes

Best for:
Any SME where work is currently tracked across memory, inboxes, spreadsheets, or messages.

## Delivery Sequence

Recommended build order:

1. Tracker
2. Enquiry follow-up
3. Standard email handler
4. Quote or proposal generator
5. Invoice and payment chaser

Reason:
The tracker becomes the spine. Every other module needs somewhere to record status and next actions.

## Review Before Client Use

Before using this with a client:

- confirm sector
- confirm tools already in use
- confirm data handling requirements
- confirm who owns each workflow
- confirm what will be automated and what stays manual
- check UK GDPR / PECR relevance
- mark final client pack as `in review`

