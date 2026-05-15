# Voice Reply

Status: active capability spec
Date: 2026-05-15
Owner: Wayne Francis

## Purpose

Voice Reply lets Axis Local OS speak responses back to Wayne so interactions can feel closer to a conversation.

The goal is not to make voice output magical or hidden. The goal is:

```text
answer text -> logged response -> text-to-speech -> local audio -> optional playback
```

## First Provider Strategy

### Primary: Kokoro-FastAPI-style endpoint

Use a Kokoro text-to-speech server with an OpenAI-compatible speech endpoint.

Why:

- natural voice quality
- local/self-hostable
- good open-source ecosystem
- OpenAI-compatible API shape makes future provider swaps easier
- can evolve as Kokoro wrappers and local TTS tooling improve

Expected endpoint shape:

```text
POST /v1/audio/speech
```

### Fallback: Piper

Use Piper as the reliable local fallback.

Why:

- fast
- mature
- local
- good voice-assistant ecosystem
- suitable when Kokoro is unavailable or too slow

## Architecture

```text
Axis answer
-> final text selected for speech
-> governance check
-> TTS provider
-> local audio file
-> optional playback
-> audit event
```

## Provider Rules

The provider must be replaceable.

Axis should not hardwire itself to one TTS engine. It should use config:

```text
config/voice_reply.json
```

## Governance Rules

- Do not speak content before it has been generated as text.
- Do not speak private relationship notes by default.
- Do not speak client-sensitive content unless explicitly requested.
- Do not send spoken content as a message.
- Store generated audio under ignored local runtime state.
- Allow voice reply to be disabled per module later.
- Keep the text answer and source/audit trail available even when audio is generated.

## First Commands

```powershell
python tools/local_os/axis_speak.py status
python tools/local_os/axis_speak.py say "Hello Wayne, Axis voice reply is ready."
```

Planned later:

```powershell
python tools/local_os/axis_answer.py "What is Axis Local OS?" --speak
```

## MVP Build Order

1. Voice Reply spec.
2. TTS provider config.
3. Safe `axis_speak.py` CLI.
4. Kokoro endpoint health check.
5. Kokoro speech file generation.
6. Piper fallback.
7. Optional playback.
8. `axis_answer.py --speak`.

## Success Condition

Axis can generate a text answer, keep the source trail visible, then create or play a local audio version of the final answer without hiding governance.

