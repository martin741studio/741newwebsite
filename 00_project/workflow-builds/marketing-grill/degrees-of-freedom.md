# Degrees of freedom — marketing-grill (Step 2.5, Rule R1.7)

## Deterministic / low freedom → isolated scripts in `scripts/`
- **Infra-state check**: a small script that greps/reads the named memory files (`coldemail-sending-infra`, `smartlead-cold-email`, `hubspot-leads-segmentation`, `leadgen-funnel-infra`, `stipendium-giveaway-page`) and reports each as "working" / "expired" / "not deployed" — a fact lookup, not a judgment call. Prevents the model from narrating infra state from memory instead of reading it fresh.
- **Playbook output writer**: a script that assembles the 4 card-round answers plus their source citations into the fixed `playbook.md` template (Step 3, assets/) — formatting is deterministic once the content exists.
- **Source-citation check**: a script that scans the drafted playbook for any claim/number and flags one with no `(source: ...)` tag next to it — a mechanical check, not a judgment call, enforcing `claims-need-real-data`.
- **Slop/STE check**: already-existing scripts (`deslop_de.py` / `slopmonster`), run on the final playbook text per house rule.

## Open / qualitative → prompt heuristics with examples, not scripted
- **The 4 card rounds themselves**: which specific options to present, how to phrase the recommended option, and how to adapt phrasing to what Martin answered in the previous round. This needs judgment grounded in the knowledge base, not a fixed script — the same question bank produces different live options depending on 741's actual current state.
- **Writing the playbook's narrative sections** (why this channel, why now): synthesis of the grounded rules into plain STE prose, with 2-3 examples of good vs. bad phrasing given in the skill body (Rule R2.9), not a template to fill in mechanically.
- **Deciding when a re-run (use case 2) only needs 1-2 rounds vs. all 4**: a judgment call based on what changed since the prior playbook, guided by heuristics in the skill body, not a fixed rule.
