# Extract: AI-agent work visibility and human-AI handoffs, rules for the 741 client work view

- Area: 02 — visibility of AI-agent work and handoffs between humans and agents.
- Fetch date: 2026-10-13. Freshness rule: published on or after 2026-07-13, or a living product doc.
- Sources: 16 files in `sources/`. Dated sources run from 2026-07-28 to 2026-10-09. The other 12 are living docs.
- Related sources in `../../ops-library/` (not repeated here): O3 (agent view, "waiting on you"), O5 (Claude Code Projects), A02 (approval queue), A06 (gate fatigue), A07 (approval decisions), A08 (oversight skills decay), V3 ("agent never marks done").
- Strength labels: "official doc" = one or more product docs. "2+ sources" = two or more independent sources. "1 source" = one source only.

## A. Ownership: agents in the same list as humans

1. **Show agent tasks in the same task list as human tasks.**
Linear and Jira put the agent in the normal assignee field. ClickUp and Planner do the same. Do not keep a separate "AI list" for each client.
Sources: `linear-agent-delegation-and-sessions`, `jira-rovo-agents-on-work-items`, `clickup-super-agents`, `microsoft-planner-agent`. Strength: official doc (4 products).

2. **Give each task two fields: the human owner and the doer.**
Linear keeps the human as owner and sets the agent as "delegate". The owner stays accountable when an agent does the work.
Sources: `linear-agent-delegation-and-sessions`, `stacker-kivo-who-signs-the-record`, `auth0-delegation-audit-gap`. Strength: 2+ sources.

3. **Use one fixed list of doers: Martin, a team member, an agent, or the client.**
Linear and Planner let people filter and group by delegate or by agent state. This gives the delegation list for each client in one view.
Sources: `linear-agent-delegation-and-sessions`, `microsoft-planner-agent`. Strength: official doc.

4. **Keep tasks that an automation created in triage until a human assigns them.**
Linear tells agents not to self-assign work that an automation delegated. A human decides the owner first.
Sources: `linear-agent-delegation-and-sessions`. Strength: 1 source (official doc).

5. **Give each agent a profile page with its full setup and its human owner.**
ClickUp and Notion keep instructions and triggers on one agent page. They also list tools and knowledge. The admin can then see what each agent can do and touch.
Sources: `clickup-super-agents`, `notion-custom-agents-activity`. Strength: official doc.

6. **Keep client rules for all agents in one shared guidance file with history.**
Linear passes workspace and team guidance to every agent. Team guidance overrides workspace guidance. For 741, use one rules file for each client.
Sources: `linear-agent-delegation-and-sessions`, `clickup-super-agents`. Strength: official doc.

## B. Status vocabulary: "agent done" is not "done"

7. **Use a small fixed status set for agent work.**
Use: queued, working, waiting for you, error, ready for review, closed. Planner and Linear use a set close to this. Devin and Relevance AI do too.
Sources: `microsoft-planner-agent`, `linear-agent-delegation-and-sessions`, `devin-session-status-api`, `relevance-ai-tasks-approvals`. Strength: 2+ sources.

8. **An agent can set "ready for review" but never "closed".**
Planner's agent never marks a task complete, and a human closes it. In Jira, "Publish" ends the agent step but does not share the output.
Sources: `microsoft-planner-agent`, `jira-rovo-agents-on-work-items`, ops-library `V3`. Strength: 2+ sources.

9. **Split "waiting" into "needs input" and "needs approval".**
Devin uses waiting_for_user and waiting_for_approval. Relevance AI uses separate Escalated and Approvals tabs. A question needs an answer, and an action needs a yes or no.
Sources: `devin-session-status-api`, `relevance-ai-tasks-approvals`, `langchain-hitl-middleware`. Strength: 2+ sources.

10. **Show a "stale" state when an agent stops reporting.**
Linear marks a session stale after 30 minutes with no activity. Devin gives a reason when a session is suspended, for example out of credits.
Sources: `linear-agent-delegation-and-sessions`, `devin-session-status-api`. Strength: official doc.

