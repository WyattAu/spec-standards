# WyattAu Spec Standards

Specification and documentation standards for the WyattAu estate: how truth
is written down, versioned, frozen, traced, and communicated. Modeled on
the proven [`engineering-standards`](https://github.com/WyattAu/engineering-standards)
anatomy (contract + gate matrix + registry + audit), applied to prose
instead of code. Boundary and pointer rules: `SPEC-CORE §1`.

## The Gate Matrix

Every repository in the estate declares a docs tier (SPEC-CORE §8) and runs
this matrix via the shared workflow:

```yaml
jobs:
  docs:
    uses: WyattAu/spec-standards/.github/workflows/docs.yml@main
    with:
      tier: a        # s | k | a | d
```

| Check (cites SPEC-CORE) | Tier S | Tier K | Tier A | Tier D |
|---|---|---|---|---|
| em-dash grep (DOC-STYLE §1) | ✅ | ✅ | ✅ | ✅ |
| markdownlint (`.markdownlint.json`) | ✅ | advisory → ✅ 2027-04 | advisory → ✅ 2027-04 | advisory → ✅ 2027-04 |
| llms.txt present, no placeholders (SC-10) | ✅ | advisory → ✅ 2027-04 | ✅ | advisory |
| truth table present, paths exist (SC-1, §3) | ✅ | advisory → ✅ 2027-04 | ✅ | : |
| status stamps well-formed (SC-5, §5) | ✅ | ✅ | ✅ | ✅ |
| oracle line or No-oracle (SC-6, §6) | ✅ | if semantics | if semantics | : |
| REQ cross-check spec↔code (SC-4, §4) | ✅ (blocking 2027-01) | advisory | advisory | : |
| llms.txt freshness vs specs (SC-10) | advisory→✅ 2027-01 | advisory→✅ 2027-01 | advisory | : |
| link rot: lychee, monthly bitrot | ✅ (advisory until 2027-04) | ✅ (advisory) | ✅ (advisory) | ✅ (advisory) |
| registry `docs:` block valid (SC-7, §7) | ✅ | ✅ | ✅ | ✅ |

Advisory windows follow the gate-matrix precedent set by llvm-cov tier C
("informational until"): gates land reporting, estates fix forward, then
the date flips them blocking in one sweep. Reason for the 2027-04 window:
the 2026-10-31 probe found 14 of 253 repos with llms.txt and 28 with
AGENTS.md; blocking on day one would have red every kit CI with no path
to green.

Implementation: all checks live in `scripts/doc-lint.sh` (POSIX shell;
markdownlint used when installed) and `scripts/spec-audit.py` (repo mode
and registry mode). CI mirrors the scripts (`.github/workflows/docs.yml`);
no gate exists only in CI.

## Adoption checklist (per repo)

1. Add the `docs:` block to the estate registry (`estate.yml`, schema:
   `SPEC-CORE §7`).
2. Add the truth table to `AGENTS.md` (or `README.md`), heading
   `## Where the truth lives` (§3).
3. Give every normative doc a status line (§5) and, at tier S, an oracle
   line (§6).
4. Add the workflow call above with the repo's tier.
5. Run `scripts/doc-lint.sh <tier>` locally; fix everything before the
   first CI run.
6. Reference implementations: accounting-spec (tier S), homebite_docs
   (tier D target state).

## Layout

| Path | Contents | Status |
| :--- | :--- | :--- |
| `SPEC-CORE.md` | the ten invariants + formats + registry schema, v1.0.0 | current |
| `DOC-STYLE.md` | prose rules, canonical since ADR-0003 | current |
| `AGENTS.md` | repo contract + truth table | current |
| `templates/` | SPEC, ADR, TRUTH-TABLE, RESEARCH_LOG skeletons | seed |
| `scripts/doc-lint.sh` | tier-aware prose/structure gate | dogfooded 2026-10-31 |
| `scripts/spec-audit.py` | repo + registry auditor | dogfooded 2026-10-31 |
| `.github/workflows/docs.yml` | reusable gate workflow (tier input) | seed |
| `.github/workflows/bitrot.yml` | monthly link-rot (lychee), advisory | seed |
| `docs/adr/` | 0001 concern split, 0002 spec location, 0003 DOC-STYLE move | accepted |
| `docs/registry-example.yml` | minimal `docs:` block example for §7 | current |

## Relationship to engineering-standards

- Code gates, CI tiers, security, supply chain: owned by
  engineering-standards (OMNI-CORE).
- Spec/doc invariants, prose gates, registry schema, spec/doc templates:
  owned here (SPEC-CORE).
- Each repo references the other; neither forks (OMNI-CORE 11i applied to
  standards). Decision record: `docs/adr/0001-concern-split.md`.

## Rollout status

Done (2026-10-31):

- Seed repository with SPEC-CORE v1.0.0, DOC-STYLE (moved canon),
  templates, gates, workflows, seed ADRs.
- Gates dogfooded at tier S on this repository (see `CHANGELOG.md` for the
  run record).
- Pushed as `WyattAu/spec-standards`; engineering-standards DOC-STYLE.md
  replaced with the pointer stub and ADR 0009 landed there (completing
  `docs/adr/0003-docstyle-move.md`).
- Registry: `docs:` blocks landed in engineering-standards `estate.yml`
  (ADR 0010 there): 177 blocks seeded from per-repo probes (168 k, 1 s,
  8 a); `estate-audit.py` validates the schema; this repo registered
  (infra/support). Verified against live GitHub + crates.io: zero new
  findings.
- Gates 0.1.1: dated advisory windows at tiers k/d (2027-04), caller
  checkout fix for `docs.yml`, spec-audit tier logic aligned with the
  matrix.
- Pilot sweep: wire-kit wired at tier k (docs CI green); accounting-spec
  brought to tier S conformance (status + oracle lines, truth table,
  llms.txt, em-dash sweep; docs CI green); homebite-scraper wired at
  tier A (truth table, REQUIREMENTS REQ-HOME-001..008, llms.txt, SC-8
  closed by vendoring D12 + the data-protection chapter with provenance).

Pending (ordered):

1. Estate sweep: wire the remaining crate repos (core first) with
   `.github/workflows/docs.yml` + `.markdownlint.json`; pre-flight each
   with `doc-lint.sh` before the commit.
2. homebite_docs (tier D): held; 598 em-dash hits across 236 files need
   the DOC-STYLE §4 mechanical sweep with human diff review first.
3. homebite-scraper CI: blocked on account billing (spending limit for
   private-repo minutes), not on the gate; rerun once billing clears.
4. Graduate registry postures `draft` → `current` per repo as CI lands;
   llms.txt for the 14-repo gap before the 2027-04 window closes.
5. Enable the monthly bitrot workflow estate-wide; tighten the advisory
   gates to blocking on the dates in the matrix.
