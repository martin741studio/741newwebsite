# Fact check: review page ana-vital (Ana Violeta Fredel)

Date: 2026-10-12. Checker did not write the page.
Inputs: `prospect.json`, all files in `evidence/`, `evidence/scan-grid.png`, `draft/index.html`.
Live pages read with curl on 12.10.2026: `/`, `/Kosten/`, `/Impressum/`, `/Kontakt/`, `/Therapien/Infusiontherapie/`, `/Therapien/Bioresonanztherapie/`, `/Therapien/Blutegeltherapie/`, `/Therapien/Ozontherapie/`, `/Therapien/Stosswellentherapie/`.

## Own calculations

- Grid from `scan-grid.png` (row 1 = north, column 1 = west):
  - R1: 20+ 20+ 20+ 20+ 20+ 20+ 20+
  - R2: 18 20 20+ 20+ 20+ 20+ 20+
  - R3: 8 15 16 20 20+ 20+ 20+
  - R4: 5 6 17 **20** 20+ 20+ 20+ (centre = 20)
  - R5: **1** 5 13 16 18 20+ 20+
  - R6: **1** 5 9 17 20+ 20+ 20+
  - R7: 5 4 7 15 20+ 20+ 20+
- Top 3: 2 points (R5C1, R6C1, both at the SILWINGEN label). Top 10: 11 points. Top 20: 23 points. 20+: 26 points.
- Mean of the 23 found ranks: 261 / 23 = 11.35. This matches Falcon `arp` 11.35. The image and the JSON agree.
- Scan time: `timestamp` 1791766875 = 2026-10-12 01:01 UTC = 03:01 CEST.
- Distance from scan centre 49.4433 / 6.6372 (haversine): Rollinger 1.73 km, Oehm 2.48 km, Mondorf 3.88 km, Czapla 1.74 km, Hilt 4.15 km, Sahl 1.47 km, ana-vital 5.12 km.
- Competitor homepage mean (comp-pages.json): (186 + 452 + 138 + 286) / 4 = 265.5, so 266. The four pages are Oehm, Czapla, Hilt (zeitRaum), Sahl. Mondorf timed out. Rollinger was not measured.
- Practices with higher SoLV than ana-vital (4.08): 10. Their `found_in`: 49, 49, 49, 49, 49, 49, 47, 49, 44, 43.
- `heilpraktiker merzig` and `heilpraktikerin merzig` have the same monthly series [110, 70, 90, 90, 110, 170, 140, 110, 140, 110, 110, 170], the same CPC 0.72 and the same competition. Google Ads groups these close variants. The sum 220 counts one demand two times.
- Newest month in `monthly_searches` is 2026-08. `search_volume` is a 12-month mean.
- Therapy page word counts (site-pages.json): Infusion 421, Bioresonanz 358, Ozon 388, Stoßwelle 253, Pulsation 357, Cellulite/Lipödem/Striae 367, Blutegel 343.
- TTFB mean: (1.01 + 0.79 + 0.87) / 3 = 0.89 s.
- Scorecard today: items 1, 3, 8, 15, 21 = 1 point each, all others 0. Total 5 / 44.

## Claim table

