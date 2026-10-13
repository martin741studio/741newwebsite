# Design rules: morning grill, decision queue, evening log

40 IF/THEN rules. Source ids in brackets refer to `../INDEX.md`. Numbers marked "(741 value)" are proposals for Martin's setup, not values from a source.

## 1. Morning brief design

1. IF the brief is built, THEN fix its job in one sentence first ("cut Martin's decisions to the ones only he can take") and start as a plain scheduled task with standing instructions. Add orchestration or code only when a real need appears. [A05]
2. IF an item is a candidate for the brief, THEN ask "would Martin act differently today if this changed?". IF not, THEN leave it out. More information is not the goal. [V2][A06]
3. IF the brief is rendered, THEN use one fixed compact layout: "Decisions waiting" on top, then per client TODAY / FIXED / WATCH / NEXT. [A05][V2]
4. IF the brief ranks items, THEN rank against a short written list of standing priorities (e.g. client deadlines > revenue > pipeline > internal), not ad hoc. [A04]
5. IF a new data source feeds the brief, THEN run a visibility check first: the agent must show one real record from that source before the brief may use it. [V2]
6. IF the same number exists in several places, THEN name one source of truth for it in a source map and ignore the others. [V2][A03]
7. IF the brief runs, THEN it first reads yesterday's evening log and all open cards, so commitments carry over. [A04][V1]
8. IF the scheduled run may start late (catch-up after sleep), THEN the prompt states the target date and a cut-off rule (e.g. after 12:00 only a short version) (741 value). [O2]

## 2. Decision queue and defaults

9. IF something needs Martin, THEN it becomes a decision card: plain-language headline (part of what, why now, what an answer makes possible), evidence link, lettered options, one recommendation, a deadline. A card without a recommendation or with agent jargon goes back to the agent. [A01][A02]
10. IF a card cannot be decided in about one minute, THEN split it or add context before it reaches Martin. [A02]
11. IF Martin answers, THEN accept a compressed reply string (e.g. `1a 2p 3b`), record it, and execute against it. [A01]
12. IF Martin parks a card, THEN a reason is required and binding. The card returns only when that reason changes. "I lack context" is a valid reason and means the card failed, not Martin. [A01]
13. IF Martin's answer conflicts with the record, THEN the agent says so with evidence and keeps the card open. [A01]
14. IF an approval is older than its validity window or the facts changed, THEN re-validate before acting and re-ask if needed. Options are approve, modify, reject, escalate. [A07]
15. IF a decision type repeats with the same answer (e.g. 5 times unchanged, 741 value), THEN propose it as a written default ("auto + notify") in the weekly review. [A02][A03]
16. IF more than about 7 cards wait in one morning (741 value), THEN the queue is too broad: tier by risk, batch related cards, move low-risk items to defaults. [A06][A07]

## 3. Per-client goals, KPIs, leading indicators

17. IF a client is active, THEN it has one quarter outcome goal, 3–5 weekly numbers, one owner per number, and a weekly threshold. IF any is missing, THEN the grill asks for it. [A10][A13]
18. IF a number is chosen, THEN prefer a leading indicator the owner can move this week (e.g. pages shipped, GBP posts, review requests sent) over a lagging one (rankings, leads). IF a number is red three weeks running, THEN question both goal and measure. [A10]
19. IF the weekly client check-in runs, THEN ask: what moved, what is off track and why, where is help needed, confidence 1–5. Do not ask "are we on track?". [A11]

## 4. Human vs agent routing and handoff

20. IF an action is external (client message, outreach, publishing, live-site change), moves money, or launches something, THEN only Martin approves it. Unattended agents get draft-only rights for email and messaging. [A03][A02][V3]
21. IF an action is internal and reversible (drafts, research, specs, staging builds), THEN the agent acts and reports it in the evening log. [A02][A03]
22. IF an automation is new, THEN it starts at L0 (propose only) and climbs (L1 act and report, L2 act within scope) only after a clean record. [A03]
23. IF a task goes to a person (Dinakar, Tantri, Gayo), THEN the card names owner, 7-day due date and done-definition. IF it goes to an agent, THEN the task row has assignee "agent", status "AI to-do", and runs only after approval. [V1][A13]
24. IF Martin's own hands-on check is the real gate (visual page walk, final copy taste), THEN put it in a separate "walk queue", not in the card string, and keep it small but real. [A01][A08]

## 5. End-of-day log

25. IF the day ends, THEN log per client: done (with link), open (with owner), tomorrow (first action), plus "what agents did while you were away". Martin's chat replies become dated captain's-log entries. [A02][V1]
26. IF a task is done, THEN only Martin or the named human owner ticks it done. The agent may set "needs review" but never "done". [V3][V1]
27. IF state is stored, THEN store it as files or table rows with status fields and idempotency (re-runs must not duplicate cards or messages), not as chat history. [A09][A03]
28. IF a scheduled job runs, THEN it writes one line to a pulse log. A job with no recent line shows as stale, never as healthy. [A03][V3]

## 6. Weekly and quarterly rhythm

29. IF it is the weekly slot (same day and time each week), THEN run a 30–60 minute solo review: scorecard on/off track, quarter rocks, to-dos, top 3 issues (identify, discuss, solve), parked cards, proposed defaults, max three rocks for next week. [A13][A12]
30. IF a to-do is older than two weeks, THEN it is done, re-planned or dropped in the weekly review. [A13]
31. IF a quarter ends, THEN score each client goal, reset 3–5 weekly numbers, and check the autonomy ladder level of each automation. [A10][A03]

## 7. Claude-native tooling facts (details in `claude-tooling-facts.md`)

32. IF the morning scan must run with the Mac asleep or off, THEN use a cloud routine (min interval 1 h, GitHub clone + connectors only) or a Cowork scheduled task (connectors + account files). Neither reads the local 741 repo. [O1][O6]
33. IF the scan needs local files or scripts, THEN use a Desktop scheduled task with "Keep computer awake". Sleep means a skipped run and one catch-up run on wake. [O2]
34. IF Martin should answer the grill from his phone, THEN run the grill session on the Mac with Remote Control on and both push toggles on. Pushes only work while Remote Control is active. [O4]
35. IF a routine runs, THEN remove connectors it does not need (it can use every included tool without asking) and open the run to check success (green means only "no infrastructure error"). [O1]
36. IF a long evening-log pass must not stop early, THEN wrap it in `/goal` with a turn limit. IF a sub-session hands a result to the grill session, THEN use cross-session messaging, which can never carry Martin's approval. [O3]
37. IF a cloud run needs a skill, THEN upload it to the claude.ai account or commit it to the cloned repo. Do not plan on Dispatch, which is closed to new users. [O1][O6][V4]

## 8. Anti-patterns

38. IF approvals pass at near 100% with seconds per card, THEN suspect gate fatigue, not quality. Cut and tier the queue. [A06]
39. IF a dashboard or brief keeps its own copy of facts, THEN it will drift. It must only show data read from the source. [V3]
40. IF every action needs approval, THEN oversight degrades. Gate by consequence and keep Martin's own checks few and real. [A08][A07]
