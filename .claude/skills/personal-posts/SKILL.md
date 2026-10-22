---
name: personal-posts
description: Turns Martin's own dictated or typed thought into finished, platform-adapted social posts in his personal voice (not a client's), for Instagram, Facebook, LinkedIn and X. Builds a matching, non-741-branded image for Instagram/Facebook, reusing the social-visuals-workflow render pipeline with its own plain template; LinkedIn/X ship text-only. Runs the slop lint and the house copy-rules on every version, asks Martin's own go per post every time, and never posts or schedules anything itself. Use when Martin says "personal post:", "/personal-post", "write a post from this thought", "turn this into a LinkedIn/X post", or "what should I post about" (pulls from the topic backlog). Do NOT use for client-voice page or blog copy (content-writing), client social-proof story automation (story-automation-system), image-only templates (social-visuals-workflow), or any client-facing message.
allowed-tools: Read, Write, Edit, Bash(python3:*), AskUserQuestion
---

# Personal posts

## Critical
- Never auto-post or auto-schedule, to any platform, ever. Deliver text (and image) ready; Martin posts himself.
- Every single post needs Martin's own explicit go, every time, before it goes anywhere — approving one post is not a go for the next one.
- No invented or exaggerated numbers (`claims-need-real-data`). No client named or shown with a real result without that specific client's own go for that specific post — default to anonymized (industry + real number, no name, no logo).
- No invented personal stories or experiences, ever. Classify every personal claim as confirmed experience / explicit opinion / inferred interpretation / hypothesis before drafting it (`references/voice-profile.md` §"Accuracy rules") — never present an inference as something Martin actually said or lived.
- This skill is scoped to Martin's **personal account** only (`references/voice-profile.md` §"Account separation"). 741 Studio's own business account is a separate, unbuilt concern — do not silently extend this skill to it.
- `disable-model-invocation` is off so natural triggers work (e.g. "write a post from this thought" with no slash command) — same reasoning as `captions`. Martin's go-per-post (step 7) is the real gate, not the invocation rule. The one external send in this skill, `cleanse.sh`'s rival-model pass, only runs when a draft scores below 5/5 in step 6 — it is not a guaranteed step on every run.

## Inputs
- Martin's raw dictated or typed thought (primary input, every real run).
- Or, if he has none ready: "what should I post about" -> offer ideas from the topic backlog (step 1 below).
- Optional: specific platforms named (skip the rest, and skip the image step if neither Instagram nor Facebook is named).
- Optional: a client name + a result inside the thought (triggers the client-go check, step 2).

## Workflow
Copy this checklist into your reply and tick it off:

- [ ] 1. **No thought ready?** Run `python3 scripts/topic_backlog.py list --status open`, offer 2-3 ideas across different pillars (AskUserQuestion, not prose). Once Martin picks or restates one as his own thought, continue below; mark it used at the end (step 10).
- [ ] 2. **Client-result check (only if the thought names a client + a result).** Ask Martin (card) whether that specific client has given a go for this specific post. No go on file -> draft anonymized (industry + the real number, no name, no logo). Go on file -> draft named, with the real result.
- [ ] 3. **Claim check.** Trace every number or result in the thought to a real source; never invent or round up. Also classify every personal claim in the thought (confirmed experience / explicit opinion / inferred interpretation / hypothesis, `references/voice-profile.md` §"Accuracy rules") — if it is anything but a confirmed experience or an explicit opinion, confirm it with Martin before drafting it as fact.
- [ ] 4. **Core draft.** Read `references/voice-profile.md` in full, every time (stance, hard no's, topic pillars, copy-rules mapping) — do not rely on memory of a previous run. Draft ONE core argument in Martin's voice: claim first, then the one reason to believe it. For a pillar-1 "uncomfortable truths" post, the optional editorial method (§"Editorial method") is often the fastest way to find the real shape of the post.
- [ ] 5. **Platform adaptation.** Using `references/voice-profile.md` §"Per-platform adaptation" and `references/platform-specs.md`, write only the platform versions actually needed (default: all 4). Save each to its own file named `draft-<platform>.txt` (`draft-x.txt`, `draft-linkedin.txt`, `draft-instagram.txt`, `draft-facebook.txt`) so the verification script can infer the platform. Before moving on, self-check each draft against copy-rules C4.1 (2 sentences per paragraph at most) — `verify_draft.py` does not check this, it is a read-it-yourself gate.
- [ ] 6. **Verify — every version, separately.** Run `python3 scripts/verify_draft.py draft-*.txt`. Any file below 5/5 or over its hard length limit: shorten/rewrite, or for the slop gate run `.claude/skills/slopmonster/tools/cleanse.sh draft-<platform>.txt`, then re-run `verify_draft.py`. Repeat until every file passes (exit 0). Do not show Martin a version that has not passed.
- [ ] 7. **Martin's go — every post, every time.** Show every verified platform version together (one `AskUserQuestion` card, not a prose list) and ask for his go. He may approve some, reject others, or ask for a rewrite of one or more. Log the result: `python3 scripts/run_log.py write martin_go <ok|rejected> "<one-line note>"`.
- [ ] 8. **Image (Instagram + Facebook only, conditional).** For each approved version on a platform that needs an image, build it with `python3 scripts/build_personal_image.py "<pull-quote line>" "Martin Drendel" <instagram|facebook>` — reuses the existing headless-Chrome render pipeline but with the separate, non-741-branded template (`references/voice-profile.md` §"Image"). Never use the 741-branded templates in `07_social/templates/` for a personal post. Skip this step entirely for LinkedIn/X-only runs or when Martin did not approve the Instagram/Facebook version. Read the rendered PNG back (`Read`) to check for collisions or overflow before delivering it.
- [ ] 9. **Deliver.** Hand Martin the approved text (and image, where built), ready to paste. Log delivery: `python3 scripts/run_log.py write delivered ok "<platforms delivered>"`. Never post or schedule it.
- [ ] 10. **Backlog housekeeping.** If the thought came from the backlog (step 1), mark it used: `python3 scripts/topic_backlog.py use <id>`. If a usable fragment came up in chat but was not used today, offer to add it: `python3 scripts/topic_backlog.py add <lane> "<idea>" "<source>"`.

## Output template
For each approved platform:
```
**<Platform>**
<final text>
(image: <path> | no image for this platform)
```

## Checkpoints
- After step 6: every platform version must show exit 0 from `verify_draft.py` before step 7 — never show Martin an unverified draft.
- After step 7: wait for Martin's explicit go, per post, every time. A go on a past post is never a go for this one.

## References
- `references/voice-profile.md` — philosophy, stance, hard no's, accuracy rules, topic pillars, account scope, per-platform shape, copy-rules mapping (read every run).
- `references/content-intelligence-brief.md` — Martin's full personal-brand brief (background, personality notes, editorial method, production philosophy); context source for `voice-profile.md`, re-read when a post needs background grounding beyond what's already extracted.
- `references/strategy-notes.md` — sourced technique notes from Martin's content-marketing knowledge base (hook framing, no-outbound-links rule, voice techniques); the parts already folded into `voice-profile.md` and `scripts/check_lengths.py` do not need re-reading every run, but check it when a post isn't landing.
- `references/platform-specs.md` — length rules used by `scripts/check_lengths.py` (also checks for outbound links in the body).
- `~/.claude/skills/content-writing/references/copy-rules.md` — external, read directly for the headline/DR pattern (C2.1, C2.8, C4.1, C4.5, C8.4). Never call `/content-write`.
- `.claude/skills/slopmonster/` — external, `tools/deslop.py` (lint) and `tools/cleanse.sh` (rival-model pass below 5/5).
- Memory: `social-visuals-workflow` (render-pipeline precedent reused by `scripts/build_personal_image.py`), `claims-need-real-data` (claim rule), `741-youtube-channel-avatar` (English, international audience context).