| # | Claim (field) | Verdict | Evidence / reason |
|---|---|---|---|
| 1 | hero_h1: only around Silwingen in the top 3 | SUPPORTED | scan-grid.png: rank 1 at R5C1 and R6C1, next to SILWINGEN. Falcon `solv` 4.08 = 2/49. |
| 2 | hero_h1: Stadtmitte on Platz 20 | SUPPORTED | Centre point R4C4 = 20. Centre 49.4433/6.6372 is next to the "Merzig" label. |
| 3 | hero_h1: plan for the next 8 weeks | SUPPORTED | roadmap ends at "Woche 3–8". Internal plan. |
| 4 | hero_sub / hero.sub: 5,0 Sterne | SUPPORTED | google-panel: 5,0 · 6. Falcon `rating` 5.000. |
| 5 | hero_sub / draft: fast 30 Jahre Erfahrung | SUPPORTED | Live homepage: "fast 30 Jährige Erfahrung in der modernen Naturheilkunde". |
| 6 | hero_sub: "Google zeigt deine Praxis fast nur in Silwingen" | WRONG | The map shows her in the top 20 at 23/49 points and in the top 10 at 11 points. These points cover the full west third (Weiler, Hilbringen, Mondorf, Oberleuken area). She is rank 20 in the centre. Only the top 3 is limited to Silwingen. |
| 7 | hero.sub / draft: sieben Therapien | SUPPORTED | site-urls.json: 7 therapy pages (Infusion, Bioresonanz, Ozon, Stoßwelle, Pulsation, Cellulite/Lipödem/Striae, Blutegel). |
| 8 | hero.sub / grid_h2 / card 2: top 3 at 2 of 49 points | SUPPORTED | See #1. |
| 9 | card 1: title "Heilpraktikerin" | SUPPORTED | Impressum: "Gesetzliche Berufsbezeichnung: Heilpraktiker/in". |
| 10 | card 1: Infusionen, Bioresonanz, Ozon, Blutegel, Merzig-Silwingen | SUPPORTED | Site menu. Falcon `address` "Bannholzer Str. 4, 66663 Merzig-Silwingen". |
| 11 | card 1 / draft: 5,0 ★ bei 6 Bewertungen | SUPPORTED | google-panel; Falcon `reviews` 6. |
| 12 | card 2: Stadtmitte Merzig Platz 20 | SUPPORTED | See #2. |
| 13 | card 3: newest review about 2 years old | SUPPORTED | google-panel: "2x vor 2 Jahren". |
| 14 | card 3: Annika Rollinger 21 | SUPPORTED | Falcon `reviews` 21. google-panel "(21)". |
| 15 | card 3: no replies from the practice | SUPPORTED | google-panel: 0 owner replies. |
| 16 | card 4: first screen "Willkommen bei Ana-Vital", no Heilpraktikerin, no Merzig | SUPPORTED | home-today-1440.jpg. Note: the page title tag has "Heilpraktiker in Merzig". It is not visible on the screen. |
| 17 | card 4 / kpi / score_today: 5 von 44 | SUPPORTED | scorecard-today.md, own sum = 5. |
| 18 | grid.intro: 49 points, 5 km around Stadtmitte, 12.10.2026 | SUPPORTED | Falcon `grid_size` 7, `points` 49, `radius` 5.0 km, timestamp = 12.10.2026 03:01 CEST. |
| 19 | caption_today: both top-3 points around Silwingen | SUPPORTED | See #1. |
| 20 | caption_today: 26 points not in top 20 | SUPPORTED | Own count 26. 49 − 26 = 23 = Falcon `found_in`. |
| 21 | caption_today: Rollinger top 3 on about 49 % | SUPPORTED | Falcon `solv` 48.98. |
| 22 | caption_goal: practices in front have 4 to 21 reviews | SUPPORTED | Top 4: 21, 4, 13, 5. Top 6 adds 12, 8. Range stays 4–21. |
| 23 | system.intro: "Jede Zahl unten stammt aus echten Messungen" | WRONG | calc defaults conv 4 %, deal 50 %, budget 150 € and "3 Infusionen" are assumptions. calc.vol 220 is a double count (#30). score_draft 36 is a target (#66). |
| 24 | system kpi: 1.900 Suchen/Monat Infusionstherapie | SUPPORTED | dfs-volumes-ads.json `search_volume` 1900. |
| 25 | system kpi / step2_h2: visible at 23 of 49 points | SUPPORTED | Falcon `found_in` 23. |
| 26 | step1_h2: your texts are longer than the others | SUPPORTED | Homepage 652 words vs 186 / 452 / 138 / 286 (homepages only). |
| 27 | step1_h2 / quick win 1: missing line "Heilpraktikerin in Merzig" | SUPPORTED | H1 has neither word (site-pages.json). See #33 for a limit. |
| 28 | step1.demand: 10 volumes (14800, 5400, 5400, 2900, 1900, 390, 260, 110, 110, 110) | SUPPORTED | dfs-volumes-ads.json, each value matches. |
| 29 | demand_sub: "(Oktober 2026)" | WRONG (minor) | Values are 12-month means. Newest month is 2026-08. Data was pulled on 12.10.2026. Write "Monatsmittel, Stand Oktober 2026" or "Sep 2025–Aug 2026". |
| 30 | demand_note: "In Merzig selbst suchen rund 220 Menschen im Monat" | WRONG | (a) 110 + 110 counts one grouped demand two times (identical monthly series). Real figure ≈ 110. (b) The volume is for all of Germany, not "in Merzig selbst". (c) Searches are not people. |
| 31 | no_data / guide.think: no volume for "naturheilpraxis merzig" | SUPPORTED | `search_volume` null. |
| 32 | depth.big: 652 words; 0 times Heilpraktikerin/Merzig in H1 | SUPPORTED | site-pages.json home `words` 652, `h1`. |
| 33 | depth.sub: "Google erfährt an der wichtigsten Stelle nicht, wer du bist und wo" | WRONG (misleading) | The title tag is "Heilpraktiker in Merzig,Naturheilpraxis in Merzig" (site.json `home_title`). Google reads it. Say "in der Hauptüberschrift" instead of "an der wichtigsten Stelle". |
| 34 | depth.bars: homepages in front, mean of 4 = 266 | SUPPORTED (note) | Arithmetic is correct. The 4 pages are Oehm, Czapla, Hilt, Sahl. All rank in front of her. They are not the "vier ersten" of the table (Rollinger not measured, Mondorf unreadable). |
| 35 | depth.note: "Drei der vier Praxen vor dir schreiben 'Heilpraktikerin (in) Merzig' als Überschrift" | WRONG | comp-pages.json: only 2 of 4. Hilt H1 "Heilpraktikerin Merzig". Sahl H1 "Heilpraktikerin in Merzig". Czapla H1s are "Herzlich Willkommen", "Ihre Naturheilpraxis in Merzig ..." (no "Heilpraktikerin"). Oehm has no H1 (only the title tag). |
| 36 | depth.note: your H1 is a long sentence without these words | SUPPORTED | site-pages.json home `h1`. |
| 37 | depth.note: Infusion page 421 words, no price | SUPPORTED | site-pages.json 421, `price_mention` false; curl confirms no price. |
| 38 | items[0].why: "Drei der vier Praxen vor dir nutzen genau diese Überschrift" | WRONG | Same as #35. 2 of 4. |
| 39 | items[0].why: homepage starts with "Willkommen bei Ana-Vital" | SUPPORTED | home-today-1440.jpg. |
| 40 | items[1].why: price 50 € per infusion only on Kosten page | SUPPORTED (incomplete) | Kosten: "50 Euro zzgl. Ampullen oder Infusionsmischungen". The text drops the "zzgl." part. |
| 41 | items[2].why: Vitamin-C 5.400; only in a list | SUPPORTED | dfs 5400. Infusion page lists "Hochdosis Vitamin C Drip" under "Infusionsbeispiele". |
| 42 | items[3].why: 14.800; 60 € only on Kosten page | SUPPORTED | dfs 14800. Kosten "60 €, zzgl. Erstanamnese". Bioresonanz page has no price. |
| 43 | items[4].why: 390; Blutegel missing on Kosten page | SUPPORTED | dfs 390. Kosten page has no Blutegel entry. |
| 44 | items[5].why: Erstgespräch 120 €, Krankenkasse, Dauer "heute verteilt auf mehrere Seiten" | WRONG (part) | 120 € and the Krankenkasse text are both on the one Kosten page. No fetched page gives the duration of the first appointment. "Verteilt auf mehrere Seiten" has no support. |
| 45 | step2_h2 / step2.h2: "Die Praxen vor dir sind an allen 49 Punkten zu sehen" | WRONG (too general) | 10 practices rank in front of her. Jochum-Leers 47, Schreier 44, Jongebloet 43 points. The statement is true only for the top 6. |
| 46 | step2.lead: the four first are in top 20 at all 49 points; yours at 23 | SUPPORTED | Falcon `found_in` 49 × 4; 23. |
| 47 | table: ana-vital, Alternativmediziner, 6, 4,1 % | SUPPORTED | Falcon `solv` 4.08, category alternative_medicine_practitioner. |
| 48 | table: Rollinger, Naturheilpraktiker, 21, 49 % | SUPPORTED | `solv` 48.98, naturopathic_practitioner; panel "Naturheilpraktiker". |
| 49 | table: Oehm, Alternativmediziner, 4, 44,9 % | SUPPORTED | `solv` 44.9. |
| 50 | table: Mondorf/Gabor, Alternativmediziner, 13, 42,9 % | SUPPORTED | `solv` 42.86. |
| 51 | table: Czapla, Heilpraktiker, 5, 36,7 % | SUPPORTED | `solv` 36.73, "Heilpraktiker (alternative practitioner)". |
| 52 | step2.fine: definition and date | SUPPORTED | Falcon definition; scan 12.10.2026. |
| 53 | meaning: Oehm 4 reviews, about 45 % | SUPPORTED | See #49. |
| 54 | meaning: practices in front 1,5 to 4 km from centre | SUPPORTED | Own: 1.73, 2.48, 3.88, 1.74 km (top 6: 1.47–4.15). |
| 55 | meaning: your practice about 5 km | SUPPORTED | Own: 5.12 km. Note: google-panel note says "6–7 km". The coordinates give 5.1 km. Do not use 6–7 km. |
| 56 | changes[0]: Google lists you only as "Alternativmediziner" | SUPPORTED | google-panel; Falcon one category. |
| 57 | changes[0]: "Praxen vor dir sind als 'Naturheilpraktiker' oder 'Heilpraktiker' eingeordnet" | WRONG (part) | Of the top 4, only Rollinger and Czapla. Oehm (#2) and Mondorf (#3) have only "Alternativmediziner", the same as her. Write "Zwei der vier Praxen vorn". |
| 58 | changes[1] / quick win 3: seven therapies list | SUPPORTED | Site menu. "Hautbehandlung" = Cellulite/Lipödem/Striae page. |
| 59 | changes[2]: newest review about 2 years | SUPPORTED | google-panel. |
| 60 | changes[3]: none of 6 reviews has a reply | SUPPORTED | google-panel. |
| 61 | changes[5]: posts e.g. about a talk (Vortrag) | SUPPORTED | dfs-serp-name2.json: Instagram "Vortragsreihe mit Heilpraktikerin Ana Fredel". |
| 62 | cleanup / check: 21 / 39 unseriöse links, e.g. casino sites | SUPPORTED (wording) | dfs-refdomains-spam.json `total_count` 21 (spam score ≥ 60); backlinks-summary `referring_domains` 39. Casino: bestnz-poker-casinoslot.com, betwinnermirror.com. These are websites (domains), not "Seiten". |
| 63 | cleanup: "ana-vital merzig" not in first 9 results; directories in front | SUPPORTED (note) | dfs-serp-name.json depth 10: 9 organic, no ana-vital.de; dasoertliche, gelbeseiten, jameda, dastelefonbuch, backinjob. A `knowledge_graph` block exists. It probably shows her profile. For "naturheilpraxis ana fredel" ana-vital.de is #3. |
| 64 | cleanup / check: homepage twice, almost the same text | SUPPORTED | site-pages.json: `/` and `/ana-vital/` same title, H1, 652 words. Text is identical, not only "fast". |
| 65 | cleanup / check: 0 / 6 reviews with reply | SUPPORTED | google-panel. |
| 66 | step3: score_draft 36, "Ziel: 36+ / 44" | UNSUPPORTED | No scored sheet for the draft. scorecard-today.md gives only a target line. The draft is the first screen only. Items 9, 13, 14, 15, 17, 19 need sections below the first screen. A first-screen-only draft can reach about 30–32, not 36. |
| 67 | step2.good: every one of 6 reviews has 5 stars | SUPPORTED | Mean 5.0 over 6 reviews = all 5. |
| 68 | step2.good: your texts are longer than the practices in front | SUPPORTED | Homepages only (see #26). |
| 69 | step3.lead: 22 check points incl. Werberecht | SUPPORTED | scorecard-today.md has 22 items, item 22 = HWG. |
| 70 | note_today: no Heilpraktikerin, Merzig, reviews or appointment in first screen | SUPPORTED | home-today-1440.jpg. |
| 71 | note_draft: same logo, your colours, your photos | PART UNSUPPORTED | Logo matches the live site. No input shows the source of `praxis.jpg` / `portrait.jpg` or the `foto-*.webp` files. Check that they come from her site or GBP. |
| 72 | five "Was?": word "Heilpraktikerin" missing | SUPPORTED | Visible homepage text has no "Heilpraktikerin". Only the title tag has "Heilpraktiker". |
| 73 | five "Wo?": Merzig not in first screen | SUPPORTED | Screenshot. The first "Merzig" in body text is below the fold and names a former employer. |
| 74 | five "Warum du?": 5,0 stars nowhere on the site | SUPPORTED | site-pages.json `rating_mention` false on all 15 pages. |
| 75 | five "Wie zum Termin?": no button, no phone at top | SUPPORTED | Screenshot. |
| 76 | five "Wer?": photo only at bottom edge | SUPPORTED | Screenshot. |
| 77 | calc.vol 220 | WRONG | See #30. Use 110. |
| 78 | calc.cpc 0.7 | SUPPORTED | dfs `cpc` 0.72 (rounded). |
| 79 | calc budget 150, conv 4 %, deal 50 % | UNSUPPORTED | No source. These are assumptions. Label them as assumptions. |
| 80 | calc.val 270 = Erstgespräch 120 € + 3 Infusionen à 50 € "laut deiner Kosten-Seite" | PART UNSUPPORTED | Prices are on the Kosten page. "3 Infusionen" is our assumption. 50 € excludes "Ampullen oder Infusionsmischungen". The Kosten page says "Erster Termin", not "Erstgespräch". |
| 81 | volumes_line: heilpraktiker merzig 110, heilpraktikerin merzig 110, infusionstherapie 1.900 (ganz Deutschland) | SUPPORTED (note) | Values match. "(ganz Deutschland)" sits only after infusionstherapie. All three are all-Germany figures. |
| 82 | volumes_line: click costs about 0,72 € (Oktober 2026) | SUPPORTED | dfs `cpc` 0.72, pulled 12.10.2026. |
| 83 | check: phone is a link on every page | SUPPORTED | site-pages.json `tel_link` true on 15/15; curl: tel:+496869510271 on all fetched pages. |
| 84 | check: http redirects to https | SUPPORTED | site.json `http_redirects_to_https` true. |
| 85 | check: server answers in about 0,9 s, "in Ordnung" | SUPPORTED (number) | Mean 0.89 s. The verdict "in Ordnung" is soft: web.dev rates TTFB above 0.8 s as "needs improvement". |
| 86 | check: form on Kontakt page | SUPPORTED | site-pages.json Kontakt `has_form` true; curl shows `<form>`. |
| 87 | check: Landhaus next to therapies in menu | SUPPORTED | Screenshot menu; /Landhaus/ title "Ferienhaus in Merzig". |
| 88 | check: H1 long sentence without Heilpraktikerin / Merzig | SUPPORTED | site-pages.json. |
| 89 | check: Google description names "Homöopathie und Nahrungsergänzungsmittel" | SUPPORTED | Meta description: "... für Homöopathie, alternative Medizin und Nahrungsergänzungsmittel in Merzig". |
| 90 | check: 2 of 15 pages without H1, incl. Stoßwelle | SUPPORTED | site.json `pages_no_h1` 2: /Therapien/ and /Stosswellentherapie/. |
| 91 | check: therapy pages have 343 to 421 words | WRONG | Stoßwelle page has 253 words. Range is 253–421. |
| 92 | check: "mehr als die meisten Seiten vor dir" | UNSUPPORTED | Only competitor homepages were measured. No competitor therapy pages are in the evidence. |
| 93 | check: visitor statistics installed | SUPPORTED | site.json `ga4` G-F1FTLBC8MQ. |
| 94 | check: no call tracking | UNSUPPORTED | No evidence either way (GA4 events not checked). The Google profile also counts calls if she has owner access. |
| 95 | check: data for Google missing (structured data) | SUPPORTED | site.json `jsonld_blocks` 0. |
| 96 | check: 5,0 stars, 6 reviews, newest 2 years, Rollinger 21, no replies | SUPPORTED | google-panel; Falcon. |
| 97 | check: Werberecht – sentences name serious diseases or sound like a healing promise | SUPPORTED | Homepage "Ausheilen von Beschwerden", "zahlreichen Therapieerfolge". Infusion page "Krebs, Depressionen, Burnout", "Alzheimer, Demenz". Ozon page "wirkt die Ozontherapie fantastisch", Asthma, Neurodermitis. Blutegel page "können Thromben auflösen". |
| 98 | quickwins_h2: "Sechs Schritte, die schon nächste Woche wirken" | UNSUPPORTED | Promise of an effect time. No evidence. |
| 99 | quick win 2: add GBP category "Heilpraktiker" | SUPPORTED | Category exists (Czapla). She holds the title (Impressum). |
| 100 | quick win 5: redirect /ana-vital/ to homepage | SUPPORTED | Duplicate confirmed (#64). |
| 101 | roadmap why: "Google vertraut einer Seite erst, wenn sie sauber ist" | UNSUPPORTED | General claim. No evidence. |
| 102 | roadmap why: "Ein voller Eintrag bringt dich auch in Merzig selbst in die Karte" | WRONG (map) | She is already in the map in the centre (rank 20) and at ranks 15–17 in the centre column. Also a result promise. Write "weiter nach vorn". |
| 103 | proof_h2: "Andere Heilpraktiker haben genau hier angefangen. Heute stehen sie oben." | UNSUPPORTED | No case-study evidence in the inputs. Check against the case-study source before use. |
| 104 | proof.lead: two Heilpraktiker and two practices with the same bottleneck | UNSUPPORTED | No case-study evidence in the inputs. |
| 105 | guide.celebrate: Schlirf from Platz 85 to Platz 1 for "Heilpraktikerin" | UNSUPPORTED | No evidence in the inputs. Check against the case-study source. |
| 106 | guide.point: Stadtmitte rank 20; top 3 only around Silwingen | SUPPORTED | See #1, #2. |
| 107 | guide.insight: biggest lever is the Google profile (category, therapies, reviews) | WEAK | Opinion. The data partly argues against the category point: Oehm and Mondorf rank on 45 % / 43 % with only "Alternativmediziner". Distance (5.1 km vs 1.5–4 km) fits the map pattern better. Soften the claim. |
| 108 | draft: phone 06869 510271 | SUPPORTED | Falcon, google-panel, Impressum. |
| 109 | draft: Bannholzer Str. 4, 66663 Merzig-Silwingen | SUPPORTED | Falcon `address`; Impressum. |
| 110 | draft: eyebrow / badge / tile "Heilpraktikerin" | SUPPORTED | Impressum. |
| 111 | draft: H1 "Naturheilkunde und Infusionen in Merzig." | INCONSISTENT | Factually OK (Silwingen is part of Merzig). But the page says the fix is H1 "Heilpraktikerin in Merzig" (step1_h2, items[0], quick win 1, roadmap). The draft H1 does not contain "Heilpraktikerin". |
| 112 | draft: first talk gives a personal plan | SUPPORTED | Kosten: "Erster Termin (inklusive: Erstanamnese, ..., Therapieplan)". |
| 113 | draft: Infusionen, Bioresonanz, Ozon-, Blutegeltherapie | SUPPORTED | Site menu. |
| 114 | draft: "Ich melde mich persönlich bei Ihnen" | SUPPORTED (weak) | Kontakt: "Wir beraten Sie gerne persönlich!" Confirm with her. |
| 115 | draft: "mit eigener Praxis in Silwingen" | SUPPORTED | Address. |
| 116 | draft: "7 Therapien von Infusion bis Blutegel" | SUPPORTED | See #7. |

## Special checks

- **(a) HWG in our text:** None found in `prospect.json` or the draft. Our text uses "Hautbehandlung", not "Lipödem". The draft sub "Ihre Gesundheit natürlich begleiten" is neutral. Caution for the new pages (Bioresonanz, Ozon, Vitamin C): write no efficacy or indication claims. Courts treat efficacy claims for Bioresonanz as misleading (§ 3 HWG).
- **(b) Protected titles:** None. She holds "Heilpraktiker/in" (Impressum). The recommended GBP category "Heilpraktiker" matches. No "Ärztin", "Therapeutin" or similar.
- **(c) Jargon:** Low. Two lines are technical for a lay reader: "„http://“ leitet automatisch auf „https://“ weiter" and "Der Server antwortet in rund 0,9 Sekunden". All other terms are plain.
- **(d) Map contradictions:** #6 ("fast nur in Silwingen") and #102 ("bringt dich ... in die Karte"). All other map statements match the image.

## Must fix

1. **#30 / #77 – 220 searches (demand_note, calc.vol).** WRONG. The two keywords have identical monthly data. Google groups them. Use 110. Do not say "in Merzig selbst" or "Menschen". The figure is all-Germany searches for the term.
2. **#35 / #38 – "Drei der vier Praxen ... Überschrift" (depth.note, items[0].why).** WRONG. Only 2 of 4 (Hilt, Sahl). Czapla and Oehm do not.
3. **#91 – "Therapie-Seiten 343 bis 421 Wörter".** WRONG. Stoßwelle has 253. Use "253 bis 421".
4. **#6 – hero_sub "Google zeigt deine Praxis fast nur in Silwingen".** WRONG versus the map. She is in the top 20 at 23 points and in the top 10 at 11 points. Write "unter den ersten drei nur in Silwingen".
5. **#102 – roadmap "bringt dich auch in Merzig selbst in die Karte".** WRONG versus the map. She is already rank 20 in the centre. Write "weiter nach vorn". Remove the result promise.
6. **#45 – step2_h2 / step2.h2 "Die Praxen vor dir sind an allen 49 Punkten".** WRONG as general. True for the top 6 only. Three practices in front have 43–47 points.
7. **#57 – "Praxen vor dir sind als Naturheilpraktiker oder Heilpraktiker eingeordnet".** WRONG in part. Only 2 of the top 4. Oehm and Mondorf have her category.
8. **#33 – "Google erfährt an der wichtigsten Stelle nicht, wer du bist und wo".** Misleading. The title tag says "Heilpraktiker in Merzig". Limit the claim to the H1.
9. **#23 – system.intro "Jede Zahl unten stammt aus echten Messungen".** WRONG. Calc values are assumptions and the draft score is a target.
10. **#44 – items[5] "heute verteilt auf mehrere Seiten".** WRONG in part. Price and Krankenkasse are both on the Kosten page. No page states the first-appointment duration.
11. **#66 – score_draft 36 / "Ziel 36+ / 44".** UNSUPPORTED. No scored sheet. A first-screen-only draft cannot meet items 9, 13–15, 17, 19. Score the draft or lower the number.
12. **#79 / #80 – calc assumptions.** UNSUPPORTED. Mark budget 150 €, conv 4 %, deal 50 % and "3 Infusionen" as assumptions. Add "zzgl. Ampullen/Infusionsmischungen" to the 50 €.
13. **#92 – "mehr als die meisten Seiten vor dir".** UNSUPPORTED. Only homepages were measured.
14. **#94 – "Keine Anruf-Messung".** UNSUPPORTED. No evidence.
15. **#98 – "Sechs Schritte, die schon nächste Woche wirken".** UNSUPPORTED promise.
16. **#101 – "Google vertraut einer Seite erst, wenn sie sauber ist".** UNSUPPORTED.
17. **#103 / #104 / #105 – proof_h2, proof.lead, guide.celebrate (Schlirf 85 → 1).** UNSUPPORTED by these inputs. Verify against the case-study source before use.
18. **#111 – draft H1 has no "Heilpraktikerin".** Inconsistent with our own main recommendation. Change the draft H1 or the recommendation.
19. **#29 – "(Oktober 2026)" on volumes.** Minor. The numbers are 12-month means up to Aug 2026.
20. **#71 – "deine Fotos".** Confirm the photo source.
21. **Jargon (minor):** rewrite the "http/https" row and "Der Server antwortet" in plain words.
22. **Wording (minor):** #62 "21 / 39 Seiten" means websites (domains). #85 "in Ordnung" for 0.89 s TTFB is soft.

## Re-check after fixes

Date: 2026-10-12. Scope: the 22 "Must fix" items. Sources: `prospect.json`, `draft/index.html`, evidence files, `case-library.json`, live Kosten page (curl).

Result: 21 of 22 FIXED. 1 STILL OPEN (item 17, headline only).

| # | Item | Status | Note |
| --- | --- | --- | --- |
| 1 | #30/#77 220 searches | FIXED | `demand_note` and `calc.vol` now say 110. "Google zählt „heilpraktikerin merzig“ dabei mit". No "in Merzig selbst". |
| 2 | #35/#38 "Drei der vier" | FIXED | `depth.note` and `items[0].why` now say "Zwei der vier". Hilt and Sahl are correct (comp-pages.json). |
| 3 | #91 343 bis 421 | FIXED | Now "253 bis 421 Wörter". |
| 4 | #6 hero_sub | FIXED | Now "unter den ersten drei zeigt Google deine Praxis nur rund um Silwingen". Falcon: 2 of 49 points in the top 3, both near Silwingen. |
| 5 | #102 roadmap | FIXED | Now "damit Google dich auch in der Stadtmitte weiter oben zeigt". No Merzig-selbst promise in the roadmap. See new issue 3 for `grid.caption_goal`. |
| 6 | #45 step2_h2 | FIXED | Now "Die vier Praxen vorn ... Du an 23". The four table practices have 49 of 49 points in the top 20 (Falcon). 23 of 49 for Ana is correct. |
| 7 | #57 category claim | FIXED | Text now names Rollinger ("Naturheilpraktiker") and Czapla ("Heilpraktiker"). Matches Falcon categories. |
| 8 | #33 H1 claim | FIXED | Claim is now limited to the Hauptüberschrift. Title tag "Heilpraktiker in Merzig" is not denied. |
| 9 | #23 system.intro | FIXED | Now: steps use measurements, the calculator uses assumptions. |
| 10 | #44 items[5] | FIXED | "Verteilt auf mehrere Seiten" is gone. Text now says the topics need one own page with a button. |
| 11 | #66 score_draft 36 | FIXED | Label now reads "Ziel für die ganze Startseite: 36+ / 44". It is a target, not a score. `score_draft: 36` stays in the JSON. Confirm the template does not show it as a measured score. |
| 12 | #79/#80 assumptions | FIXED | "Budget, Anfrage- und Buchungsanteil sind Annahmen". "3 Infusionen" is gone. Start value 250 = 120 + 80 + 50 "plus Material". Kosten page confirms 120 €, 80 € (from the second appointment), 50 € "zzgl. Ampullen oder Infusionsmischungen". |
| 13 | #92 "mehr als die meisten" | FIXED | Row now says "Deine Startseite ist länger als die Startseiten vor dir". 652 words vs 186, 452, 138, 286. See new issue 1 for two similar lines. |
| 14 | #94 "Keine Anruf-Messung" | FIXED | Text is gone. |
| 15 | #98 "Sechs Schritte ... wirken" | FIXED | Now "die du schon nächste Woche umsetzen kannst". |
| 16 | #101 "Google vertraut ..." | FIXED | Text is gone. |
| 17 | #103/#104/#105 proof | STILL OPEN | `proof.h2`, `proof.lead` and `guide.celebrate` are OK against case-library.json (Schlirf, Heilpraktikerin, Regensburg, "Platz 85 → 1", "Heilpraktikerin"). But `headlines.proof_h2` still reads "Andere Heilpraktiker haben genau hier angefangen. Heute stehen sie oben." Only 2 of the 4 featured cases are Heilpraktiker (Schlirf, Laserstein). Abel is Familienberatung, Lengauer is Innenarchitektur. Schlirf started at 85 and Laserstein at about 6, not "genau hier". |
| 18 | #111 draft H1 | FIXED | Draft H1 is now "Ihre Heilpraktikerin in Merzig." |
| 19 | #29 "(Oktober 2026)" | FIXED | Now "Mittel der letzten 12 Monate, Abruf 12.10.2026". |
| 20 | #71 "deine Fotos" | FIXED | `sources["draft.photos"]` states the photos come from ana-vital.de. |
| 21 | Jargon | FIXED | Rows are now "Immer verschlüsselt" and "Deine Seite beginnt nach rund 0,9 Sekunden zu laden". Mean of 1.01, 0.79, 0.87 is 0.89. |
| 22 | Wording | FIXED | "21 von 39 Websites". "Ladezeit knapp" replaces "in Ordnung". 21 spam domains and 39 referring domains match the evidence. |

### New or remaining issues in the changed texts

1. **Text length claim, same weakness as #92.** `headlines.step1_h2`: "Deine Texte sind länger als die der anderen". `system.step2.good`: "deine Texte sind ausführlicher als die der Praxen vor dir". Only homepages were measured (4 competitor homepages; Mondorf was unreadable). Write "Startseite" instead of "Texte".
2. **New unsupported benchmark.** `check[0].rows[2].text`: "Gut sind unter 0,8 Sekunden". No source in the evidence. Add a source (for example the Google web.dev time-to-first-byte guide) or remove the sentence.
3. **Result promise on the map.** `grid.caption_goal`: "Unter den ersten drei auch in Merzig selbst." The same type of promise as #102. Label it as a goal ("Ziel: ...") or soften it.
4. **Minor, headline wording.** `items[0].why`: "nutzen genau diese Überschrift". Hilt uses "Heilpraktikerin Merzig", Sahl uses "Heilpraktikerin in Merzig". Use "eine fast gleiche Überschrift".
5. **Minor, volumes.** The shown volumes are the Google Ads `search_volume` field. The mean of the 12 monthly values is different for some terms (heilpraktiker merzig 118, ozontherapie 3283, infusionstherapie 1792). Keep the label "Google-Angabe, Mittel der letzten 12 Monate" and do not recompute.
6. **Minor, calc.** `calc.cpc` is 0.7, the text says 0,72 €. `calc.val` and the text say "Erstgespräch"; the Kosten page says "Erster Termin".

## Fixes after the re-check (orchestrator, 2026-10-12)
- 17 proof_h2 → "Andere Praxen hatten ähnliche Lücken. Heute stehen sie oben." (cases: Schlirf 85→1, Laserstein →1, Abel 0→100 %, Lengauer 18→1; case-library.json)
- step1_h2 and step2.good now say "Startseite" (only homepages measured).
- Load time: the 0,8 s threshold was removed.
- caption_goal is labelled "Das Ziel:".
- items[0].why: "eine solche Überschrift"; "Erstgespräch" → "erster Termin" (Kosten page wording); cpc text "rund 0,70 € (genau 0,72 €)" (slider step 0.1).
- score_draft: the page shows only the label "Ziel für die ganze Startseite: 36+ / 44"; the 36 sets the bar width.
Rebuilt; validate.py 0 errors. Status: clean.
