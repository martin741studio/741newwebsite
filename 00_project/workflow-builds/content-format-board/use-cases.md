# Use cases (step 2.1)

## UC1 — Prospect pitch board
**Trigger phrase:** "content format board for <prospect>", "build a content strategy board for the pitch with <prospect>", "what video content should we show <prospect>".
**Steps:** Read the prospect's existing folder (`00_project/prospects/<slug>/`) if one exists — reuse intake/demand/competitors data, never re-derive. Source real public questions for the prospect's field (Reddit/forum search, travel/industry blog roundups, competitor comment mining, Google autocomplete). State the one real finding/gap plainly before any format talk. Map the verified format taxonomy onto the prospect's actual situation (not generic advice). Flag readiness check and on-camera person as open questions for the client to answer. Write execution steps and a quality bar per chosen format.
**Tools:** `firecrawl_search`/`firecrawl_scrape` (public questions), existing prospect-folder files (reuse), `content-format-library/001` (verified taxonomy reference).
**Deliverable:** `00_project/prospects/<slug>/content-format-board.md` — feeds into `sales-pitch`/`booking-sequence` material, never auto-sent.

## UC2 — Running client content planning
**Trigger phrase:** "content format board for <client>", "plan the next content batch for <client>", "what should <client> be filming next".
**Steps:** Same research and mapping steps as UC1, but using the client's live site/GBP/existing social presence as context, and (if known) their actual team bandwidth for the readiness check. Output is framed as a production plan for the next batch, not a pitch.
**Tools:** same as UC1, plus the client's own `00_project/assets/<client>/` folder for existing material.
**Deliverable:** `00_project/assets/<client>/content-format-board/<date>/board.md`.

## UC3 — Paraphrased trigger (covers 2.2 scenario 2)
**Trigger phrase:** "what social content formats should we pitch <prospect> with", "give <client> a video content strategy board", "social content board for <name>".
Same workflow as UC1/UC2 depending on whether `<name>` is a prospect or a running client (the skill checks `prospects/` then `assets/` to decide).
