# Voice Intake

Status: active capability spec
Date: 2026-05-15
Owner: Wayne Francis

## Purpose

Voice Intake lets Wayne talk to Axis Local OS when typing is slow, tiring, or impractical.

The goal is not voice autonomy. The goal is safe voice capture:

```text
voice -> transcript -> review -> route -> draft/answer/proposed action -> approval
```

## First Principle

Voice input must not bypass governance.

Axis may transcribe, summarise, route, and draft from voice input. It must not execute commands, send messages, update permanent memory, or create introductions without review.

## Recommended Open-Source Components

### First Engine: faster-whisper

Use for the first Python-native MVP.

Why:

- local transcription
- good Python fit
- practical for recorded audio files
- easier to integrate with existing Axis tools

### Later Engine: whisper.cpp

Use when Axis needs lower-level microphone support, smaller deployment, or direct streaming experiments.

Why:

- fully local
- lightweight C/C++ engine
- strong Windows ecosystem
- can support microphone workflows

### Optional External Dictation Apps

Tools like OpenWhispr, FreeWispr, Stype, and Vibe Transcribe may be useful alongside Axis for general dictation, but they should not become the governed Axis voice layer unless they can be audited and controlled.

## MVP Build Order

1. Voice Intake spec and module registration.
2. File transcription command.
3. Transcript review output.
4. Route transcript through `axis_modules.py`.
5. Ask Axis from transcript using grounded retrieval.
6. Create review-only memory proposals from transcript when requested.
7. Add microphone capture only after file transcription is stable.
8. Add hotkey/live dictation later, if needed.

## First Commands

```text
AXIS: VOICE TRANSCRIBE
AXIS: VOICE ASK
AXIS: VOICE ROUTE
AXIS: VOICE CAPTURE DRAFT
```

First CLI surface:

```powershell
python tools/local_os/axis_voice.py transcribe path/to/audio.wav
python tools/local_os/axis_voice.py route path/to/audio.wav
python tools/local_os/axis_voice.py ask path/to/audio.wav
```

Current implementation:

- `status` reports the configured engine and whether `faster-whisper` is importable.
- `transcribe` validates a local audio file, runs local file transcription when `faster-whisper` is installed, prints the transcript for review, proposes a module route, and writes an audit event.
- `route` uses the same safe transcript-first path and proposes a route without executing the request.
- `ask` transcribes and blocks before answering unless `--confirm-transcript` is provided.
- `--transcript "..."` can be used as a manual correction; the raw transcript is still shown and audited.
- `capture-draft` remains a planned governed follow-on step.

First runtime test:

- `faster-whisper` installed successfully in the current Python environment.
- A short local WAV file transcribed successfully and proposed the Relationship Connector OS route.
- The transcript contained a small recognition error, which confirms the review-first design.
- A confirmed voice ask produced a grounded Axis answer with sources and a model audit trail.

## Governance Rules

- Do not execute commands directly from voice.
- Do not send messages directly from voice.
- Do not update permanent memory directly from voice.
- Always show transcript before action.
- Mark unclear transcript sections.
- Keep audio files local unless Wayne explicitly asks otherwise.
- Treat relationship, client, health, finance, legal, and safeguarding content as sensitive.
- Require review before turning voice notes into relationship memory, client records, or public outputs.

## Transcript Review Standard

Every voice transcript should show:

- source audio file
- transcription engine
- timestamp
- transcript text
- uncertainty notes, if available
- proposed route
- proposed next action
- confirmation requirement

## Relationship Connector Interaction

Voice Intake is especially useful for Relationship Connector OS.

Example:

```text
Met Sarah from a recruitment agency. Interested in reducing admin and open to practical AI. Follow up next week.
```

Axis should:

- transcribe the note
- identify it as relationship context
- route it to `relationship_connector_os`
- propose a relationship capture draft
- require review before saving it

## Success Condition

Wayne can record a short voice note, review the transcript, and have Axis route it into the right module without typing the full request.
