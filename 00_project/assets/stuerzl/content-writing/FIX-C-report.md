# FIX-C report: ST-21, ST-26, ST-20, ST-23 (fix round after REVIEW-C, 2026-10-11)

Status words: "behoben" = fixed in the text. "belegt" = new source saved in `_work/` and added to `claims.json`. "bewusst offen" = left for a decision by Martin or the firm, with the reason in `OPEN-FLAGS.md`.

## Summary

| Page | Words before | Words now | Seller layer now (550 max) | Gates G1 to G6 | Cleanse calls in this round |
| --- | --- | --- | --- | --- | --- |
| ST-21 Unternehmensvertretung | 1520 | 1520 | 527 (538 with Markdown marks) | pass | 1 (taken) |
| ST-26 Compliance | 1474 | 1593 | 507 (517) | pass | 1 (2 of 3 changes taken) |
| ST-20 Wirtschaftsstrafrecht | 1361 | 1453 | 528 (537) | pass | 1 (1 of 2 changes taken) |
| ST-23 Ordnungswidrigkeiten | 1434 | 2148 | 527 (542) | pass | 1 (no change by the model) |

Backups: `05-final/page-vorreview.md` in each folder. New drafts: `03-draft/draft-v3.md` (before cleanse) and `draft-v4.md` (final). Cleanse files: `cleansed-r2.md`, `cleanse-notes-r2.txt`. `diff_claims.py diff` passed for each taken cleanse. G3 shows one warning only on ST-23: 2148 words is over the target range of 900 to 1600. The page carries the full wording of § 30 and § 130 OWiG for the whole site. The seller layer stays under 550 words by both counting methods.

## Wording rule for § 130 OWiG and § 30 OWiG (owned by ST-23)

- Source texts saved in `st-23.../_work/law/`: `owig_1968__130`, `__30`, `__9`, `__17`, `__31`, `__33` (new: § 9 and § 33). Copies of § 9 are in the other three folders.
- ST-23 S07 block 3 (§ 30) and block 4 (§ 130) hold the near-literal version: Inhaber, duties that bind the Inhaber, penalty or fine, "durch gehörige Aufsicht verhindert oder wesentlich erschwert worden wäre", Satz 2 on Aufsichtspersonen, § 130 Abs. 3 with the tenfold rule, § 30 Abs. 1 to 4, and § 9 Abs. 1 OWiG as literal text. The page does not say that a Geschäftsführer is an Inhaber.
- The same § 130 Abs. 1 sentence stands word for word on ST-23, ST-21 (FAQ) and ST-26 (S07 block 2). The same § 30 Abs. 1 sentence stands on ST-23 and ST-21. ST-26 and ST-20 link to /ordnungswidrigkeiten/ for § 30. ST-20 does not name § 130 and links to the page. A script check confirmed the equal sentences.
- The sentence "Ausreichende Compliance-Maßnahmen können helfen, Leitungspersonen zu schützen" is cut.

## ST-23 Ordnungswidrigkeiten

