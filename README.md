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
| markdownlint (`.markdownlint.json`) | ✅ | ✅ | ✅ | ✅ |
| llms.txt present, no placeholders (SC-10) | ✅ | ✅ | ✅ | advisory |
| truth table present, paths exist (SC-1, §3) | ✅ | advisory | ✅ | : |
| status stamps well-formed (SC-5, §5) | ✅ | ✅ | ✅ | ✅ |
| oracle line or No-oracle (SC-6, §6) | ✅ | if semantics | if semantics | : |
| REQ cross-check spec↔code (SC-4, §4) | ✅ (blocking 2027-01) | advisory | advisory | : |
| llms.txt freshness vs specs (SC-10) | advisory→✅ 2027-01 | advisory→✅ 2027-01 | advisory | : |
| link rot: lychee, monthly bitrot | ✅ (advisory until 2027-04) | ✅ (advisory) | ✅ (advisory) | ✅ (advisory) |
| registry `docs:` block valid (SC-7, §7) | ✅ | ✅ | ✅ | ✅ |

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

Pending (ordered):

1. Push to `WyattAu/spec-standards`; then land the DOC-STYLE stub + ADR in
   engineering-standards (blocked on this push; `docs/adr/0003-docstyle-move.md`).
2. Add `docs:` blocks for all estate repos to `estate.yml`; run
   `spec-audit.py --registry --remote`.
3. Wire `docs.yml` into kit repos (tier K) in one sweep.
4. Pilots: one private estate application repo (tier A: truth table +
   REQUIREMENTS + vendor the uncited external docs, SC-8; instance
   recorded in the private rollout tracker), homebite_docs (tier D).
5. Enable the monthly bitrot workflow estate-wide; tighten the advisory
   gates to blocking on the dates in the matrix.
