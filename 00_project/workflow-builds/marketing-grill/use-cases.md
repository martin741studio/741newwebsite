# Use cases — marketing-grill (Step 2.1)

## Use case 1: 741's own channel focus, from scratch
- Trigger phrase: "marketing grill", "/marketing-grill", "what should 741's marketing be", "grill me on marketing".
- Steps: grep the knowledge base (Hormozi library + `_derived/visibility-leads-master-reference.md` + `playbook-notes-channel-selection.md`) for the relevant rules → read 741's own current state (team-roster capacity, existing infra per `coverage-map.md`, the `marketing-quarter-campaign` plan) → run 4 card rounds (what to do, where to reach people, how to focus, how to structure) grounded in those sources → write the playbook.
- Tools: Read/Grep on the knowledge base and memory files, AskUserQuestion for the card rounds, Write for the playbook output.
- Deliverable: `00_project/assets/741studio/marketing-grill/<date>/playbook.md` — one channel chosen, a volume commitment, a weekly structure, every claim sourced.

## Use case 2: Re-run after a channel stops working
- Trigger phrase: "re-run the marketing grill", "LinkedIn outreach isn't working anymore, what now", "let's revisit 741's marketing focus".
- Steps: read the PREVIOUS playbook (if one exists) and the real state of the chosen channel (e.g. read `marketing-quarter-campaign`, check actual infra state like `smartlead-cold-email` EXPIRED) → run only the card rounds relevant to re-deciding (likely rounds 1 and 3, not all 4 from scratch) → write an updated playbook, noting what changed from last time and why.
- Tools: same as use case 1, plus Read on the prior playbook file.
- Deliverable: an updated playbook, with a short "what changed since the last grill" section.

## Use case 3 (paraphrase of use case 1, for trigger testing): Martin asks a narrower marketing-strategy question
- Trigger phrase: "should I be doing cold email or LinkedIn outreach right now", "help me figure out 741's lead gen".
- Steps: same pipeline as use case 1 — a narrower phrasing should still trigger the full grill, not a one-off opinion, because the question needs the grounded card-round process to answer honestly (depends on infra state, focus discipline, etc.), not a quick guess.
- Tools: same as use case 1.
- Deliverable: same as use case 1 (or 2, if a prior playbook exists).

## Must-NOT-trigger case (for Step 2.2)
- "write a LinkedIn post for 741" → `personal-posts`, not this skill (content EXECUTION, not channel-strategy decision).
- "build the content board for Suriya" → `content-format-board`, a CLIENT workflow, out of scope (this skill is 741-only for now, per `inputs-grill.md`).
- "prep me for my call with [prospect]" → `sales-call-prep`, downstream of an engaged lead, not this skill's job.
