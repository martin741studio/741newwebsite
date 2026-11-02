# 04 — Grok Bot docs: "Work with Grok Bot" (Bots, jobs, skills, routines)

Type: vendor documentation (primary source named in the video). Fetched 2026-11-03.
URL: https://cursor.com/docs/grok-bot/work

## Key content
- A Bot is "a durable AI teammate with a name, a job, its own conversation, and working context that develops over time. Create a separate Bot when the work has a distinct goal, set of tools, working style, approval boundary, or recurring schedule."
- Named jobs ("Talent Scout, Expense Manager, Bug Reproduction") "give a Bot guidance and make its saved context reusable; a General Helper does neither."
- Role example in operational terms: "Own the weekly account-health review. Pull product usage and support signals, flag evidence of churn or expansion, and produce a linked watch list for the customer-success team. Never contact a customer or change an account without approval."
- First message = job + sources + approval boundaries + "ask it to remember them" + one real first task with a clear finish line.
- Lasting rule vs task: "From now on, never send external messages without approval." vs "Draft follow-ups for these twelve accounts."
- Memory warning: "Memory is not a substitute for an authoritative source ... back safety boundaries with approvals and Auto-review rules rather than memory alone."
- Reviewable results: "separate facts found in source systems, assumptions, actions already completed, actions waiting for approval, and unresolved questions." Strong results = source links, screenshots, timestamps, action log, "an explicit list of anything the Bot couldn't verify."
- "A reaction alone shouldn't carry a safety-critical decision."
- Group chats: "assign one owner per stage"; "parallel handoffs create duplicate work and noisy updates."
- Skills: "A useful skill states when to use it, the required inputs and access, the sequence of work, how to validate the result, what to return, and what requires approval." Save prompt: "Save the process we used for this task as a skill called 'Weekly account health'. Include the source systems, risk definitions, output format, and the rule that customer contact always requires approval."
- Routines: "Start with a one-time task, make it reliable, save the method as a skill, and only then automate it." Routine prompt must confirm: owning Bot, schedule and time zone, input source, expected result, approval boundary, what happens when a source is missing ("report the failure instead of using old data").
- Avoid broad listeners ("every new message").
- Closing rule: "Routines earn trust the same way people do: automate preparation before execution, keep sending, purchasing, deleting, publishing, and production changes behind approval, report missing or stale sources instead of working around them, and re-test after a website, app, or source format changes."

## Assessment for 741
New vs. video: (a) the split criterion for when a role deserves its own agent (distinct goal, tools, working style, approval boundary, schedule); (b) the five-part reviewable result (facts / assumptions / done / waiting for approval / unresolved); (c) the memory-is-not-enforcement warning; (d) the staged trust ladder task → skill → routine; (e) the missing-source rule.
Marketing: product framing ("durable teammate"); the shared cloud computer section is Grok-specific.
Usable for 741: the split criterion decides the roster (which chats get a job description, which are one tool of a bigger agent); the five-part result shape becomes the mandatory report format for every agent; "re-test after a source format changes" becomes a review trigger; the lasting-rule vs task distinction maps to memory files vs chat messages in 741.
