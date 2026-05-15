from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MODULES_PATH = ROOT / "config" / "modules.json"


def load_registry(path: Path = MODULES_PATH) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Module registry not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def module_exists(module: dict[str, Any]) -> list[str]:
    missing: list[str] = []
    file_groups = [
        "authority_docs",
        "workflow_docs",
        "governance_docs",
        "template_docs",
    ]
    for group in file_groups:
        for relative_path in module.get(group, []):
            if not (ROOT / relative_path).exists():
                missing.append(relative_path)
    return missing


def list_modules(registry: dict[str, Any]) -> str:
    lines = ["# Axis Modules", ""]
    for module_id, module in registry.get("modules", {}).items():
        lines.append(f"- `{module_id}` - {module.get('name')} ({module.get('status')})")
    return "\n".join(lines)


def show_module(registry: dict[str, Any], module_id: str) -> str:
    modules = registry.get("modules", {})
    module = modules.get(module_id)
    if not module:
        available = ", ".join(sorted(modules)) or "none"
        raise SystemExit(f"Unknown module '{module_id}'. Available modules: {available}")

    missing = module_exists(module)
    lines = [
        f"# {module.get('name', module_id)}",
        "",
        f"ID: `{module_id}`",
        f"Status: {module.get('status')}",
        f"Type: {module.get('type')}",
        f"Purpose: {module.get('purpose')}",
    ]
    if module.get("base_path"):
        lines.append(f"Base path: {module.get('base_path')}")

    for title, key in [
        ("Authority Docs", "authority_docs"),
        ("Workflow Docs", "workflow_docs"),
        ("Governance Docs", "governance_docs"),
        ("Template Docs", "template_docs"),
        ("Commands", "commands"),
        ("Routing Keywords", "routing_keywords"),
        ("Governance Rules", "governance_rules"),
    ]:
        values = module.get(key, [])
        if values:
            lines.extend(["", f"## {title}", ""])
            lines.extend(f"- {value}" for value in values)

    lines.extend(["", "## File Check", ""])
    if missing:
        lines.append("Missing files:")
        lines.extend(f"- {path}" for path in missing)
    else:
        lines.append("All registered files found.")
    return "\n".join(lines)


def route_module(registry: dict[str, Any], query: str) -> str:
    query_lower = query.lower()
    scored: list[tuple[int, str, dict[str, Any]]] = []
    for module_id, module in registry.get("modules", {}).items():
        keywords = module.get("routing_keywords", [])
        score = sum(1 for keyword in keywords if keyword.lower() in query_lower)
        if score:
            scored.append((score, module_id, module))

    if not scored:
        default_id = registry.get("default_module", "core")
        module = registry.get("modules", {}).get(default_id, {})
        return f"No specialist module matched. Default route: `{default_id}` - {module.get('name', 'Unknown')}"

    score, module_id, module = sorted(scored, reverse=True, key=lambda item: item[0])[0]
    return f"Route: `{module_id}` - {module.get('name')}\nMatched keywords: {score}"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Inspect Axis Local OS registered modules")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List registered modules")

    show_parser = subparsers.add_parser("show", help="Show a registered module")
    show_parser.add_argument("module_id", help="Module ID, for example charity_cic_ai_os")

    route_parser = subparsers.add_parser("route", help="Route a query to the best module")
    route_parser.add_argument("query", help="Request or question to route")

    parser.set_defaults(command="list")
    args = parser.parse_args()
    registry = load_registry()

    if args.command == "show":
        print(show_module(registry, args.module_id))
    elif args.command == "route":
        print(route_module(registry, args.query))
    else:
        print(list_modules(registry))


if __name__ == "__main__":
    main()

