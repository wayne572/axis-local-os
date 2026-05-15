# OS Startup Test

Status: active
Purpose: Check whether Claude has loaded and understood the OS.

## Test Prompt

After running `LAUNCH_PROMPT.md`, ask Claude:

```text
Run the OS startup test.
Tell me:
1. What is the active priority?
2. What mode are you in?
3. What workstreams are active?
4. What is excluded?
5. Is Hermes active?
6. What is Relationship Connector Mode for?
7. What would you do next if I say: Build the next asset?
8. What happens if I say: AXIS: NEW CLIENT?
9. During first-time client setup, do you ask whether the client wants to name their AI PA?
```

## Pass Conditions

Claude passes if it answers:

1. Active priority: SF&W Project Solutions / consultancy first.
2. Mode: ORCHESTRATE by default.
3. Active workstreams include:
   - SME AI Automation Audit
   - AXIS OS Claude Build
   - Pipeline-as-a-Service
   - Relationship Connector Mode
   - Client OS Handover Template
4. Excluded: Black Map.
5. Hermes: not active; archived as reference only.
6. Relationship Connector Mode: warm intros, referrals, follow-ups, relationship memory, consent-aware communication.
7. Next build action: create the next SF&W asset, likely the SME audit checklist or cleaned outreach runbook.
8. `AXIS: NEW CLIENT` starts the client OS setup workflow in BUILD mode.
9. Yes. It asks once whether the client wants to name their AI PA or keep the default `Axis`.

## Fail Conditions

Claude fails if it:
- treats Hermes as active
- routes into Black Map
- ignores active workstreams
- cannot identify SF&W as the priority
- treats Telegram or WhatsApp as separate agents
- invents client facts
- fails to recognise `AXIS: NEW CLIENT`
- misses the one-time AI PA naming step

## If It Fails

Tell Claude:

```text
Stop. Re-read CLAUDE.md, START_HERE.md, ACTIVE_WORKSTREAMS.md, and CLAUDE_OPERATOR_MODEL.md. Then rerun the startup test.
```
