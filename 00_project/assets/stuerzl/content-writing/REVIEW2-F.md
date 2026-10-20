# REVIEW2-F: ST-40, ST-41, ST-42, ST-33 (read only, 2026-10-11, round 2)

Method: I read page.md, page-vorreview.md, FIX-F-report.md, claims.json, OPEN-FLAGS.md, the _work sources, nap.json, the Source of Truth and section 2 of the fixes file. I re-scraped finanzamt.hessen.de/Frankfurt. Status: C = closed, P = partly, O = open.

## ST-40 Kontakt: VERDICT FIX FIRST (one small fix)
Round 1: no. 1 C ("Termine und Erstberatungen sind auch außerhalb der Telefonzeiten nach Absprache möglich"). 2 C (numbers only, no hours). 3 C ("üblicherweise gegen Pauschale", no amount). 4 C (cut). 5 P (FAQ uses the BRAO wording, the hero does not, see N1). 6 C. 7 C (all questions use "Sie"). 8 C (148/146 cut). Top gaps: Frankfurt route and entrance rule O (client fact, flags B2/B3); placeholders C (1 left, the consent text, correct form); trust line C (S08); schema O (tool limit).
N1 M, hero: "Ihre Angaben unterliegen unserer gesetzlichen Verschwiegenheit." Claim C15 says "Keine Aussage zu Anfragen vor dem Mandat". The hero says the opposite for an inquiry. Same on ST-41 hero ("Es gilt unsere gesetzliche Verschwiegenheit") and ST-42 hero ("Auch hier gilt unsere gesetzliche Verschwiegenheit"). Fix: "Als Rechtsanwälte sind wir zur Verschwiegenheit verpflichtet (§ 43a Abs. 2 BRAO)."
N2 L, S03 Munich access ("Haltestelle Marienplatz ... Sendlinger Tor (U1, U2, U7 und U8)") is a fact here. ST-42 S05 hedges it ("nennt die Kanzlei"). Claim C07 says "nicht unabhängig geprüft". Fix: one hedge on all pages, or check with MVV.
N3 L, no claim in claims.json for "Eine E-Mail ... können Sie jederzeit schicken" and for "erklären verständlich, welche Schritte möglich sind" (the second is in approved-copy line 93). Fix: add both claims.
OK: addresses, phones, e-mail, hours, garage, access match nap.json. Emergency numbers: no hours. Services list equal on 40/41/42. No old address.

## ST-41 Standort Frankfurt: VERDICT FIX FIRST
Round 1: no. 1 P (the "sechs Finanzämter" claim is cut; the new Finanzamt fact has no saved source, see N1). 2 C (neutral list). 3 C (Hoppe removed here). 4 C ("Begleitung vor Ort im Einzelfall"). 5 C. 6 C (§ 386 Abs. 1 to 3, § 388 Abs. 1 follow the saved text; I checked). Top gaps: catchment and route O (client, B3/B10); court/StA fact O (B11); staff and photo O; schema O.
N1 M, S03: "Das Finanzamt Frankfurt am Main hat ... seine Anschrift in der Gutleutstraße 118 bis 124, 60327". Claim C24 cites _work/finanzamt-frankfurt-verzeichnis.txt. The file is 0 bytes. My live scrape confirms the address and "ca. 5 Minuten (Ausgang Süd)", so the fact is true. The evidence is missing. Fix: save the scrape into the file.
N2 L, S06: "In Frankfurt war sie von 2022 bis 2023 Partnerin bei Rettenmaier". It names a former firm. Rule 11 bars former colleagues. It is on the live CV. Fix: client confirms, else cut.
N3 L, H1 and title "Anwalt für Steuerstrafrecht in Frankfurt am Main". Rule 13 approves this only for ST-14 and ST-11. Flag A1 exists, approval does not. Fix: Martin approves, or use "Steuerstrafrecht in Frankfurt".
N4 L, S05 heading "Anfahrt und Termin in Frankfurt" has no route. Fix: "Adresse und Termin" until the client sends the route.
OK: Untermainkai 26, 60329, phone, garage, Nr. 23 match nap.json. FAQ Steuerfahndung sentence matches the saved Hessen extract. Pauschale sentence matches kosten.txt.

