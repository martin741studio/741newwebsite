# Agent job descriptions — questions for Martin (derived)

Derived 2026-11-03. Each line: the question, the source that raised it, and whether the research answers it. Only "open" lines become AskUserQuestion cards at Checkpoint 1.

## Answered by the research (do not ask)
- What blocks a job description has → R1.1, union of 01/03/06/07/11. Answered.
- Whether the agent may grade itself → no; 10 shows self-grading bias; grade comes from outside (R4.2). Answered.
- Whether "remember this" is enough to hold a boundary → no; 04 and 09 say memory and CLAUDE.md are not enforcement (R1.4, R1.9). Answered.
- Whether to build a second approval mechanism → no; map onto the go-gate and cards (R2.3). Answered by 13.
- Whether workflows (registry) are agents → no, tools (R0.3). Answered by 04/13.
- What counts as "irreversible" in general → send, spend, delete, publish, DB write, client-visible change (R2.1), from 01/04/06. Only the 741-specific additions are open (below).
- Where the weekly review results go → the grill ledger and the roster (R6.3). Answered by 13.
- Whether the "12-block system" should be a source → not locatable (12). Answered.

## Open (card candidates for Checkpoint 1)
- Q1 Which agents get a job description first? Roster A1–A7, B1–B7 in `roster-2026-11-03.md`. The unattended ones (A1–A5) carry the drift risk; client chats (B3) carry the client-visible risk. Src: 04 (split criterion), 13 (roster). OPEN.
- Q2 Where does a job description live so the agent actually loads it? Options from 09: scheduled task SKILL.md (A), project rules file `.claude/rules/agents/<id>.md` (B, loads every session in the repo), memory file + MEMORY.md line (B, advisory), or a skill the chat must invoke. Src: 09, 11, 13. OPEN.
- Q3 How does the gate map onto the go-gate without a second system? Proposal R2.3: hook-enforced list vs card-enforced list named per agent; the chat shows the change and asks one card with "Go". Confirm or change. Src: 13, 05. OPEN (confirm).
- Q4 Who is the manager and what does the weekly review look like? Proposal: Martin is manager for all; review = one grill card per agent on a fixed weekday; the agent writes facts, Martin grades A–F in one sentence, or a fresh reviewer session pre-grades from evidence and Martin confirms. Which weekday, and reviewer session yes/no. Src: 01, 10, 13. OPEN.
- Q5 What counts as risky for 741 beyond send/spend/delete/publish? Candidates from 13: Supabase writes, client-visible text changes (portal, status pages), Ads bid/budget changes, GBP edits, Zapier/automation edits, WhatsApp message drafts leaving the chat, creating scheduled tasks. Src: 06 (four factors), 13. OPEN.
- Q6 Language of the job descriptions: German (Martin's working language, memory files are German) or English (STE house style for artifacts, scheduled-task prompts are English). Src: 13 (CLAUDE.md STE rule vs German memories). OPEN.
- Q7 Confirm the 4 inputs of step 0.0 (Job, Surface, Cadence, Hard limits) as pre-filled from the chat-base brief. Src: creation workflow step 0.0. OPEN (confirm).

## Open for later (not Checkpoint 1)
- Q8 Should client chats (B3) get one template with per-client parameters instead of 12 descriptions? Src: 07 (placeholders in role/goal), 04 (duplicate a Bot per scope). Ask at hand-run of the first client agent.
- Q9 Should a reviewer session run on a different model than the agent (10: writer Sonnet, editor Opus)? Ask when the review routine is built.
- Q10 Should the roster live in the Command Center admin tab? Src: 13 (D29 home). Ask after install.
