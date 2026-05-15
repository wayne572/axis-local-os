# RAG Implementation Lessons

This file is the teaching track for building the Axis AI Knowledge Base.

## Lesson 1: What We Are Building

We are building a retrieval layer for Axis OS.

The AI model is good at reasoning and explaining. The knowledge base is responsible for facts.

Mental model:

```text
AI model = reasoning engine
Knowledge base = trusted memory
Retriever = the librarian
Sources = proof
```

## Lesson 2: Ingestion

Ingestion means taking business documents and converting them into a searchable form.

In this MVP, ingestion:

1. scans approved folders
2. reads Markdown, HTML, and text files
3. removes noisy markup
4. splits the text into chunks
5. saves chunks into `.kb/index.json`

Common mistake: indexing everything without a registry. That makes the AI retrieve outdated, private, or irrelevant material.

## Lesson 3: Chunking

Chunking means splitting long files into smaller evidence blocks.

Good chunks are large enough to contain meaning but small enough to search accurately.

This MVP uses word-count chunks. Later we can improve this with heading-aware chunking.

## Lesson 4: Retrieval

Retrieval means ranking chunks against a question.

This MVP uses local token scoring. Later, embeddings will improve semantic matching.

The important lesson is the workflow:

```text
question -> search index -> top chunks -> cited context
```

## Lesson 5: Answering

The answer step should come after retrieval.

The AI OS should receive:

- user question
- retrieved source chunks
- instruction to answer only from those chunks
- instruction to cite sources
- instruction to admit when evidence is missing

## Lesson 6: Business Deployment

For each business/client deployment:

1. create a source registry
2. approve sources
3. index sources
4. test common questions
5. review source citations
6. add permissions
7. schedule re-indexing

The goal is not just "answers." The goal is correct, traceable, current answers.

