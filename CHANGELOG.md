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
