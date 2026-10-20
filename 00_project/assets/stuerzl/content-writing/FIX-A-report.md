# FIX-A-report: Stürzl, correction round after REVIEW-A (ST-18, ST-12, ST-19, ST-29)

Date: 2026-10-11. Writer: fix agent A. Scope: the four page folders only. No upload, no CMS, no email. Source rules: `content-writing-stuerzl-fixes.md`, `REVIEW-A.md`, `content-writing-stuerzl-batch.md`.
Page text is German. This report is in STE.

## Result in one table

| ID | Words now (before) | Seller layer (limit 550) | Links in text (3 to 8) | G1 to G6 | Lint G5 | Cleanse calls | Claims | Placeholders left | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-18 | 1800 (1616) | 544 | 7 | pass | 5/5 | 1 try, failed (codex usage limit) | 38 | 1 (Rechtsschutz) | fixed, approval open |
| ST-12 | 1784 (1515) | 530 | 8 | pass | 5/5 | 1 try, failed | 43 | 1 (Rechtsschutz) | fixed, approval open |
| ST-19 | 1560 (1231) | 522 | 6 | pass | 5/5 | 1 try, failed | 30 | 1 (Schulung format, duration, billing) | fixed, approval open |
| ST-29 | 1681 (1336) | 500 | 8 | pass | 5/5 | 1 try, failed | 36 | 1 (Rechtsschutz) | fixed, approval open |

Gates: `run_gates.py <folder> --page 05-final/page.md` passes for all four. `schema_tool.py check` passes. `diff_claims.py trace` passes. Highest 5-word overlap with any other written page: 19 % (limit 25 %), measured on a copy of all 30 pages in the scratch folder (`link_network.py` would write `LINK-NETWORK.md` in the shared folder, so I did not run it there). DataForSEO cost: 0 USD. Backup of each old text: `05-final/page-vorreview.md`. New draft: `03-draft/draft-v2.md` (ST-29: `draft-v3.md`).

**Cleanse did not run.** Each cleanse call stopped at once: "You've hit your usage limit ... try again at 5:20 PM" (see `03-draft/cleanse-notes-fix.txt`). No cleansed text exists. The G5 lint is 5/5. The skill rule says G5 is not complete without the rival model. The lead agent can run one cleanse per page after 17:20 and must check `diff_claims.py diff`.

## ST-18 Steuerfahndung und Durchsuchung

| Review point | Status |
| --- | --- |
| 1. § 105 Abs. 1 StPO without "und ihre Ermittlungspersonen" | Fixed. S04 step 1, S02 and FAQ name the Ermittlungspersonen. S02 and FAQ add § 404 Abs. 1 Satz 2 AO (Steuerfahndung officers). |
| 2. H1 and meta promise presence ("für die erste Stunde", "wie wir Sie begleiten") | Fixed. H1 "Anwalt bei Steuerfahndung und Durchsuchung". Meta "wie wir Sie beraten". Hero, step 2, FAQ 1 and the claim list say the same line: first advice by phone, then the firm clarifies if presence on site is possible. |
| 3. "Hierfür ist es nie zu spät" | Cut. "Wir unterstützen Sie auch bei bereits laufenden Verfahren" stays. |
| 4. § 371 Abs. 2 misquoted ("Wirkung", "bei dieser Tat") | Fixed. Text follows the saved statute (unverjährte Taten, vor Berichtigung, Ergänzung oder Nachholung, Amtsträger zur Ermittlung). The page writes "Strafbefreiung" like approved ST-14, not "Straffreiheit" (forbidden word). **Open for Martin** (flag A4). |
| 5. § 386 Abs. 2 incomplete | Fixed with saved texts: limits § 399 Abs. 1 and §§ 400, 401, Nr. 2, Abs. 3 (Haftbefehl or Unterbringungsbefehl), Abs. 4. New: § 399 Abs. 1 AO replaces the picture "Staatsanwaltschaft des Finanzamts". |
| 6. § 107 "auf Verlangen"; "kein Schuldeingeständnis" without source | "auf Verlangen" fixed (also for the Bescheinigung). The Schuldeingeständnis sentence is cut in block 4 and in the FAQ. No statute text exists. Open for the firm: a court source can bring it back (flag A3). |
| Gap: local 45 | Address block with both offices and the hours line in S09 (exact text of fixes file point 5). Old "Frankfurt ohne Straße" note removed from the TECH block and from flags. |
| Gap: "Hausdurchsuchung", "steuerfahndung anwalt", München, Hessen | "Hausdurchsuchung" in S03 and FAQ 2. "Anwalt bei der Steuerfahndung" in FAQ 4 (new). München is in the address block. "Hessen" is not used: no backed local fact (flag C4). |
| Gap: pillar link, Person and Service schema | Link to /steuerstrafrecht/ added. Person and Service nodes added by `_work/add-schema.py` after `run_gates.py` (the skill script cannot make them). |
| Cross-page: witness rules | FAQ 5 now gives § 163 Abs. 3 Satz 1 StPO, § 55 Abs. 1 StPO and links to ST-29. |
| Cross-page: cost softeners, S03 and S09 lines | Cost block in own words with "grundsätzlich" and "üblicherweise". Erstberatung amount placeholder removed. S02 "Rufen Sie uns an, bevor Sie sich äußern" removed. "Vernichten oder verändern Sie nichts" removed (no statute, flag A2). |

