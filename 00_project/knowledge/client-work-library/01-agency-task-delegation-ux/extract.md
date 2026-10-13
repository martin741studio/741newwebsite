# Extract: Agency task and delegation UX, rules for the client work view of 741 Studio

Scope: how modern work tools show task lists, owners, delegation, workload, status, and "what matters now". The rules apply to the client work view. Martin uses it first. The team and maybe the client use it later. Sources are in `sources/`. Fetch date: 2026-10-13.

## A. One list per person and "what matters now"

1. **Give each person one personal work list across all clients.**
Linear, Notion, and the agency queue spec all use one "my work" list that filters to the viewer. One view serves every person, because the filter uses "me". Sources: linear-my-issues, notion-projects-tasks, ashbi-operator-queue-issue. Strength: 2+ sources.

2. **Sort the personal list in a fixed focus order, then by priority.**
Linear groups assigned work as urgent, deadline-bound, blockers, then planned work. Inside each group, started work comes first. Sources: linear-my-issues. Strength: official doc.

3. **Keep notifications apart from the work list.**
The Inbox shows events (comments, mentions, assignments). "My Issues" shows the work. Do not mix the two in one list. Sources: linear-inbox, linear-my-issues. Strength: official doc.

4. **Split "needs attention now" from "can wait".**
Linear added a Priority tab to the Inbox in September 2026. Items that need action stay on top, other updates go to a second tab. Sources: linear-inbox, linear-changelog-2026. Strength: 2+ sources.

5. **Let people snooze an item or set a reminder, with a return date.**
Snooze hides an item until a set time or new activity. A reminder brings an item back to the Inbox at a set time. Sources: linear-inbox, linear-triage, plane-intake. Strength: 2+ sources.

6. **Show a small set of queue counts at the top of the admin view.**
The agency queue spec uses four views with a count each: Needs action, Awaiting approval, Waiting on client, At risk or overdue. Sources: ashbi-operator-queue-issue, monday-pm-ai-agents. Strength: 2+ sources.

## B. Ownership and delegation

7. **Give every task exactly one accountable owner.**
Each piece of work needs one named owner, a date, and an estimate. A row without an owner is a defect. Sources: productive-agency-pm-guide, ashbi-operator-queue-issue. Strength: 2+ sources.

8. **Use the same owner field for people, agents, and the client.**
Linear and Onplana put agents in the normal assignee menu. Plane lets client guests set an assignee on requests. One field keeps one list. Sources: linear-agents, onplana-agent-review-inbox, plane-intake. Strength: 2+ sources.

9. **When work goes to an agent, keep the human delegator visible.**
Linear keeps delegated issues in the delegator's own list with the agent session status. The human stays responsible for the result. Sources: linear-agents, linear-changelog-2026. Strength: official doc.

10. **Require a next action or a waiting reason on every open task.**
The queue spec rejects rows that have neither. This is the handoff note in its shortest form. Sources: ashbi-operator-queue-issue, productive-agency-pm-guide. Strength: 2+ sources.

11. **Split decision rights by role, not by task.**
The project lead owns order and dates. The account lead owns what the client was promised. The resource lead owns capacity. At 741, Martin holds most roles, so the view must show which hat applies. Sources: productive-agency-pm-guide. Strength: 1 source.

12. **Name who handles new incoming work.**
Linear's triage responsibility names the person who reviews new items. It can notify that person or auto-assign. Sources: linear-triage. Strength: official doc.

13. **Do not let agents change owners or dates without approval.**
Agents fail at priority and people decisions. A human approves each change to a date or an owner. A human also approves each message that leaves the team. Sources: quire-ai-agents-pm, onplana-agent-review-inbox. Strength: 2+ sources.

## C. Status, blocked, and "waiting on"

14. **Put all new requests into an intake area first.**
New requests from clients or tools wait in triage or intake. A person accepts, declines, merges as duplicate, or snoozes each one. Sources: linear-triage, plane-intake, monday-pm-ai-agents. Strength: 2+ sources.

15. **Use few status stages and keep "waiting on client" as its own state.**
Approval and queue views separate waiting on the client, awaiting internal approval, and at risk. A blocked task must show who it waits on. Sources: ashbi-operator-queue-issue, teamwork-accelo-alternatives. Strength: 2+ sources.

16. **Show the age of every waiting or open item.**
The queue spec shows due date and age per row. Slow client replies are an early warning sign of trouble. Sources: ashbi-operator-queue-issue, productive-agency-pm-guide. Strength: 2+ sources.