11. **Label each outcome as confirmed or assumed.**
Intercom counts a resolution as "assumed" when the customer just leaves. An assumed outcome is a guess, so show it apart from confirmed results.
Sources: `intercom-fin-outcomes-reporting`. Strength: 1 source (official doc).

12. **Let a closed outcome reopen, and log the reversal.**
Intercom removes a resolution when the customer returns to the case. A result in the client view must show if it changed later.
Sources: `intercom-fin-outcomes-reporting`. Strength: 1 source (official doc).

13. **Write the definition of done on the task before the agent starts.**
Without a written done check, agents stop when they feel fairly sure. Write the check in a form that the agent can test.
Sources: `mindstudio-agent-self-verification`, `microsoft-planner-agent`. Strength: 2+ sources.

## C. Evidence: run log, artifacts, and sources on the task

14. **Link each task to its run log with one stable run ID.**
GitHub links each agent commit to its session log. Auth0 advises one run ID through all logs. Linear stores links to the pull request on the session.
Sources: `github-copilot-agent-sessions`, `auth0-delegation-audit-gap`, `linear-agent-delegation-and-sessions`. Strength: 2+ sources.

15. **Attach the evidence to each result. A "done" message alone is not enough.**
Cursor attaches screenshots and videos to the pull request. It adds the run logs too. Use screenshots, live URLs, and check results for client work.
Sources: `cursor-cloud-agents`, `mindstudio-agent-self-verification`. Strength: 2+ sources.

16. **Keep the agent output on the task itself.**
Planner puts all agent output in one component in the task details. Jira puts it in an "Agents" section on the work item.
Sources: `microsoft-planner-agent`, `jira-rovo-agents-on-work-items`. Strength: official doc.

17. **Record which sources and data the agent used.**
ClickUp lists the knowledge of each agent. Jira says which item fields the agent reads. Provenance (code and data history) does not prove approval.
Sources: `clickup-super-agents`, `jira-rovo-agents-on-work-items`, `stacker-kivo-who-signs-the-record`. Strength: 2+ sources.

18. **Log typed steps: action with result, question, final answer, and error.**
Linear uses these activity types. Notion shows the trigger of each run. It also shows the actions and any errors. Typed steps make the log easy to scan.
Sources: `linear-agent-delegation-and-sessions`, `notion-custom-agents-activity`. Strength: official doc.

19. **Log every change to agent instructions, with the author and the date.**
Notion keeps version history with restore. ClickUp logs edits to agent instructions and triggers. A result then links to the agent version that made it.
Sources: `notion-custom-agents-activity`, `clickup-super-agents`, `stacker-kivo-who-signs-the-record`. Strength: 2+ sources.

20. **Archive run records. Do not delete them.**
GitHub lets users archive cloud sessions but not delete them. ClickUp keeps the history of a deactivated agent.
Sources: `github-copilot-agent-sessions`, `clickup-super-agents`. Strength: official doc.

21. **Show the full chain when agents hand work to other agents.**
Devin records parent and child sessions. The Stacker article says to log the fixes that reviewer agents make before a human sees the work.
Sources: `devin-session-status-api`, `stacker-kivo-who-signs-the-record`. Strength: 2+ sources.

22. **Keep agent output as a draft until a human shares it.**
In Jira, only the person who started the agent sees the output at first. Use this for anything that goes to a client.
Sources: `jira-rovo-agents-on-work-items`, `langchain-hitl-middleware`. Strength: 2+ sources.

## D. Escalation and the "waiting on you" queue

23. **Collect all open agent questions and approvals in one queue for Martin.**
Relevance AI has separate tabs for approvals and escalations. It also has an Errors tab and bulk actions. Show each item next to its client and task.
Sources: `relevance-ai-tasks-approvals`, `langchain-hitl-middleware`, ops-library `O3`, `O5`, `A02`. Strength: 2+ sources.

