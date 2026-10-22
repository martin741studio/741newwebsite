# Trigger tests — personal-posts (4.1, run in fresh sessions)

Method: 3 fresh `general-purpose` subagents, no memory of this build conversation, each given exactly one scenario's user message and asked to decide which skill (if any) it would invoke, without executing the task or calling the Skill tool.

## Scenario 1 — obvious (`/personal-post <Martin's full quoted opinion>`)

**Result: PASS.** Agent identified `personal-posts` as the match, citing the description's "turns Martin's own dictated or typed thought into finished, platform-adapted social posts" and the `/personal-post` trigger. High confidence, no competing skill.

**Finding:** at test time the skill still had `disable-model-invocation: true` (first draft). The agent correctly noted that would block natural auto-invocation and only the literal `/personal-post` command would fire it. See the correction below.

## Scenario 2 — paraphrase (`"write a LinkedIn and X post from this thought: ..."`, no slash command)

**Result: PASS on identification, FAIL on invocation mode.** Agent matched `personal-posts` correctly by description and correctly said it would restrict output to LinkedIn and X only (no Instagram/Facebook, no image). But it flagged that with `disable-model-invocation: true`, this paraphrased, non-slash message would NOT auto-trigger the skill — only an explicit `/personal-post` would.

**This is the real finding of 4.1:** the first draft's frontmatter choice (`disable-model-invocation: true`, copied from `content-writing`/`content-pool`'s precedent) was wrong for this skill. Those two skills send to an external model on EVERY run (their cleanse step is unconditional). `personal-posts` only sends externally when a draft scores below 5/5 in the slop gate — an exception path that did not even fire in the 2.3 hand run (all 4 drafts were 5/5 on the first pass). The correct precedent is `captions` (the skill Martin named as this workflow's input-pattern analog), which leaves `disable-model-invocation` OFF with the stated reason "the go card is the gate," not the invocation rule.

**Fix applied:** removed `disable-model-invocation: true` from `SKILL.md`. Natural-language triggers like scenario 2 now work; Martin's go-per-post (step 7) remains the real gate against anything shipping without his approval.

## Scenario 3 — must-not-trigger (`"Write the homepage copy for Praxis Suriya"`)

**Result: PASS.** Agent did not select `personal-posts`, explicitly citing its own negative-trigger line ("Do NOT use for client-voice page or blog copy") and chose `content-writing`'s territory instead (noting `content-writing` was not itself visible in its available-skills list at test time, a subagent-session artifact, not a skill-loading bug — the description match was still correctly rejected on the merits). High confidence `personal-posts` was the wrong skill.

## Overall

2 of 3 scenarios passed clean on both identification and scope. Scenario 2 exposed a real frontmatter defect (`disable-model-invocation` wrongly copied from an unrelated precedent), fixed before shipping. Re-verified after the fix: `personal-posts` now appears in this session's own live available-skills listing (confirms natural invocation is enabled), and the fix follows the `captions` precedent exactly, which is the workflow Martin named as the input-pattern analog for this one.
