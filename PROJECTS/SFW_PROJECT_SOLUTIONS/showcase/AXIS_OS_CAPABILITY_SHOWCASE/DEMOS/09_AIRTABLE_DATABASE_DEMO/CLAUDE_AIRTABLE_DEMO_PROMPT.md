# Claude Airtable Demo Prompt

Paste this into Claude AI OS when demonstrating the Airtable database build.

```text
You are working inside Wayne AI OS / AXIS AI OS.

Task:
Create a safe Airtable database demo plan for the AXIS Client Delivery Hub.

Important safety rule:
Do not touch, edit, import into, delete from, or modify this existing Airtable base:
https://airtable.com/appgAvB8R0sNnhTps/tblUd1ajHmKozINu2/viwMFEW4Flfa7rPTa?blocks=hide

That existing base is read-only reference only.

Use it only to identify the current Airtable context:
- Existing base ID: appgAvB8R0sNnhTps
- Existing table ID: tblUd1ajHmKozINu2
- Existing view ID: viwMFEW4Flfa7rPTa

For the demo, create or describe a NEW empty base called:
AXIS Demo - Client Delivery Hub

Brand architecture:
- Wayne Francis / waynefrancis.co.uk is the public professional brand
- SF&W Project Solutions is the trading entity
- AXIS AI OS is the system created by Wayne Francis

Demo objective:
Show how AXIS turns a messy SME delivery process into a structured Airtable database.

Build these four demo tables:

1. Demo Clients
Fields:
- Client Name
- Client Code
- Sector
- Team Size
- Primary Contact
- Primary Email
- Current Tools
- Delivery Stage
- Risk Level
- Notes

2. Demo Audit Capture
Fields:
- Audit Name
- Client Code
- Completed Date
- Completed By
- Main Pain Points
- Current Workflow
- Tools And Systems
- Data Risks
- Success Criteria
- Fit Outcome

3. Demo Opportunities
Fields:
- Opportunity Name
- Client Code
- Business Area
- Value Level
- Difficulty Level
- Risk Level
- Priority
- Suggested Workflow
- Human Approval Needed
- Expected Outcome

4. Demo Delivery Tasks
Fields:
- Task Name
- Client Code
- Phase
- Owner
- Status
- Due Date
- Client Facing
- Acceptance Check
- Notes

Use sensible Airtable field types:
- Email for email addresses
- Date for dates
- Checkbox for Client Facing
- Long text for notes and larger answers
- Single line text for short labels
- Single select only where easy and safe

Seed fictional sample data only.

Use this fictional SME:
Client name: Harbour & Holt Kitchens Ltd
Client code: HHK-TEST
Sector: Kitchen design and installation
Team size: 12
Primary contact: Amelia Holt
Primary email: amelia@example.com
Current tools: Gmail, Google Drive, spreadsheets, WhatsApp, Xero, Trello
Delivery stage: Audit capture
Risk level: Medium

Create sample rows showing:
- one client profile
- one audit capture
- one AI opportunity
- four delivery tasks

Recommended demo forms:
- Client Intake Form -> Demo Clients
- Audit Capture Form -> Demo Audit Capture
- Opportunity Review Form -> Demo Opportunities
- Delivery Update Form -> Demo Delivery Tasks

Recommended views:
- Active Clients
- Ready For Scope
- Top Opportunities
- Open Delivery Tasks

Output format:
1. Confirm the existing Airtable base is read-only reference only.
2. Show the new demo base name.
3. Show the table list.
4. Show the fields per table.
5. Show the fictional sample records.
6. Show the recommended forms and views.
7. Give Wayne a short talk track for explaining this to a prospect.

Do not ask to modify the existing base.
If Airtable access or a token is required, ask me before proceeding.
```
