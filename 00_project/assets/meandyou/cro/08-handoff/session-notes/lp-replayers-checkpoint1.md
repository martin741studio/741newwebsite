# LP Replayers — state at Checkpoint 1 (2026-10-12)

- CRO run: `cro/lp-replayers/` (`_status.md`). Copy run: `content-writing/lp-replayers/` (`05-final/page.md`, draft-v4, G1–G6 PASS, 1.698 words, 14 sections).
- Drive: "CRO LP Replayers" https://drive.google.com/drive/folders/1UX5Df9ZF8KcAShJ4Qk0hocgDOSP8_UeU (11 markdown files). The v2 screenshot PNG is not in Drive: Claude in Chrome could not click or run scripts in the Drive tab ("Cannot access a chrome-extension:// URL of different extension"). All my Chrome tabs are closed.
- Proposed URL `/schlagfertigkeit-lernen` (the Overlooked and Undersold runs use `/lp-overlooked`, `/lp-undersold`). Decision Martin (RP2).
- For integration: no page links to this LP yet (link network: 0 inbound). Proposal: homepage situation card 1 "Mehr dazu" → this URL; rhetorik S10 and faq "Ich bin introvertiert" one text link each.
- ERFOLG Magazin written in past tense here ("zählte ihn zu den Top 100 Trainern", cover 2017). Sibling pages use present tense (RP8).
- New sourced facts other runs can reuse: book "Nie wieder sprachlos!" Gütersloher Verlagshaus 26.08.2019, 256 pages, "50 kurze Kapitel" (publisher text; a new edition with a changed title is announced). Podcast episode 193 (07.09.2026) show notes: "dreißig Sekunden Selbstaufnahme", "Technik ohne geklärte Person ein Kostüm bleibt". Sources in `cro/lp-replayers/02-data/dataset.md` L5–L11.
- registry.json not touched. Nothing committed, nothing deployed.

# LP Replayers — state at Checkpoint 2 (2026-10-12)
- Copy approved ("confirmed continue" via main session). `cro/lp-replayers/04-copy/approved-copy.md` = `content-writing/lp-replayers/05-final/page.md`, `_run.json` status "freigegeben".
- Prototype `cro/lp-replayers/07-prototype/index.html`, build `build.py` (imports rhetorik → michael → seminare → homepage, text parsed from approved-copy.md). Server port 8831 still running. Self-check 43/44 (v2 18), visual check 30/11/2, verify.py 23/0 (footer texts allowed in M11).
- Mockup `06-gpt-assets/full-page-v1-final.png` (chat 6acc56ab-…), hero image `06-gpt-assets/images/01-hero-heimweg.png` (chat 6acc56d0-…), same persona face as the homepage `sit-replayers.webp`.
- Persona rule in code: the header button hides while a section button is in view (JS at the end of build.py). Integration: keep it, or drop it if the site header must always show the button.
- CSS warning for integrators: the homepage `.q` and the homepage `.acc` (2-column grid) clash with page-specific names. I use `.rpq`.
- Drive: 17 files + CP1 extras; old `_status.md`, `00-lead-info.md`, `04-copy-page-entwurf.md` moved to `_archiv`. Chrome Drive upload worked this time.
- registry.json not touched. Nothing committed, nothing deployed. Downloads left in ~/Downloads: lpr-01-hero-heimweg.png, lpr-full-page-v1.png (copies are in the run folder).

# LP Replayers — community rebuild done (2026-10-12)
- Prototype v2: `cro/lp-replayers/07-prototype/v2/index.html` (server 8831, URL /v2/index.html). v1 call version stays in `07-prototype/`.
- Copy v7 = `cro/lp-replayers/04-copy/approved-copy.md` (call version archived as `approved-copy-v1-call.md`).
- All CTAs: https://www.skool.com/talk-to-me-9409/about?utm_source=lp-replayers&utm_content=<section>, data-event community_click. Header and footer: no „Gespräch buchen“ on this page (footer link renamed „Community Talk to ME“). Integration: the shared header/footer need a page switch for this.
- Price conflict on Skool: text 39 €/Monat Gründungsmitglied, button $44/Monat (DE and US). Every price on the page carries a yellow mark. Must be cleared before go-live (PAngV).
- The Skool about text has result promises; recommend the client softens it (RP4).
- Drive: v1 files moved to _archiv with -v1 suffix; v2 files uploaded.
