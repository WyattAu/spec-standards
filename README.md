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
- Gates 0.2.0: advisory windows self-flip on their dates in both gates;
  this repo runs its own CI (`ci.yml`).
- Pilot sweep: wire-kit wired at tier k (docs CI green); accounting-spec
  brought to tier S conformance (status + oracle lines, truth table,
  llms.txt, em-dash sweep; docs CI green); homebite-scraper wired at
  tier A (truth table, REQUIREMENTS REQ-HOME-001..008, llms.txt, SC-8
  closed by vendoring D12 + the data-protection chapter with provenance).
- Estate sweep executed (record: `docs/sweep-2026-10-31.md`): 136 repos
  wired and pushed, zero push/commit/clone failures; homebite_docs swept
  and wired at tier D (598 instances, 45 files); accounting-spec
  graduated to `current` in the registry.

Pending (ordered):

1. 34 HOLD repos (large prose debt; list in `docs/sweep-2026-10-31.md`):
   reviewed sweep per DOC-STYLE §4, then wire. engineering-standards
   itself is one of them (196 hits): owner-reviewed, not mechanical.
2. 5 HOLDA repos (tier A): authored artifacts (truth table, REQUIREMENTS,
   llms.txt) per the scraper-pilot pattern, then wire.
3. CI on the 7 private wired repos (homebite-scraper, homebite_docs,
   deploy-webhook-rs, eventbusd, authbox, clyde-costing-verified,
   flagsd): blocked on account billing (spending limit for private-repo
   minutes), not on the gate; rerun once billing clears.
4. Watch the CI wave drain; graduate wired repos to `current` as each
   earns conformance (truth table + llms.txt authored), not just CI green.
5. Close the 14/253 llms.txt gap before the 2027-04 window; the gates
   flip to blocking automatically on the matrix dates.
