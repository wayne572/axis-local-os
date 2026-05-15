# Axis OS v2 — Setup Scripts

Step-by-step setup instructions per tool. Read by the Handover Agent at Stage 5.

**Rule of use:** The agent gives ONE instruction at a time. Waits for the customer to type "done" or paste an error. Never sends a wall of steps.

**Order of setup (always):**
1. Data tools (Airtable)
2. Capture tools (Typeform, Calendly)
3. Communication tools (Gmail labels, Slack)
4. Connector tools last (Zapier)

Connectors go last because they need the other tools to exist first.

---

## How the Handover Agent uses this file

For each tool in the approved stack:

1. Read the relevant `## Tool — [name]` section
2. Run the prerequisites check
3. Walk through the steps in order, one at a time
4. After each step, wait for "done" or an error
5. If error, run the matching item from the troubleshooting section
6. After all steps, run the verification check
7. Move to the next tool

If a step fails three times, halt and flag for Wayne. Do not push through.

---

## Tool — Airtable

**Purpose in stack:** structured database for leads, clients, content, or invoices.

**Prerequisites**
- Customer has a free Airtable account at airtable.com
- Browser open and signed in

**Setup steps**

1. Go to airtable.com and click "Add a base". Choose "Start from scratch". Name it: `[CustomerBusiness] — Axis OS`.
2. Rename the default table to match the workflow (e.g. "Leads", "Proposals", "Invoices").
3. Add these standard fields to the table (delete others):
   - `Name` (single line text — already exists)
   - `Email` (email)
   - `Phone` (phone number)
   - `Source` (single select — values: Website, Referral, LinkedIn, Other)
   - `Status` (single select — values: New, Contacted, Qualified, Closed Won, Closed Lost)
   - `Notes` (long text)
   - `Created` (created time — set to auto)
   - `Last Contact` (date)
4. Create a view called "Active" with filter: Status is not Closed Won or Closed Lost.
5. Create a view called "New This Week" with filter: Created in the last 7 days.
6. Go to Account → Developer Hub → Personal access tokens. Create a new token with scopes `data.records:read` and `data.records:write` and `schema.bases:read`. Add the base just created. Copy the token.
7. Paste the token here so it can be saved to the Zapier connection later. (The agent will store it temporarily — never write to a file.)

**Verification**
- Confirm the base is created and named correctly
- Confirm the table has all required fields
- Confirm the two views exist
- Confirm the personal access token was generated

**Troubleshooting**
- "I can't see Developer Hub" → Tell them: top-right profile menu → Builder Hub → Personal access tokens
- Token field is greyed out → They are on a free workspace that has restricted permissions; ask them to upgrade to a paid plan or use a personal workspace
- Field type doesn't match → Delete the field and recreate with correct type

---

## Tool — Typeform

**Purpose in stack:** capture enquiries from the website.

**Prerequisites**
- Customer has a Typeform account (Basic plan or higher)
- They know the URL of the page where the form will be embedded

**Setup steps**

1. Go to typeform.com and click "Create new typeform". Choose "Start from scratch".
2. Name the form: `[CustomerBusiness] — Enquiry`.
3. Add these questions in order:
   - Short text: "What is your name?"
   - Email: "What is your email address?"
   - Phone: "What is the best phone number to reach you?"
   - Long text: "What can we help you with?"
   - Multiple choice: "How did you hear about us?" (Website, Referral, LinkedIn, Other)
   - **Yes/No (required) — GDPR consent:** "I'm happy to be contacted about my enquiry. I can withdraw at any time by replying STOP or emailing you." Mandatory field. Link the customer's privacy notice URL under this question.
4. Set the welcome screen and thank you screen with the customer's brand voice (pull from BRAND.md).
5. Go to Settings → Notifications → turn ON email notification to the owner's address.
6. Click Connect → Webhooks → add a placeholder webhook (the actual Zapier webhook URL is added in the Zapier setup later).
7. Go to Share → Embed → copy the embed code for their website.
8. **Cookie banner reminder:** Before embedding on the website, confirm the customer's site has a PECR-compliant cookie banner. Typeform sets cookies. If their site lacks a banner, list free options (Cookiebot Free, Termly, CMS built-in) and tell them to install one before going live with the embed.

**Verification**
- Submit a test response
- Confirm the email notification arrives
- Confirm the response appears in Typeform's Responses tab
- Confirm the customer's website has a cookie banner before sharing the form publicly

**Troubleshooting**
- Embed code not working on website → Check whether their site uses a builder (Wix, Squarespace) — each has a specific embed block. Direct them to the platform's "Add Typeform" guide.
- Email notification not arriving → Check spam, then check the email field is correctly entered in Typeform settings

