# ADR-0005: Canon conformance to standards-core (SPEC-CORE unchanged)

**Status:** Accepted
**Date:** 2026-10-31

## Context

`standards` (L0, STANDARDS-CORE v0.1) now defines the anatomy, lifecycle,
and dependency mechanics of standards estate-wide. SPEC-CORE is an L1
canon and already satisfies the anatomy in practice (invariant table with
whys and enforcement, gates with scripts, registry schema, lifecycle,
projections).

## Decision

spec-standards declares L1 conformance to STANDARDS-CORE v0.1. No
SPEC-CORE content change is required; the conformance is structural.
Domain standards (skill, mcp, math, invariants) may tighten SPEC-CORE and
never loosen it.
