# Project Manager — open questions for Martin (derived 2026-11-03)

## Answered by Martin's cards (do not ask again)
- Doers the PM drives → Dinakar, Tantri, Gayo's non-sales tasks, the Upwork partner, the AI agents.
- Task source of truth → work_items in the portal; roadmaps feed it.
- How the list reaches people → Martin briefs everyone himself; the PM only drafts the list, no per-person messages.
- Alone vs card → drafts alone, one Go per day publishes the whole list.
- Scope → clients and 741's own tasks, one list.
- Cadence → daily list (grill), Monday plan, Friday review.
- Stale/escalation → 3 working days stale, blocked same-day card, 7-day client wait → dashboard request.
- Friday number → milestone on-time rate + done-with-proof count by doer.

## Open (ask only if it blocks the next step)
- Q1 The admin "Erledigt" button still forces a URL even for decision-type rows (data-model.md, Martin's 14.10. call not yet built into the UI). Does the PM work around the UI (label-only via API) or wait for the fix? Src: 04. OPEN when the first decision-type row needs closing.
- Q2 Dinakar and Tantri have no portal login. Rows name them as doer but they never see the row directly — confirmed acceptable for now (round 1), revisit if it causes real confusion. Src: Martin 03.11. round 1 answer "You brief everyone yourself". Not open, logged as accepted.
- Q3 Should the Upwork partner's daily list go into work_items too, or stay a separate Upwork-side list per the existing execution-partner model? Src: 04 (team-briefs model), not yet asked. OPEN before the first partner-facing list.

## Later
- Q4 Workload capacity per person (lib-01 "plan from real hours") — 741 has no time tracking; revisit if the done-with-proof count needs a denominator.
- Q5 Typed agent-run steps (lib-02) — only relevant if agent_run logging gets richer than today's state/summary fields.
