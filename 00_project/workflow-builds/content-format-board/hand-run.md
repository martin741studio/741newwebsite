# Hand-run (step 2.3) — Little Frenchie, Pererenan/Canggu (prospect pitch case)

Real task, solved by hand, before writing the skill body. Source: existing prospect folder `00_project/prospects/little-frenchie-bali/` (intake.md, demand.md, competitors.md) — not re-derived.

## 0. What's already known (reused, not re-researched)
- Business: Little Frenchie, French restaurant/brunch spot, Jl. Munduk Kedungu 39, Pererenan, Bali. Owner on the intake record: "Lovely". 4.8 stars, 1,421 reviews — more reviews than 2 of the 3 competitors who outrank her.
- Only own-listing category is "French restaurant." The three competitors who beat her (Woods Pererenan, Artisan, Brunch Club Pererenan) all carry the broader category "Restaurant"/"Brunch restaurant"/"Cafe" — she is the only genuinely French-positioned listing in her own 7×7 grid.
- Real search demand already measured: "best restaurant canggu" 2,400/mo, "dinner canggu" 1,000/mo, "brunch canggu" 590/mo, "restaurant pererenan" 320/mo (her scan keyword), "french restaurant bali" 90/mo.

## 1. Public questions sourced (step 1 of Martin's 5 process questions)
Searched live (firecrawl_search, web), not guessed:
- Reddit r/bali, "Best brunch in Canggu?" — a real, recurring thread. Real answer quoted: "I've been to most of the famous brunch cafes: Copenhagen, 7am, baked. All good! Recently I tried Gather in Pererenan, which was amazing!" None of the real answers in this thread name Little Frenchie.
- Travel-blog roundups (weareglobaltravellers.com, adventuresnsunsets.com) list Woods Bali, Brunch Club Pererenan, Honey, Touche, ST. Ali, Gather for "best brunch Pererenan" — same gap, Little Frenchie absent.
- Direct search for "Little Frenchie Pererenan Bali review reddit instagram" surfaced only her Jakarta sister location's Instagram — no Bali-location public conversation at all.

**Finding to put in front of her (real, not invented):** she already out-reviews several competitors who out-rank her, but she does not exist in the actual public conversation ("best brunch Canggu/Pererenan," "French food Bali") where her buyers are asking the question right now. That gap is the pitch's opening, and it is also exactly the content she should be making.

Sourcing method that worked (answers Martin's process question 2): Reddit/forum search (`firecrawl_search`, `sources: ["web"]`, plain query, not a scraper) + travel-blog roundups surfaced the real recurring questions faster than guessing. A DataForSEO PAA/related-questions pull is the deterministic complement for scale (not run here — see decisions.md on tooling).

## 2. Format mapped to her situation (verified taxonomy, `content-format-library/001`)
| Format | Level | Her execution |
| --- | --- | --- |
| One-Shot | LV1 (lofi + title/visual hook) | Single shot of the steak frites being plated tableside; title hook text: "Why fly to Paris for steak frites when it's 5 minutes from the beach?" |
| One-Shot | LV3 (vignette) | A regular arriving by scooter, greeted by name, sitting at "their" table, bread basket arriving unprompted — the actual bistro-regulars world, not a staged shot. |
| Ten-Shot | LV1 (no text) | Fast cuts: croissant lamination, butter brushing, steak sear, flambé, plating, dining room, beach light outside. Needs one well-chosen sound track, no narration. |
| Ten-Shot | LV3 (narration + shot list) | Lovely narrates why she opened a French spot in Pererenan, shots matched line by line: dough → sear → guests → sunset. |
| Yap | LV1 (raw) | Lovely, phone propped in the kitchen, answering "why steak frites in Bali?" straight to camera. |
| Yap | LV3 (prop) | Same answer, built around one prop — a baguette, or the cut of beef on a board. |
| How/Why We Do It | — | Answers the real gap found above directly: "why real steak frites needs this specific cut" or "why we don't shortcut croissant lamination" — category education riding on her one real differentiator (she is the only genuinely French kitchen in the grid, not a brunch-cafe copy). |

Readiness check (the video's actual pre-step, not a named format): the 3 questions — does volume break ops, drop quality, or outpace team skill — need the client's own answer, not a guess. Flagged as a required input in the skill, not assumed in this hand-run (no bandwidth/team data exists in the prospect folder).

## 3. Who's on camera
Owner "Lovely" is the only real on-camera candidate in the current record (no other staff named). The skill must ask this explicitly per client/prospect rather than assume an owner is willing or available — flagged as a required question, not a default.

## 4. Friction points found while doing this by hand (feed into SKILL.md)
1. Reddit cannot be `firecrawl_scrape`d directly (site blocked) — must come from `firecrawl_search` result snippets, not a scrape call. Script/skill must not retry a direct Reddit scrape.
2. The real finding worth leading with wasn't a format at all — it was "she out-reviews people who out-rank her and isn't in the conversation at all." The skill needs a step that states this gap in plain words BEFORE listing formats, or the board reads as generic advice.
3. "Who's on camera" and the readiness check both have no default — the skill must ask, never assume a willing owner or spare production capacity.
4. The taxonomy names ("One-Shot," "Yap," etc.) are fine as internal labels working with Martin, but the deliverable shown to Lovely must not use "Yap" or any Cut-30/Alex-Garcia wording — needs 741-neutral labels in the client-facing template (step 3 build task).