## ST-42 Standort München: VERDICT FIX FIRST
Round 1: no. 1 P (year cut; "Fachanwältin für Steuerrecht" still in S02 answer block, S06, alt text; live profile only; rule 11 allows it with a flag; no Kammer proof). 2 C. 3 C (firm-level sentence). 4 C ("oft" gone). 5 P (still in hero, see N1). 6 C. 7 C. Top gaps: catchment P ("Altstadt" only, from Source of Truth tab 09 Z12); court/StA O; titles and photos O; schema O.
N1 L, hero: "In München sprechen Sie mit Lea Wimmer und Dr. Monika Glogger." This promises contact with Dr. Glogger (Source of Truth: 50 % Teilzeit, operative). Fix: name Wimmer only until the client confirms.
N2 L, FAQ "Wie kommen Sie zu unserem Büro am Oberanger?" repeats S05 and states the lines without the hedge. Fix: cut the FAQ item or add the hedge.
N3 L, titles for Wimmer and Glogger need written client proof before live (flag A2). Keep as a launch gate.
OK: Oberanger 32, 80331, phone, hours. § 387 Abs. 1, § 388 Abs. 1 match the saved text. Nine Steuerfahndungsstellen and the Finanzamt München link match the saved LfSt extract. Emergency numbers: no hours.

## ST-33 Aktuelles: VERDICT PASS (launch gate: teasers)
Round 1: no. 1 C (S03 "Vertraulich anfragen"). 2 C (flag A1 now lists all four risky teasers; the CMS list still shows them until the client retitles). 3 C ("Beiträge und Hinweise"). 4 O (/ratgeber/ is only a proposal, flag B1). Top gaps: depth P (98 words); links P; schema O.
N1 L, S02: "Erklärende Texte stehen im Ratgeber". It points to a page that may not exist. Fix: cut the sentence if ST-34 is not approved.
N2 L, no link to /steuerstrafrecht/ or a service. Fix: add one link in S01.
No new fact claims. Claims C01 to C04 cover the text.

## Rules, section 2 (all four pages)
1 C. 2 C. 3 C (Pauschale wording exact on ST-40, in own words on 41/42). 4 C. 5 C (three lines exact on 40/41/42, none on 33). 6 n/a (the statutes follow the saved text). 9 P: my recount incl. headings gives non-FAQ words 574 / 545 / 553 (limit 550). Run measure_plan.py to confirm. 10 C (overlap, see below). 11 P (N2 on ST-41). 12 C (one client placeholder, no internal notes in visible text). 13 P (N3). 14 C (all links are in slugs.json). Consent text: placeholder, correct.

## ST-41 and ST-42 overlap
5-word phrases in visible text, link targets removed: ST-41 vs ST-42 13.6 % / 14.0 %. ST-40 vs ST-42 14.2 %. ST-40 vs ST-41 12.4 %. Limit 25 %: PASS. Most shared phrases are the fixed address block and the services list. The two pages still use the same section order and parallel headings ("Anfahrt und Termin in X", "Wer Sie in X berät", "Sprechen wir vertraulich über Ihre Situation in X"). The legal content differs (Hessen vs Bayern). Acceptable, but template-like.

## Cross-page problems
1. Hoppe: ST-43 (lines 86, 102) and ST-44 (lines 43, 59) put him at both offices and give him the Frankfurt phone. ST-40/41/42 omit him. Pick one rule for all pages.
2. ST-43 line 43 keeps "Auf Wunsch schreiben Sie uns zuerst per E-Mail." ST-40 cut it (needs_client). Cut it on ST-43.
3. "Das Mandanteninteresse steht für uns immer im Vordergrund" is on ST-40 S08 and ST-43 line 39. Claim C17 on ST-42 says ST-40 only. Rule 10 says no repeated blocks.
4. Start page still says RVG; kosten.txt says no RVG (flags B4/B5/B6). Fix the start page before live.
5. Frankfurt address: GBP, anwalt.de and the live site still show Wiesenhüttenstraße 17. Do not publish ST-40/41 before Martin's go.
6. Schema: no per-office node, no ContactPage, no CollectionPage. The tool cannot do it. The main agent must change schema_tool.py.
7. Emergency numbers appear on ST-18, ST-19, ST-40, ST-42, ST-43 with no hours. Good. Keep it so until the client sends hours.