24. **Show the proposed action and the reason on each pending item.**
LangChain shows the tool call with its arguments. It also lists the allowed decisions. Relevance AI shows the proposed action and the reasoning of the agent.
Sources: `langchain-hitl-middleware`, `relevance-ai-tasks-approvals`. Strength: 2+ sources.

25. **Ask for approval only for high-impact actions.**
Gate publish, send, delete, pay, and permission changes. Limit tools and keys for other risks, because prompt rules are weak.
Sources: `auth0-delegation-audit-gap`, `mindstudio-agent-self-verification`, `relevance-ai-tasks-approvals`, ops-library `A06`. Strength: 2+ sources.

26. **Reject with a reason, and never mark a denied action as answered.**
LangChain warns that a "respond" decision makes the agent think the action ran. A rejection should tell the agent to stop or to try a safer way.
Sources: `langchain-hitl-middleware`. Strength: 1 source (official doc).

27. **Let the human answer on the task, and let the agent resume from there.**
Planner sends answers back with "Regenerate". GitHub and Linear accept follow-up messages in a running session.
Sources: `microsoft-planner-agent`, `github-copilot-agent-sessions`, `linear-agent-delegation-and-sessions`. Strength: 2+ sources.

28. **Give each pending item a timeout or a reminder.**
Relevance AI keeps approvals open until someone acts, unless a timeout is set. Auth0 logs "expired" as a result of an approval request.
Sources: `relevance-ai-tasks-approvals`, `auth0-delegation-audit-gap`, ops-library `A02`, `A07`. Strength: 2+ sources.

## E. Run cost and quality of oversight

29. **Record cost and time for each agent run.**
Devin records compute units per session. GitHub shows tokens and session length. Jira and Notion show credit use by feature and by run.
Sources: `devin-session-status-api`, `github-copilot-agent-sessions`, `jira-rovo-agents-on-work-items`, `notion-custom-agents-activity`. Strength: 2+ sources.

30. **Keep the human engaged: give a visual map, and require real review.**
Chat-only work erodes understanding, and a live project map helped in one study. A checkbox sign-off with no real check is weak.
Sources: `arxiv-vibe-guide-cognitive-debt`, `arxiv-agentgui-observe-steer`, `stacker-kivo-who-signs-the-record`, ops-library `A08`. Strength: 2+ sources (small studies).

## Gaps and warnings

- **No agency source.** All products serve software, support, or general project teams. No fresh source shows a local-SEO agency view across clients.
- **Client view is missing.** No source shows how to show agent work to an end client. Jira's "private until shared" (rule 22) is the closest pattern.
- **Provenance per claim is weak.** No product shows which source each agent statement used. Rule 17 is the weakest rule in Section C.
- **Status names differ.** Each vendor uses other words. The set in rule 7 is a merge, not a standard.
- **Asana AI Teammates not covered.** The Asana help center did not load (script error). I found no fresh third-party source after 2026-07-13.
- **ClickUp audit log.** The audit log article returned HTTP 403. Those details come from search snippets of the official help center.
- **Dropped as too old or undated:** Collibra audit trail post (2026-06-24), Doe.so agent overview (no date), AgentMail agent inbox guide (no date, page now 404), Helix email approval (2026-05-14), arXiv 2604.04918 and 2602.16844 (before cut-off).
- **Not fetched:** PMI blog on RACI with agents (2026-07-29 per search) returned HTTP 403.
- **Vendor bias.** 12 of 16 sources are product docs. Three articles come from vendors (Kivo via Stacker, MindStudio, Auth0). The two studies are small preprints.
- **Moving targets.** Linear plans, Jira credits, Planner agent, and Copilot naming are in preview or rollout. Check the live docs before any build.
- **Billing bias.** Intercom bills on "assumed" outcomes. Do not copy its labels without the confirmed/assumed split.
