# Case Study Capture

Status: capability spec — pending build
Date: 2026-05-16
Owner: Wayne Francis

## Purpose

Case Study Capture turns each Axis engagement into a structured proof artefact that Wayne can use in sales conversations, on the website, and in content. It runs in two tiers:

- **Tier 1 — Sector Snapshot.** Anonymised. No permission needed. One per active client folder. Captures sector, situation, intervention, outcome, transferable pattern. Reads in 60 seconds. Built for volume.
- **Tier 2 — Hero Case Study.** Named, full-narrative, permission-confirmed. Like the existing Gavin Brown case study. Used as headline proof on the site and in proposals. One per quarter is plenty.

Both tiers run through the same capture workflow. The only difference is whether the output is anonymised before publishing.

## First Principle

The transferable pattern is the asset. A prospect does not care who the client was. They care whether someone like them has been helped by Axis before, what Axis actually did, and what changed. Names are nice to have. Patterns are the proof.

This principle is what makes Tier 1 viable. The sector, the situation, and the structural fix carry the value. The name is decorative.

## Why Two Tiers

Most consultancies publish nothing until a client signs a permission form. Permission forms are slow, often refused, and bias the published portfolio towards the loudest clients. Two tiers fixes both problems:

- Tier 1 ships immediately from any engagement with usable material. No permission bottleneck. Reach across every sector Wayne has touched.
- Tier 2 layers on top when a named client is willing. The hero stories carry more weight, but they are not the only proof.

By the time Wayne has 8–10 Tier 1 snapshots and 2–3 Tier 2 case studies, the prospect-facing portfolio looks deep, varied, and credible — without any single client being asked to "be the face" of anything.

## Capture Workflow

Every case study, Tier 1 or Tier 2, follows the same nine-step workflow:

```text
1. Select source       -> client folder under D:\Wayne Francis\Clients\<name>\
2. Scan contents       -> classify what was delivered, what was learned, what changed
3. Extract pattern     -> sector / stage / situation / intervention / outcome / evidence
4. Compliance check    -> CAP code rules, no unsubstantiated claims, regulated-sector flags
5. Anonymise (Tier 1)  -> strip names, swap to sector identifiers, neutralise specifics
6. Draft               -> sector snapshot or full case study in Wayne's voice
7. Brand apply         -> navy/teal/gold, DM Serif + DM Sans, Wayne's signature
8. Permission gate     -> Tier 1: skip. Tier 2: route to permission email template.
9. File + index        -> save artefact, append to MASTER_INDEX, update website-ready block
```

Tier 2 hero case studies add three steps after #6: client review, named pull-quote selection, permission confirmation logged in `04 Client Proof/PERMISSION_LOG.md`.

## Required Fields Per Case Study

Every output, Tier 1 or Tier 2, must contain:

- **Sector** — UK cleaning startup, London-based artist, Brighton serviced accommodation, charity / CIC, mixed-trade contractor, recruitment agency, etc.
- **Stage** — pre-revenue, scaling, established, in transition
- **Headcount** — solo, 2–5, 6–20, 20+
- **Engagement type** — Readiness Review, Solo Operator OS, SME AI Audit, Client OS Build, Audit + Build Bundle, Care Plan
- **Tier delivered** — Starter / Standard / Premium / Foundation / Growth / Enterprise / Lite / Core / Deep Dive (per locked pricing)
- **Situation** — 2–3 sentences on what was broken before Axis arrived
- **Intervention** — bullet list of what Axis built or delivered
- **Outcome** — what changed; qualitative if not measured (default), with measurement only when evidence exists
- **Transferable pattern** — one sentence: "any [sector] business with [situation] benefits from [intervention]"
- **Compliance flags** — pricing match, claim substantiation, regulated-sector notes
- **Pull-quotes** — three options, compliance-safe, ready for site / social

## Anonymisation Rules (Tier 1)

When anonymising, the system must:

- Replace the client name with a sector identifier (e.g. "a Brighton-based serviced accommodation operator", "a South London mixed-media artist", "a UK cleaning startup")
- Strip any property addresses, registration numbers, named contractors, named beneficiaries
- Generalise specific numbers that could identify (e.g. "a 12-week plan" stays; "47 contacts on the outreach list" becomes "a structured contact list")
- Keep the sector, stage, intervention, and pattern fully intact — those are the value
- Flag any residual identifying detail before publishing

The anonymisation pass runs as a Tier C check under the Response Fidelity Policy: synthesise, verify against the original, then hand to Wayne for approval before publishing.

## Compliance Rules (Both Tiers)

Aligned with the UK compliance posture in Wayne's global CLAUDE.md:

- **No unsubstantiated outcome claims.** Plan-and-strategy claims are fine ("delivered a 12-week occupancy plan"). Results claims need evidence ("increased occupancy by 23%" requires measured proof).
- **No invented testimonials.** Pull-quotes come from real client words or are clearly framed as Wayne's description of what was built.
- **Pricing matches locked tier.** Every case study cites the actual offer at the actual published price. Never quote a discounted figure.
- **Regulated-sector flags.** If the client is MLR-regulated (accountancy, legal, lettings), special category data, or B2C high-volume, the case study includes a one-line compliance note.
- **No safeguarding, medical, financial, or legal advice published as Axis output.** Those engagements can be referenced ("supported a charity to draft its safeguarding framework with their DPO") but not detailed.

## Output Locations

