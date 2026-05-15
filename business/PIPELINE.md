# PIPELINE.md

## Purpose

Track leads, prospects, and clients clearly.

This is the live operating file for business momentum.

Update it after every meaningful interaction.

---

## Leads

### Name:
### Business:
### Status:
### Last Contact:
### Next Action:
### Notes:

---

## Active Prospects

### Name:
### Business:
### Current Need:
### Stage:
### Next Step:
### Risk:
### Notes:

---

## Active Clients

### Name:
### Service:
### Stage:
### Current Priority:
### Next Action:
### Notes:

---

## Pipeline Stages Reference

**Lead stages:**
New → Contacted → Engaged → Qualified → Proposal → Closed Won / Closed Lost / Dormant

**Client stages:** see canonical list in `## Client Stage Vocabulary` below. The earlier short-form sequence has been deprecated 2026-05-03 in favour of the 8-stage vocabulary, which aligns with the v3 onboarding/handover/post-lock chain.

---

## Rule

Only keep active records here.

Move old or inactive records to an archive file.

---

## Client Stage Vocabulary

Authoritative list of client-stage values used in `Stage:` fields above and in `ACTIVE_CLIENTS.md`. Use these exact strings:

| Stage | Meaning |
|---|---|
| Closed / Intake Sent | Deal closed; intake form has been sent; awaiting client response |
| Intake Received | Client has returned the intake; ready to summarise and audit |
| Audit In Progress | `audit` agent producing findings |
| System Mapping | `workflow` defining structure; `design` if visual map needed |
| Build In Progress | `builder` configuring; pre-handover |
| Onboarding Scheduled | Build complete; walkthrough call booked |
| Delivered | Day-7 lock complete (`handover` Section 10); playbook handed over |
| Active Support | Post-lock adoption phase (`POST_LOCK_SUPPORT.md`) |

Status progression for a single client typically runs top-to-bottom. A client may also enter `Paused` or `Closed` at any point — those override the above sequence.

Lead stages (above) and client stages (above) are distinct axes. A lead becomes a client when the deal is closed and intake is sent.
