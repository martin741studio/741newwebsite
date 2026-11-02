# Block template — one 741 agent job description (ALWAYS this order)

```
# Job description — <Title> (agent id: <id>)

**Title:** <real profession, specific> (R1.2). Where it runs: <chat name | scheduled task id | runner>.
**Goal:** <one outcome sentence>. Success = <measurable criterion> (R1.1, source 07).
**Trigger / cadence:** <what starts a run; schedule with time zone; "no X = no run"> (R1.1, source 04).
**Duties:**
1. <verb + object + number> (R1.3)
2. …
**Data it may read:** <folders, tables, sites, APIs, read-only> (source 03).
**Tools (risk):** <tool> (low|medium|high[, hook-enforced|card-enforced]) · … (R1.6).
**Actions it may take alone:** <list>.
**Actions that need a Go (card with "Go", same turn):** <hook-enforced list> ; <card-enforced list> (R2.1–R2.3).
**Never (rung):**
- <never-line> — rung: hook|runner|card|skill|rule|advisory [+ check] (R1.4, R1.5)
**Caps:** <runs/day · spend/run · retries (default 3) · time box> (R2.5, R2.6).
**May delegate to:** <none | read-only subagents | named sessions> (source 07).
**Expected output / report:** facts · assumptions · done (with evidence) · waiting for Go · unresolved · unreadable (R3.1, R3.2).
**Manager:** Martin via <morning grill | this chat>; tasks arrive <how>.
**Review day:** Friday, grill card; the agent writes facts, Martin grades A–F in one sentence (R4.1, R4.2).
**Edge cases:** source missing → … ; login expired → … ; spec incomplete → ask one card ; retry exhausted → BLOCKED (R1.8, R2.5).
```

Guidance per section (one line each):
- Title: no "assistant", no "helper"; the roster id is kebab-case.
- Goal: one sentence, one measurable success; no adjectives.
- Trigger: name the inbox, the card, or the schedule; state the time zone (WITA).
- Duties: 3–6 lines; each ticked with evidence in the report.
- Data: read-only list; name the folders, not "the repo".
- Tools: registry ids and fully qualified MCP names; rating from the four factors.
- Actions alone: only writes inside the agent's own folders and drafts.
- Actions with Go: everything that sends, spends, deletes, publishes, writes Supabase or portal tables, or changes a client-visible thing.
- Never: each line one rung; "advisory" is allowed and honest.
- Caps: numbers, not words.
- Delegate: default none.
- Report: the six-part shape, every "done" with a path, link or screenshot.
- Manager: Martin; name the inbox.
- Review day: Friday; no self-grade.
- Edge cases: at least the missing-source rule and the retry rule.
