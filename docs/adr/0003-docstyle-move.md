# ADR-0003: Move DOC-STYLE.md canon to spec-standards

**Status:** Accepted (landing blocked on the first push of spec-standards)
**Date:** 2026-10-31

## Context

`DOC-STYLE.md` lives in `engineering-standards` but its rules apply to
every document in every repository, including repos that consume no
engineering gate. Ownership follows the concern, not the history: prose
rules belong to the docs standard (SPEC-CORE §1 boundary).

## Decision

Move the canon: `spec-standards/DOC-STYLE.md` becomes normative (extended
with the spec citation pointer and the status-stamp rule). When
spec-standards is pushed, engineering-standards replaces its
`DOC-STYLE.md` with a stub containing the pointer and lands an ADR there
recording the move. Kit linters that grep for the rule file update their
paths in the same sweep; no fork is retained.

## Consequences

- Positive: single source of truth; the stub preserves discoverability;
  the docs gate (`doc-lint.sh`) and the rule file finally live in one repo.
- Negative: one CI-window where both copies exist; kept short by landing
  the stub immediately after the first push.
- Risks: a stale fork re-appearing in a kit; mitigated by the pointer rule
  (AGENTS non-negotiable 6) and the monthly bitrot link check, which fails
  on the dead path once the stub points here.

## Alternatives considered

| Alternative | Pros | Cons | Reason rejected |
|---|---|---|---|
| Leave DOC-STYLE.md in engineering-standards, referenced from here | zero migration | wrong owner; boundary table (SPEC-CORE §1) would be fictional | forks the concern the standard was created to fix |
