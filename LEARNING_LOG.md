# Axis Local OS Learning Log

Purpose: record what Wayne is learning while Axis Local OS is built.

This is not a changelog. It explains the ideas behind the build in plain language.

## 2026-05-15 - Build Method

Lesson:

Plan before building.

Why:

Axis Local OS is supposed to be governed infrastructure, not a pile of clever scripts. Planning first keeps scope under control and makes each change easier to review, test, and roll back.

What this means in practice:

- define the goal before editing files
- keep each phase small
- verify before moving on
- commit working checkpoints to GitHub
- write down what was learned

## 2026-05-15 - Why Start With A Runtime Boundary

Lesson:

Do not let the whole system depend directly on one model tool.

Why:

Today the easiest local runtime may be Ollama. Later it may be LM Studio, vLLM, or something better. If Axis talks through a small runtime adapter, the rest of the system does not need to be rewritten when the model provider changes.

Simple version:

```text
Axis Local OS -> runtime adapter -> Ollama/Qwen/other model
```

The adapter is the plug socket. The model is the appliance. We want to be able to change the appliance without rewiring the building.

## 2026-05-15 - What A Health Check Is

Lesson:

A health check asks whether a dependency is available before the system tries to use it.

Why:

If Axis tries to use a local model before Ollama is installed, running, or loaded with the right model, the failure will look confusing. A health check turns that into a clear message.

In Phase 1, the health check asks:

- is the local runtime reachable?
- which models are installed?
- is the primary model available?
- what should Wayne do next if something is missing?

This is a small example of governance thinking: check the operating conditions before taking action.

## 2026-05-15 - Health Check vs Model Call

Lesson:

A health check and a model call are different things.

A health check asks:

```text
Is the local model runtime available?
```

A model call asks:

```text
Can the runtime produce a response to this prompt?
```

Why:

It is safer to prove availability first, then generation second. If both are mixed together, it becomes harder to understand what failed.

Current result:

- Ollama is reachable.
- `gemma4:latest` is installed.
- `qwen3-coder` is not installed yet.
- The first governed model prompt can use `gemma4:latest` as a temporary test model.

Governance boundary:

The first prompt call is text-only. It cannot run tools, edit files, or update memory. It only proves that Axis can speak to a local model through the runtime adapter.

## 2026-05-15 - First Ungrounded Model Lesson

Lesson:

A local model can answer confidently but refer to the wrong context if we do not ground it.

What happened:

We asked the installed local model to explain Axis Local OS in one sentence. The model produced an answer about Axis network devices, not Wayne's Axis Local OS.

Why this matters:

The model was not broken. It simply did not have the right project context in the prompt. This proves the original architecture decision:

```text
retrieval first -> context injection -> model response
```

Takeaway:

Axis Local OS must not rely on model memory or brand-name guessing. Project claims need retrieved context with source IDs.

## 2026-05-15 - Grounded Prompting

Lesson:

Grounded prompting means giving the model retrieved project context before asking it to answer.

Why:

The model does not automatically know Wayne's Axis Local OS. It may know other things named Axis. Retrieval gives it the local project material it should use.

The new flow is:

```text
question -> KB search -> source-backed context -> model prompt -> audited answer
```

Important:

The model is still not allowed to update memory or run tools. Grounding improves the answer, but governance still controls the action.

First grounded result:

The same question that previously produced the wrong "Axis network devices" answer produced a correct Axis Local OS answer when local project context was injected.

Second lesson:

The primary coding model `qwen3-coder:latest` is installed, but it timed out on the first grounded generation test. `gemma4:latest` completed the grounded test successfully. This means model availability and model practicality are separate checks.

## 2026-05-15 - Tool Layer vs User Command

Lesson:

Developer tools and everyday commands should be separate.

Why:

`model_runtime.py` is useful for testing the machinery. It shows prompts, retrieved context, runtime details, and audit paths. That is good for debugging, but too noisy for daily use.

`axis_answer.py` is the first cleaner user-facing command. It still uses retrieval, grounding, local generation, source IDs, and audit logging, but it prints the answer in a simpler shape.

Simple version:

```text
model_runtime.py = inspect the engine
axis_answer.py = ask Axis a sourced question
```

## 2026-05-15 - Retrieval Quality Matters

Lesson:

Getting an answer from local context is not enough. The system needs the right local context.

What happened:

The first `axis_answer.py` test worked, but it leaned on learning-log chunks instead of the Axis Local OS constitution. The answer was sourced, but not sourced from the strongest authority document.

Fix:

We added a small authority boost for core Axis Local OS documents, especially `AXIS_LOCAL_OS_SPEC.md`.

Why:

This is an early version of reranking. Later, Axis should use stronger metadata and reranker logic so source quality is handled systematically.