## ST-12 Verteidigung im Steuerstrafverfahren

| Review point | Status |
| --- | --- |
| 1. "Hierfür ist es nie zu spät" next to the Strafbefehl | Cut. New: "Gegen einen Strafbefehl läuft eine Einspruchsfrist von zwei Wochen nach Zustellung (§ 410 Abs. 1 StPO). Melden Sie sich in diesem Fall früh bei uns." |
| 2. "viele Verfahren enden schon dort" (S02 and FAQ) | Cut in both places (flag A1). |
| 3. "gelten Sie nicht als vorbestraft" without BZRG | Fixed with saved §§ 3, 4 BZRG: register entries need a court decision that "auf Strafe erkannt" (§ 4 Nr. 1). The page adds "Eine Einstellung ist keine solche Entscheidung". That last sentence is our own conclusion from the statute. **Open: the firm confirms** (flag A2). |
| 4. § 153a conditions missing | Fixed. Both conditions added (geeignet, öffentliches Interesse zu beseitigen; Schwere der Schuld steht nicht entgegen). |
| 5. § 371 FAQ rewritten | Fixed with the statute words of Nr. 1 Buchst. b ("dem an der Tat Beteiligten oder seinem Vertreter", unverjährte Taten). "Strafbefreiung" as on ST-18 (flag A8). |
| 6. "Das Gesetz nennt keine feste Dauer"; "Leichtfertige Fehler" | First cut. The duration answer now rests on `kosten.txt` (client source: duration is a circumstance the firm cannot influence directly). Second now uses § 378 Abs. 1 and 2 AO words. |
| Also: FAQ "Geständnis" | Rebuilt on § 153a text. The statute has no word "Geständnis" (checked in the saved text). |
| Also: FAQ Steuerberater | Question made general, answer from the live FAQ, the "mit strafbar" fear sentence cut (flag A6). |
| Gap: Strafbefehl and Verjährung lines, links | New block "Verjährung" with § 78 Abs. 3 Nr. 4 StGB (5 years), § 376 Abs. 1 AO (15 years for § 370 Abs. 3 Satz 2 Nr. 1 to 6), § 376 Abs. 3 AO (2.5 times). Link to /ratgeber/verjaehrung/. Links to /verteidigung-von-individualpersonen/ and /steuerstrafrecht/durchsuchungsbegleitung-schulung/ added. Link to /ratgeber/steuerhinterziehung-strafe/ dropped to stay at 8 links. |
| Gap: address block, schema | Address block in S09. Person and Service by `_work/add-schema.py`. |
| Cross-page: "Staatsanwaltschaft des Finanzamts", § 386 Abs. 3, cost, S09 line | Picture cut and § 399 Abs. 1 AO used. § 386 limits and Abs. 3 complete. Cost block with softeners, own words. "Wir melden uns per Telefon oder E-Mail" cut. FAQ question "Welche Strafen drohen" became "Welche Strafen sieht das Gesetz ... vor". |

## ST-19 Durchsuchungsbegleitung und Schulung

| Review point | Status |
| --- | --- |
| 1. Hero and title promise "Begleitung"; FAQ says "klären wir im Telefonat" | Fixed. Hero: "Im Ernstfall sind wir Ihr Notfallkontakt am Telefon. Dort beraten wir Sie zuerst ... und klären danach, ob wir vor Ort dabei sein können." H1 "Schulung und Notfallkontakt für den Ernstfall". Title "Durchsuchung im Unternehmen: Schulung & Notfall | STÜRZL" (60-character limit). Meta says "wer im Ernstfall am Telefon berät". Step 4 and FAQ say the same line. |
| 2. Witness answer only § 161a | Fixed. § 163 Abs. 3 Satz 1 StPO fetched, saved and used in block 4 and the FAQ (witnesses before Ermittlungspersonen, incl. Steuerfahndung, only with a Staatsanwaltschaft order). |
| 3. § 68b exclusion missing | Fixed. Full text of Satz 2 and 3 in block 4. |
| 4. "Zeugenstatus bewusst halten ... muss man aussagen" | Cut. The two rights are written plainly (§ 136 for Beschuldigte, §§ 55, 68b for Zeugen). |
| 5. No link to /verteidigung-von-individualpersonen/ | Added in block 4. |
| Gap (a) staff behaviour list | New block "Verhalten bei einer Durchsuchung im Unternehmen: Was das Gesetz regelt" (§§ 94, 98 Abs. 2, 105, 106, 107, 136). Framed as general information "im Einzelfall". |
| Gap (b) H3 keywords | H3 "Verhalten bei einer Durchsuchung im Unternehmen ..." and "Durchsuchung der Geschäftsräume ...". "Durchsuchungsbeschluss" added. |
| Gap (c) address block, Person and Service | Done (same method as ST-18). |
| Cross-page | Cost block in own words, Erstberatung amount placeholder removed. S09 "Wir melden uns per Telefon oder E-Mail" cut. |

