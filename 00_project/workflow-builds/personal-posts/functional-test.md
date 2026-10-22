# Functional test — personal-posts (4.2, run in a fresh session)

Method: one fresh `general-purpose` subagent, no memory of this build, given the real task (Martin's quoted "we're all a family" opinion, `/personal-post <text>`) and told to follow `SKILL.md` for real, using its own scripts, writing only to scratch paths (not the real `00_project/assets/741studio/personal-posts/`). Told to stop and report instead of calling `AskUserQuestion` at any Martin-go point, stating its assumption and continuing.

## Where it stalled, guessed, or needed something the skill didn't anticipate

1. **Step 7 (Martin's go):** correctly identified this as a real stop point; reported what it would ask (one card, all 4 texts, approve/reject/rewrite per platform) rather than guessing an answer silently. Expected behaviour, not a defect.
2. **Step 8 (image):** at test time the skill said only "build it through the existing social-visuals-workflow pipeline" with no template named. The agent improvised a 741-branded image (yellow, "741 STUDIO" footer) because that is what `07_social/templates/` actually contains. **Real defect** — the skill had never settled whether personal posts carry 741 branding. Fixed: asked Martin directly (card), answer "No 741 branding." Built a new, separate, non-branded template (`07_social/templates/personal_post_quote.html`) and a dedicated build script (`scripts/build_personal_image.py`), test-rendered it, and verified the PNG by reading it back (no text collision, clean layout, no 741 marks). `SKILL.md` step 8 and `references/voice-profile.md` now name this explicitly.
3. **Step 10 (backlog housekeeping):** the agent found topic-backlog idea 1 already marked `used` (seeded that way, since the hand-run in step 2.3 used that exact thought before the skill existed) and correctly left it untouched since this run's thought was given directly, not pulled from the backlog. Not a defect — confirms step 10's conditional logic reads correctly.

## Real defects found and fixed

4. **Wrong path for `copy-rules.md`.** `SKILL.md` and `references/voice-profile.md` pointed at `.claude/skills/content-writing/references/copy-rules.md` (project path), but `content-writing` is installed globally at `~/.claude/skills/content-writing/`. Fixed everywhere it was referenced, including in this build's own design docs (`research-note.md`, `voice-profile.md`, `decisions.md`).
5. **No deterministic check for the C4.1 paragraph rule** (2 sentences per paragraph). `verify_draft.py` only checks the slop lint and length, so a draft that broke the paragraph rule still passed. This is intentionally NOT scripted (paragraph judgment is qualitative, per the `decisions.md` degrees-of-freedom table), but `SKILL.md` step 5 now says explicitly "self-check against C4.1, `verify_draft.py` does not check this" so it isn't silently skipped.
6. **Learned phrasing tell.** First-pass LinkedIn draft in the test run scored 4/5 on the slop lint for "the truth is" (a throat-clearing opener). Added to `references/voice-profile.md`'s hard-no list with the finding noted, per the house homeostatic rule (patch the skill, not a one-off fix).

## Verification result

Final `verify_draft.py` run on the test's 4 drafts: all 5/5, exit 0. Re-ran the same check on the original step-2.3 hand-run drafts after all fixes landed: still 5/5, exit 0 (fixes did not break the existing good drafts).

## Overall verdict

The skill is usable end-to-end without outside knowledge beyond its own files, after the fixes above. The three real defects (image branding undefined, wrong reference path, unscripted paragraph rule not flagged) are the kind step 4.2 exists to catch — none would have surfaced from re-reading the skill myself, only from someone actually executing it blind.
