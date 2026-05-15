from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from html import unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / ".kb"
OUTPUT_PATH = OUTPUT_DIR / "index.json"

SOURCE_DIRS = [
    ROOT,
    ROOT / "CORE",
    ROOT / "OS_GUIDES",
    ROOT / "PRODUCT_MANUAL",
    ROOT / "business",
    ROOT / "PROJECTS" / "SFW_PROJECT_SOLUTIONS",
    ROOT.parent / "final-docs-drafts",
]

ALLOWED_EXTENSIONS = {".md", ".txt", ".html"}
EXCLUDED_PARTS = {".git", ".claude", ".kb", "__pycache__"}
EXCLUDED_RELATIVE_PREFIXES = {
    "CORE/KNOWLEDGE_BASE",
    "tools/rag",
}
CHUNK_WORDS = 220
CHUNK_OVERLAP = 45


@dataclass
class Chunk:
    id: str
    source_path: str
    source_type: str
    title: str
    chunk_index: int
    text: str
    tokens: list[str]
    indexed_at: str
    modified_at: str


def should_index(path: Path) -> bool:
    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        return False
    if any(part in EXCLUDED_PARTS for part in path.parts):
        return False
    try:
        relative = path.relative_to(ROOT).as_posix()
        if any(relative.startswith(prefix) for prefix in EXCLUDED_RELATIVE_PREFIXES):
            return False
    except ValueError:
        pass
    if path.name.lower().endswith(".review.html"):
        return False
    return True


def iter_source_files() -> list[Path]:
    seen: set[Path] = set()
    files: list[Path] = []
    for source_dir in SOURCE_DIRS:
        if not source_dir.exists():
            continue
        if source_dir.is_file() and should_index(source_dir):
            resolved = source_dir.resolve()
            if resolved not in seen:
                seen.add(resolved)
                files.append(resolved)
            continue
        for path in source_dir.rglob("*"):
            if path.is_file() and should_index(path):
                resolved = path.resolve()
                if resolved not in seen:
                    seen.add(resolved)
                    files.append(resolved)
    return sorted(files)


def clean_text(raw: str, suffix: str) -> str:
    text = raw
    if suffix.lower() == ".html":
        text = re.sub(r"(?is)<script.*?</script>", " ", text)
        text = re.sub(r"(?is)<style.*?</style>", " ", text)
        text = re.sub(r"(?s)<[^>]+>", " ", text)
        text = unescape(text)
    text = re.sub(r"`{3}.*?`{3}", " ", text, flags=re.S)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_title(text: str, path: Path) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip() or path.stem
        if stripped:
            return stripped[:90]
    return path.stem


def tokenize(text: str) -> list[str]:
    words = re.findall(r"[a-zA-Z0-9][a-zA-Z0-9_-]{1,}", text.lower())
    stopwords = {
        "the", "and", "for", "with", "that", "this", "from", "are", "you",
        "your", "into", "what", "when", "where", "have", "has", "will",
        "axis", "should", "use", "not", "but", "can", "all", "each",
    }
    return [word for word in words if word not in stopwords]


def chunk_text(text: str) -> list[str]:
    words = text.split()
    if not words:
        return []
    chunks: list[str] = []
    step = max(1, CHUNK_WORDS - CHUNK_OVERLAP)
    for start in range(0, len(words), step):
        chunk_words = words[start : start + CHUNK_WORDS]
        if len(chunk_words) < 25 and chunks:
            break
        chunks.append(" ".join(chunk_words))
    return chunks


def relative_to_workspace(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT.parent))
    except ValueError:
        return str(path)


def build_index() -> dict:
    indexed_at = datetime.now(timezone.utc).isoformat()
    chunks: list[Chunk] = []
    files = iter_source_files()

    for path in files:
        try:
            raw = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        text = clean_text(raw, path.suffix)
        if not text:
            continue
        title = extract_title(text, path)
        modified_at = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()
        source_path = relative_to_workspace(path)
        for index, chunk in enumerate(chunk_text(text), start=1):
            chunk_id = f"{source_path}::chunk-{index}"
            chunks.append(
                Chunk(
                    id=chunk_id,
                    source_path=source_path,
                    source_type=path.suffix.lower().lstrip("."),
                    title=title,
                    chunk_index=index,
                    text=chunk,
                    tokens=tokenize(chunk),
                    indexed_at=indexed_at,
                    modified_at=modified_at,
                )
            )

    return {
        "schema": "axis-kb-index-v1",
        "root": str(ROOT),
        "indexed_at": indexed_at,
        "chunk_count": len(chunks),
        "chunks": [asdict(chunk) for chunk in chunks],
    }


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    index = build_index()
    OUTPUT_PATH.write_text(json.dumps(index, indent=2), encoding="utf-8")
    print(f"Indexed {index['chunk_count']} chunks")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
