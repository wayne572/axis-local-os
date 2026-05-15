# Airtable Demo Table Spec

Status: demo spec
Demo base name: AXIS Demo - Client Delivery Hub
Do not touch existing base: appgAvB8R0sNnhTps

## Demo Scope

This is a small demonstration version of the full AXIS Client Delivery Hub.

It proves that AXIS can create:

- a clear client capture database
- form-ready tables
- a delivery tracker
- an audit-to-build pathway
- fictional sample data for testing

## Table 1: Demo Clients

Purpose:
Store the client profile.

Fields:

| Field | Type | Notes |
|---|---|---|
| Client Name | Single line text | Primary field |
| Client Code | Single line text | Example: HHK-TEST |
| Sector | Single line text | Business sector |
| Team Size | Number or single line text | Keep simple for demo |
| Primary Contact | Single line text | Main client contact |
| Primary Email | Email | Contact email |
| Current Tools | Long text | Systems currently used |
| Delivery Stage | Single select or text | Audit, Build, Handover, Review |
| Risk Level | Single select or text | Low, Medium, High |
| Notes | Long text | Context and caveats |

Sample record:

| Field | Value |
|---|---|
| Client Name | Harbour & Holt Kitchens Ltd |
| Client Code | HHK-TEST |
| Sector | Kitchen design and installation |
| Team Size | 12 |
| Primary Contact | Amelia Holt |
| Primary Email | amelia@example.com |
| Current Tools | Gmail, Google Drive, spreadsheets, WhatsApp, Xero, Trello |
| Delivery Stage | Audit capture |
| Risk Level | Medium |
| Notes | Fictional SME used to test the AXIS Audit to Client OS Growth pathway. |

## Table 2: Demo Audit Capture

Purpose:
Capture AI readiness and audit questionnaire answers.

Fields:

| Field | Type | Notes |
|---|---|---|
| Audit Name | Single line text | Primary field |
| Client Code | Single line text | Connects to Demo Clients manually in demo |
| Completed Date | Date | Date captured |
| Completed By | Single line text | Respondent |
| Main Pain Points | Long text | Business problems |
| Current Workflow | Long text | How work happens now |
| Tools And Systems | Long text | Current tool stack |
| Data Risks | Long text | Personal data, compliance, access risks |
| Success Criteria | Long text | What good looks like |
| Fit Outcome | Single select or text | Proceed, Not yet, Needs more discovery |

Sample record:

| Field | Value |
|---|---|
| Audit Name | HHK-TEST Audit Capture |
| Client Code | HHK-TEST |
| Completed By | Amelia Holt |
| Main Pain Points | Missed follow-ups, slow quotes, scattered job notes, owner bottleneck. |
| Current Workflow | Enquiries arrive from phone, web form, email, referrals, and WhatsApp. Quotes are prepared manually. |
| Tools And Systems | Gmail, Drive folders, spreadsheets, WhatsApp, Xero, Trello. |
| Data Risks | Customer addresses, photos, measurements, quote data, payment status. |
| Success Criteria | Faster enquiry response, fewer missed follow-ups, clearer handovers, less owner dependency. |
| Fit Outcome | Proceed to Client OS Growth scope |

## Table 3: Demo Opportunities

Purpose:
Turn audit evidence into prioritised AI opportunities.

Fields:

| Field | Type | Notes |
|---|---|---|
| Opportunity Name | Single line text | Primary field |
| Client Code | Single line text | Example: HHK-TEST |
| Business Area | Single line text | Sales, delivery, admin, finance |
| Value Level | Single select or text | Low, Medium, High |
| Difficulty Level | Single select or text | Low, Medium, High |
| Risk Level | Single select or text | Low, Medium, High |
| Priority | Number or text | 1, 2, 3 |
| Suggested Workflow | Long text | What AXIS would build |
| Human Approval Needed | Long text | Where people stay in control |
| Expected Outcome | Long text | Business value |

Sample record:

| Field | Value |
|---|---|
| Opportunity Name | AI-assisted enquiry and quote follow-up system |
| Client Code | HHK-TEST |
| Business Area | Sales and customer journey |
| Value Level | High |
| Difficulty Level | Medium |
| Risk Level | Medium |
| Priority | 1 |
| Suggested Workflow | Capture enquiry, summarise customer need, recommend next action, draft follow-up. |
| Human Approval Needed | All outbound messages approved by owner or admin before sending. |
| Expected Outcome | Faster responses, more consistent follow-up, better pipeline visibility. |

## Table 4: Demo Delivery Tasks

Purpose:
Show implementation control after audit.

Fields:

| Field | Type | Notes |
|---|---|---|
| Task Name | Single line text | Primary field |
| Client Code | Single line text | Example: HHK-TEST |
| Phase | Single select or text | Setup, Build, Test, Train, Handover |
| Owner | Single line text | Wayne or client role |
| Status | Single select or text | Not started, In progress, Blocked, Done |
| Due Date | Date | Planned date |
| Client Facing | Checkbox | Whether client sees it |
| Acceptance Check | Long text | Pass/fail proof |
| Notes | Long text | Context |

Sample records:

| Task Name | Client Code | Phase | Owner | Status | Client Facing | Acceptance Check |
|---|---|---|---|---|---|---|
| Create command centre | HHK-TEST | Build | Wayne | Not started | No | Command centre includes context, modules, workstreams, and usage notes. |
| Add enquiry tracker sample records | HHK-TEST | Build | Wayne | Not started | No | At least five fictional lead records show status, next action, and owner. |
| Run new enquiry test | HHK-TEST | Test | Wayne + Amelia | Not started | Yes | Client can capture enquiry, assign next action, and draft follow-up. |
| Handover owner guide | HHK-TEST | Handover | Wayne | Not started | Yes | Owner knows how to run daily and weekly review. |

## Demo Forms

Create form views manually after tables exist:

| Form | Target Table | Demo Purpose |
|---|---|---|
| Client Intake Form | Demo Clients | Show first client capture |
| Audit Capture Form | Demo Audit Capture | Show readiness/audit capture |
| Opportunity Review Form | Demo Opportunities | Show value/risk prioritisation |
| Delivery Update Form | Demo Delivery Tasks | Show delivery progress capture |

## Demo Views

Recommended views:

| View | Table | Filter / Sort |
|---|---|---|
| Active Clients | Demo Clients | Delivery Stage is not Review complete |
| Ready For Scope | Demo Audit Capture | Fit Outcome contains Proceed |
| Top Opportunities | Demo Opportunities | Priority ascending |
| Open Delivery Tasks | Demo Delivery Tasks | Status is not Done |
