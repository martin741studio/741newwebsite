---
name: personal-posts
description: Turns a dictated thought into platform-adapted social posts (Instagram, Facebook, LinkedIn, X) for one of TWO Martin-controlled accounts picked by the command used — his personal voice (/personal-post, no 741 branding) or 741 Studio's business voice (/741-post, full 741 branding). Proposes a few distinct angles on the thought first (hook technique + reach rationale from the knowledge base), Martin picks one before drafting. Builds a matching image for Instagram/Facebook; LinkedIn/X ship text-only. Runs the slop lint and house copy-rules on every version, needs Martin's go per post every time, never posts or schedules itself. Use on "personal post:", "/personal-post", "741 post", "/741-post", "write a post from this thought", "turn this into a LinkedIn/X post", or "what should I post about". Do NOT use for client-voice page/blog copy (content-writing), client social-proof stories (story-automation-system), image-only templates (social-visuals-workflow), or any client-facing message.
allowed-tools: Read, Write, Edit, Bash(python3:*), AskUserQuestion
---

# Personal posts

## Critical
- Never auto-post or auto-schedule, to any platform, ever. Deliver text (and image) ready; Martin posts himself.
- Every single post needs Martin's own explicit go, every time, before it goes anywhere — approving one post is not a go for the next one.
- No invented or exaggerated numbers (`claims-need-real-data`). No client named or shown with a real result without that specific client's own go for that specific post — default to anonymized (industry + real number, no name, no logo).
- No invented personal stories, experiences, or unclear details presented as fact, ever. Classify every personal claim as confirmed experience / explicit opinion / inferred interpretation / hypothesis before drafting it (`references/voice-profile.md` §"Accuracy rules"; the same standard applies to the business account) — never present an inference as something Martin actually said, lived, or confirmed.
- **Two accounts, two commands, never mixed.** `/personal-post` = Martin's personal account, `references/voice-profile.md`, no 741 branding, `scripts/build_personal_image.py`. `/741-post` = 741 Studio's business account, `references/voice-profile-business.md`, full 741 branding, `scripts/build_business_image.py`. Determine the account from which command triggered the run (step 0) and use ONLY that account's voice file and image script for the rest of the run — never blend them.
- **Angles before drafting, every post (Martin, 2026-10-22).** Never jump straight to one framing. Step 4 reads `references/strategy-notes.md` fresh and proposes a few distinct angles, grounded in that knowledge base's actual reach data, before any full draft exists. This is the answer to "are you actually checking the knowledge base": yes, every run, at this specific step, not just once at build time.
- `disable-model-invocation` is off so natural triggers work (e.g. "write a post from this thought" with no slash command) — same reasoning as `captions`. Martin's go-per-post (step 8) is the real gate, not the invocation rule. The one external send in this skill, `cleanse.sh`'s rival-model pass, only runs when a draft scores below 5/5 in step 7 — it is not a guaranteed step on every run.

## Inputs
- Which account: `/personal-post` or `/741-post` (or the equivalent natural-language phrasing — "741 post" / "post for the studio account" means business, anything else defaults to personal, ask if genuinely unclear).
- Martin's raw dictated or typed thought (primary input, every real run).
- Or, if he has none ready: "what should I post about" -> offer ideas from that account's topic backlog (step 1 below).
- Optional: specific platforms named (skip the rest, and skip the image step if neither Instagram nor Facebook is named).
- Optional (personal account only): a client name + a result inside the thought (triggers the client-go check, step 2) — the business account's client-transformation posts follow the same rule, see `voice-profile-business.md`.

## Workflow
Copy this checklist into your reply and tick it off:

