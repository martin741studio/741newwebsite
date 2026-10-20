# Night Shift 2026-09-15 — 5 pages planned · 4 pass · 1 executed (needs Critic) · 0 skipped

## Summary

First real end-to-end test of the feedback pipeline. Two processes ran back to back on this
date (a manual test before 20:00, then the real 20:00 LaunchAgent) and both wrote to this same
folder — the concurrency lock added after this run prevents that going forward. This file is
rebuilt from `state.json` and the actual `critic/`/`feedback/` files on disk, not from the stale
auto-generated `REVIEW.md` an earlier Reviewer step left behind.

The Planner found the Supabase `client_locations` NAP query broken (Postgres error 42703 —
wrong column names; fixed in `night-shift.sh` after this run). Since Rule 2 needs real NAP data
for every CREATE/AUDIT page, the Planner correctly skipped all task-queue (CREATE/AUDIT) work
rather than risk fabricated NAP, and filled the queue with 5 open client-feedback items instead
(2 clients, oldest feedback first: Praxis Suriya, Rabenmütter Shop).

**4 of 5 pages finished and passed the Critic. 1 page has a draft but was not yet graded.**

## Praxis Suriya

- [ ] freigeben  **6 · A · Google Business Profil** (FEEDBACK) — pass
      → `feedback/Praxis Suriya/7fd15e89-27b8-426c-a28a-d88998ef37b1.md`
      Top-Fixes: none required. One eyeball item: the draft marks Mon/Sat/Sun as "geschlossen"
      in the GBP hours block. The client did not state this directly — check this line before
      entering it into GBP.

- [ ] freigeben  **8 · C · NAP / Citations / Domains** (FEEDBACK) — pass
      → `feedback/Praxis Suriya/d1c58471-eafc-4ef9-8418-1611a2345445.md`
      Top-Fixes: confirm the exact spelling of the "Femalecare" domain with the client. Give a
      go/no-go on the "ayurveda-mainz" domain — the practice sits in Ingelheim, not Mainz.

- [ ] freigeben  **3 · Beschreibung** (FEEDBACK) — pass
      → `feedback/Praxis Suriya/21a25f8b-8ee2-4f8f-8378-36aac01e35c4.md`
      Top-Fixes: none. The client gave a ready-made text (669 characters, verified against the
      750-char GBP limit). Copy it in as-is.

## Rabenmütter Shop

- [ ] freigeben  **2 · Trauerkarten (Pillar)** (FEEDBACK) — pass
      → `feedback/Rabenmütter Shop/801d4d7d-1a22-4d45-a08e-e0b213dff2ec.md`
      Client approved the section and asked how handwritten-look cards could work. Draft lays
      out two real implementation models (printed handwriting font vs. genuinely hand-written)
      with trade-offs, and correctly stages the client-facing explanation for Martin rather than
      answering the client itself. Top-Fixes: decide which of the two models to offer, then
      brief Martin's reply to the client.

- [ ] **6 · Zusätzliche Verkaufskanäle** (FEEDBACK) — **executed, not yet graded**
      → `feedback/Rabenmütter Shop/66478f5c-02a4-4076-b1c3-ad9d211e3533.md`
      Draft: Etsy dropped (brand mismatch with Etsy's handmade/artisan segment, per the client's
      own reasoning), Pinterest Business/Shop + TikTok Shop listed as the existing channels
      instead. Read it before use — the Critic pass this needs did not run tonight (budget/
      process end, not a content problem). Run it through the Critic (or a human read) before
      treating this one as verified.

## What went wrong tonight (fixed, for the record)

1. **NAP query used wrong column names** (`address`, `category` don't exist on
   `client_locations`; real columns are `street`, `postal_code`, `city`, `country`,
   `primary_category`). This blocked all CREATE/AUDIT work tonight. **Fixed** in
   `reporting/night-shift.sh`.
2. **No concurrency lock** — an earlier manual test run overlapped the real 20:00 LaunchAgent
   run, both writing this folder at once (visible as interleaved log lines and this file being
   overwritten mid-run). **Fixed**: an atomic lock now makes a second run exit immediately
   instead of racing.
3. **Executor/Critic pairs were silently re-run twice per page even after passing on the first
   attempt** — a bug in how the runner checked pass/fail. Roughly halved how many pages a night
   could finish. **Fixed**: the Critic now writes its verdict to a dedicated marker file the
   runner reads directly, no more guessing.
4. Multiple invocations printed `Error: Reached max turns (25)` but still produced correct,
   complete output before hitting the cap — not a hard failure, but the budget is tight. Worth
   raising to 35–40 turns if this keeps showing up on cleaner nights.

None of the above affected the quality of what did get produced — every passed page cites real
client comments only, uses `[fehlt: …]` instead of inventing anything, and stayed on-language
and HWG-clean.

## Martin: action items

- [ ] Run the Critic (or read it yourself) on the Rabenmütter "Zusätzliche Verkaufskanäle" draft
      before treating it as done.
- [ ] Check the Praxis Suriya GBP-hours draft (Mon/Sat/Sun "geschlossen" line) before entering
      it into GBP.
- [ ] Give a go/no-go on the "ayurveda-mainz" domain and confirm "Femalecare" spelling before
      booking anything.
- [ ] Decide the Trauerkarten handwriting model (printed font vs. real handwriting) so Martin's
      reply to the client can go out.
- [ ] 3 clients had open feedback but were not queued tonight (2-client cap): Praxis Hüwel,
      Maria Brasse, Naturheilpraxis Dumann. They carry over to the next run automatically.
- [ ] No CREATE/AUDIT task work ran tonight (NAP bug, now fixed) — the next run should pick that
      queue back up alongside feedback.