17. **Keep status in one place with four fields: stage, owner, next action, date at risk.**
Do not copy status into a second document. Copies go stale and conflict with the team record. Sources: productive-agency-pm-guide. Strength: 1 source.

18. **Label stale or missing data and never show it as healthy.**
If a source fails or is old, the view says so. It must not invent urgency, and it must not show green. Sources: ashbi-operator-queue-issue. Strength: 1 source.

19. **Separate "still figuring out" from "only executing".**
Hill Charts show uphill work (open unknowns) and downhill work (clear path). A dot that does not move signals unclear scope. Sources: basecamp-hill-charts. Strength: official doc.

## D. Per-client health and summaries

20. **Give each client one health value with three levels, set by a person.**
Linear uses On track, At risk, Off track. Teamwork shows a health color on each project card. The lead picks it and adds a short text. Sources: linear-project-updates, teamwork-accelo-alternatives. Strength: 2+ sources.

21. **Pair each health value with a short written update: status, problems, next steps.**
The newest update shows on the overview. Older updates stay in a history tab. Sources: linear-project-updates, basecamp-hill-charts. Strength: 2+ sources.

22. **Set an update rhythm and flag a missing update.**
Linear reminds the lead on a schedule. It shows "Update Missing" when the update is one cycle plus 3 days late. Sources: linear-project-updates. Strength: official doc.

23. **Do not use percent-done as the health signal.**
Task progress can hide risk and margin problems. Hill Charts and manual health values use human judgment instead. Sources: basecamp-hill-charts, productive-agency-pm-guide, notion-projects-tasks. Strength: 2+ sources.

24. **Show workload per person against a capacity limit.**
Asana and the PSA vendors show capacity bars that turn red when a person is over the limit. Plan from real hours, not 40 per week. Sources: asana-workload, productive-agency-pm-guide, teamwork-accelo-alternatives. Strength: 2+ sources.

25. **Let the client view read the same record as the team view.**
A client portal is useful only when it reads the team record, not a copy. Clients see only what is shared with them. Sources: productive-agency-pm-guide, teamwork-accelo-alternatives, plane-intake. Strength: 2+ sources.

## E. Evidence, outcomes, and AI agents

26. **Link every row to its source record and change data only there.**
Each queue row traces to one source record with a link. Notion keeps notes and documents on the project page. Sources: ashbi-operator-queue-issue, notion-projects-tasks. Strength: 2+ sources.

27. **Route agent output to a review inbox before it goes live.**
All agent drafts wait for a human, also reports and email drafts. Approve or reject is one click, and a reject note goes back to the agent. Sources: onplana-agent-review-inbox, monday-pm-ai-agents, linear-changelog-2026. Strength: 2+ sources.

28. **Record who approved what, and keep a run log for every agent.**
The approval goes into the audit trail under the approver's name. Agent runs and Loops keep a log that anyone with access can inspect. Sources: onplana-agent-review-inbox, monday-pm-ai-agents, linear-changelog-2026. Strength: 2+ sources.

29. **Do not accept "done" from an agent without a check.**
Badly bounded agents can mark work done without proof. Mark agent "done" as "done, not verified" until a person or a test confirms it. Sources: quire-ai-agents-pm, linear-changelog-2026. Strength: 2+ sources.

30. **Start agent work with one reversible job, for example the weekly status draft.**
Give the agent clear stop points such as "draft only". Review its output for one week before you add more jobs. Sources: quire-ai-agents-pm, monday-pm-ai-agents. Strength: 2+ sources.

## Gaps and warnings

- Vendor bias: 15 of 16 sources come from tool vendors. Most of them promote their own product.
- Software focus: Linear and Plane build for software teams. Their intake and focus rules need small changes for a local-SEO agency.
- Linear weight: 6 of 16 sources are Linear pages. Several rules rest on one vendor's design choices.
- No source measures results. No source shows that one view layout gives faster delivery or happier clients.
- No source covers an "outcomes" or "results" field per client (for example rankings or leads gained). Tools track tasks and hours, not client results.
- No source covers a mixed team of people, AI agents, and the client in one owner list at small-agency scale.
- No source covers what a client should see versus what stays internal, beyond "same record, limited access".
- Help-center pages for Asana, ClickUp and monday did not load. Asana data comes from a product page only. ClickUp is not covered.
- Living pages have no date. Their content can change after 2026-10-13.
