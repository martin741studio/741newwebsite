# Workflow Library — building Claude workflows (skills, subagents, hooks, routines, Cowork, projects, mods)

Built 2026-10-11. Freshness rule: nothing older than 3 months. Official docs are living pages fetched 2026-10-11; blog posts are from 2026-07-10 to 2026-10-08; videos were uploaded 2026-07-15 to 2026-10-09. Last refresh: 2026-10-11. Next refresh due: 2026-11-22 (section 7 of `00_project/workflow-creation-workflow.md`).

How to use:
1. Follow `00_project/workflow-creation-workflow.md` for every new workflow.
2. `grep -ril <term> 00_project/knowledge/workflow-library/` and read hits in this order: official doc → blog → `_derived/extracts/NNN.md` → raw `videos/NNN-*.md`.
3. Derived layer: `_derived/rules.md` (741 Workflow-Raster), `_derived/patterns.md` (blocks, decision tree, templates), `_derived/scorecard.md` (pre-ship gate).

Internal library. Never name YouTube sources in client material.

## Older foundations (links only, not stored: older than 3 months)

These Anthropic engineering posts shaped the current docs. The living docs above supersede them. Read them on the web if you need the reasoning.

| Date | Post |
| --- | --- |
| 2024-12-19 | https://www.anthropic.com/engineering/building-effective-agents |
| 2025-06-13 | https://www.anthropic.com/engineering/multi-agent-research-system |
| 2025-09-11 | https://www.anthropic.com/engineering/writing-tools-for-agents |
| 2025-09-29 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| 2025-10-16 | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills |
| 2025-11-26 | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents |
| 2026-01-09 | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents |
| 2026-03-24 | https://www.anthropic.com/engineering/harness-design-long-running-apps |
| 2026-03-25 | https://www.anthropic.com/engineering/claude-code-auto-mode |
| 2026-04-07 | https://claude.com/blog/how-and-when-to-use-subagents-in-claude-code |
| 2026-04-08 | https://www.anthropic.com/engineering/managed-agents |
| 2026-04-14 | https://claude.com/blog/introducing-routines-in-claude-code |
| 2026-03-03 (updated Oct 2026) | https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills |
| 2026-06-05 | https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering (a seller's daily-brief / daily-recap skills; relevant for non-dev work) |
| undated (JS page) | https://medium.com/@ashleyha/i-mastered-the-claude-code-workflow-145d25e502cf (from Martin's planning note; not fetched) |

## Official docs: Claude Code (living pages, `code.claude.com/docs/en/<name>.md`)

| Title | Size | File | Source |
| --- | --- | --- | --- |
| Orchestrate teams of Claude Code sessions | 40 k | `official-docs/claude-code/agent-teams.md` | https://code.claude.com/docs/en/agent-teams |
| Run agents in parallel | 8 k | `official-docs/claude-code/agents.md` | https://code.claude.com/docs/en/agents |
| Best practices for Claude Code | 36 k | `official-docs/claude-code/best-practices.md` | https://code.claude.com/docs/en/best-practices |
| Claude Code changelog | 598 k | `official-docs/claude-code/changelog-recent.md` | https://code.claude.com/docs/en/changelog |
| Explore the .claude directory | 92 k | `official-docs/claude-code/claude-directory.md` | https://code.claude.com/docs/en/claude-directory |
| Let Claude coordinate ongoing work with Projects | 61 k | `official-docs/claude-code/claude-projects.md` | https://code.claude.com/docs/en/claude-projects |
| Common workflows | 18 k | `official-docs/claude-code/common-workflows.md` | https://code.claude.com/docs/en/common-workflows |
| Explore the context window | 60 k | `official-docs/claude-code/context-window.md` | https://code.claude.com/docs/en/context-window |
| Message your other Claude Code sessions | 34 k | `official-docs/claude-code/cross-session-messaging.md` | https://code.claude.com/docs/en/cross-session-messaging |
| Schedule recurring tasks in Claude Code Desktop | 9 k | `official-docs/claude-code/desktop-scheduled-tasks.md` | https://code.claude.com/docs/en/desktop-scheduled-tasks |
| Extend Claude Code | 28 k | `official-docs/claude-code/features-overview.md` | https://code.claude.com/docs/en/features-overview |
| Keep Claude working toward a goal | 14 k | `official-docs/claude-code/goal.md` | https://code.claude.com/docs/en/goal |
| Run Claude Code programmatically | 34 k | `official-docs/claude-code/headless.md` | https://code.claude.com/docs/en/headless |
| Automate actions with hooks | 61 k | `official-docs/claude-code/hooks-guide.md` | https://code.claude.com/docs/en/hooks-guide |
| How Claude Code works | 19 k | `official-docs/claude-code/how-claude-code-works.md` | https://code.claude.com/docs/en/how-claude-code-works |
| Set up Claude Code in a monorepo or large codebase | 34 k | `official-docs/claude-code/large-codebases.md` | https://code.claude.com/docs/en/large-codebases |
| How Claude remembers your project | 51 k | `official-docs/claude-code/memory.md` | https://code.claude.com/docs/en/memory |
| Test plugins with evals | 61 k | `official-docs/claude-code/plugin-evals.md` | https://code.claude.com/docs/en/plugin-evals |
| Add components to a plugin | 54 k | `official-docs/claude-code/plugins_components.md` | https://code.claude.com/docs/en/plugins/components |
| Create a Claude Code plugin | 25 k | `official-docs/claude-code/plugins_create.md` | https://code.claude.com/docs/en/plugins/create |
| Mods overview | 23 k | `official-docs/claude-code/plugins_mods_overview.md` | https://code.claude.com/docs/en/plugins/mods/overview |
| Plugins overview | 14 k | `official-docs/claude-code/plugins_overview.md` | https://code.claude.com/docs/en/plugins/overview |
| Automate work with routines | 36 k | `official-docs/claude-code/routines.md` | https://code.claude.com/docs/en/routines |
| Run prompts on a schedule | 16 k | `official-docs/claude-code/scheduled-tasks.md` | https://code.claude.com/docs/en/scheduled-tasks |
| Extend Claude with skills | 107 k | `official-docs/claude-code/skills.md` | https://code.claude.com/docs/en/skills |
| Create custom subagents | 108 k | `official-docs/claude-code/sub-agents.md` | https://code.claude.com/docs/en/sub-agents |
| What's new | 16 k | `official-docs/claude-code/whats-new.md` | https://code.claude.com/docs/en/whats-new |
| Orchestrate subagents at scale with dynamic workflows | 41 k | `official-docs/claude-code/workflows.md` | https://code.claude.com/docs/en/workflows |
| Run parallel sessions with worktrees | 39 k | `official-docs/claude-code/worktrees.md` | https://code.claude.com/docs/en/worktrees |

## Official docs: Claude Platform (skills, prompting, context)

| Title | Size | File | Source |
| --- | --- | --- | --- |
| Skill authoring best practices | 42 k | `official-docs/platform/best-practices.md` | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices |
| Prompting best practices | 68 k | `official-docs/platform/claude-prompting-best-practices.md` | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices |
| complete-guide-skills.md | 36 k | `official-docs/platform/complete-guide-skills.md` |  |
| The Complete Guide to Building Skills for Claude (PDF, 33 pages) | 561 k | `official-docs/platform/complete-guide-skills.pdf` | resources.anthropic.com |
| Context windows | 16 k | `official-docs/platform/context-windows.md` | https://platform.claude.com/docs/en/build-with-claude/context-windows |
| Manage tool context | 5 k | `official-docs/platform/manage-tool-context.md` | https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context |
| Agent Skills | 21 k | `official-docs/platform/overview.md` | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview |
| Prompting Claude Fable 5.1 | 55 k | `official-docs/platform/prompting-claude-fable-5-1.md` | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1 |
| Get started with Agent Skills in the API | 37 k | `official-docs/platform/quickstart.md` | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart |

## Official docs: Cowork and Claude help center

| Title | Size | File | Source |
| --- | --- | --- | --- |
| assign-tasks-from-anywhere.md | 9 k | `official-docs/cowork/assign-tasks-from-anywhere.md` | https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork |
| claude-code-power-user-tips.md | 24 k | `official-docs/cowork/claude-code-power-user-tips.md` | https://support.claude.com/en/articles/14554000-claude-code-power-user-tips |
| cowork-and-chat-are-one-claude.md | 10 k | `official-docs/cowork/cowork-and-chat-are-one-claude.md` | https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude |
| get-started-with-cowork.md | 22 k | `official-docs/cowork/get-started-with-cowork.md` | https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork |
| how-to-create-custom-skills.md | 12 k | `official-docs/cowork/how-to-create-custom-skills.md` | https://support.claude.com/en/articles/12512198-how-to-create-custom-skills |
| organize-tasks-with-projects.md | 6 k | `official-docs/cowork/organize-tasks-with-projects.md` | https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork |
| schedule-recurring-tasks.md | 5 k | `official-docs/cowork/schedule-recurring-tasks.md` | https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork |
| use-plugins-in-claude.md | 15 k | `official-docs/cowork/use-plugins-in-claude.md` | https://support.claude.com/en/articles/13837440-use-plugins-in-claude |

## Official docs: Claude Code weekly what's-new (2026 weeks 28–37; weeks 31 and 38+ had no page on 2026-10-11)

| Title | Size | File | Source |
| --- | --- | --- | --- |
| Week 28 · July 6–10, 2026 | 4 k | `official-docs/whats-new/2026-w28.md` |  |
| Week 29 · July 13–17, 2026 | 5 k | `official-docs/whats-new/2026-w29.md` |  |
| Week 30 · July 20–24, 2026 | 7 k | `official-docs/whats-new/2026-w30.md` |  |
| Week 32 · August 3–7, 2026 | 8 k | `official-docs/whats-new/2026-w32.md` |  |
| Week 33 · August 10–14, 2026 | 7 k | `official-docs/whats-new/2026-w33.md` |  |
| Week 34 · August 17–21, 2026 | 8 k | `official-docs/whats-new/2026-w34.md` |  |
| Week 35 · August 24–28, 2026 | 8 k | `official-docs/whats-new/2026-w35.md` |  |
| Week 36 · August 31 – September 4, 2026 | 8 k | `official-docs/whats-new/2026-w36.md` |  |
| Week 37 · September 7–11, 2026 | 6 k | `official-docs/whats-new/2026-w37.md` |  |

## Blog posts (published 2026-07-10 to 2026-10-08)

| Published | Title | File | Source |
| --- | --- | --- | --- |
| 2026-07-10 | Auto mode for Claude Code | `blog/auto-mode.md` | https://claude.com/blog/auto-mode |
| 2026-09-28 | Automating eval design and hillclimbing with Claude | `blog/automating-eval-design-and-hillclimbing.md` | https://claude.dev/blog/automating-eval-design-and-hillclimbing/ |
| 2026-09-25 | Build plugins for Claude | `blog/build-plugins-for-claude.md` | https://claude.com/blog/build-plugins-for-claude |
| 2026-10-08 | Building effective agent automations | `blog/building-effective-agent-automations.md` | https://claude.dev/blog/building-effective-agent-automations/ |
| 2026-07-22 | Building verification loops in Claude Code with skills | `blog/building-verification-loops-with-skills.md` | https://claude.com/blog/building-verification-loops-in-claude-code-with-skills |
| 2026-10-06 | Claude Code in the cloud: a field guide to cloud sessions | `blog/claude-code-in-the-cloud.md` | https://claude.dev/blog/claude-code-in-the-cloud/ |
| 2026-10-01 | Customize Claude Code with mods | `blog/claude-code-mods.md` | https://claude.com/blog/claude-code-mods |
| 2026-09-17 | Projects redesigned: from folder to conversation | `blog/projects-redesigned.md` | https://claude.com/blog/projects-redesigned |

## Videos (44 transcripts; number 43 was removed as off-topic, Base44 not Claude, uploads 2026-07-15 to 2026-10-09, sorted newest first)

Discovery: `yt-dlp --flat-playlist -J "ytsearch25:<query>"` over these queries: Claude Code skills tutorial · CLAUDE.md best practices · context engineering Claude Code · Claude Code subagents hooks workflow · Claude Code best practices Anthropic · Anthropic building effective agents · Claude Cowork workflow automation · Anthropic agent skills guide · Claude Code plan mode workflow · Claude Code custom slash commands · Claude Code routines scheduled tasks 2026 · Claude Code goal mode workflows tool 2026 · Claude skills best practices October 2026 · Claude Code agent teams subagents 2026 · Claude Code memory CLAUDE.md 2026 setup · Claude Cowork skills workflow 2026 · Claude Code plugins marketplace 2026 · Claude Managed Agents tutorial · Claude Code workflow non technical business automation 2026 · Claude Code hooks 2026 · Code with Claude 2026 talk agents · context engineering agents 2026 Anthropic. Filter: upload ≥ 2026-07-15, 4–90 min, ≥ 5,000 views, English, workflow-relevant. Transcripts: Apify `johnvc/YoutubeTranscripts` (auto captions). Files 020, 024, 032, 034, 038, 043, 045, 012 and the three mods videos 001/008/010 were re-typed by a helper agent from tool output, not copied byte for byte; wording may differ slightly from the captions.

Each video has an extract in `_derived/extracts/NNN.md` (rules, facts, mistakes, non-dev relevance, quotes).

| # | Published | Channel | Title | Chars | File |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-10-09 | Claude | Getting started with Claude Code Projects | 4,645 | 001-getting-started-with-claude-code-projects.md |
| 2 | 2026-10-09 | Dubibubi | Can an Army of Claude Haiku 5.5 Subagents Beat Opus 5.5? | 12,439 | 002-can-an-army-of-claude-haiku-5-5-subagents-beat-opus-5-5.md |
| 3 | 2026-10-09 | AI LABS | Claude Mods Are Insane... You Need To Try These Right Now | 16,356 | 003-claude-mods-are-insane-you-need-to-try-these-right-now.md |
| 4 | 2026-10-08 | Nate Herk | AI Automation | Anthropic Engineers Just 10x'd Everyone's Claude Code | 17,137 | 004-anthropic-engineers-just-10x-d-everyone-s-claude-code.md |
| 5 | 2026-10-07 | CJ Avilla (cjav_dev) | Getting started with Claude Managed Agents | 7,340 | 005-getting-started-with-claude-managed-agents.md |
| 6 | 2026-10-06 | Austin Marchese | Anthropic Just Released 13 New Skills To Level Up Your Claude Setup | 20,061 | 006-anthropic-just-released-13-new-skills-to-level-up-your-claude-setup.md |
| 7 | 2026-10-06 | Ben AI | Anthropic Just Revealed 8 New Rules for Building Great Claude Skills | 16,857 | 007-anthropic-just-revealed-8-new-rules-for-building-great-claude-skills.md |
| 8 | 2026-10-05 | Tristen O'Brien | Claude Code Just Dropped MODS. (Master it in 10 Minutes). | 12,520 | 008-claude-code-just-dropped-mods-master-it-in-10-minutes.md |
| 9 | 2026-10-05 | Jay E | RoboNuggets | Anthropic Just Revealed 10 NEW Rules for Claude Skills | 14,174 | 009-anthropic-just-revealed-10-new-rules-for-claude-skills.md |
| 10 | 2026-10-05 | Mark Kashef | These Mods Take Claude Code to Another Level | 18,138 | 010-these-mods-take-claude-code-to-another-level.md |
| 11 | 2026-10-05 | AI LABS | You Need To Add This In Your Claude Code Setup Right Now | 19,300 | 011-you-need-to-add-this-in-your-claude-code-setup-right-now.md |
| 12 | 2026-10-04 | AI Coding Daily | New in Claude Code: Mods and "You Should Know" Plugin | 5,288 | 012-new-in-claude-code-mods-and-you-should-know-plugin.md |
| 13 | 2026-10-01 | Simon Scrapes | Everything You Know About Skills IS OUTDATED | 15,996 | 013-everything-you-know-about-skills-is-outdated.md |
| 14 | 2026-09-30 | Tech With Diego | Every Claude Code Concept Explained in 9 Minutes (2026) | 9,125 | 014-every-claude-code-concept-explained-in-9-minutes-2026.md |
| 15 | 2026-09-26 | Dubibubi | 9 Claude Skills I Use Every Single Day | 20,317 | 015-9-claude-skills-i-use-every-single-day.md |
| 16 | 2026-09-17 | AI Edge | Claude's Creator Just Told Us How to Actually Use Claude in 2026 | 24,117 | 016-claude-s-creator-just-told-us-how-to-actually-use-claude-in-2026.md |
| 17 | 2026-09-17 | Tristen O'Brien | Learn 95% of Claude Cowork in Under 9 Minutes | 10,811 | 017-learn-95-of-claude-cowork-in-under-9-minutes.md |
| 18 | 2026-09-13 | Nate Herk | AI Automation | Anthropic Engineer Explains: What to Build Instead of AI Agents | 14,121 | 018-anthropic-engineer-explains-what-to-build-instead-of-ai-agents.md |
| 19 | 2026-09-09 | Agentic AI Institute | Claude Context Engineering Explained: From RAG to Knowledge Graphs | 49,861 | 019-claude-context-engineering-explained-from-rag-to-knowledge-graphs.md |
| 20 | 2026-09-08 | Claude | How founders build on Claude Managed Agents | 37,661 | 020-how-founders-build-on-claude-managed-agents.md |
| 21 | 2026-09-07 | Tech With Tim | Claude Code: The Advanced Guide (99% of Devs Skip These Features) | 24,490 | 021-claude-code-the-advanced-guide-99-of-devs-skip-these-features.md |
| 22 | 2026-09-02 | Ben AI | Anthropic Just Revealed 7 New Rules for Prompting Claude 5 Models | 15,511 | 022-anthropic-just-revealed-7-new-rules-for-prompting-claude-5-models.md |
| 23 | 2026-09-02 | Claude | How the Claude Code team uses Claude Code | 23,613 | 023-how-the-claude-code-team-uses-claude-code.md |
| 24 | 2026-08-28 | Zero To Mastery | 10 Claude Code Plugins You Need Right Now! | 11,566 | 024-10-claude-code-plugins-you-need-right-now.md |
| 25 | 2026-08-27 | Agentic Lab | Claude Code Hooks, Explained Simply. | 8,539 | 025-claude-code-hooks-explained-simply.md |
| 26 | 2026-08-24 | AI LABS | Insane Claude Design Skills You Need To Actually Build Beautiful Sites | 15,653 | 026-insane-claude-design-skills-you-need-to-actually-build-beautiful-sites.md |
| 27 | 2026-08-22 | Simon Scrapes | 19 Claude Code Mistakes "Pro" Users Are Still Making | 24,595 | 027-19-claude-code-mistakes-pro-users-are-still-making.md |
| 28 | 2026-08-18 | The Coding Sloth | I Have Spent 1000+ Hours With Claude Code. This Is What I Learned | 28,632 | 028-i-have-spent-1000-hours-with-claude-code-this-is-what-i-learned.md |
| 29 | 2026-08-17 | Kevin Stratvert | How to Use Claude Cowork (Step-by-Step Tutorial) | 10,891 | 029-how-to-use-claude-cowork-step-by-step-tutorial.md |
| 30 | 2026-08-17 | Zinho Automates | The Ultimate Claude Code Tutorial (Beginner to Pro) | 19,464 | 030-the-ultimate-claude-code-tutorial-beginner-to-pro.md |
| 31 | 2026-08-17 | Greg Isenberg | Claude Code New Features, Explained | 44,346 | 031-claude-code-new-features-explained.md |
| 32 | 2026-08-16 | Simon Scrapes | The Only Claude Cowork Setup Busy Entrepreneurs Actually Need | 23,400 | 032-the-only-claude-cowork-setup-busy-entrepreneurs-actually-need.md |
| 33 | 2026-08-13 | Cole Medin | Every Claude Code Skill I Use to Drive My Entire Development Process | 26,720 | 033-every-claude-code-skill-i-use-to-drive-my-entire-development-process.md |
| 34 | 2026-08-11 | Nate Herk | AI Automation | How to Build a One Person AI Business (Using Claude Code) | 35,836 | 034-how-to-build-a-one-person-ai-business-using-claude-code.md |
| 35 | 2026-08-11 | IBM Technology | What Is Context Engineering? Why It Matters for AI Agents | 6,936 | 035-what-is-context-engineering-why-it-matters-for-ai-agents.md |
| 36 | 2026-08-11 | NDC Conferences | How Anthropic uses Claude Code: Agentic Software Engineering at Scale - Daisy Hollman | 53,143 | 036-how-anthropic-uses-claude-code-agentic-software-engineering-at-scale-d.md |
| 37 | 2026-08-07 | Eric Tech | Matt Pocock's Claude Code Skills Beat Superpowers Now | 29,884 | 037-matt-pocock-s-claude-code-skills-beat-superpowers-now.md |
| 38 | 2026-08-03 | Greg Isenberg | Why Graph Engineering will 10x your Claude/Codex | 23,165 | 038-why-graph-engineering-will-10x-your-claude-codex.md |
| 39 | 2026-08-01 | 100x Engineers | The ONLY Claude Skills Tutorial Beginners Need in 2026 | 29,293 | 039-the-only-claude-skills-tutorial-beginners-need-in-2026.md |
| 40 | 2026-07-31 | AI LABS | Claude Code Setup Guide By The Creator Himself | 17,153 | 040-claude-code-setup-guide-by-the-creator-himself.md |
| 41 | 2026-07-29 | Eric Tech | Anthropic's New Rules Break Most Claude Code Setups | 11,576 | 041-anthropic-s-new-rules-break-most-claude-code-setups.md |
| 42 | 2026-07-28 | Duncan Rogoff | Learn Claude Code | Anthropic Engineers Just Fixed Claude Code and Nobody's Talking About it! | 12,144 | 042-anthropic-engineers-just-fixed-claude-code-and-nobody-s-talking-about.md |
| 44 | 2026-07-17 | Brock Mesarich | AI for Non Techies | The SIMPLE Claude Cowork Setup That Runs my Life (Steal It) | 25,354 | 044-the-simple-claude-cowork-setup-that-runs-my-life-steal-it.md |
| 45 | 2026-07-15 | Google Cloud Tech | Context engineering explained: What every AI developer should know | 7,934 | 045-context-engineering-explained-what-every-ai-developer-should-know.md |
