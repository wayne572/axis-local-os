from __future__ import annotations

import argparse
import fnmatch
import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from html import unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / ".kb"
OUTPUT_PATH = OUTPUT_DIR / "index.json"
SCOPE_PATH = ROOT / "config" / "copilot_scope.json"

DEFAULT_SOURCE_DIRS = [
    ROOT,
    ROOT / "CORE",
    ROOT / "OS_GUIDES",
    ROOT / "PRODUCT_MANUAL",
    ROOT / "business",
    ROOT / "PROJECTS" / "SFW_PROJECT_SOLUTIONS",
    ROOT.parent / "final-docs-drafts",
]

ALLOWED_EXTENSIONS = {".md", ".txt", ".html"}
EXCLUDED_PARTS = {".git", ".claude", ".kb", "__pycache__", ".axis", "node_modules"}
EXCLUDED_RELATIVE_PREFIXES = {
    "CORE/KNOWLEDGE_BASE",
    "tools/rag",
}
CHUNK_WORDS = 220
CHUNK_OVERLAP = 45
MAX_FILE_BYTES = 2_500_000


@dataclass
class ScopeRoot:
    label: str
    path: Path
    kind: str
    scope_tag: str
    authority_boost: float = 0.0
    per_client_subfolders: bool = False


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
    scope_tag: str = "internal_only"
    kind: str = "build"
    ingest_label: str = "axis_local_os_repo"
    authority_boost: float = 0.0
    client_slug: str | None = None


def load_scope_config(scope_path: Path = SCOPE_PATH) -> tuple[list[ScopeRoot], list[str]]:
    if not scope_path.exists():
        return [], []
    try:
        data = json.loads(scope_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return [], []
    roots: list[ScopeRoot] = []
    for entry in data.get("ingest_roots", []):
        raw_path = entry.get("path")
        if not raw_path:
            continue
        if raw_path == ".":
            resolved = ROOT
        else:
            resolved = Path(raw_path)
            if not resolved.is_absolute():
                resolved = (ROOT / raw_path).resolve()
        roots.append(
            ScopeRoot(
                label=entry.get("label", resolved.name or "unknown"),
                path=resolved,
                kind=entry.get("kind", "build"),
                scope_tag=entry.get("scope_tag", "internal_only"),
                authority_boost=float(entry.get("authority_boost", 0.0)),
                per_client_subfolders=bool(entry.get("per_client_subfolders", False)),
            )
        )
    excludes = list(data.get("exclude_patterns", []))
    return roots, excludes


def should_index(path: Path, extra_excludes: list[str] | None = None) -> bool:
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
    if extra_excludes:
        name = path.name
        rel_parts = path.parts
        for pattern in extra_excludes:
            if fnmatch.fnmatch(name, pattern):
                return False
            if any(fnmatch.fnmatch(part, pattern) for part in rel_parts):
                return False
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            return False
    except OSError:
        return False
    return True


def resolve_client_slug(path: Path, root: ScopeRoot) -> str | None:
    if not root.per_client_subfolders:
        return None
    try:
        rel = path.relative_to(root.path)
    except ValueError:
        return None
    parts = rel.parts
    if not parts:
        return None
    return parts[0]


def iter_scope_files(roots: list[ScopeRoot], extra_excludes: list[str]) -> list[tuple[Path, ScopeRoot]]:
    seen: set[Path] = set()
    files: list[tuple[Path, ScopeRoot]] = []
    for root in roots:
        if not root.path.exists():
            continue
        if root.path.is_file() and should_index(root.path, extra_excludes):
            resolved = root.path.resolve()
            if resolved not in seen:
                seen.add(resolved)
                files.append((resolved, root))
            continue
        for path in root.path.rglob("*"):
            try:
                if not path.is_file():
                    continue
            except OSError:
                continue
            if not should_index(path, extra_excludes):
                continue
            try:
                resolved = path.resolve()
            except OSError:
                continue
            if resolved in seen:
                continue
            seen.add(resolved)
            files.append((resolved, root))
    return sorted(files, key=lambda pair: str(pair[0]).lower())


def default_roots() -> list[ScopeRoot]:
    return [
        ScopeRoot(label="axis_local_os_repo", path=src, kind="build", scope_tag="internal_only")
        for src in DEFAULT_SOURCE_DIRS
    ]


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


def build_index(roots: list[ScopeRoot], extra_excludes: list[str]) -> dict:
    indexed_at = datetime.now(timezone.utc).isoformat()
    chunks: list[Chunk] = []
    files = iter_scope_files(roots, extra_excludes)

    skipped = 0
    per_root_counts: dict[str, int] = {}

    for path, root in files:
        try:
            raw = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            skipped += 1
            continue
        text = clean_text(raw, path.suffix)
        if not text:
            continue
        title = extract_title(text, path)
        modified_at = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()
        source_path = relative_to_workspace(path)
        client_slug = resolve_client_slug(path, root)
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
                    scope_tag=root.scope_tag,
                    kind=root.kind,
                    ingest_label=root.label,
                    authority_boost=root.authority_boost,
                    client_slug=client_slug,
                )
            )
            per_root_counts[root.label] = per_root_counts.get(root.label, 0) + 1

    return {
        "schema": "axis-kb-index-v2",
        "root": str(ROOT),
        "indexed_at": indexed_at,
        "chunk_count": len(chunks),
        "per_root_chunk_counts": per_root_counts,
        "skipped_files": skipped,
        "chunks": [asdict(chunk) for chunk in chunks],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the Axis Local OS knowledge-base index")
    parser.add_argument(
        "--scope",
        default=str(SCOPE_PATH),
        help="Path to copilot_scope.json. Pass 'none' to use the default repo-only roots.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Scan files and print counts without writing the index.",
    )
    args = parser.parse_args()

    scope_path = None if args.scope.lower() == "none" else Path(args.scope)
    if scope_path is not None and scope_path.exists():
        roots, extra_excludes = load_scope_config(scope_path)
        print(f"Loaded scope: {scope_path}")
        print(f"Scope roots: {len(roots)}")
    else:
        roots = default_roots()
        extra_excludes = []
        if scope_path is not None:
            print(f"Scope file not found at {scope_path}. Falling back to default roots.")
        else:
            print("Scope disabled. Using default roots.")

    if not roots:
        print("No ingest roots resolved. Nothing to do.")
        return

    for root in roots:
        status = "found" if root.path.exists() else "missing"
        print(f"  [{root.scope_tag:14s}] {root.label:28s} {status:7s} {root.path}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    index = build_index(roots, extra_excludes)
    print(f"Indexed {index['chunk_count']} chunks across {len(index['per_root_chunk_counts'])} root(s)")
    for label, count in sorted(index["per_root_chunk_counts"].items(), key=lambda kv: -kv[1]):
        print(f"  {label:28s} {count} chunks")
    if args.dry_run:
        print("(dry run; nothing written)")
        return
    OUTPUT_PATH.write_text(json.dumps(index, indent=2), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
