# Axis Local OS Build Plan

Status: active
Date started: 2026-05-15
Owner: Wayne Francis

## Build Rule

Always plan before building.

Each build phase should include:

- goal
- why it matters
- files changed
- verification performed
- learning notes
- next action

## Current Phase

Phase 1: Local Model Runtime

Goal:

Create the first local model boundary so Axis Local OS can detect and later talk to a local model runtime without hard-wiring the whole system to one provider.

Why it matters:

The model should be replaceable. Axis Local OS is built around governance, memory, retrieval, and workflow control, so the runtime layer must be modular from the start.

## Phase Roadmap

| Phase | Name | Status | Outcome |
|---|---|---|---|
| 0 | Constitution and governed loop | complete | Axis has source-backed retrieval, approval classification, audit logging, and review-only memory drafts. |
| 1 | Local model runtime | complete | Axis can check whether Ollama or another local provider is available. |
| 2 | Model invocation | first pass complete | Axis can send a prompt to a configured local model and capture the response through governance. |
| 3 | Coding-agent workflow | planned | Axis can prepare repo edits through a governed local assistant workflow. |
| 4 | Durable RAG memory | planned | Axis can move from local JSON search to a stronger memory store. |
| 5 | Reranking and source discipline | planned | Axis improves retrieval quality and reduces bad context. |
| 6 | Governance review queue | planned | Axis can review command approvals and memory updates in a structured queue. |
| 7 | Multi-agent orchestration | planned | Axis can route planner, coder, researcher, memory, and governance roles. |
| 8 | Reflection and learning loops | planned | Axis can detect repeated mistakes and propose workflow improvements. |

## Phase 1 Scope

Included:

- local runtime config
- Ollama-first provider definition
- runtime health check
- clear error messages if Ollama is not installed or not running
- learning notes for Wayne

Not included yet:

- model prompting
- autonomous coding
- LangGraph
- Qdrant/PostgreSQL
- command execution by agents

## Next Action

Build the local model runtime health check.

## Phase 1 Progress Notes

- Ollama is reachable locally.
- `gemma4:latest` is installed and can be used as a temporary test model.
- `qwen3-coder` did not finish installing during the first pull attempt.
- Axis now needs a governed prompt call that can use an explicit model override while the primary model is pending.

## Phase 2 Progress Notes

- Axis can send one prompt to a local Ollama model.
- The prompt call writes an audit event.
- The prompt call does not run tools, edit files, or update memory.
- First test with `gemma4:latest` proved generation works but also showed ungrounded model risk.
- `qwen3-coder:latest` is now installed, but the first grounded generation test timed out.
- `gemma4:latest` completed the grounded generation test and answered from Axis context.

Next action:

Build a grounded prompt path that retrieves Axis context before calling the model.

## Phase 3 Progress Notes

Status: first pass complete

Goal:

Add a grounded model path that retrieves local Axis KB chunks before generation.

Expected result:

The same local model that guessed incorrectly should answer from Axis Local OS source material when retrieved context is injected.

Verified result:

`gemma4:latest` answered correctly from retrieved Axis context. `qwen3-coder:latest` needs further performance testing before it becomes the default practical model.

## Phase 4 Progress Notes

Status: in progress

Goal:

Create a clean everyday command for sourced Axis answers.

Why:

The low-level runtime tool is useful for debugging, but normal use needs a smaller answer surface: answer, sources, model, audit path.

Progress:

- Added `tools/local_os/axis_answer.py`.
- Verified it produces a clean sourced answer.
- Found that source quality matters even when retrieval works.
- Added an initial authority boost for core Axis Local OS documents.

## Phase 5 Progress Notes

Status: in progress

Goal:

Register specialist modules so Axis Local OS can recognise and route to domain functionality.

First module:

`charity_cic_ai_os`

Why:

The Charity/CIC OS already existed as sector-build material. Registration turns it into something the local runtime can inspect, validate, and route toward.

## Phase 6 Progress Notes

Status: first pass complete

Goal:

Register the core product modules that sit underneath sector overlays.

Registered product modules:

- `solo_operator_os`
- `client_os_build`

Verified:

- module list includes both products
- file checks pass for both products
- routing sends solo requests to `solo_operator_os`
- routing sends client build requests to `client_os_build`

## Phase 7 Progress Notes

Status: in progress

Goal:

Register Relationship Connector OS and bring in best-practice patterns from PingCRM and OpenVolo without breaking Axis governance.

Module:

`relationship_connector_os`

Key boundary:

Start with local relationship memory, intro tracking, and draft-only follow-ups before adding external account integrations.

## Phase 8 Progress Notes

Status: first pass complete

Goal:

Add safe voice intake so Wayne can talk to Axis Local OS when typing is a barrier.

Completed scope:

- voice safety spec
- module registration
- file transcription CLI surface
- faster-whisper dependency detection
- transcript review output
- proposed module route
- voice intake audit events

Verification:

- `python tools\local_os\axis_voice.py status` reports config and dependency state.
- `python tools\local_os\axis_voice.py transcribe missing.wav` blocks cleanly when the file is missing.
- `faster-whisper` installed successfully in the current Python 3.14 environment.
- `python tools\local_os\axis_voice.py transcribe .axis\voice_intake_test\axis_voice_test.wav` produced a transcript, proposed the `relationship_connector_os` route, required review, and wrote a voice intake audit event.
- The test transcript misheard "Axis" as "Access", confirming that transcript review is necessary before routing or memory capture.

Additional progress:

- Added a governed `ask` path.
- `python tools\local_os\axis_voice.py ask .axis\voice_intake_test\axis_voice_question.wav` transcribes and blocks before answering.
- `python tools\local_os\axis_voice.py ask .axis\voice_intake_test\axis_voice_question.wav --confirm-transcript --model gemma4:latest --timeout 180` produced a grounded Axis answer with sources and model audit trail.

Next implementation:

Build the review-only voice capture draft path for turning a corrected transcript into a proposed memory/update draft.

Transcript correction:

- Added `--transcript` override for voice commands.
- The corrected transcript is used for routing and confirmed asks.
- The raw transcript is still shown and audited.

## Phase 9 Progress Notes

Status: in progress

Goal:

Add voice reply as a replaceable text-to-speech capability.

Provider strategy:

- primary: Kokoro-FastAPI-style OpenAI-compatible speech endpoint
- fallback: Piper

Safety choice:

Voice reply is disabled by default until a local TTS provider is running and tested.
