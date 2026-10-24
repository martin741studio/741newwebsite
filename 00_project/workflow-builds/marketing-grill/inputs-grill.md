# Inputs grill — marketing-grill

Date: 2026-10-25. Martin's answers (AskUserQuestion, 2 rounds).

## Job
Input: Martin's own answers to card rounds, grounded in the knowledge base (the Hormozi library, the second NotebookLM export, and the derived master reference).
Transform: match 741's current situation against the Core Four (warm outreach, cold outreach, organic content, paid ads), the Lead Getters (referrals, affiliates, agencies, employees), and the More/Better/New scaling rules.
Output: a written focused marketing playbook for 741 itself — one channel chosen first (depth-then-width), a Rule-of-100 volume commitment, a weekly structure (owner, cadence, definition of done), and what to STOP doing. Every claim in the playbook traces to a library source or to 741's own real data.
Who uses it: Martin, to decide and run 741's own marketing. Later reusable per client (not built in this first pass — see scope note below).

Scope note (confirmed): Martin chose the first option — build the 741-specific grill now, not a parameterized multi-client version in the same pass. Per-client reuse is a future extension, not part of this build.

## Runtime Surface
Terminal / Claude Code skill. Same architecture as `cro-homepage`, `content-format-board`: lives at `.claude/skills/marketing-grill/`, triggered in a chat with `/marketing-grill` or a natural trigger phrase ("marketing grill", "what should 741's marketing be", "grill me on marketing").

## Cadence
On demand. No fixed schedule, no auto-run (the grill needs Martin present to answer AskUserQuestion cards). Martin re-triggers it when 741's own channel focus needs re-evaluating — e.g. a channel stops working, or roughly quarterly.

## Hard Limits
No workflow-specific limit beyond the standing house rules, which already cover every side effect this workflow could have:
- Never launches ads, never sends outreach, never spends money, never changes a live site (`ads-changes-need-reasoned-go`, `no-website-changes-without-go`, `email-sending-airmailer`) — each of those stays its own per-change "Go" later, outside this workflow.
- Questions to Martin only as AskUserQuestion cards, max 4 per round (`questions-as-grill-me`).
- `no-method-sources-in-deliverables`: Hormozi and book titles stay in the internal library and derived rules files; the playbook Martin reads may name them (internal document), but anything that could reach a client or team must not.
- Never invents a number; every figure traces to a library source or to 741's own real data (`claims-need-real-data`).
- STE replies; slop check on every delivered text (CLAUDE.md).

## Knowledge base note (confirmed)
Second NotebookLM notebook at https://notebook.google.com/notebook/7f6a765f-7a30-446e-9259-e1a497c318ee is titled "The Content Marketing Playbook" (37 sources) — not a second Hormozi-branded notebook as the original brief assumed. Martin confirmed: export it as-is, it is the right one.
