# ADR-0001: Split specification and documentation standards out of engineering-standards

**Status:** Accepted
**Date:** 2026-10-31

## Context

`engineering-standards` governs how code is built, tested, and shipped
(OMNI-CORE, gate matrix, supply chain). Spec and documentation discipline
exists but is scattered: streamformer hand-rolled a full spec system
(`docs/SPEC.md` normative sections, executable oracle, truth table, ADRs,
freeze stamps); `DOC-STYLE.md` sits in engineering-standards though it
governs prose estate-wide; homebite-scraper cites two normative external
documents that are neither vendored nor linked (SPEC-CORE SC-8 failure);
homebite_docs is a doc factory with no content contract.

## Decision

One new repository, `spec-standards`, owns specification and documentation
standards for the estate: SPEC-CORE (invariants), DOC-STYLE (prose rules),
tiered gates (S/K/A/D), the registry `docs:` block schema, and spec/doc
templates. engineering-standards retains code gates, security, supply
chain, and the REQUIREMENTS/THREAT-MODEL/SECURITY templates. Each repo
references the other and never forks (OMNI-CORE 11i pattern applied to
standards).

## Consequences

- Positive: one gate matrix for prose; mechanical audits
  (`doc-lint.sh`, `spec-audit.py`); spec discipline stops being per-repo
  folklore; the estate gains the docs analog of `estate-audit.py`.
- Negative: engineering-standards loses DOC-STYLE.md from its tree
  (resolved by ADR-0003 stub); an estate-wide adoption sweep is required
  before gates bite.
- Risks: standard duplication re-emerges if either repo copies instead of
  referencing; mitigated by the templates ownership table and the AGENTS
  non-negotiable 4.

## Alternatives considered

| Alternative | Pros | Cons | Reason rejected |
|---|---|---|---|
| Extend engineering-standards in place | no new repo, existing CI | concern bloat: prose gates need a different toolchain (markdownlint, lychee) and their own registry; OMNI-CORE is the wrong home for doc invariants | the engineering repo already spans CI/security/supply-chain/agents; spec+doc is a distinct concern with its own gates |
| Two repos (spec-standards + docs-standards) | maximal focus | spec and doc share the citation rule, truth table, and freshness machinery | splitting duplicates the exact sync mechanism the standard exists to enforce |
