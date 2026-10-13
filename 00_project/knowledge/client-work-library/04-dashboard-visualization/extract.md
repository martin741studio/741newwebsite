# Extract: 04 Dashboard and visualization, rules for the client-work view of 741 Studio

Built 2026-10-13. Freshness rule: sources published on or after 2026-07-13. Help pages count as living pages on the fetch date. 16 sources in `sources/`. Date range: 2026-07-23 to 2026-10-07, plus 2 living help pages (fetched 2026-10-13).

Strength scale:
- **Strong:** 3 or more independent sources agree, or one product shows it in a live tool.
- **Medium:** 2 sources agree, or one good source plus a clear fit for 741.
- **Weak:** one source, or our own inference.

## A. Admin portfolio view (Martin, all clients)

1. **Show exceptions first, not all clients.**
The start screen shows only items that need Martin: red or amber clients, decisions that wait, blocked tasks. Clients with no issue go into one collapsed "on track" line.
Sources: aufait-dashboard-design-guide, fivex-client-health-dashboard, aiai-agent-interface-architectures. Strength: Strong.

2. **Give each client one health band with a word, a reason and an owner.**
Use green, amber or red, and always write the word next to the color. Each amber or red band needs one line of reason, one named owner and one next action.
Sources: fivex-client-health-dashboard, storyflow-client-status-update, aufait-dashboard-design-guide. Strength: Strong.

3. **Calculate health from effort and decision signals, not only from SEO results.**
Use signals such as "client decision waits more than 5 business days", hours over plan, open escalations and overdue deliverables. Rankings and leads go into the client view. They do not decide the internal band alone.
Sources: fivex-client-health-dashboard, teamwork-client-portals-ladder. Strength: Medium.

4. **Calibrate the thresholds once by hand.**
Start with 8 to 10 signals. Score every client by hand. If all clients are red or all are green, change the thresholds.
Sources: fivex-client-health-dashboard. Strength: Weak.

5. **Cap each list on the start screen.**
Show a maximum of about 12 items per list. Put the full activity stream in a separate tab. Attention drops on long rows of repeated cards.
Sources: github-dashboard-agent-sessions, aufait-dashboard-design-guide. Strength: Medium.

6. **Put 3 to 5 key numbers at the top, trends in the middle and detail lower.**
Each number must link to an action. If a number does not change a decision, remove it from the start screen.
Sources: aufait-dashboard-design-guide. Strength: Medium.

7. **Drill down in three levels: portfolio, client, task.**
One click opens the next level. Keep the summary on top and open detail on request (progressive disclosure).
Sources: aufait-dashboard-design-guide, quire-project-views. Strength: Medium.

8. **Use a table for the portfolio, a board for daily flow and a timeline only for dated work.**
A table finds the one client that is wrong. A board shows where work stops. A timeline helps only when dates and dependencies are the main risk, for example a site launch.
Sources: quire-project-views. Strength: Medium.

9. **Make all views read the same task data.**
Never copy tasks into a second list for the portal or for a report. Copies drift in days.
Sources: quire-project-views, atwork-client-portal-what-client-sees, teamwork-client-portals-ladder. Strength: Strong.

10. **On the phone, show only the decision list and the blockers.**
The phone view answers one question: "What waits on me?" Charts and full lists stay on desktop.
Sources: aufait-dashboard-design-guide (operational view), github-dashboard-agent-sessions (cap). Strength: Weak (no fresh mobile source, see gaps).

## B. Client view

11. **Give the client a scoped view of the same data, not the internal board.**
The client sees only their own work and only client-ready items. Use folder-level or field-level permissions to hide the rest.
Sources: docsiv-portal-vs-project-board, atwork-client-portal-what-client-sees, productive-client-project-visibility. Strength: Strong.

12. **Show four blocks first: where we are, what is next, what we need from you, who to ask.**
These four blocks come before any chart. Results and proof come below them.
Sources: atwork-client-portal-what-client-sees, storyflow-client-status-update, superthread-weekly-client-status. Strength: Strong.

13. **Put "what we need from you" near the top, with a deadline and the effect of a delay.**
If the client has nothing to do, say so. Keep all client actions in one list.
Sources: storyflow-client-status-update, superthread-weekly-client-status. Strength: Medium.

14. **Hide internal items.**
Hide internal notes, estimates, per-task assignees, hours, margins, unfinished drafts, internal review comments and agent step logs.
Sources: docsiv-portal-vs-project-board, atwork-client-portal-what-client-sees, productive-client-project-visibility. Strength: Strong.

15. **Show only the current version of a deliverable.**
Old versions stay in the internal record. The client sees one current file or one current page link.
Sources: atwork-client-portal-what-client-sees. Strength: Weak.

16. **Report outcomes, not activity.**
Write "Leistungsseite Rückenschmerzen live" and not "3 meetings, 12 emails". Activity counts stay internal.
Sources: superthread-weekly-client-status, teamwork-client-portals-ladder. Strength: Medium.

17. **Tell the client about AI agent work at the level of the deliverable.**
Use one short note on the deliverable or in the FAQ. Do not show each agent step. Tell the client before a third party does.
Sources: nngroup-paced-ai-disclosure, docsiv-portal-vs-project-board. Strength: Medium (inference, see gaps).

