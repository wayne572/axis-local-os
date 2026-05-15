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