- [ ] 0. **Account.** Fix which account this run is for (`/personal-post` or `/741-post`) before anything else. State it at the top of your reply.
- [ ] 1. **No thought ready?** Run `python3 scripts/topic_backlog.py list --status open --account <personal|business>`, offer 2-3 ideas across different pillars for THAT account (AskUserQuestion, not prose). Once Martin picks or restates one as his own thought, continue below; mark it used at the end (step 11).
- [ ] 2. **Client-result check (only if the thought names a client + a result, either account).** Ask Martin (card) whether that specific client has given a go for this specific post. No go on file -> draft anonymized (industry + the real number, no name, no logo). Go on file -> draft named, with the real result.
- [ ] 3. **Claim check.** Trace every number or result in the thought to a real source; never invent or round up. Also classify every personal or business claim in the thought (confirmed experience / explicit opinion / inferred interpretation / hypothesis) — if it is anything but a confirmed experience or an explicit opinion, confirm it with Martin before drafting it as fact. An unclear detail (a name, a tool, a reference you can't place) is confirmed, never guessed.
- [ ] 4. **Angle generation (default on every post; skip only if Martin explicitly says "skip angles").** Read `references/strategy-notes.md` fresh — its "Directly actionable" and "Useful mental models" sections — and propose 3-4 distinct angles on the thought. Each angle is ONE hook line plus: the technique it leans on (negative/contrarian framing, numerical specificity, "How I not How To" narrative, a damaging admission, an SPCL pillar — Status/Power/Credibility/Likeness, a BVT-calibrated edge, a save-worthy framework/checklist shape) and one line on why it reaches further, citing the strategy-notes.md figure where one exists (e.g. "negative framing: 1.3-1.8x higher hook rate"). For a personal-account pillar-1 post, the editorial method (`voice-profile.md` §"Editorial method") is itself a good source of angles. Show hook lines only — not full drafts — as ONE `AskUserQuestion` card. Martin picks one, asks for a blend, or rejects all and gives a new thought. Log: `python3 scripts/run_log.py write angle_picked ok --account <personal|business> "<picked technique>"`.
- [ ] 5. **Core draft.** Read the matching voice file in full, every time — `references/voice-profile.md` for `/personal-post`, `references/voice-profile-business.md` for `/741-post` — do not rely on memory of a previous run. Draft ONE core argument in that account's voice, built on the chosen angle from step 4: claim first, then the one reason to believe it.
- [ ] 6. **Platform adaptation.** Using the matching voice file's §"Per-platform adaptation" and `references/platform-specs.md`, write only the platform versions actually needed (default: all 4). Save each to its own file named `draft-<platform>.txt` (`draft-x.txt`, `draft-linkedin.txt`, `draft-instagram.txt`, `draft-facebook.txt`) so the verification script can infer the platform. Before moving on, self-check each draft against copy-rules C4.1 (2 sentences per paragraph at most) — `verify_draft.py` does not check this, it is a read-it-yourself gate.
- [ ] 7. **Verify — every version, separately.** Run `python3 scripts/verify_draft.py draft-*.txt`. Any file below 5/5 or over its hard length limit: shorten/rewrite, or for the slop gate run `.claude/skills/slopmonster/tools/cleanse.sh draft-<platform>.txt`, then re-run `verify_draft.py`. Repeat until every file passes (exit 0). Do not show Martin a version that has not passed.
- [ ] 8. **Martin's go — every post, every time.** Show every verified platform version together, labeled with the account (one `AskUserQuestion` card, not a prose list) and ask for his go. He may approve some, reject others, or ask for a rewrite of one or more. Log the result: `python3 scripts/run_log.py write martin_go <ok|rejected> --account <personal|business> "<one-line note>"`.
- [ ] 9. **Image (Instagram + Facebook only, conditional).** For each approved version on a platform that needs an image: personal account -> `python3 scripts/build_personal_image.py "<pull-quote line>" "Martin Drendel" <instagram|facebook>` (no branding); business account -> `python3 scripts/build_business_image.py "<pull-quote line>" <instagram|facebook>` (full 741 branding). Never cross them. Skip entirely for LinkedIn/X-only runs or when Martin did not approve the Instagram/Facebook version. Read the rendered PNG back (`Read`) to check for collisions or overflow before delivering it.
- [ ] 10. **Deliver.** Hand Martin the approved text (and image, where built), ready to paste, clearly labeled with the account. Log delivery: `python3 scripts/run_log.py write delivered ok --account <personal|business> "<platforms delivered>"`. Never post or schedule it.
- [ ] 11. **Backlog housekeeping.** If the thought came from the backlog (step 1), mark it used: `python3 scripts/topic_backlog.py use <id>`. If a usable fragment came up in chat but was not used today, offer to add it: `python3 scripts/topic_backlog.py add <lane> "<idea>" "<source>" --account <personal|business>`.

## Output template
For each approved platform:
```
**<Account> / <Platform>**
<final text>
(image: <path> | no image for this platform)
```

## Checkpoints
- After step 0: the account is fixed and stated before any drafting starts.
- After step 4: Martin has picked an angle before any full draft is written.
- After step 7: every platform version must show exit 0 from `verify_draft.py` before step 8 — never show Martin an unverified draft.
- After step 8: wait for Martin's explicit go, per post, every time. A go on a past post is never a go for this one. A go on the personal account is never a go for the business account.

## References
- `references/voice-profile.md` — personal account: philosophy, stance, hard no's, accuracy rules, topic pillars, account scope, per-platform shape, copy-rules mapping (read every `/personal-post` run).
- `references/voice-profile-business.md` — business account: 741 Studio voice, topic pillars, image branding (read every `/741-post` run).
- `references/content-intelligence-brief.md` — Martin's full personal-brand brief (background, personality notes, editorial method, production philosophy); context source for `voice-profile.md`, re-read when a personal-account post needs background grounding beyond what's already extracted.
- `references/strategy-notes.md` — sourced technique and reach-data notes from Martin's content-marketing knowledge base (hook framing, no-outbound-links rule, voice techniques, SPCL/BVT mental models). Applies to both accounts. Read fresh at step 4 (angle generation) every single run — this is the knowledge-base check Martin asked for, not a one-time build-time read.
- `references/platform-specs.md` — length rules used by `scripts/check_lengths.py` (also checks for outbound links in the body); applies to both accounts.
- `~/.claude/skills/content-writing/references/copy-rules.md` — external, read directly for the headline/DR pattern (C2.1, C2.8, C4.1, C4.5, C8.4). Never call `/content-write`.
- `.claude/skills/slopmonster/` — external, `tools/deslop.py` (lint) and `tools/cleanse.sh` (rival-model pass below 5/5).
- Memory: `social-visuals-workflow` (render-pipeline precedent reused by both image scripts), `claims-need-real-data` (claim rule), `741-youtube-channel-avatar` (English, international audience context), `741studio-design-system` (CI reused by `business_post_quote.html`).
