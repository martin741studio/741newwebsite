# Use cases — personal-posts

## Use case 1 — Agency-insight / build-in-public post

**Trigger phrase:** "Personal post: [raw thought]" or "/personal-post [raw thought]" or "write a post from this: [thought]".

**Steps:**
1. Martin dictates or types a raw thought (e.g. a real 741 number, a decision he made).
2. Skill checks the claim against real data where one is stated (`claims-need-real-data`); asks Martin for the source if it cannot find one.
3. Skill drafts ONE core text in Martin's voice (`references/voice-profile.md`), then adapts it to 4 platform versions (Instagram, Facebook, LinkedIn, X), each inside that platform's length and format.
4. Skill runs `slopmonster/tools/deslop.py` on each version; cleanses with `cleanse.sh` if below 5/5; re-lints until 5/5.
5. Skill shows Martin all 4 versions side by side and asks for his go per post (he can approve some, reject others, ask for a rewrite).
6. For Instagram and Facebook: skill builds the matching image via the existing `social-visuals-workflow` pipeline (`07_social/templates/` → headless Chrome PNG).
7. Skill delivers the approved text (and image, where relevant) ready to paste/post. Martin posts it himself.

**Tools:** Read/Write (drafts), Bash (slop scripts, image render), AskUserQuestion (go per post).

**Deliverable:** 4 platform-ready post texts + 2 images (IG, FB), all through Martin's explicit go.

## Use case 2 — Client-result post (named vs. anonymized)

**Trigger phrase:** "Personal post about [client]'s result: [thought]".

**Steps:**
1. Same drafting steps 2-4 as use case 1.
2. Before showing Martin the draft, skill checks: has this specific client given their own go for this specific post, naming them? If unknown, skill asks Martin via a card.
3. If no client go exists: skill drafts the post anonymized (industry + real number, no client name, no logo) — same pattern as the existing social-proof stories.
4. If a client go exists: skill drafts it with the client named and the real result, and records the go in the post's working file.
5. Rest as use case 1 (slop check, Martin's go, image if IG/FB, delivery).

**Tools:** same as use case 1, plus AskUserQuestion for the client-go check.

**Deliverable:** same as use case 1, with the naming decision recorded.

## Use case 3 — Personal/mindset piece (text-only platform)

**Trigger phrase:** "Personal post, LinkedIn only: [raw thought]" or Martin says a platform explicitly.

**Steps:**
1. Martin's raw thought goes straight to the voice-profile drafting step (steps 2-4 of use case 1).
2. Skill adapts only the named platform(s) — e.g. LinkedIn and X, skipping Instagram/Facebook and skipping the image step entirely.
3. Slop check, Martin's go, delivery as text only.

**Tools:** same as use case 1, minus the image pipeline.

**Deliverable:** 1-2 platform-ready texts, no image, Martin's go.

## Use case 4 — No thought ready, pull from the topic backlog

**Trigger phrase:** "what should I post about" / "give me a personal post idea" / "I've got nothing today, what's in the backlog".

**Steps:**
1. Skill reads `00_project/assets/741studio/personal-posts/topic-backlog.json`, filters to `status: open`, and offers 2-3 ideas across different topic lanes.
2. Martin picks one or restates it in his own words.
3. From there, the run continues exactly as use case 1 (or 2, if it is a client-result idea) — the backlog only supplies the starting thought, never the final wording.
4. Skill marks the picked idea `used` with today's date in the backlog file.

**Tools:** Read/Write (backlog file), AskUserQuestion (idea pick), then use case 1/2/3's tools.

**Deliverable:** same as use case 1/2/3, plus an updated backlog file.
