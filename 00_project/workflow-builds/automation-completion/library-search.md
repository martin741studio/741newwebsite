# 1.2 Library search (automation-completion)

grep -ril over 00_project/knowledge/workflow-library/:

- "automation" -> 20+ hits: official docs (scheduled-tasks, memory, features-overview,
  sub-agents, complete-guide-skills), blog/building-effective-agent-automations.md,
  blog/automating-eval-design-and-hillclimbing.md, several video extracts.
- "reliability" -> hits in platform/best-practices.md and ~15 video extracts
  (checklist/gate patterns, "19 mistakes" video, "1000 hours with Claude Code" video).
- "task completion" / "done criteria" / "definition of done" -> rules.md itself
  (R1.6, R4.1-R4.9), hooks-guide.md, two video extracts (016, 027).
- "verification" -> rules.md (R4.1-R4.9), best-practices.md, routines.md,
  blog/automating-eval-design-and-hillclimbing.md, several video extracts.
- "zapier" -> complete-guide-skills.md (Partner Skills Directory lists a Zapier skill),
  videos 029 and 044 (both: Zapier MCP = connect Claude to 9,000+ apps; not Zapier's own
  AI Zap-builder).

Read in order (official doc -> blog -> extract), per 1.2's instruction:

- `_derived/rules.md` sections 0, 1, 4, 6 already hold the rules this workflow needs:
  R1.6 (measurable done criteria), R1.8 (plan-validate-execute), R4.1-R4.9 (give Claude a
  check, gate the stop, fresh adversarial reviewer, demand evidence, three-tier trigger
  test), R6.1-R6.12 (bookmarks not windows, failed read = unreadable, confirm before
  ledger, time zone, read-only creds, spend cap, routine prompts self-contained).
- `_derived/patterns.md` section 4.4 (plan-validate-execute), 4.6 (writer/reviewer),
  4.8 (scheduled brief: verify live right before posting, two memory stores).
- `blog/building-effective-agent-automations.md` and
  `blog/building-verification-loops-with-skills.md`: both already fully absorbed into
  `_derived/rules.md` R6.x and R4.3/R4.4.

Conclusion: the general "how to make an agent finish a scoped build reliably" question is
already answered in the derived layer, current as of 2026-10-11. No gap here. The one real
gap is Zapier's own AI-assisted Zap-builder (Copilot/Agents) — not covered locally beyond
a one-line mention of Zapier MCP (a different tool: Claude-to-Zapier, not Zapier's
in-house AI builder). See freshness.md for the light live research done to close that gap.
