# Research note — personal-posts

**1.1 Building block:** Skill, not subagent/hook/routine. Reason: a multi-step procedure Martin triggers on demand (R0.2), no fixed schedule (rules out routine, R0.7), needs gates and gos at each run (R2.6).

**Correction found during 4.1 trigger testing (2026-10-22):** first draft set `disable-model-invocation: true`, copying `content-writing`/`content-pool` (their cleanse step sends to OpenAI on every run, an unconditional side effect). A fresh-session trigger test compared this against `captions` — the skill Martin named as this workflow's input-pattern analog — which leaves `disable-model-invocation` OFF with the stated reason "the go card is the gate" against its only side effect (a Drive upload after Martin's go). `personal-posts`'s only external send (`cleanse.sh`) is conditional, only below 5/5 in the slop gate, and did not even fire in the step-2.3 hand run (all 4 drafts scored 5/5 on the first pass). So the `captions` precedent applies, not the `content-writing` one: `disable-model-invocation` is OFF, and Martin's go-per-post (step 7) is the real gate. See `trigger-tests.md`.

**3 relevant rules (rules.md):**
- R1.7 (degrees of freedom): platform-length adaptation and the house-style checks (slop lint, claims check) are deterministic scripts; voice and opinion-framing stay a guided prompt, because Martin's raw thought is different every time.
- R2.10: side effect (external send in the cleanse step) → `disable-model-invocation: true`.
- R8.3 (741-specific): every claim verified or asked for, never guessed — matches the hard limit "no invented numbers" from the grill.

**1 pattern (patterns.md §4):** 4.1 Sequential workflow with gates — matches this job exactly: dictate → draft → adapt per platform → slop-check → Martin's go → (image for IG/FB) → done. One gate that matters (Martin's go per post), not two checkpoints like a full page build.

**1.2 Library search:** `grep -ril "social\|personal.brand\|founder.voice\|voice.profile" 00_project/knowledge/workflow-library/` found nothing — no existing pattern for personal-brand/founder-voice posts in the library. Confirms the gap Martin named.

**1.3 Freshness:** Library `INDEX.md` last refresh 2026-10-11, next due 2026-11-22. Inside the 3-month window, no re-fetch needed.

**1.4 Existing 741 assets to reuse (no rebuild):**
- Image pipeline: `social-visuals-workflow` memory → `07_social/templates/*.html` + headless-Chrome PNG render. This skill calls that pipeline for IG/FB images; it does not build a second one.
- Copy rules: `~/.claude/skills/content-writing/references/copy-rules.md` (741 Content-Raster: no em-dashes, tables, direct-response structure) — reused for post-length, not page-length.
- Slop check: `.claude/skills/slopmonster/tools/deslop.py` (English, pure regex, no external call) + `tools/cleanse.sh` (external GPT pass via `codex`, only when below 5/5), per CLAUDE.md hard rule.
- Claims rule: memory `claims-need-real-data` — every number real and sourced; this skill's "no invented numbers" limit is this rule applied to social copy.
- Avatar/context: `741-youtube-channel-avatar` confirms English, international creative-agency-owner audience — matches Martin's own language choice for this workflow.

**Open questions:** none outstanding — Martin's live grill (brief, 2026-10-22) already answered platforms, input, topics, approval, cadence, voice, and the client-result rule before this build started.
