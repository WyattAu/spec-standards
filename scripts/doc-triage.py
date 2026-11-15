#!/usr/bin/env python3
"""doc-triage: which SPEC-CORE docs tier governs this repo, and which gates fire?

Encodes SPEC-CORE §8 (tier table) and §7 (registry) plus the README gate
matrix. Does not re-implement the gates; it names them and their commands.
`scripts/doc-lint.sh <tier>` and `scripts/spec-audit.py --repo .` remain
the authoritative checks (SC-9: no gate exists only in CI).

Usage:
  doc-triage.py --repo <path> [--tier s|k|a|d]
  doc-triage.py --repo <path> --registry <path/to/estate.yml>

Tier inference (when --tier is absent): SPEC*.md present -> s;
mkdocs/astro/docs-pipeline markers -> d; library manifest without app
markers -> k; otherwise a. Inference is advisory; an explicit --tier or
the estate.yml `docs.tier` declaration (SC-7) always wins.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TIERS = {
    "s": ("spec-heavy: semantics governed by SC-3/SC-4/SC-6",
          "accounting-spec, spec-standards, estate research repos"),
    "k": ("library kits: public interfaces need REQ anchors and projections, not full oracles",
          "the kit estate"),
    "a": ("application/business: normative business rules need truth tables and citable sources (SC-8)",
          "estate application repos"),
    "d": ("doc pipelines: build reproducibility and link rot dominate",
          "homebite_docs and peers"),
}


def infer(repo: Path) -> tuple[str, str]:
    if list(repo.glob("SPEC*.md")):
        return "s", "SPEC*.md present"
    markers_d = ["mkdocs.yml", "astro.config.mjs", "docusaurus.config.js"]
    if any((repo / m).exists() for m in markers_d):
        return "d", "docs-pipeline marker"
    lib = (repo / "Cargo.toml").exists() or (repo / "pyproject.toml").exists()
    app_markers = any((repo / m).exists() for m in
                      ["src/main.rs", "src/main.py", "cmd", "package.json"])
    if lib and not app_markers:
        return "k", "library manifest, no app entrypoint"
    return "a", "default for application/business repos"


def registry_tier(repo: Path, registry: Path) -> str | None:
    try:
        import yaml  # type: ignore
    except ImportError:
        return None
    data = yaml.safe_load(registry.read_text(encoding="utf-8")) or {}
    repos = data.get("repos") or {}
    entry = repos.get(repo.name) or {}
    docs = (entry or {}).get("docs") or {}
    return docs.get("tier")


def main() -> int:
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--repo", default=".")
    ap.add_argument("--tier", choices=["s", "k", "a", "d"])
    ap.add_argument("--registry", help="path to engineering-standards estate.yml")
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    if not repo.is_dir():
        print(f"doc-triage: not a directory: {repo}", file=sys.stderr)
        return 2

    tier = a.tier
    source = "explicit --tier"
    if not tier and a.registry:
        rt = registry_tier(repo, Path(a.registry))
        if rt:
            tier, source = rt, "estate.yml registry (SC-7)"
    if not tier:
        tier, why = infer(repo)
        source = f"advisory inference: {why}"

    print(f"tier {tier} ({source})")
    print(f"SPEC-CORE §8: {TIERS[tier][0]}")
    print(f"examples: {TIERS[tier][1]}")
    print()
    print("gates that fire (authoritative checks; SC-9: no gate exists only in CI):")
    print(f"  1. bash scripts/doc-lint.sh {tier}            # em-dash, lint, truth table, llms, stamps, oracle")
    if tier == "s":
        print("  2. bash scripts/doc-lint.sh s --req-check     # REQ cross-check (advisory -> blocking 2027-01-01)")
    print("  3. python3 scripts/spec-audit.py --repo .     # registry vs reality (SC-7)")
    print("  4. .github/workflows/docs.yml -> WyattAu/spec-standards docs.yml@main (SC-9)")
    print()
    print("tier artifacts:")
    print("  truth table (SC-1): required at s,a — '## Where the truth lives' in AGENTS.md")
    print("  llms.txt (SC-10):   required at s,a")
    print("  status stamps (SC-5): required always; FROZEN needs ISO date")
    if tier == "s":
        print("  oracle line (SC-6): required in every SPEC*.md, or 'No-oracle: <reason>'")
        print("  REQ anchors (SC-4): requirements table + code tags")
    print()
    print("register the posture in engineering-standards estate.yml `docs:` block (SC-7).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