---

## Tool — Calendly

**Purpose in stack:** self-serve booking for sales calls or onboarding sessions.

**Prerequisites**
- Customer has a Calendly account (Standard plan or higher for redirects)
- Their Google or Outlook calendar is connected

**Setup steps**

1. Go to calendly.com and create a new event type. Choose "One-on-One".
2. Name it based on the workflow purpose (e.g. "Discovery Call", "Onboarding Session").
3. Set duration: 30 minutes for discovery, 60 minutes for onboarding.
4. Set availability windows that match their working hours.
5. Add a buffer of 15 minutes before and after each booking.
6. Customise the booking page with their business name and a one-line description.
7. Set the confirmation email subject and body using BRAND.md voice rules.
8. Copy the public booking link.

**Verification**
- Open the booking link in an incognito window
- Confirm available slots show
- Book a test slot and confirm it lands in their calendar
- Cancel the test booking

**Troubleshooting**
- Calendar not syncing → Reconnect the calendar integration in Calendly → Account → Calendars
- Time zone wrong → Check Calendly profile time zone matches their actual location

---

## Tool — Gmail (existing)

**Purpose in stack:** outreach drafts land here for owner to review and send.

**Prerequisites**
- Customer uses Gmail or Google Workspace
- They are signed in to their primary business inbox

**Setup steps**

1. In Gmail, go to Settings → Labels.
2. Create a new label called: `Axis OS — Drafts to Send`.
3. Create another label called: `Axis OS — Sent`.
4. Optional: create a filter that auto-applies the "Drafts to Send" label to messages with a specific subject prefix (set later in Zapier).

**Verification**
- Confirm both labels appear in the left sidebar
- Send a test email to themselves with subject "Axis OS test" and confirm filter works (if set up)

**Troubleshooting**
- "Labels" not visible → They may be on Gmail mobile — direct them to gmail.com on desktop
- Filter not catching emails → Check the filter conditions for typos in the subject prefix

---

## Tool — Slack

**Purpose in stack:** ping owner on important events (new lead, overdue invoice, stalled proposal).

**Prerequisites**
- Customer has a Slack workspace (Free plan is fine)
- They are an admin or have permission to add apps

**Setup steps**

1. In Slack, create a new private channel called `#axis-os-alerts`.
2. Invite only the owner (and any team members who should see alerts).
3. Go to api.slack.com → Your Apps → Create New App → From scratch.
4. Name it `Axis OS` and pick their workspace.
5. Go to Incoming Webhooks → Activate. Click "Add New Webhook to Workspace" and select `#axis-os-alerts`.
6. Copy the webhook URL.

**Verification**
- The webhook URL is copied and saved temporarily
- The `#axis-os-alerts` channel exists

**Troubleshooting**
- "Can't create an app" → They may not be a workspace admin. Ask them to request admin permission or have an admin do this step.
- Webhook URL doesn't work → Re-add the webhook, sometimes Slack requires a fresh authorisation

---

## Tool — Zapier (always last)

**Purpose in stack:** connect everything. Triggers automations between tools.

**Prerequisites**
- All other tools in the stack are set up and verified
- Customer has a Zapier account (Starter plan)
- Tokens, webhook URLs, and credentials from previous tools are ready

**Setup steps — Lead Qualifier Zap (Stack 01 example)**

1. Go to zapier.com → Create Zap.
2. Trigger: Typeform → New Entry. Connect their Typeform account. Select the enquiry form.
3. Action 1: Airtable → Create Record. Connect their Airtable using the personal access token. Select the base and table. Map Typeform fields to Airtable fields.
4. Action 2: Gmail → Create Draft. Subject: `New enquiry — [Name]`. Body: a brief acknowledgement using BRAND.md voice. Send to themselves (so it sits in drafts for review).
5. Action 3: Slack → Send Channel Message. Channel: `#axis-os-alerts`. Message: `New lead from [Name] — [Source]`.
6. Test the Zap end-to-end with the test data Zapier provides.
7. Turn the Zap ON.

**Verification**
- Submit a real test response through Typeform
- Confirm record appears in Airtable
- Confirm draft appears in Gmail
- Confirm message appears in Slack

**Troubleshooting**
- Airtable token rejected → Regenerate the token in Airtable; Zapier sometimes loses tokens between sessions
- Gmail draft not creating → Check Gmail account is connected and "Create Draft" (not "Send Email") is selected
- Slack message not sending → Verify the webhook URL was correctly pasted; reconnect the Slack integration

