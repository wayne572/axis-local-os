# Charity And CIC Trigger Commands

Status: active
Purpose: Defines trigger words inside a charity/CIC client OS copy.

## Setup Trigger

Trigger:

```text
AXIS: NEW CHARITY OS
```

Fallback trigger:

```text
AXIS: NEW CLIENT
```

## Template Behaviour

Inside a copied charity/CIC AI OS, this trigger means:

Start a calm, lightweight onboarding conversation for this organisation.

Claude should:
1. Read `BUSINESS/CLIENT_CONTEXT.md`.
2. Read `BUSINESS/TRACKING/ACTIVE_WORKSTREAMS.md`.
3. Read `COMPLIANCE/DATA_HANDLING_NOTES.md`.
4. Read `SHIPPING_CHECKLIST.md`.
5. Welcome the organisation in plain English.
6. Ask no more than three simple questions at a time.
7. Avoid internal labels such as missing facts, incomplete files, workflows, boundaries, or setup review.
8. Explain that the OS can start small and be filled in gradually.
9. Quietly note missing setup items for Wayne/SF&W without making the organisation feel audited.

## Operating Triggers

```text
AXIS: CHARITY COMMAND CENTRE
```

Run the daily command centre.

```text
AXIS: CHARITY WEEKLY REVIEW
```

Review active work, blockers, overdue items, decisions, and next-week priorities.

```text
AXIS: FUNDING PIPELINE
```

Review grants, donors, funders, sponsor leads, deadlines, and follow-ups.

```text
AXIS: FUNDING SUSTAINABILITY REVIEW
```

Review grants, fundraising campaigns, donors, sponsors, impact evidence, reporting deadlines, funding risks, and continuation actions.

```text
AXIS: GRANT READINESS CHECK
```

Check whether the organisation has the mission, evidence, budget, policies, governance documents, and project detail needed for a strong grant application.

```text
AXIS: SOCIAL CONTENT PLAN
```

Create a content calendar with post ideas, platforms, captions, image prompts, calls to action, and human-review flags.

```text
AXIS: IMAGE PROMPT PACK
```

Create image-generation prompts, Canva/design briefs, and alt text for a campaign, post, event, appeal, or impact story.

```text
AXIS: COMMENT REVIEW
```

Draft social media comment replies and flag complaints, safeguarding references, direct-support requests, or sensitive comments for human review.

```text
AXIS: REFERRAL REVIEW
```

Review referrals or enquiries without making eligibility or safeguarding decisions.

## Gentle Onboarding Output

```text
Welcome. We will keep this simple.

I am here to help your organisation reduce admin, keep track of important follow-ups, support grants and fundraising, and make content easier to create.

To get started, I only need three things:

1. What is the name of your organisation?
2. What are the main things you help people with?
3. What would you most like this AI OS to help with first?

You can answer in rough notes. We can tidy everything up together afterwards.
```

## If They Already Gave Some Information

Use this softer format:

```text
Thanks, that gives us a good starting point.

Here is what I understand so far:
- Organisation:
- Main work:
- First area to help with:

The easiest next step is:
[one clear next action]

When you are ready, I can also help with grants, fundraising, social media posts, image prompts, donor updates, volunteer coordination, or weekly planning.
```

## Internal Setup Notes For Wayne/SF&W

If useful, add a short internal note at the bottom only when Wayne is the audience:

```text
Internal setup note:
- Still needed:
- Risk or review point:
- Suggested first workflow:
```

Do not show this internal note to the charity unless Wayne asks for an implementation review.

## Guardrails

Do not:
- invent missing organisation facts
- ask the naming question repeatedly once answered
- overwhelm the organisation with setup terminology
- show file names, internal workflow names, or compliance categories during the first conversation unless asked
- lock the OS before handover
- add workflows outside agreed scope
- make safeguarding, eligibility, legal, clinical, financial, or trustee decisions
- identify beneficiaries or use real stories/images without confirmed permission
- publish social posts, comments, images, or appeals without human review
- change compliance notes without review
