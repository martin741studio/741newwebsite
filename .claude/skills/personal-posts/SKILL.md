---
name: personal-posts
description: Turns a dictated thought or a raw braindump into platform-adapted posts (Instagram, Facebook, LinkedIn, X) for the personal account (/personal-post) or the 741 Studio business account (/741-post). Angles first, Martin's go per post, never posts itself. Triggers "personal post:", "/personal-post", "741 post", "/741-post", "write a post from this thought", "what should I post about", "grill me for post ideas". Not for client page/blog copy.
allowed-tools: Read, Write, Edit, Bash(python3:*), AskUserQuestion
---

# Personal posts

## Critical
- Never auto-post or auto-schedule, anywhere. Deliver text (and image) ready; Martin posts himself.
- Every post needs Martin's own explicit go. A go on one post, or on the other account, is not a go for this one.
- No invented or exaggerated numbers (memory `claims-need-real-data`). No client named with a real result without that client's go for that post; default anonymized (industry + real number).
- No invented personal stories or unclear details as fact. Classify every claim as confirmed experience / explicit opinion / inferred interpretation / hypothesis (`references/voice-profile.md` §"Accuracy rules"). Never present an inference as something Martin said or lived.
- **A raw dump is never a complaint dressed up as a post (Martin, 2026-10-22).** It goes through step 2 first. If only frustration is left and no real claim about how something works, say so and do not draft (`references/voice-profile.md` §"Braindumps and the complaint-vs-insight rule").
- **Two accounts, never mixed.** `/personal-post`: `references/voice-profile.md`, no 741 branding, `scripts/build_personal_image.py`. `/741-post`: `references/voice-profile-business.md`, full 741 branding, `scripts/build_business_image.py`. The command fixes the account (step 0).
- **Angles before drafting, every post** (step 5).

## Inputs
- Account: "741 post" / "post for the studio account" = business; otherwise personal; ask if unclear.
- A single clear thought, no thought ("what should I post about"), or a raw braindump (step 2). Optional: named platforms (skip the image step if neither Instagram nor Facebook).
- "grill me for post ideas" / "brainstorm topics" / "I have no ideas today" runs the Topic grill instead of step 1. Details: `references/topic-grill.md`

## Workflow
Copy this checklist into your reply and tick it off.

- [ ] 0. **Account.** Fix and state it at the top of the reply.
- [ ] 1. **No thought ready?** `python3 scripts/topic_backlog.py list --status open --account <personal|business>`; offer 2-3 ideas across different pillars (AskUserQuestion).
- [ ] 2. **Raw dump?** Save verbatim: `python3 scripts/braindump.py add <personal|business> "<raw text>"`. Distill with the editorial method (`voice-profile.md` §"Editorial method"): what real claim is left? State it back as a card (inferred until confirmed). Then `python3 scripts/braindump.py mark <id> distilled` and use the claim as "the thought".
- [ ] 3. **Client-result check** (client + result in the thought). Card: client's go for this post? No go: anonymize.
- [ ] 4. **Claim check.** Trace every number to a real source. Confirm unclear details with Martin, never guess. Research world claims yourself (`voice-profile.md` §"Externally verifiable claims get researched") and report what the research says, even if it contradicts the framing.
- [ ] 5. **First-principles note, then angles** (skip only if Martin says "skip angles"). Three separate cards, one stop each, never one prose block: 5a root mechanism, 5b cross-domain translation (especially to business), 5c 3-4 angle hooks from `references/strategy-notes.md` (read fresh). Martin picks one, a blend, or a new thought. Log: `python3 scripts/run_log.py write angle_picked ok --account <personal|business> "<picked technique>"`. Details: `references/steps-5-11.md`
- [ ] 6. **Core draft.** Read the matching voice file in full every run. ONE core argument, claim first, then the one reason to believe it.
- [ ] 7. **Platform versions** per the voice file's §"Per-platform adaptation" and `references/platform-specs.md`, saved as `draft-<platform>.txt` (x, linkedin, instagram, facebook). Self-check copy-rules C4.1 (max 2 sentences per paragraph).
- [ ] 8. **Verify.** `python3 scripts/verify_draft.py draft-*.txt`. Below 5/5 or over limit: rewrite or `.claude/skills/slopmonster/tools/cleanse.sh draft-<platform>.txt`, re-run until exit 0.
- [ ] 9. **Martin's go.** All verified versions together, labeled with the account, one `AskUserQuestion` card. Log: `python3 scripts/run_log.py write martin_go <ok|rejected> --account <personal|business> "<note>"`.
- [ ] 10. **Image (Instagram + Facebook only).** Business: `python3 scripts/build_business_image.py "<pull-quote line>" <instagram|facebook>`. Personal quote card (default): `python3 scripts/build_personal_image.py "<pull-quote line>" "Martin Drendel" <instagram|facebook>`. "Assume X / actually Y": `python3 scripts/build_personal_mechanism.py "<assumption>" "<reality>" "Martin Drendel" <instagram|facebook>`. Read the PNG back to check overflow. Never cross a personal style with the business template.
- [ ] 11. **Deliver** text (and image) ready to paste, labeled with the account. Business account: also upload to Drive `Socials Martin > Fertige Posts` (Martin, 2026-10-29). Log: `python3 scripts/run_log.py write delivered ok --account <personal|business> "<platforms delivered>"`. Never post or schedule. Drive details: `references/steps-5-11.md`
- [ ] 12. **Backlog.** Used from backlog: `python3 scripts/topic_backlog.py use <id>`. Unused fragment: offer `python3 scripts/topic_backlog.py add <lane> "<idea>" "<source>" --account <personal|business>`.

## Output template
```
**<Account> / <Platform>**
<final text>
(image: <path> | no image for this platform)
```

## Checkpoints
- Step 0: account fixed. Step 2: distilled claim confirmed before any angle or draft. Step 5: angle picked before any full draft. Step 8: exit 0 on every version before step 9. Step 9: explicit go, per post.

## References
- `references/voice-profile.md` (personal) and `references/voice-profile-business.md` (business): read every run for that account.
- `references/strategy-notes.md` (hook and reach data), `references/platform-specs.md` (length rules for `scripts/check_lengths.py`), `references/content-intelligence-brief.md` (personal-brand background).
- `references/outlier-content-notes.md`, `references/outlier-carousel-pipeline.md` (incl. Drive IDs), `references/producer-formats.md`: business-account research and carousel/story/reel formats.
- `references/topic-grill.md`, `references/steps-5-11.md`: detail moved out of this body.
- `~/.claude/skills/content-writing/references/copy-rules.md`: C2.1, C2.8, C4.1, C4.5, C8.4. Never call `/content-write`.
- `.claude/skills/slopmonster/`: `tools/deslop.py`, `tools/cleanse.sh`.
- Memory notes: `social-visuals-workflow`, `story-automation-system`, `claims-need-real-data`.
