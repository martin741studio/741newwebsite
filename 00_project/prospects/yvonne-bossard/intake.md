# Intake: Yvonne Bossard (step 0, 2026-10-29, intake.py)

- Name: Yvonne Bossard
- Business: Yvonne Bossard
- Website: https://innere-arbeit.ch/ (200, 2.09 s)
- Home title: Energetisches Heilen –Yvonne Bossard - Innere Arbeit | Yvonne Bossard-Serio
- Form of address on the site: "du" (Sie-forms 6, du-forms 15). Page = "du"; homepage draft = "du".
- Branch class: health (HWG: no healing or success promise, no protected titles)
- Country: CH, location_code 2756 (from domain .ch).
- City: (not given: take it from the place address)
- Google profile: place_id **ChIJkYD_t1uvn4ERKkcs4VFAdn8** (corrected manually, see below). Business name on Google: "Innere Arbeit". Category: Naturheilkundler. Phone +41 78 231 59 21. Unclaimed signal is weak (no public address, no visible reviews); is_claimed=true per DataForSEO.
  - WRONG auto-match (ignore): intake.py's name search for "Yvonne Bossard" returned only US results (Houston, TX) — the short Maps link (https://maps.app.goo.gl/2UKMP3nLJKJGWdxZ7) has no ChI-format place_id, only a CID (`0x819faf5bb7ff8091:0x7f764051e12c472a`, decimal 9184599210483009322), which intake.py's regex does not resolve to a place_id, so it fell back to the unrelated name search. Two further Local Falcon proximity searches ("Innere Arbeit" near Zürich, by city name and by exact coordinates) also returned 20 unrelated Zürich wellness/health listings, not this one — it does not surface for a plain keyword search.
  - Resolved via `dfs.py prospects/yvonne-bossard serp/google/maps/live/advanced` with keyword "innere-arbeit.ch" (the domain, not the name) within 3 km of 47.3774417,8.5367356 → exact match on feature_id, cid, lat/lng, phone AND domain simultaneously. Full record: `evidence/dfs-maps-serp2.json` (item with `place_id: "ChIJkYD_t1uvn4ERKkcs4VFAdn8"`).
- Existing scans (0 credits): 0
- Old review page / folder: none (grep 04_site/review/ and prospects/)
- Full name: Yvonne Bossard-Serio. Title on site: "Naturheilpraktikerin und Human Energetikerin". Address (Impressum/Kontakt): Gasometerstrasse 40, 8005 Zürich.
- **Identity three-way check (hard rule, done 29.10.2026):** LinkedIn (https://www.linkedin.com/in/yvonne-b-5a391ba2/, "Yvonne B.", Zürich Metropolitan Area, company "Innere Arbeit", Martin is a mutual connection) ↔ website imprint (Innere Arbeit, Yvonne Bossard-Serio, Gasometerstrasse 40, 8005 Zürich, +41 78 231 59 21) ↔ Google entry (place_id ChIJkYD_t1uvn4ERKkcs4VFAdn8, "Innere Arbeit", phone +41 78 231 59 21, website innere-arbeit.ch). All three agree.
- **Content note:** her site's language is strongly esoteric/alternative (energetisches Heilen, Quantenmedizin, DNA/Urfrequenz, Organcodes, lemurianische Zeitlinien). The review page must stay strictly factual about search visibility, never echo or endorse these specific claims — use only her neutral professional framing ("Naturheilpraktikerin", "energetisches Heilen").
- Channel: LinkedIn found (see above), Martin is a mutual connection.
- Loom: none yet (placeholder)

Run time intake.py: 62.4 s
