# Axis AI Knowledge Base

Purpose: give Axis OS a reliable memory layer for business knowledge, client knowledge, decisions, SOPs, offers, and research.

This is the first local RAG module. It starts with a simple file-based retriever so the workflow is easy to learn and test before adding hosted embeddings or a vector database.

## What This Module Does

1. Finds approved knowledge files.
2. Splits them into retrievable chunks.
3. Stores chunk metadata and source paths.
4. Searches the knowledge base when a user asks a question.
5. Returns the most relevant source-backed passages.

The AI should use retrieved passages as evidence. If the answer is not present in the sources, it should say so.

## Folder Map

| Path | Purpose |
|---|---|
| `SOURCE_REGISTRY.md` | Approved source areas and rules for what can be indexed |
| `RAG_IMPLEMENTATION_LESSONS.md` | Teaching notes for each build step |
| `EVALUATION_QUESTIONS.md` | Test questions used to check retrieval quality |
| `../../tools/rag/` | Local ingestion and search scripts |
| `../../business/KNOWLEDGE_CAPTURE/` | Inbox for newly discovered knowledge |
| `../../.kb/index.json` | Generated local index, not hand edited |

## Current MVP

The MVP uses local text search with chunk scoring. This is not the final RAG engine, but it teaches the same core workflow:

```text
documents -> chunks -> searchable index -> retrieved context -> cited answer
```

Later upgrades:

- OpenAI embeddings
- Qdrant, Chroma, Supabase pgvector, Pinecone, or Azure AI Search
- user/role permissions
- business/client-specific indexes
- freshness and approval gates
- answer generation with citations

## Commands

From `AXIS_OS_CODEX_CURRENT`:

```powershell
python tools/rag/kb_ingest.py
python tools/rag/kb_search.py "What is the current Axis AI business priority?"
python tools/rag/kb_capture.py "Useful thing we learned" "The detail to remember." --source "source name" --tags "tag1,tag2"
```

## Retrieval Rule

The AI OS should follow this rule when using the knowledge base:

```text
Use the retrieved sources as the factual base.
Cite source paths.
If the answer is not supported by retrieved sources, say what is missing.
Do not invent policies, pricing, delivery promises, legal claims, or client facts.
```
