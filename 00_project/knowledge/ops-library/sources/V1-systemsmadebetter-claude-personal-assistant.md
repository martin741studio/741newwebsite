# V1 — I Made Claude My Personal Assistant (Full Build)

- Channel: Systems Made Better (Simon)
- URL: https://www.youtube.com/watch?v=3ZT0upsICHk
- Type: YouTube tutorial, 28m 37s
- Upload date: 2026-09-25
- Views: 47,472 (at fetch)
- Fetch date: 2026-10-13 (transcript via Apify johnvc/YoutubeTranscripts, dataset bC8FIf44JlT9gFC2P. Raw transcript not stored here)

## Key points (paraphrased from transcript)

1. Daily 08:00 brief built as a **Cowork scheduled task**. On Mondays it briefs the day and the week. Other workdays only the day.
2. Sources: Google Calendar, Gmail (split into "tagged for me" vs. unread that may need attention, excluding vendor outreach), a Notion task database, Slack.
3. The scheduled task prompt is short: it only says "read the folder". The real instructions live in files inside a project folder: operating instructions (scope rule: only act inside this folder), brief template, design system, memory file, writing rules. This makes the system portable.
4. The brief is delivered in the task chat (readable on mobile) and saved as a file in a briefs folder.
5. The Notion task database has an **assignee column with "Claude AI" as an assignee** and a status "To-do AI". Tasks fit for the agent are flagged.
6. **Two-task pattern**: the brief only lists AI-ready tasks and asks for approval. Martin-equivalent approves by tag. A second scheduled "task executor" (weekdays 10:00) does only approved tasks and sets them to "needs review".
7. **Captain's log**: every reply the owner gives in the brief chat is written as a dated log entry and used to update the task database. This creates a running memory.
8. To run without the computer, the files are reached via a Dropbox connector instead of the local folder.
9. Missing piece he names: a **context map** telling the executor where outputs belong.
10. He uses ASD-STE100 Simplified Technical English as the writing rule for reports.

## Use for 741

Near-exact blueprint: brief → approval tags → separate executor → captain's log. The "AI assignee + AI status" column maps to Martin's human-vs-agent routing. Note: V1 mentions Opus 4.8. Details of the UI may differ after the 6 Oct cloud move (O6).

Short quote: "Your job is to do the Notion tasks Simon has approved"