18. **Start the client view with one easy client.**
Pick the least complicated retainer client. If that client stops asking "where are we?", add the next client.
Sources: atwork-client-portal-what-client-sees, docsiv-portal-vs-project-board. Strength: Medium.

## C. Task and delegation display

19. **Give every task row the same five fields.**
The fields are: owner type (Martin, team, agent, client), status word, due date, next action and link to the source. A task without an owner is not a valid task.
Sources: fivex-client-health-dashboard, storyflow-client-status-update, superthread-weekly-client-status. Strength: Strong.

20. **Show agent work next to human work, with a filter to separate them.**
Use one list with an "Agent" filter. Do not build a separate agent screen.
Sources: github-dashboard-agent-sessions, netlify-activity-feed-agent-runs. Strength: Medium.

21. **Do not let an agent set "done" on client-facing work.**
An agent sets "draft ready" or "needs check". A person sets "done" after the check. The approval state is visible on the row.
Sources: parallel-ai-agent-ux, superthread-weekly-client-status, aiai-agent-interface-architectures. Strength: Strong.

22. **Keep blockers visible until they close, and show their age.**
Each blocker has an owner, a deadline and a consequence. The age in days shows next to it.
Sources: storyflow-client-status-update, fivex-client-health-dashboard. Strength: Medium.

23. **Show client-owned tasks as their own lane in both views.**
In the admin view, the lane shows how long each client item waits. In the client view, the same lane is "what we need from you".
Sources: storyflow-client-status-update, teamwork-client-portals-ladder, docsiv-portal-vs-project-board. Strength: Medium.

## D. Evidence and outcome display

24. **Link every "done" item to proof.**
Proof is a live URL, a screenshot, a file or a before/after pair. A "done" without proof stays "needs check".
Sources: parallel-ai-agent-ux, atwork-client-portal-what-client-sees, teamwork-client-portals-ladder. Strength: Medium.

25. **Keep a decision log with the name and the date.**
Each client decision gets one line: what, who decided, when. Scope additions get their effect on time or date.
Sources: storyflow-client-status-update, teamwork-client-portals-ladder. Strength: Medium.

26. **Write the outcome summary in fixed blocks, and edit it by hand.**
Use four blocks: Wins, Issues, Next steps, Needs from client.
An AI can draft the summary from the report data. A person edits and approves it before the client sees it.
Sources: swydo-ai-reporting-assistant, superthread-weekly-client-status. Strength: Medium.

27. **Put the reason behind a "why" link, not in the main row.**
The row shows the result. One click shows the reason, the source and the data. Keep the agent log on a separate surface from chat.
Sources: parallel-ai-agent-ux, aiai-agent-interface-architectures. Strength: Medium.

## E. Cadence and notifications

28. **Send the client update on a fixed weekday, also when nothing changed.**
Send a link to the client view, not a copy. A missed update causes worry.
Sources: storyflow-client-status-update, superthread-weekly-client-status, agencyanalytics-client-portal-help. Strength: Strong.

29. **Review internal health weekly and send the results report monthly.**
The weekly review sets the bands and owners. The monthly client report shows results with proof.
Sources: fivex-client-health-dashboard, teamwork-client-portals-ladder. Strength: Medium.

30. **Batch routine agent actions into a digest. Send an alert only for blockers and approvals.**
Use a daily digest for routine agent work. The agent reports at once only when a job ends with a result for Martin or gets stuck.
Sources: parallel-ai-agent-ux, aiai-agent-interface-architectures. Strength: Medium.

## Gaps and warnings

- **No fresh UX research body.** No Nielsen Norman Group, Baymard or Smashing article on dashboards, status or progress was published after 2026-07-13. The NN/g source (PACED) is about AI disclosure. Most rules come from vendor and practitioner articles.
- **No fresh client survey.** No independent study after 2026-07-13 asks agency clients what they want to see. Rules 12 to 16 are practitioner consensus, not tested data.
- **No fresh mobile source.** VP0 (published 2026-05-30, updated 2026-07-17) failed the freshness rule. Rule 10 is weak.
- **No DACH or health-sector source.** No source covers German clients, health practices or German-language status words.
- **Health-score points are from e-commerce.** FiveX scores marketplace agencies. 741 must select its own local-SEO signals.
- **AI disclosure is an inference.** PACED studies text content for general audiences. It does not study agency deliverables.
- **Not counted (too old or no date):** WhatConverts radical transparency (2026-03-10), Noloco client portals (2026-03-29), ManyRequests reporting (updated 2026-03-23), Agiled status reports (2026-06-25), SEOmonitor agency dashboard help (2025-04-09), Microsoft agent activity feed (2025-10-08), Boundev dashboards vs agents (2026-05-27).
- **Not duplicated:** Assembly, SuperOkay and AgencyPlatform SEO dashboards are in `client-approval-library/`. Morning brief sources are in `ops-library/`.
- **Tool note:** The Firecrawl account reported low credits. Most pages came through WebFetch.
