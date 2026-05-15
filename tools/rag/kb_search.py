from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = ROOT / ".kb" / "index.json"


def tokenize(text: str) -> list[str]:
    words = re.findall(r"[a-zA-Z0-9][a-zA-Z0-9_-]{1,}", text.lower())
    stopwords = {
        "the", "and", "for", "with", "that", "this", "from", "are", "you",
        "your", "into", "what", "when", "where", "have", "has", "will",
        "axis", "should", "use", "not", "but", "can", "all", "each",
    }
    return [word for word in words if word not in stopwords]


def load_index() -> dict:
    if not INDEX_PATH.exists():
        raise SystemExit(
            f"No index found at {INDEX_PATH}. Run: python tools/rag/kb_ingest.py"
        )
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def build_document_frequency(chunks: list[dict]) -> Counter:
    df: Counter = Counter()
    for chunk in chunks:
        df.update(set(chunk.get("tokens", [])))
    return df


def score_chunk(query_terms: list[str], chunk: dict, df: Counter, total_chunks: int) -> float:
    chunk_terms = chunk.get("tokens", [])
    if not chunk_terms:
        return 0.0
    term_counts = Counter(chunk_terms)
    score = 0.0
    for term in query_terms:
        tf = term_counts.get(term, 0)
        if tf == 0:
            continue
        idf = math.log((total_chunks + 1) / (df.get(term, 0) + 1)) + 1
        score += (1 + math.log(tf)) * idf
    title = chunk.get("title", "").lower()
    source_path = chunk.get("source_path", "").lower()
    for term in query_terms:
        if term in title:
            score += 1.5
        if term in source_path:
            score += 0.75
    return score


def search(query: str, limit: int) -> list[tuple[float, dict]]:
    index = load_index()
    chunks = index.get("chunks", [])
    query_terms = tokenize(query)
    if not query_terms:
        return []
    df = build_document_frequency(chunks)
    scored = [
        (score_chunk(query_terms, chunk, df, len(chunks)), chunk)
        for chunk in chunks
    ]
    return [(score, chunk) for score, chunk in sorted(scored, reverse=True, key=lambda item: item[0])[:limit] if score > 0]


def preview(text: str, max_chars: int = 600) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= max_chars:
        return compact
    return compact[: max_chars - 3].rstrip() + "..."


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Search the Axis AI Knowledge Base")
    parser.add_argument("query", help="Question or search phrase")
    parser.add_argument("--limit", type=int, default=5, help="Number of chunks to return")
    args = parser.parse_args()

    results = search(args.query, args.limit)
    if not results:
        print("No matching chunks found.")
        return

    for rank, (score, chunk) in enumerate(results, start=1):
        print(f"\n[{rank}] score={score:.2f}")
        print(f"source: {chunk['source_path']}")
        print(f"title: {chunk['title']}")
        print(f"chunk: {chunk['chunk_index']}")
        print(preview(chunk["text"]))


if __name__ == "__main__":
    main()
