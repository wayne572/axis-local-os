# Reset For First-Time Setup Test

Status: reference
Purpose: Explain how to test the first-time setup flow after live testing the configured version.

## Why This Exists

The live-test build is configured with setup complete so Wayne can test the operating commands immediately.

To test first-time setup, temporarily edit:

`PERSONAL_CONTEXT.md`

Change:

```text
First-time setup complete: yes
```

to:

```text
First-time setup complete: no
```

Then run:

```text
AXIS: SOLO START
```

Expected result:
Claude should ask:

1. What should I call you?
2. Would you like to give your AI PA a name, or should we keep the default name Axis?
3. What are the main areas of your life or work you want this OS to support?
4. What usually gets dropped, delayed, or forgotten?
5. What does a good week look like for you?

## After Test

Set setup back to:

```text
First-time setup complete: yes
```

Do not leave the live-test build in setup mode unless you are testing onboarding.
