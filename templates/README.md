# templates/

Skeletons shipped by spec-standards. Reference, never duplicate
(`AGENTS.md` non-negotiable 4).

| Template | Purpose | Owner |
|---|---|---|
| `SPEC.md` | normative spec skeleton (status line, oracle line, REQ table, delta log) | spec-standards |
| `ADR-NNNN.md` | decision record (Status/Context/Decision/Consequences/Alternatives) | spec-standards |
| `TRUTH-TABLE.md` | the `## Where the truth lives` block (SPEC-CORE §3) | spec-standards |
| `RESEARCH_LOG.md` | research campaign ledger with dispositions | spec-standards |
| `REQUIREMENTS.md` | EARS-style requirements skeleton | [engineering-standards templates/](https://github.com/WyattAu/engineering-standards/tree/main/templates) |
| `THREAT-MODEL.md` | STRIDE skeleton for untrusted-input parsers | engineering-standards templates/ |
| `SECURITY.md` | security policy | engineering-standards templates/ |
| `CHANGELOG.md` | ledger of changes | engineering-standards templates/ |

Usage: copy a skeleton into the target repo, fill every bracket, delete
nothing normative (status lines, oracle lines, REQ tables are
gate-enforced).
