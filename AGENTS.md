# AGENTS.md: spec-standards agent contract

Derived from the WyattAu estate contract
([`engineering-standards`](https://github.com/WyattAu/engineering-standards),
AGENTS.md + OMNI-CORE invariants). This repository extends the estate
contract to specifications and documentation (SPEC-CORE); code gates,
security, and supply chain remain owned by engineering-standards. Pointer
files reference this contract and never fork it (OMNI-CORE 11i).

## Non-negotiables

1. **The character rule is absolute.** The em-dash character appears in no
   document in this repository, including code blocks; checks construct it
   with `printf` escapes (`DOC-STYLE §1`).
2. **Scripts are canonical; CI mirrors them** (OMNI-CORE 1, SPEC-CORE
   SC-9). The gates are `scripts/doc-lint.sh` and `scripts/spec-audit.py`;
   `.github/workflows/docs.yml` runs exactly those.
3. **SPEC-CORE is normative.** Any change to an invariant (SC-1 through
   SC-10) or a schema (§3, §4, §5, §7) requires an ADR in `docs/adr/`, a
   header version bump, and a `CHANGELOG.md` entry.
4. **Templates reference, never duplicate.** REQUIREMENTS.md,
   THREAT-MODEL.md, SECURITY.md, and CHANGELOG skeletons are owned by
   engineering-standards `templates/`; this repo links them
   (`templates/README.md`).
5. **Dogfood: this repository runs its own gates at tier S** (`make ci`);
   a gate that fails on its own repo is a release blocker with no waivers.
6. **Pointers never forks:** `CLAUDE.md` and any future vendor file
   reference `AGENTS.md`.
7. **Measured claims only** (estate contract): gate results, audit outputs,
   and coverage numbers carry the run date and the command that produced
   them.
8. **Registry schema changes are breaking:** a §7 field change requires an
   ADR, a schema version note in SPEC-CORE, and an audit-script version
   bump in the same commit.

## Where the truth lives

| Concern | File |
|---|---|
| Spec + doc invariants (normative) | `SPEC-CORE.md` |
| Prose register + citation rule | `DOC-STYLE.md` |
| Gate matrix + adoption + rollout | `README.md` |
| Registry schema | `SPEC-CORE.md` §7 |
| Seed decisions | `docs/adr/` |
| Gate scripts | `scripts/` |

## Decisions

Any decision that changes an invariant, a schema, a gate, or the boundary
with engineering-standards gets an ADR in `docs/adr/NNNN-*.md`
(Status / Context / Decision / Consequences / Alternatives). Superseding
an ADR keeps the original text visible.
