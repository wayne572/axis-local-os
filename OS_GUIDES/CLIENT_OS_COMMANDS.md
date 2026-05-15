# Client OS Commands

Status: client-facing draft
Purpose: Commands and workflows for a Client OS.

## Start Command

```text
AXIS: NEW CLIENT
```

Use this during first setup or when creating a new client copy.

## First-Time Setup Flow

The OS should collect:

1. Business name
2. Main contact
3. What the business does
4. Current pain points
5. Key workflows
6. Tools currently used
7. Important clients or stakeholders
8. Data and compliance considerations
9. What should be improved first
10. Handover expectations

## Daily Use Commands

| Command | What It Does |
|---|---|
| `Status` | Shows current client OS state |
| `Next action` | Gives one concrete next action |
| `Block list` | Shows blocked items |
| `Summarise this session` | Captures session decisions and actions |

## Workflow Commands

| Command | What It Does |
|---|---|
| `Build workflow` | Turns a process into a repeatable workflow |
| `Review workflow` | Checks a workflow for gaps |
| `Create checklist` | Makes a step-by-step checklist |
| `Create handover note` | Turns work into a handover-ready note |
| `Create SOP` | Drafts a standard operating procedure |

## Client Communication Commands

| Command | What It Does |
|---|---|
| `Draft client email` | Creates a client message |
| `Review this email` | Checks tone, clarity, and risk |
| `Create update note` | Writes a progress update |
| `Create meeting agenda` | Prepares meeting structure |
| `Create meeting summary` | Summarises decisions and next actions |

## Review Commands

| Command | What It Does |
|---|---|
| `Run 30 day review` | Checks whether the Client OS is working |
| `Review risks` | Looks for data, compliance, delivery, and expectation risks |
| `What is missing?` | Finds gaps |
| `What should we improve next?` | Creates next improvement options |
| `Run AI ROI review` | Checks whether the Client OS is creating measurable value |
| `Run client governance check` | Checks data, consent, usage tracking, and human review |

## Good Example Prompts

```text
Here are our enquiry steps. Turn them into a workflow and checklist.
```

```text
Review this client email for clarity and professionalism.
```

```text
Create a 30-day review summary from these notes.
```

```text
What needs to be handed over before this system is locked?
```

## Client Boundary

The Client OS should not expose Wayne's internal strategy, pricing review, lead generation system, or hidden operating rules unless those are part of the agreed client scope.

## Locking Rule

Client work should move through:

```text
active -> in review -> locked
```

Locked work should not be casually edited. Create a superseded version if something changes.
