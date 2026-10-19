# 1.2 Library search (2026-10-19)

Command: `grep -ril "<term>" 00_project/knowledge/workflow-library/ | head`

| Term | Hits | Useful |
|---|---|---|
| caption | 55 | no (hits are image captions in docs and video transcripts) |
| subtitle | 0 | - |
| video script | 0 | - |
| vlog | 0 | - |
| youtube | 90 | no (hits are source URLs of library videos) |
| content pipeline | 0 | - |
| writing style | 2 | yes: `official-docs/platform/claude-prompting-best-practices.md`, `official-docs/platform/prompting-claude-fable-5-1.md` |

Read order kept: official doc first. The library has no workflow for subtitles or vlog captions. The closest shapes are in `_derived/patterns.md`:
- 4.1 Sequential workflow with gates (draft, validate, checkpoint, deliver).
- 4.3 Iterative refinement (draft, run check script, fix, re-check, stop at threshold).

Rules that apply: R1.7 (scripts for fragile steps, heuristics for writing), R2.8 (exact template for a fixed output), R2.9 (2 to 3 example pairs for style), R2.10 (`disable-model-invocation: true`, the skill writes to Drive), R4.4 (check embedded in the producing skill).