---

## Tool — Buffer

**Purpose in stack:** schedule social content (LinkedIn + 1 other platform on Essentials).

**Prerequisites**
- Customer has a Buffer account (Essentials plan)
- They have admin access to their LinkedIn company page (and any other platforms)

**Setup steps**

1. Sign in to buffer.com.
2. Connect LinkedIn → Company Page (not personal profile, unless they only have personal).
3. Connect any other platform on their plan.
4. Set posting schedule: default to weekday mornings (9am UK).
5. Skip the AI Assistant — content is drafted inside Axis OS, not in Buffer.

**Verification**
- Confirm both platforms are connected and showing in Buffer dashboard
- Schedule a test post for tomorrow morning, then delete it

**Troubleshooting**
- LinkedIn page not appearing → They may not be an admin of the company page; check via LinkedIn → Me → Manage → Company Pages
- Connection drops → LinkedIn requires re-auth every 60 days; this is normal, the agent should remind them at month 2

---

## Off-Catalogue Tool Fallback

If a customer wants to use a tool that is not in this script library (e.g. they prefer Pipedrive over Airtable, or Notion over Google Sheets), the Handover Agent runs the fallback flow.

**Step 1 — Confirm with the customer**
Tell them: "That tool isn't in our standard catalogue, so I don't have a pre-tested setup script for it. I can guide you through it using the tool's official documentation, or send you to their setup guide directly. Which do you prefer?"

**Step 2 — Search for current setup guidance**
Use WebSearch to find the tool's most recent official setup or onboarding documentation. Search terms to use:
- `[tool name] official setup guide`
- `[tool name] getting started`
- `[tool name] [the integration they need, e.g. "webhook", "Zapier integration"]`

Prefer official sources over third-party blogs:
- Official help/docs subdomains (help.[tool].com, docs.[tool].com, support.[tool].com)
- The tool's own YouTube channel or knowledge base
- Recent (within 12 months) third-party guides only if no official source exists

**Step 3 — Fetch and summarise**
Use WebFetch on the top official result. Extract:
- Account creation steps (if needed)
- Core setup steps relevant to the workflow
- Any API or webhook setup needed for Zapier connection
- Known gotchas mentioned in the docs

**Step 4 — Guide the customer**
Walk the customer through the official steps, one at a time, same atomic format as the catalogued tools. Use the language and screenshots from the official docs where possible.

**Step 5 — If guidance is unclear or unavailable**
If WebSearch returns no reliable official source, or the documentation is paywalled/incomplete, tell the customer:
> "I can't find a clear official setup guide for this tool. The safest path is to follow [tool]'s help centre directly — here is the link: [url]. When you have the tool set up to the point where it can connect to other tools (usually an API key or webhook), come back here and I will help you wire it into the rest of your stack."

**Step 6 — Log the off-catalogue setup**
After the tool is set up:
- Add an entry to `business/Sales/CHANGELOG.md`: "Off-catalogue tool used — [tool] — [customer] — [date]. Steps captured for review."
- Save the steps to `business/HANDOVER/_OFF_CATALOGUE_LOG.md` with date and customer name. This becomes the source for future catalogue additions.

**Wayne's review trigger:** if the same off-catalogue tool appears 3 times across deployments, it's a candidate for the main catalogue. Quarterly review picks up these patterns.

**Hard limits — even in fallback mode:**
- Never enter the customer's credentials, passwords, or payment info on their behalf
- Never accept terms of service for them — they must click accept themselves
- Never proceed if the tool requires regulated data (financial, medical, legal) without explicit Wayne sign-off
- Never improvise around a paywall — if docs are gated, send them to the official source

---

## Failure protocol

If any tool setup fails three times in a row:

1. Halt the handover at this tool
2. Save progress to `business/MEMORY.md` with a clear note: "Stage 5 paused — [tool] setup blocked at [step]. Reason: [error]."
3. Tell the customer: "Let's pause here. I'll flag this for Wayne so he can help unstick this one tool. The rest of your setup is fine — we can resume tomorrow."
4. Add a CHANGELOG.md entry: "Handover paused — [customer] — [tool] blocker"

Do not push through a broken tool setup. Better to pause than deliver a half-broken stack.

---

## Maintenance

**Quarterly review checklist (Wayne to run):**
- Walk through each tool setup yourself — UI changes regularly
- Update step numbers and menu names where tools have rebranded buttons
- Add new troubleshooting items for issues seen during real handovers
- Remove tools that have been retired from the Stack Catalogue

**Last reviewed:** 2026-04-30
**Next review due:** 2026-07-30
