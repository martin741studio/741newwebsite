# Decisions (Martin's gos, with date and his words)

**2026-10-24, round 1 (inputs grill):**
- Job scope: "Format-and-reference board only (Recommended)" — board only, no scripts, no final copy. personal-posts stays fully separate; this workflow never calls it and is never called by it.
- Runtime surface: "Terminal / Claude Code skill (Recommended)."
- Cadence: "On demand, per client or prospect (Recommended)."
- Hard limit selected: "No outside-method-name leakage (Recommended)" (the only one explicitly picked in the multi-select; no-auto-publish and no-invented-examples are inherited standing house rules, applied regardless).

**2026-10-24, round 2 (source video):**
- Martin supplied the real source link directly: `https://www.youtube.com/watch?v=Q2T1kv0aAyA` ("You Only Need 4 Content Formats to Blow Up Your Brand," channel Alex Garcia) — chosen over proceeding on an unconfirmed web-search guess.

**2026-10-24, round 3 (hand-run case):**
- "Little Frenchie Bali (prospect pitch)" chosen as the real step-2.3 test case over Swatma Bali or a running client.

**2026-10-24, round 4 (hand-run result + build decisions):**
- Hand-run result: "Looks right, proceed (Recommended)" — the gap finding, format mapping, and friction points in `hand-run.md` are confirmed good raw material.
- Client-facing format labels: "Plain descriptive English (Recommended)" — e.g. "Single-Scene Hook," "Fast-Cut Story," "Talk-to-Camera," "Why-We-Do-It Educational." No 741-branded naming system, no creator/program names, ever, in client-facing output.
- Missing readiness-check or on-camera answers: "Flag it as an open question in the board, keep going (Recommended)" — never blocks the run, never guessed or defaulted.

**2026-10-24, round 5 (CP1 go held — knowledge base question):**
- Asked at CP1: "which knowledge base is here integrated?" Answer given (content-format-library + client folder + live web search). Martin: "should be this one https://notebook.google.com/notebook/7f6a765f-7a30-446e-9259-e1a497c318eb" — his NotebookLM notebook "The Content Marketing Playbook" (36 sources, includes the Alex Garcia video, hook/retention/looping research, algorithm reports, trend-discovery tools, Hormozi content strategy, Jonah Berger virality). Integrated as knowledge source 4: video-relevant findings extracted into the skill's `references/playbook-notes.md` (the personal-posts extraction of the same notebook deliberately left the video findings out). CP1 go still open after this integration.

**2026-10-24, round 6 (Checkpoint 1):**
- GATE PASSED cp1 shown in full. Martin: "Go (Recommended)" for the build (step 3), with the knowledge base confirmed as: content-format-library (Alex Garcia transcript) + NotebookLM "Content Marketing Playbook" (video findings → playbook-notes.md) + the client/prospect's own folder + live Reddit/forum/blog search per run.

**2026-10-24, round 7 (Checkpoint 2):**
- GATE PASSED cp2 shown in full; scorecard 58/60 = 96.7 %, no blocking zeros. Martin: "Go, ship it (Recommended)".
- Little Frenchie board (the skill's step-9 checkpoint): "Go, use it for the pitch (Recommended)" — first two ideas: Idea 1 (steak frites, single scene) and Idea 2 (brunch fast-cut); open points for the client: 3 readiness answers, on-camera, 4 fact checks.

**2026-10-24, round 8 (after install — Martin confirms the board and names the next phase):**
- Martin: "We have the video content board, Little Frenchie. We just go with it as it is now. That is the checkpoint, and I confirm."
- Next phase requested (his words, condensed): before building the HTML/10-minute-script part, save the client's logo, corporate identity and existing visuals (Instagram) first; research references for the outcome "which we already saw somewhere else"; then create 2–3 GPT images per idea (e.g. Idea 1) with proper prompts, as a visual reference board that shows the vibe — so the client sees "that's actually our venue, that's how it could look" — plus how the socials could look with those images. "You need to research that first." This is a new checkpoint of the workflow after the written board.
- Excel-sync card (openpyxl venv) left unanswered in this round.
- Martin's 9 example links (from his original request, relayed by the parent session 2026-10-24): all live, saved to `references/outcome-references.md`.

**2026-10-24, round 9 (Martin's correction during the visual hand-run):**
- Martin: "What's missing now here is that we had to actually research reference material for how it should look beforehand, before we create anything in GPT."
- Consequence (skill rule, phase 2): the order is brand inventory → reference research per idea (real posts/reels in the client's category and the chosen format, 3–5 per idea, screenshots + look notes: angle, light, text placement, pacing, proof numbers) → prompts derived from those references → Martin's gate → generation. Never prompts straight from the brand file. The three Idea-1 frames generated before this correction are test material only; Idea 2 waits for its references.

**2026-10-24, round 10 (Martin's second correction, visual hand-run):**
- Martin: plain food images are "fine, but just a steak and fries"; the client's current Instagram grid "is more impressive". The big-word reference is good "because it shows what they really want to highlight with these big letters". "I don't want to see only food images. I want to see concepts and why they're actually drawing attention."
- Rule (phase 2): a visual board shows CONCEPT frames, not product photos. Each frame carries the attention mechanism visibly (big word per cut, the client's hand-lettered red line, a context line, two stories in one frame, hand in motion) in the client's own visual language (their grid is attached as style input), plus one line per concept on why it draws attention, backed by the reference. The v2 plain frames are base plates only.
- Round 10b, Martin on the first v2/v3 renders: "not so high-key. They're looking like: 1. AI, 2. out of a fable book where the princess is eating. It's a bit too much." Rule: the style block asks for a candid phone-video still (uneven daylight, clutter, slight motion blur, no editorial polish, no cinematic glow), never "hyperrealistic editorial photograph". Applied from concept 1B on; 1A/2A kept as the too-polished comparison.
- Round 11 (visual board checkpoint, Martin): "First of all, we need Celine, the creative in her wine-red trousers character" as the guide on the board (not Martin). The big-word fast-cut is "one of numerous things we want to take on Reels that work very well... that's one that could work. Everything else is quite fine." Drop the "What we need from you before shooting" summary block ("we don't really need that kind of summary page"). After the changes the creative director (Céline) gives feedback.
- Round 12 (Martin, with Céline's feedback): "this kind of fulfilment, in terms of how much we present and what we would do, is already quite a lot. She doesn't want to do more, so we can take that. That's a good result for this workflow, and we keep it for now and save it how it is." Board v2 (https://claude.ai/artifact/FSU8xpVv4QsTFxiqVPLxWT) = final for Little Frenchie. "Write it now" for the skill (phase 2).
- Hand-over to the 10-minute-script workflow (prospect review pages): put the Little Frenchie board in; present everything from Céline's character, not Martin's; the whole visual review page in TALKNFIVE corporate identity.
