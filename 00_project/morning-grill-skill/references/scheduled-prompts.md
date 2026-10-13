# Scheduled task prompts (Desktop scheduled tasks, WITA)

**Updated 2026-10-13 (D24–D26):** the live prompts now end with Part 1 of the grill (the full `status-report.md`) instead of one line, and the evening run reports per client in the same style. The live text is in `~/.claude/scheduled-tasks/morning-grill-0600/SKILL.md` and `.../morning-grill-1700/SKILL.md`; the blocks below are the first version.

Each run starts with no memory. The prompts are self-contained. Both runs are READ ONLY outside `00_project/assets/morning-grill/`.

## morning-grill-0600 (cron `0 6 * * *`)

```
Morning grill, scheduled run. Repo: /Users/martindrendel/741website. Time zone: WITA (UTC+8). Today = the local date.
Use the morning-grill skill (~/.claude/skills/morning-grill/SKILL.md), Mode A, steps 1 to 6 only:
build the scan since the bookmark in 00_project/assets/morning-grill/state/bookmarks.json (if missing: yesterday 06:00 WITA),
write inputs (sessions, S2 chat summary via ONE Sonnet subagent, calendar), run scan.py, write judgment-cards.json,
run build_cards.py, render_brief.py, validate_brief.py until PASS.
Also read 00_project/assets/morning-grill/state/carry-over.md and yesterday's evening-log.md; put open items in the brief.
If it is after 12:00 WITA when you start (catch-up run), build the short brief: priority 1-2 cards and the walk queue only.
HARD LIMITS: read only outside 00_project/assets/morning-grill/; never send a message, never publish, never spend,
never write to the portal, Supabase, Drive or a client site; never mark a task done. A source that fails is "unreadable".
Do NOT start the card rounds: Martin is not here. End with exactly this reply, in STE:
"Brief <date> ready: <path to brief.html>. <n> cards, <m> walk items, unreadable: <list>. Say 'grill me' to start."
Then write _run.json (client "741 Studio (intern)", workflow "morning", status "in Arbeit", mode "Echt") and one line
in state/pulse.log: "<ISO time> morning ok|fail <cards> <unreadable>". Do not move the bookmark until Martin answered.
```

## morning-grill-1700 (cron `0 17 * * *`)

```
Morning grill evening log, scheduled run. Repo: /Users/martindrendel/741website. Time zone: WITA (UTC+8).
Use the morning-grill skill (~/.claude/skills/morning-grill/SKILL.md), Mode B, steps 1 and 2 only:
read the same sources since this morning's bookmark (sessions, ONE Sonnet subagent for chat summaries, registry, git in all
worktrees, standup, night shift, citations) and draft 00_project/assets/morning-grill/<date>/evening-log.md from
assets/evening-log.template.md: per client Done (with link), Open (owner), Tomorrow (first action), Blockers.
Mark it "status: draft". HARD LIMITS as in the morning run (read only, no sends, no portal, never "done").
End with exactly this reply, in STE:
"Evening log <date> drafted: <path>. <n> clients with steps, <k> without a step today. Say 'confirm' or correct lines."
Write one line in state/pulse.log: "<ISO time> evening ok|fail <clients>".
```
