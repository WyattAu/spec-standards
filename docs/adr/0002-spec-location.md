# ADR-0002: Spec location rule (incubator vs in-repo)

**Status:** Accepted
**Date:** 2026-10-31

## Context

Per-kit specs live centrally today: `engineering-standards/specs/`
(wire-kit and peers) while implementation-heavy specs live in their repos
(streamformer `docs/SPEC.md`). Both patterns are load-bearing: wire-kit is
SPEC-ONLY (pre-implementation, owner sign-off gate), streamformer's spec
must sit next to the oracle it governs.

## Decision

A spec lives in the repository whose code it governs, once that repository
exists. `engineering-standards/specs/` is the incubator for
pre-implementation SPEC-ONLY specs. Graduation is a step at repo creation:
the spec moves into `<repo>/docs/SPEC.md`, the incubator entry is stamped
`SUPERSEDED by <repo>/docs/SPEC.md`, and the repo registers a `docs:` block
(SPEC-CORE §7).

## Consequences

- Positive: specs sit beside their oracles, tests, and truth tables, so
  SC-3/SC-6 citations are intra-repo and grep-able; no cross-repo gate
  coupling.
- Negative: existing incubated specs must migrate when their repos are
  created; the incubator needs the SUPERSEDED stamp discipline.
- Risks: drift between incubator text and graduated spec; mitigated by the
  SUPERSEDED pointer rule (SPEC-CORE §5 rule 2).

## Alternatives considered

| Alternative | Pros | Cons | Reason rejected |
|---|---|---|---|
| Centralize all specs in engineering-standards/specs | one place to audit | gates need co-location with code and oracle; cross-repo citation rot | violates SC-6 adjacency |
| Always in-repo from birth | no migration | pre-implementation specs have no repo to live in; the SPEC-ONLY sign-off flow needs a venue | the incubator pattern is already proven by wire-kit |
