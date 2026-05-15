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
