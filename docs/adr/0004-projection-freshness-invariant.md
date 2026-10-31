# ADR-0004: SC-11 projection freshness (SPEC-CORE v1.1.0)

**Status:** Accepted
**Date:** 2026-10-31

## Context

SPEC-CORE v1.0.0 governed documents in repos. Packaging the standard for
agents (skills in `standards-dist`, a standards MCP server) creates
off-repo projections of the canon. SC-10 already treats llms.txt as a
gated projection; skills and MCP multiply the same drift surface.

## Decision

Add SC-11: projections declare their source rev, are rebuilt by canon CI,
and a stale projection fails the canon gate. SPEC-CORE bumped to v1.1.0;
paired with OMNI-CORE 11p (engineering-standards ADR 0011).

## Consequences

- Positive: N projections, one truth; staleness is a loud failure.
- Negative: every new projection type needs a build step in this repo's
  CI; build breakage blocks canon commits.
- Risks: projection builds flaking; mitigated by keeping builds to
  copies + rev pins (no compilation).

## Alternatives considered

| Alternative | Pros | Cons | Reason rejected |
|---|---|---|---|
| Leave projections ungoverned | zero cost | silent drift reintroduces the fork problem SC-1 exists to prevent | rejected |