## 2026-05-15 - Docs vs Registered Functionality

Lesson:

A folder of documents is not the same thing as runtime functionality.

What happened:

The Charity/CIC AI OS already existed in the repo as a strong sector build, but Axis Local OS did not yet know it was a module.

Fix:

We added `config/modules.json` and registered Charity/CIC AI OS as the first sector module.

Why:

Registration gives Axis a structured way to know:

- what the module is called
- what it is for
- which docs are authoritative
- which workflows belong to it
- which governance rules apply
- which keywords should route into it

Simple version:

```text
folder of docs = knowledge
registered module = routable functionality
```

## 2026-05-15 - Product Modules vs Sector Modules

Lesson:

Axis modules need categories.

Product modules are reusable offers or operating-system templates. Sector modules adapt a product module for a specific market or use case.

Current examples:

```text
product_module: solo_operator_os
product_module: client_os_build
sector_module: charity_cic_ai_os
```

Why:

Charity/CIC AI OS should not float as an isolated build. It sits on top of the wider product architecture, especially Client OS Build. Registering Solo Operator OS and Client OS Build makes the framework clearer.

Simple version:

```text
Core runtime = how Axis works
Product module = what Axis can deliver
Sector module = who it is adapted for
```

## 2026-05-15 - Relationship Connector OS

Lesson:

Boardy-style functionality belongs in Axis as a governed relationship module, not as a loose chatbot feature.

What we are borrowing from PingCRM:

- unified contact timelines
- relationship scoring
- identity resolution
- weekly follow-up digests
- contextual follow-up drafts
- self-hosted ownership of relationship data

What we are borrowing from OpenVolo:

- local-first CRM design
- unified contacts
- workflow types
- analytics and sync-health thinking
- AI assistant over CRM data
- encrypted credentials before real integrations

Axis adaptation:

```text
relationship memory + source IDs + consent gates + draft-only messaging + human approval
```

The first Relationship Connector OS build should work locally from approved notes and trackers before adding Gmail, LinkedIn, Telegram, WhatsApp, or browser-based enrichment.

## 2026-05-15 - Voice Intake Before Voice Autonomy

Lesson:

Before Axis can listen, it needs rules for what happens after it hears something.

Why:

Voice makes it easier to capture thoughts, but it can also make accidental actions easier. The safe pattern is transcript-first:

```text
voice -> transcript -> review -> route -> draft/answer/proposed action -> approval
```

Current decision:

Register `voice_intake` as a capability module before installing speech-to-text packages.

Recommended first engine:

`faster-whisper`

Why:

It fits the current Python build and is good for local file transcription. Live microphone support can come later once file transcription is stable and governed.

## 2026-05-15 - Voice Reply Provider Interface

Lesson:

Axis should not hardwire itself to one text-to-speech engine.

Decision:

Use a Kokoro-FastAPI-style OpenAI-compatible speech endpoint as the first natural-voice provider, with Piper as the fallback.

Why:

Kokoro gives better natural voice potential, while Piper is a strong reliable local fallback. The provider interface means Axis can swap engines later as open-source voice tech improves.

Governance:

Axis should speak only text that already exists as an answer or approved draft. Speech should not hide the written answer, source trail, or audit record.

## 2026-05-15 - File Transcription Boundary

Lesson:

The first useful voice feature is not a microphone. It is a reviewed transcript from a local audio file.

Why:

A file transcription command is easy to test, audit, and repeat. It lets Axis prove the voice intake path without turning spoken words into automatic actions.

Current implementation:

```text
audio file -> faster-whisper transcript -> proposed module route -> review required
```

Important:

`faster-whisper` is detected at runtime. If it is missing, Axis blocks clearly and records the attempt in the voice intake audit log instead of pretending transcription happened.

First runtime test:

`faster-whisper` installed successfully on Python 3.14. A short local WAV file was transcribed and routed to Relationship Connector OS. The transcript changed "Axis" into "Access", which is a useful real-world reminder that speech-to-text is helpful but not authoritative.

Governance:

The transcript is not treated as an instruction to execute. It is treated as draft input that Wayne reviews before asking Axis to route, answer, or capture anything.

## 2026-05-15 - Confirmed Voice Ask

Lesson:

Voice ask should require transcript confirmation before model generation.

What changed:

Axis can now transcribe a local audio question and stop before answering. If Wayne explicitly reruns with `--confirm-transcript`, Axis sends the transcript through the normal grounded answer path, with retrieved sources and the model runtime audit still visible.

First result:

A test question, "What is Axis Local OS?", was transcribed as "What is access local OS?" but still produced a sourced answer from the Axis spec. This proves the answer path works, but it also shows the next practical improvement: Wayne needs a way to correct the transcript before confirmation.