## ST-29 Verteidigung von Privatpersonen

| Review point | Status |
| --- | --- |
| 1. § 164 Abs. 1 StGB without "wider besseres Wissen" and Absicht | Fixed. Block and FAQ quote the statute (wider besseres Wissen, Absicht, Verfahren herbeizuführen oder fortdauern zu lassen). "Doch Vorsicht" and the fear line are gone. |
| 2. "Hierfür ist es nie zu spät" next to the 2-week deadline | Cut. S03 now states the 2-week periods (§ 410 Abs. 1 StPO, § 67 Abs. 1 OWiG). |
| 3. § 378 and § 130 OWiG words | Fixed. § 378 Abs. 1 and § 130 Abs. 1 Satz 1 OWiG in statute words, with the condition of a Zuwiderhandlung that proper supervision would have stopped or made much harder. Link to /ordnungswidrigkeiten/. |
| 4. § 68b exclusion; § 52 list; "In einfachen Sachen" | All three added. § 52 Abs. 1 now names Verlobter, Ehegatte, Lebenspartner and the Nr. 3 relatives. |
| 5. "oft" and "Antragsdelikte" | "oft" sentence cut. § 152 Abs. 2 quoted with "soweit nicht gesetzlich ein anderes bestimmt ist". |
| 6. "hartnäckig", "schnell beenden ... Kompromiss", "egal wie lange", "Strafverteidiger" | Cut or replaced: "Wir vertreten Ihre Interessen", "was Sie erreichen möchten und welche Wege das Verfahren bietet". H1 "Verteidigung im Steuerstrafrecht für Privatpersonen". Title "Verteidigung im Steuerstrafrecht: Privatpersonen | STÜRZL". Brief keyword changed to "verteidigung im steuerstrafrecht" (no volume data). |
| Gap (a) "Vorladung als Zeuge", "Beschuldigtenvernehmung" | New H3 words in blocks 1 and 2. New facts: § 163a Abs. 3 Satz 1 StPO (Ladung vor der Staatsanwaltschaft), § 163 Abs. 3 StPO. |
| Gap (b) Vermögensarrest | Expanded with § 111e Abs. 1 Satz 2, Abs. 2 and Abs. 4 StPO. |
| Gap (c) address block, link to ST-19 | Done. |
| Also: FAQ "Ja" to reader questions (fix point 7) | Questions made general ("Können Zeugen einen Anwalt mitbringen?", "Was gilt, wenn jemand eine Strafanzeige stellt?"). |

## Decisions for Martin or the firm

1. "Strafbefreiung" (our word, as on ST-14) or the statute word "Straffreiheit" in the negative § 371 Abs. 2 sentences (ST-18 and ST-12). Flag A4 and A8.
2. ST-12: the sentence "Eine Einstellung ist keine solche Entscheidung" (BZRG) is our conclusion. The firm confirms or we cut it.
3. ST-18: the "kein Schuldeingeständnis" sentence is cut. The firm can name a court source.
4. ST-29: new primary keyword has no volume data. "Strafverteidiger" is out of H1 and title.
5. The phone-first line for presence on site (ST-18 and ST-19) needs one confirmation from the firm.

## Notes for the skill and the lead agent

- `schema_tool.py` has no Service node and no Person for service pages. I added both with `_work/add-schema.py` in each folder. Run it after each `run_gates.py`, because the gate run rebuilds `schema.jsonld`.
- Codex usage limit blocks G5 for the whole client until 17:20.
- `brief.word_range` raised for ST-19 (1600) and ST-29 (1750). Reason is in each `brief.json` (`fix_note_2026-10-11`).
- Not run by me: reviewer agents, `link_network.py` in the shared folder, any upload.
- Files outside my four folders: only this report. The scratch folder holds my helper scripts.
