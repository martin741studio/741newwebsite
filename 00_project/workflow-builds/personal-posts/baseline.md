# Baseline comparison — personal-posts (4.3, with vs without the skill)

Same real task (Martin's quoted "we're all a family" opinion, asked for 4 platforms) given to two fresh sessions: one explicitly forbidden from touching `personal-posts` or any skill (ad hoc baseline), one running the real skill (functional test, `functional-test.md`).

## Without the skill (ad hoc baseline)

- **Tool calls: 0.** Drafted all 4 platforms from its own judgment, no script run.
- **Slop check:** self-described as a manual mental check, not the project's `deslop.py`. Re-ran `verify_draft.py` on its actual output afterward (see below) — it happened to pass, but the run produced zero verifiable evidence of the check at the time (R4.6: a self-report is not evidence; a command and its exit code are).
- **Claims:** no numbers in this particular thought, so the claims check was not exercised either way.
- **Image:** Instagram/Facebook both need one; it explicitly said "I did not make one." The gap is left for Martin to notice and ask again.
- **Martin's go:** correctly said it would not post without Martin's approval, but had no card mechanism in this run — noted it would need one.
- **Voice match:** noticeably more hedged than the voice-profile-driven draft. Opens "I do not think it is true. Not because people are cruel." vs. the skill's "That's not the problem. The problem is the pretense that came before it." The baseline is a reasonable generic take; it is not Martin's stated "direct, willing to be polarizing" voice without the voice profile forcing it.
- Tokens: 99,049. Duration: 34.3s. Cheaper, because it skipped verification, the image step, and reading any reference file.

## With the skill (functional test)

- **Tool calls: 16**, including two real script runs (`verify_draft.py`, `build_personal_image.py`) with recorded exit codes, not a self-report.
- **Slop check: verifiable.** `verify_draft.py` output is the evidence, not a claim about having checked.
- **Image: built.** A real PNG, read back and checked for collisions, not a noted gap.
- **Voice:** matches `voice-profile.md`'s stance and per-platform shape directly, because the skill forces reading that file every run instead of relying on the model's default judgment of what "direct" means.
- **Backlog + telemetry:** `topic_backlog.py` and `run_log.py` give this run a persistent record the baseline has none of.
- Tokens: 136,910. Duration: 227s. Costs more per run.

## Re-check: did the ad hoc baseline's output actually pass the real gate?

Ran `verify_draft.py` on the baseline's 4 drafts after the fact: all 5/5, all within length. **The gate itself did not catch a difference here** — this particular baseline run happened to write clean copy. What the skill adds is not "the baseline would have failed the lint," it is: a verifiable, repeatable, forced check every single run (not dependent on this run's instincts), the image Martin explicitly asked for and the baseline skipped, the persistent voice profile, the client-go and claims-check branches for topics that do have a client or a number, and the backlog/telemetry record. On a harder topic (a client result, an invented-sounding number, a more polarizing line), the gap would likely show on the lint too; this run's topic did not have those triggers.

## Verdict

Measurable gain: 1 image delivered vs. 0, 1 verifiable check vs. 0, persistent state (backlog + telemetry) vs. none, voice match closer to the stated brief. Cost: roughly 1.4x the tokens and 6-7x the wall-clock time for a run that also builds an image and runs real scripts, not just drafts text.