| Point of the review | Result |
| --- | --- |
| 1 § 130 conditions missing | behoben (full wording, Satz 2, Abs. 3), belegt (O19, O20) |
| 2 "Compliance ... schützen" without statute | behoben (sentence cut, replaced by "hängt vom Sachverhalt ab"); flag A3 closed |
| 3 FAQ "Ja" for the reader's company, only 10 and 5 million | behoben ("Das ist möglich, wenn ...", OWi maximum, tenfold rule); belegt (O21, O22) |
| 4 Steuerberater example | behoben (live FAQ sentence restored with "im Einzelfall"; examples now name the three acts of § 370 Abs. 1 AO); belegt (O26); flag A9 |
| 5 Verjährung only § 384 AO | behoben (scope in the question, § 377 Abs. 2 AO, § 31 Abs. 3 and § 33 OWiG); belegt (O25) |
| 6 "Auf der Kanzleiseite" | behoben ("Auf der Startseite") |
| 7 § 378 Abs. 3 written as a duty | behoben (Satz 1 to 3 as conditions, "gegenüber der Finanzbehörde", § 371 Abs. 4 AO named); belegt (O24); flag A11 |
| 8 court representation without claim | belegt (K15, live pages) and worded as "gegenüber der Finanzbehörde und, soweit nötig, den Gerichten" |
| 9 pillar and other links missing | behoben (ST-20, ST-11, ST-36, ST-18 added; 8 links; ST-21 link dropped for the 8-link limit). ST-24 not linked: no slug in `slugs.json` (flag B5) |
| 10 seller layer 566 words | behoben (527) |
| NAP, cost text, boilerplate | behoben (three address lines, standard cost text in own words, S03 and S09 reworded, hero "droht" replaced) |
| Term "Aufsichtspflichtverletzung" | behoben (H3 "Verletzung der Aufsichtspflicht (§ 130 OWiG)", the statute's own heading; "Organisationsverschulden" with live source O27) |
| "leichtfertig" definition with source | bewusst offen (no case law saved; the page states that the law does not define it; flag A10) |

## ST-21 Unternehmensvertretung

| Point of the review | Result |
| --- | --- |
| 1 § 146 StPO Satz 2 missing | behoben (both sentences in S07 and FAQ); belegt (U05) |
| 2 "Leitung" instead of "Inhaber", duty condition | behoben (FAQ carries the canonical § 130 sentence; heading says Inhaber); flag A10 |
| 3 § 30 Abs. 2 Satz 3 and Abs. 4 | behoben (exact § 30 Abs. 1 sentence; tenfold rule, maxima and Abs. 4 by link to ST-23 plus Abs. 5 kept) |
| 4 co-authors | behoben ("gemeinsam mit Co-Autoren", no names; flag A11) |
| 5 "Auf der Kanzleiseite" | behoben ("Auf der Startseite") |
| 6 Übernahme von Geldbußen | behoben (cut); bewusst offen: flag A5 (firm must explain) |
| 7 § 164 StGB conditions | behoben (Behörde, wider besseres Wissen, Absicht, Verfahren herbeizuführen); belegt (U13) |
| 8 Zeuge/Beschuldigter client sentences | behoben (softened to "im Einzelfall"; two client sentences not adopted); flag A9 |
| 9 H1 "Unternehmensstrafrecht" vs. text | bewusst offen (decision by Martin, flag A1) |
| 10 seller layer 606 words | behoben (527) |
| 11 internal notes in placeholders | behoben (both placeholders cut from visible text; `placeholders.md` lists none) |
| Gaps (a) NAP, (b) Zeugenbeistand and Sockelverteidigung, (c) direct answer | behoben (three address lines; H3 "Mitarbeiter als Zeugen und Zeugenbeistand", Sockelverteidigung defined in one sentence; FAQ starts with the answer) |
| Fixes list: link to ST-19 | behoben (/steuerstrafrecht/durchsuchungsbegleitung-schulung/); ST-13 link dropped for the 8-link limit |
| Schema vs. TECH note | behoben (TECH note matches `schema_tool` output) |
| Sub-pages ST-22 | not linked: no slug in `slugs.json` (flag B4) |

## ST-26 Compliance

| Point of the review | Result |
| --- | --- |
| A1 "rechtssicher" | behoben ("rechtlich geprüft", step 3 reworded, no "rechtssicher" left) |
| A2 garbled § 130 sentence | behoben (canonical sentence) |
| A3 "Leitung" in § 130 | behoben (Inhaber; FAQ "Wer haftet" reworded) |
| A4 one million only | behoben (§ 30 Abs. 2 Satz 3 and the fine rule for fine-backed duties named); belegt (G02) |
| A5 § 17 HinSchG | behoben ("nach der Bestätigung des Eingangs", Abs. 1 and 2); belegt (G06) |
| A6 Gutachten sentence | belegt (G21: approved-copy.md card 06 and live ST-13) and worded as "bewerten wir ... in einem Gutachten" |
| A7 unsourced sentences | behoben (personal-liability sentence replaced by "nur natürliche Personen können sich strafbar machen", G23; definition of Verstoß derived and recorded, G22) |
| A8 process steps 2 and 3 | behoben (use the client words: Überprüfung, Aufbau und Optimierung, Richtlinien, Hinweisgeberschutz, Schulungen; G25) |
| A9 /leistungen/ not linked | behoben (plus ST-20 pillar; ST-14 link dropped for the 8-link limit) |
| A10 seller layer 590 words | behoben (507) |
| B client text restored | behoben where the meaning was lost, see below |
| Gaps (a) NAP, (b) H3 terms, (c) links | behoben (three address lines; H3 "Hinweisgebersystem und interne Meldestelle", "Compliance-Schulung"; FAQ on the Rechtsanwalt role; links added) |

Part B (compare with `compliance.txt`):
- Restored: "zentrales Steuerungsinstrument moderner Unternehmensführung" (S02); "Unabhängig von Größe und Struktur ... essenziell" (S07 block 1); effect of structures on (straf-)rechtliche Risiken, Reputation, Vertrauen and Stabilität ("dienen der Begrenzung", "können stärken"); "kein nice-to-have, nie nur Prävention, Bestandteil einer Verteidigungsstrategie"; "Aufgrund unserer langjährigen Erfahrung ... kennen wir die praktischen Herausforderungen" (S03); the full bullet on aufsichts- und organisationsrechtliche Pflichten; "Unterstützung bei der Umsetzung komplexer regulatorischer Vorgaben"; "in allen Phasen ... bis zur Verteidigung im Ermittlungs- und Gerichtsverfahren"; the goal "Risiken frühzeitig zu erkennen und zu kontrollieren" (S09).
- Kept out on purpose (result words, flag A2/A6): "schützen" as a result, "sichern", "maßgeblich", "vermeiden", "Haftung zu vermeiden", "Handlungsspielraum sichern", "rechtssicher", "ganzheitlich", "integral", "effektiv". The Leitlinie says "entfaltet ihre Wirkung" instead of "ihren Schutz".
- Sentence "Steuerliche Pflichten gehören ..." cut for length.

## ST-20 Wirtschaftsstrafrecht

| Point of the review | Result |
| --- | --- |
| 1 Subventionsbetrug ceiling | behoben (Abs. 1, Abs. 2 ten years, Abs. 5); belegt (W05) |
| 2 Untreue ceiling | behoben (Abs. 1 plus Abs. 2 with § 263 Abs. 3); FAQ asks "Welche Strafe sieht das Gesetz ... vor?"; belegt (W02) |
| 3 § 15a InsO "ohne schuldhaftes Zögern", "spätestens" | behoben in S07 and FAQ; belegt (W06) |
| 4 § 14 StGB wording | behoben (statute wording; invented "Pflichten des Unternehmens" cut); belegt (W04) |
| 5 co-author | behoben ("gemeinsam mit einer Co-Autorin"; flag A10) |
| 6 Dr. Glogger practice-area list | behoben (cut; same confirmed block as ST-21 and ST-26; flag A8) |
| 7 "Kern" undefined | behoben (the delikt list of the live page replaces "Kern"; W10); flag A1 stays for Martin |
| 8 definition without source | behoben ("Zum Wirtschaftsstrafrecht zählen häufig ..."; W17) |
| 9 § 74c GVG "soweit" | behoben (S02, S07, FAQ) |
| 10 Bankrott conditions | behoben (Überschuldung or Zahlungsunfähigkeit, listed acts, Abs. 6); belegt (W07) |
| 11 seller layer 588 words | behoben (528) |
| Gaps (a) NAP, (b) "Insolvenzverschleppung", (c) LL.M. teaching post | behoben (address lines; H3 and FAQ; Dozentin LL.M. Köln added with W13; term source W18, flag A11) |
| § 130 and § 30 | link only (ST-20 does not use them) |

## Cross-page points of the review

| Point | Result |
| --- | --- |
| 1, 2 one § 130 and § 30 wording, ceilings | behoben (see wording rule) |
| 3 quote source | behoben on all four pages ("Auf der Startseite") |
| 4 co-authors | behoben: one rule, no names; flagged for Martin on each page |
| 5 boilerplate | behoben in own words per page (S03 closing, cost block, confidentiality and cost FAQ, S09). "Fehler passieren" stays only on ST-23. "möglichst geräuschlos" stays only on ST-21. The three address lines are equal by order of the fixes file (Nr. 5). The link tool shows no pair over 25 percent |
| 6 "Pauschale" two meanings | behoben (ST-26: "Pauschalvergütung" for a Gutachten, "Pauschale" only for the Erstberatung) |
| 7 Tax Compliance overlap with ST-13 | bewusst offen (client decision, placeholder 1 on ST-26) |
| 8 Dr. Glogger blocks | behoben (one block) |
| 9 ST-22 and ST-24 not linked | not linked: both have an empty slug in `slugs.json`. ST-21 flag B4 and ST-23 flag B5 say where to add the links |
| 10 schema vs. TECH note | behoben on ST-21 (TECH note now matches); the other pages already matched |
| 11 seller layer | behoben on all four |
| 12 internal notes in placeholders | behoben (ST-21, ST-23, ST-20: no placeholder in the text; ST-26: one clean fact placeholder) |
| 13 grey-zone flags | open for Martin: "Anwalt für Wirtschaftsstrafrecht" (ST-20 A1), "Unternehmensstrafrecht" (ST-21 A1), "langjährige Erfahrung" (A-flags), "möglichst geräuschlos" (ST-21 A3) |

## Other notes

- Fixes file Nr. 10 says no equal Telefonsatz. Nr. 5 says "genau diese drei Zeilen". I followed Nr. 5 for the address block (equal on all four pages) and used own words everywhere else.
- Cost block: the RVG sentence, the Vorschuss and the Vier-Augen sentences are gone from the visible text to keep to the standard text of the fixes file. They stay in `claims.json` (K05) as supported facts.
- Outside my scope by accident: I ran `link_network.py` once on the shared folder. This rewrote `content-writing/LINK-NETWORK.md` with the state of that minute. Run the tool again after all fix agents finish. All later runs used a copy in the scratchpad.
- New law files in `_work/law/`: ST-23 has `owig_1968__9`, `owig_1968__33`; ST-21, ST-26, ST-20 have `owig_1968__9`. Live text of the OWi page: `st-23.../_work/live/ordnungswidrigkeiten.txt`.
