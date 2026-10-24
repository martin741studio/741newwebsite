---
name: marketing-grill
description: Runs a grill-me session (AskUserQuestion cards) for 741 Studio's OWN marketing — what to do, where to reach people, how to focus on one channel, and how that activity is structured (owner, cadence, done). Grounded in the Hormozi library (00_project/knowledge/hormozi-library/), 741's real infra/campaign state (never assumed from memory), and 741's real avatar (agency owners, not the health-client roster). Produces a sourced playbook; never launches ads, sends outreach, spends money, or changes a live site. Use on "marketing grill", "/marketing-grill", "what should 741's marketing be", "grill me on marketing", or a channel question like "should I do cold email or LinkedIn right now". Do NOT use for 741's own social content once a channel is decided (personal-posts), a CLIENT's content board (content-format-board), or call prep after a lead is engaged (sales-call-prep, booking-sequence).
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3:*), AskUserQuestion
---

# Marketing Grill

## Critical
- **Grep the knowledge base at run time, never carry its content in this file.** Read `00_project/knowledge/hormozi-library/_derived/marketing-grill-rules.md`, `_derived/marketing-grill-questions.md`, `_derived/playbook-notes-channel-selection.md`, and `_derived/visibility-leads-master-reference.md` fresh every run; `grep -ril <term> 00_project/knowledge/hormozi-library/` for anything more specific.
- **Never state a specific name, team assignment, or infra state from a memory file as settled fact in a card.** Run `scripts/check_infra_state.py` first and read its output; if something is stale or unclear, ask Martin rather than assert it (2026-10-25 hand-run: a card almost shipped with a team member who no longer exists on `team-roster.md`).
- **This skill only produces a document.** It never launches ads, sends outreach, spends money, or changes a live site. Those stay separate per-change "Go"s outside this workflow (`ads-changes-need-reasoned-go`, `no-website-changes-without-go`, `email-sending-airmailer`).
- **AskUserQuestion cards only, max 4 per round, recommended option first.** Never a prose list of open questions.
- **No internal method names in anything that could reach a client or the team.** Hormozi and book titles stay internal — this playbook, read only by Martin, may name them; nothing downstream of it may.
- Replies in STE. Slop-check the finished playbook (`.claude/skills/slopmonster/tools/deslop.py --text "$(cat <playbook>)"`) before showing it to Martin — only deliver at 5/5, cleanse and re-lint if below.

## Inputs
- Nothing required to trigger — 741 itself is the only subject this build covers (per `inputs-grill.md`, a per-client version is a future extension, not this skill).
- Optional: a narrower starting question (e.g. "should I be doing cold email or LinkedIn right now") — still runs the full pipeline below, grounded by that question, rather than giving a quick opinion.

## Workflow
Copy this checklist into your reply and tick it off:

- [ ] 1. **Read phase (read-only, no cards yet).**
  - Grep the knowledge base files listed under `## Critical`.
  - Run `python3 scripts/check_infra_state.py` and read its output in full — this is the deterministic fact check, not a judgment call. Read the flagged files themselves before stating anything from them as fact.
  - Check `00_project/assets/741studio/marketing-grill/` for a prior playbook. If one exists and is recent, this run is a RE-RUN (use case 2): Round 1 confirms/adjusts the prior diagnosis instead of re-deriving from scratch, and only the rounds that need re-deciding get a card.
- [ ] 2. **Round 1 card — what marketing to do.** Grounded in `_derived/marketing-grill-rules.md` §Round 1 and the read phase's findings. If a recent diagnosis already exists (e.g. in `revenue-model-100k.md`), present it as a confirmation question, not a blank Core Four re-derivation.
- [ ] 3. **Round 2 card — where to reach people.** Grounded in `_derived/marketing-grill-rules.md` §Round 2, 741's real avatar (`741-youtube-channel-avatar` memory), and the Lead Getter categories. Verify any named owner against `team-roster.md` before it appears in the card text.
- [ ] 4. **Round 3 card — how to focus and double down.** Grounded in §Round 3: diagnose the specific break before adding volume, apply depth-before-width, and ask what should stop with "nothing stops" as a valid, expected answer — never presuppose something must pause.
- [ ] 5. **Round 4 card — how the activity is structured.** Grounded in §Round 4: owner, definition of done, speed-to-contact where relevant, and routing into the existing Morning Grill / Command Center rather than a new tracker.
- [ ] 6. **Write the playbook** from `assets/playbook-template.md` to `00_project/assets/741studio/marketing-grill/<YYYY-MM-DD>/playbook.md`. Every claim cites its source file in the `## Sources` section (backtick-quoted filename). If this is a re-run, add the "What changed from the standing plan" section and name any stale fact caught along the way explicitly — never silently fix it.
- [ ] 7. **Verify.** Run `python3 scripts/check_citations.py <playbook path>` — fix until it passes. Run the slop/STE check on the playbook text — only proceed once it is 5/5.
- [ ] 8. **Telemetry.** `python3 scripts/run_log.py 00_project/assets/741studio/marketing-grill/<date> delivered ok --result <playbook path> "<one-line summary>"`.
- [ ] 9. **Report to Martin.** The playbook, plus (if a re-run) what changed and why. No further cards unless something in the playbook needs his go before it can be acted on outside this workflow.

## Output template
`assets/playbook-template.md` — always use this exact structure (4 numbered sections + "What changed" + "Sources"), never a different shape.

## Checkpoints
- No mid-pipeline "go" beyond the 4 card rounds themselves — each round's AskUserQuestion answer IS the checkpoint; nothing proceeds without it.
- After step 9: Martin may ask for changes to the playbook before anything downstream (an actual ads change, an outreach send, a site edit) gets its own separate go, per house rules.

## References
- `references/card-pattern.md` — how to write a grounded-vs-blank-slate Round 1 card, reusing the `morning-grill` mechanics without its content.
