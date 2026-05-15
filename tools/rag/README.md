# Local RAG Tools

These scripts are the first working implementation of the Axis AI Knowledge Base.

## Ingest

```powershell
python tools/rag/kb_ingest.py
```

Creates:

```text
.kb/index.json
```

## Search

```powershell
python tools/rag/kb_search.py "What is the current Axis AI business priority?"
```

Use the returned chunks as source-backed context for an answer.

## Governed Local OS Loop

```powershell
python tools/local_os/governed_loop.py "What is the current Axis AI business priority?"
```

This is the first Axis Local OS governed loop:

```text
request -> retrieve -> cite -> stale-check -> classify -> propose -> audit
```

For work that may change files, run commands, use external services, or mutate memory, the loop marks the request as review or approval gated.

To create a memory update for review only:

```powershell
python tools/local_os/governed_loop.py "Remember that Axis Local OS starts with a governed loop before multi-agent orchestration." --propose-memory
```

Review drafts are saved under:

```text
.axis/memory_review/
```

Only move reviewed notes into `business/KNOWLEDGE_CAPTURE/`, then rebuild the index.

## Local Model Runtime Health

```powershell
python tools/local_os/model_runtime.py
```

This checks whether the configured local model runtime is reachable.

The current config is:

```text
config/local_model_runtime.json
```

Phase 1 is only a health check. It does not send prompts to the model yet.

Expected outcomes:

- If Ollama is not installed or running, the check explains that clearly.
- If Ollama is running but `qwen3-coder` is missing, the check suggests `ollama pull qwen3-coder`.
- If Ollama and the primary model are available, Axis has its first local model runtime boundary.

## Capture New Knowledge

```powershell
python tools/rag/kb_capture.py "RAG build decision" "Axis will start with local retrieval, then upgrade to embeddings after the workflow is tested." --source "Wayne and Codex planning session" --tags "rag,knowledge-base,architecture" --confidence "confirmed"
python tools/rag/kb_ingest.py
```

Captured notes are saved in:

```text
business/KNOWLEDGE_CAPTURE/
```

## Why This Starts Local

This version avoids external services while we learn the implementation flow.

Once the workflow is stable, replace the scoring engine with embeddings and a vector database. The rest of the architecture stays the same:

```text
ingest -> chunk -> index -> retrieve -> cite -> answer
```
