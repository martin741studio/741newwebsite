# 1.5 Research note (automation-completion)

Block chosen: reuse the existing `/automation-build` skill (disable-model-invocation) + 3
hooks (UserPromptSubmit, PreToolUse, Stop) + scripts + verifier subagent. Not a new design
— see block-choice.md.

3 relevant rules:
- R0.5 — a step that must happen every time with zero exceptions goes in a hook, not
  prose. Why this matters here: the Gewinnspiel incident's root failures (claiming
  "live and tested" with skipped tests; publishing without a go) are exactly the two
  things `automation_done_gate.py` and `automation_guard.py` were written to block — on
  paper, since 2026-10-11. They were never given the chance to block anything because they
  were never installed.
- R4.2/R4.5 — gate the stop (Stop hook / `/goal`), and have a fresh subagent review against
  the plan. Already designed as the P5 "verifier subagent" step; not yet run on a real
  live build end to end (only the Skool funnel was "replayed" through the guard on paper).
- R6.2/R6.3 — a failed read is "unreadable", never "nothing there" or "zero"; count a send
  as sent only after the destination confirms it. Directly maps to two Gewinnspiel gaps:
  nobody re-read the Zap run history after the first real test (treated "no complaint yet"
  as "it works"), and the Zapier auto-pause alert sat in Marcel's inbox for 8.5 hours
  before anyone at 741 saw it.

1 pattern: patterns.md 4.4 plan-validate-execute (spec -> go -> build draft/off -> test ->
verify -> go-live) is the whole P0-P7 pipeline already drafted for automation-build.

Open questions (for Martin, see cp1 report):
1. Scope: finish/install the existing `automation-build` design under this id, or build a
   genuinely separate workflow? Recommendation: finish/install the existing one.
2. Where to install the 3 hooks: user-level `~/.claude/settings.json` (covers every
   project/folder, incl. client repos outside 741website) or project-level
   `741website/.claude/settings.json` (narrower, but misses client work done in other
   folders). This was already an open point in design-note.md section 9 on 2026-10-11 and
   is still unresolved.
3. Whether the P3a Zapier-AI-draft step (added 2026-10-14, after Martin's own "Zapier has
   AI teammates" comment in the Marcel chat) needs anything more than what is already
   written — research below suggests one addition: Copilot's own UI nudges straight to
   "Test" then "Publish" inside its own chat, which is exactly the fast-path that caused
   the Gewinnspiel fake-done claim. The skill should say explicitly that Copilot's own
   "tested"/"published" language never counts as 741's test gate (this is implied by the
   existing wording "the draft stays off... every step below still applies, the AI draft
   is not evidence" but is not yet explicit about Copilot's own test/publish prompts).