- **Tier 1 sector snapshots** → `D:\Wayne Francis\Outputs\Axis AI Final Documentation\04 Client Proof\SECTOR_SNAPSHOTS\<sector_slug>.md`
- **Tier 2 hero case studies** → `D:\Wayne Francis\Axis AI\Launch\case-study-<name>.md` (existing convention)
- **Master index** → `D:\Wayne Francis\Outputs\Axis AI Final Documentation\04 Client Proof\CASE_STUDY_MASTER_INDEX.md`
- **Website-ready block** → updates to `D:\Wayne Francis\Axis AI\Launch\testimonials-website-block.md`
- **Permission log** (Tier 2 only) → `D:\Wayne Francis\Outputs\Axis AI Final Documentation\04 Client Proof\PERMISSION_LOG.md`

## Reuses Existing Artefacts

The capability builds on what already exists rather than replacing it:

- `AXIS_TESTIMONIAL_PERMISSION_FORM.md` — Tier 2 permission form (kept)
- `Launch/permission-email-template.md` — Tier 2 permission outreach (kept)
- `Launch/testimonials-website-block.md` — auto-updates with new pull-quotes
- `AXIS_CLIENT_PROOF_PACK.md` — sales-call proof pack, auto-regenerated from the master index
- `Launch/case-study-gavin-brown.md` — Tier 2 reference format (use as template)

## Active Engagement Inventory

As of 2026-05-16, the following client folders exist under `D:\Wayne Francis\Clients\`:

| Folder | Files | Tier 1 candidate | Tier 2 candidate |
|---|---:|---|---|
| Lenox – Crystal Moss | 47 | ✅ heaviest material | possible after permission |
| Tianna | 27 | ✅ multi-project Solo OS | possible |
| Together We Ride CIC | 19 | ✅ Charity / CIC sector ref | already public charity |
| Gavin Brown | 13 | already Tier 2 ✅ | done |
| WKS Building Contractors | 10 | ✅ trades sector ref | possible |
| Shimmer Cleaning Ltd | 8 | ✅ cleaning startup | possible |
| Joseph Farodoye / Bluxe | 4 | ✅ Solo OS baseline | likely (per memory) |
| Anthony Lewis Property | 3 | ✅ estate agent prompts | possible |
| Reliable and Shine | 3 | possibly | unlikely |
| Mark Francis | 1 | not yet | not yet |
| Blux | 1 | not yet | not yet |
| Shimmer Cleaning | 1 | not yet | not yet |

Plus existing captured proof:
- SCC Homes Ltd (testimonial, permission pending)
- Sonjie Francis / Care Rota (qualitative, family attribution)
- Sonjie Francis / TikTok Review (qualitative, family attribution)
- Gavin Brown (Tier 2 hero case study, permission confirmed)

**Initial Tier 1 sweep target: 8 snapshots.** Lenox, Tianna, Together We Ride, WKS, Shimmer Cleaning Ltd, Joseph/Bluxe, Anthony Lewis, plus the SCC Homes engagement (Tier 1 version while we wait for permission on the Tier 2).

## MVP Build Order

1. Spec + module registration (this file + entry in `axis_modules.py`).
2. `tools/local_os/axis_case_study.py` — accepts a client folder, runs the nine-step workflow, writes Tier 1 or Tier 2 output. CLI: `axis_case_study.py capture <client_folder> --tier 1|2`.
3. Sector-identifier dictionary at `config/sector_identifiers.json` so anonymisation is consistent across snapshots (no "Brighton property" in one and "south coast lettings" in another).
4. Compliance checker — sweeps every draft for unsubstantiated claims, missing pricing tier, regulated-sector flags. Halts publishable artefacts that fail.
5. Master index updater — appends to `CASE_STUDY_MASTER_INDEX.md` and regenerates the proof pack.
6. Website-block builder — picks the strongest pull-quote from each snapshot and updates `testimonials-website-block.md` for site embed.
7. Permission workflow (Tier 2 only) — drafts the permission email, logs the outcome, gates publication on confirmation.

## First CLI Surface

```powershell
python tools/local_os/axis_case_study.py inventory
python tools/local_os/axis_case_study.py capture "D:/Wayne Francis/Clients/Together We Ride CIC" --tier 1
python tools/local_os/axis_case_study.py capture "D:/Wayne Francis/Clients/Gavin Brown" --tier 2
python tools/local_os/axis_case_study.py index
python tools/local_os/axis_case_study.py compliance-check <case_study_path>
```

## Governance Rules

- Tier 1 case studies never include client names, property addresses, registration numbers, named contractors, or named beneficiaries.
- No outcome claim ships without evidence. Default to qualitative plan-and-strategy framing.
- Pricing in case studies matches the locked tier exactly.
- Every snapshot writes an audit event recording the source folder, the tier, the sector identifier, and the file path of the published artefact.
- A Tier 2 case study cannot publish without a written permission record in `PERMISSION_LOG.md`.
- Regulated-sector engagements (MLR, financial, legal, medical, safeguarding) require an explicit compliance note in the published artefact.
- Anonymisation runs as a Tier C check before publication. Wayne approves the anonymised version before any output goes live.
- Case studies are stored under Wayne's existing folder convention — the capability follows, not replaces, the file layout already in use.

## What This Lets Wayne Promise

In a sales conversation, instead of "we've built systems for businesses like yours," Wayne can hand the prospect a one-page sector snapshot that names the exact pattern, the exact intervention, the exact tier, and the exact price. The prospect sees themselves in the snapshot. The conversation moves from sceptical to specific.

When the prospect asks "who was this for," Wayne says "an anonymised client in the same sector — I can introduce you to a named reference once we are further along." That keeps Tier 2 hero studies for the deals that actually warrant them.

## Success Condition

Within one focused session, the capability runs against the eight Tier 1 candidates and produces eight sector snapshots filed under `04 Client Proof/SECTOR_SNAPSHOTS/`, each compliance-checked, brand-applied, with three ready pull-quotes. The master index updates. The website-ready block updates. Wayne has a portfolio he can use in tomorrow's sales conversations.
