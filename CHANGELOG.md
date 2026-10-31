# Changelog

## 0.1.0 - 2026-10-31

Seed release.

- SPEC-CORE v1.0.0: ten invariants (SC-1..SC-10), truth-table/REQ/lifecycle
  formats, oracle rule, registry schema, tiers S/K/A/D.
- DOC-STYLE canon moved here from engineering-standards (ADR-0003; stub in
  the origin repo pending first push).
- Gates: scripts/doc-lint.sh (tier-aware), scripts/spec-audit.py (repo +
  registry modes). Dogfooded at tier S on this repository 2026-10-31.
- Shared workflow .github/workflows/docs.yml (tier input); monthly bitrot
  (lychee, advisory until 2027-04).
- Templates: SPEC, ADR-NNNN, TRUTH-TABLE, RESEARCH_LOG; REQUIREMENTS and
  THREAT-MODEL remain owned by engineering-standards (AGENTS.md rule 4).
- Seed ADRs: 0001 concern split, 0002 spec location rule, 0003 DOC-STYLE
  move.

## 0.1.1 - 2026-10-31

- docs.yml reusable workflow: gate scripts now checked out from
  spec-standards into `gate-tools` (persist-credentials: false); caller
  repos no longer need the scripts locally. Fixes the external-caller
  path bug in 0.1.0.
- Gate softening with dated windows (README matrix): markdownlint,
  llms.txt, and truth-table advisories at tiers k/d until 2027-04;
  em-dash and status stamps stay blocking everywhere. Applied in BOTH
  gates (doc-lint.sh and spec-audit.py repo mode; the first pilot run
  caught the auditor miss). Precedent: llvm-cov tier C "informational
  until". Rationale: 2026-10-31 estate probe found 14/253 repos with
  llms.txt, 28 with AGENTS.md.
- Estate rollout: registry docs blocks landed in engineering-standards
  (ADR 0010 there): 177 blocks from probes; spec-standards registered
  (infra/support).

## 0.2.0 - 2026-10-31

- Advisory windows are self-flipping: gates escalate to blocking
  automatically on their matrix dates (2027-01: REQ cross-check at s,
  llms freshness at s,k; 2027-04: markdownlint/llms/truth-table at k,d).
  Implemented in both gates; nothing to flip by hand, no forgotten sweep.
- spec-standards runs its own CI (`.github/workflows/ci.yml`): doc-lint s,
  spec-audit repo mode, registry example schema; dogfood non-negotiable 5
  now enforced by CI, not just locally.
- Estate sweep: shared docs gate + bitrot + canonical markdownlint config
  wired across the registered estate, pre-flighted per repo (em-dash
  sweep applied where small and reviewed; large-prose repos held).

## 0.2.1 - 2026-10-31

- Vendored trees out of scope: the gates exclude `node_modules/`,
  `vendor/`, `dist/` from em-dash/stamp/SPEC discovery (DOC-STYLE §1
  scope note added). Motivated by pediment: a committed vendored tree
  failed the gate on first wire while the local sweep walker (which
  already excluded it) saw nothing.
- spec-audit repo mode: a missing AGENTS.md/README.md follows tier
  severity now (advisory at k/d, blocking at s/a); bizkit exposed the
  unconditional fail.
- CI wave verdicts: 136 wired, green where runnable; 6 wired repos are
  private and blocked on account billing (same as homebite-scraper);
  pediment and bizkit green after this fix and rerun.

## 0.3.0 - 2026-10-31

- SPEC-CORE v1.1.0: SC-11 projection freshness + §11 (packaged skills /
  MCP are projections of the canon; stale projection fails the gate).
  ADR-0004. Paired with OMNI-CORE 11p (engineering-standards ADR 0011).
- doc-lint: lint invocations wrapped in timeouts (a gate that hangs is a
  gate bug; found while wiring tier A repos over a cold npx cache).
- Estate: 31 HOLD repos swept + wired (regenerated from pre-sweep state
  after two repair passes found mechanical damage; record in
  docs/sweep-2026-10-31.md), 5 tier-A repos adopted with authored truth
  tables, 9 Omni templates folded (born-conformant derived repos).

- doc-lint: a lint TIMEOUT is environmental and SKIPs locally (CI decides
  with reliable egress); findings from a running linter still block.
  Found when the local npm registry path degraded mid-push.
