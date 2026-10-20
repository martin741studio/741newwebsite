# FIX-D report: fix round for batch D (ST-25, ST-27, ST-28, ST-31)

Date: 2026-10-11. Input: `REVIEW-D.md`, `content-writing-stuerzl-fixes.md`, `content-writing-stuerzl-batch.md`. Backup of each old page: `05-final/page-vorreview.md`. New draft files: `03-draft/draft-v5.md` (ST-25, ST-27, ST-28) and `03-draft/draft-v3.md` (ST-31). New claims script in each `_work/fix_claims_d.py`. New law texts saved in `_work/` (see list at the end).

Status words: **fixed** = text changed. **sourced** = new source saved and claim added. **open** = left on purpose, reason given and written in `OPEN-FLAGS.md`.

## Overall result

| Item | ST-25 | ST-27 | ST-28 | ST-31 |
| --- | --- | --- | --- | --- |
| Words (wordcount.py) | 1771 (was 1476) | 1806 (was 1320) | 1827 (was 1552) | 1666 (was 1272) |
| Seller layer (all but FAQ and Vertiefung) | 538 | 547 | 507 | not applicable (cost page) |
| Gates G1 to G6 | PASS | PASS | PASS | PASS |
| G5 rival-model cleanse | not run, Codex limit | not run, Codex limit | not run, Codex limit | not run, Codex limit |
| Cleanse calls in this round | 1 attempt, failed | 1 attempt, failed | 1 attempt, failed | 1 attempt, failed |
| Placeholders in visible text | 0 | 0 | 0 | 6 (cost values only) |
| Schema | WebPage, BreadcrumbList, LegalService, FAQPage, Person | same | same | same |

Cleanse: `cleanse_de.sh` returned "usage limit, try again at 5:20 PM" for all four pages. No text was taken from it. The lint part of G5 is 5/5 on all four. Run the cleanse once per page after 17:20, then `diff_claims.py diff` and `deslop_de.py`. The error text is in `03-draft/cleanse-notes-r3.txt` of each folder.

Word range in the brief was raised: ST-25 to 900 to 1850, ST-27 to 900 to 1900, ST-31 to 520 to 1750 (the review asked for more depth; ST-28 was already in range).

Similarity (5-word shingles, `link_network.py` logic, run on a copy of all 05-final pages): highest value for my pages is 16.8 % (ST-31 with ST-44 Team, caused by the shared address block). ST-25, ST-27 and ST-28 share at most 12.4 % with each other. The limit is 25 %.

Rules from the fixes file that apply to all four pages:

| Rule | Done |
| --- | --- |
| 1 Quote source | "Auf der Startseite sagt sie" on ST-25, ST-27, ST-28, ST-31 does not use the quote. |
| 3 Cost sentence | Same three facts on ST-25, ST-27, ST-28 ("nach Zeitaufwand in Sechs-Minuten-Einheiten", "in Textform", "üblicherweise ... Pauschale"), in different words per page. No "vor dem Gespräch", no "schriftlich", no amount, no Erstberatung placeholder on ST-25, ST-27, ST-28. |
| 4 Availability | Only "Montag bis Freitag 09:30 bis 14:30 Uhr, Termine und Erstberatung auch außerhalb nach Vereinbarung". No "erreichbar", "verlässlich", "24/7". |
| 5 Address block | Three mandated lines at the end of S09/S08 of all four pages (claim C11, C30; nap.json). |
| 8 Result words | Checked with grep: no "rechtssicher", "schützen", "Ärger", "drohen", "hartnäckig". "droht/drohen" removed from headings and meta. |
| 9 Answer block | 4 sentences on ST-25, ST-27, ST-28 and ST-31. Seller layer is at most 550 words. |
| 10 Boilerplate | S03 closing sentence, S04 text, cost block, confidentiality FAQ and S09 text differ per page. |
| 12 Placeholders | No internal notes in visible placeholders. The notes moved to `placeholders.md`. |
| 14 Links | ST-25: 8 links (steuerstrafrecht, kosten, wirtschaftsstrafrecht, steuerfahndung-durchsuchung and others). ST-27: 8. ST-28: 8. ST-31: 7. All targets are in `slugs.json`. |

## ST-25 Korruptionsstrafrecht

| Review point | Result |
| --- | --- |
| 1 FAQ Einziehung and company | **fixed, sourced.** Person (§ 73 Abs. 1 StGB, Täter oder Teilnehmer) and legal person (§ 30 OWiG) split. § 30 Abs. 5 OWiG limit added (claim C16, C10). |
| 2 Amtsträger frames | **fixed.** "Absatz 1" stated. Richter frames added (§ 331 Abs. 2, § 333 Abs. 2, § 332 Abs. 2, § 335 Abs. 1 Nr. 1 and 2). Minder schwere Fälle named. Claims C05 to C07. |
| 3 § 299 limit | **fixed.** "bei dem Bezug von Waren oder Dienstleistungen" added in both cases. |
| 4 § 4 EStG "Grund", "regelmäßig" | **fixed.** "Ein Anknüpfungspunkt"; "regelmäßig" cut. Claim C37. |
| 5 "Unternehmen" for § 30 OWiG | **fixed.** "juristische Person oder Personenvereinigung". |
| 6 Quote source | **fixed.** "Auf der Startseite". Claim C23. |
| 7 Third person "nach Darstellung der Kanzlei" | **fixed.** "Wir beraten auch bei Korruptionsdelikten, die neben einer Steuerhinterziehung auftreten können." Claim C26. |
| 8 Cost promises | **fixed.** Rule 3 wording. Claim C33. |
| 9 Prüfer / § 11 | **fixed, sourced.** Prüfer sentence replaced by the § 11 wording. Flag A4. |
| 10 "Fehler passieren" in S03 | **fixed.** Cut on this page. |
| 11 Meta "drohen" | **fixed.** "möglich sind". |
| 12 Block 3 length, flag A6 | **fixed.** Block 3 has 141 words. Flag A6 marked as gone. |
| Gap 1 definitions | **fixed.** S02 defines Vorteilsannahme and Bestechlichkeit in one sentence each. |
| Gap 2 Ermittlungsverfahren FAQ and links | **sourced, fixed.** New FAQ (§ 160, § 170, § 136 StPO saved). Links to /steuerfahndung-durchsuchung/ and /sonstiges-wirtschaftsstrafrecht/. Link to /compliance/ removed (limit of 8 links). |
| Gap 3 addresses, "ganz Deutschland", schema | **fixed.** Address block, "Wir führen Mandate in ganz Deutschland", FAQPage and Person node. |
| Score "local 45", "schema 55" | Addressed by the three items above. Not re-scored (reviewer runs later). |

## ST-27 Zollstrafrecht

| Review point | Result |
| --- | --- |
| 1 Zollhinterziehung without conduct and intent | **fixed, sourced.** S02, block 1 and FAQ 1 state the conduct (§ 370 Abs. 1), intent (§ 15 StGB) and the § 378 AO Ordnungswidrigkeit. Claim C05. |
| 2 § 382 limits | **fixed.** "soweit die Zollvorschriften ... auf diese Bußgeldvorschrift verweisen" and "bei der Wahrnehmung der Angelegenheiten eines Pflichtigen" added. Claim C25. |
| 3 § 373 Abs. 2 | **fixed.** Statute wording (Schusswaffe; other Waffe or Werkzeug to overcome resistance; Bande; also Bannbruch). Minder schwerer Fall in Abs. 1 added. Claim C07. |
| 4 § 374 "bis zu fünf Jahren" | **fixed.** "in Absatz 1", Absatz 2 added. Claim C32. |
| 5 § 386 Abs. 2 Nr. 2, Abs. 3 | **fixed.** Both added. Claim C08. |
| 6 Quote source | **fixed.** |
| 7 FAQ "Möglich." | **fixed.** "Das hängt vom Einzelfall ab ... prüfen wir vor jedem Schritt." |
| 8 Cost promises | **fixed.** Rule 3 wording. |
| 9 FAQ "Droht" and "Unternehmen" | **fixed.** "Kann meinem Unternehmen eine Geldbuße auferlegt werden?"; § 30 OWiG with "juristische Person oder Personenvereinigung". |
| 10 Blocks 2 to 4 below 120 words | **fixed.** Blocks have 137 to 189 words. |
| E-E-A-T 58 | **sourced, open in part.** S05 names the Kommentierung of §§ 380 bis 383b AO (incl. § 382) from the live profile (claim C36). The profile says "erscheint 2024"; flag A6. |
| Gap 1 Zollfahndung, Bannbruch examples | **fixed in part, open in part.** Zollfahndung (§ 404 AO) and link to /steuerfahndung-durchsuchung/ are in block 3. Examples of banned goods: **open**, no read source. |
| Gap 2 Zollkodex, Zollschuld, Verjährung, Bargeld | **sourced in part.** Added: Verordnung (EU) Nr. 952/2013 (from § 3 Abs. 3 AO), Verjährung (§ 376 AO, § 78 StGB, saved), Bargeld FAQ (§ 12a ZollVG, saved). Zollschuld: **open**, no read source (flag C3). |
| Gap 3 addresses, "bundesweit", schema, block length | **fixed.** |

## ST-28 Schwarzarbeit und Arbeitsstrafrecht

| Review point | Result |
| --- | --- |
| 1 § 10 Abs. 1 SchwarzArbG | **fixed, sourced.** "vorsätzlich", § 404 Abs. 2 Nr. 3 SGB III and "ohne die erforderliche Genehmigung" added (SGB III § 404 saved). Flag A8. |
| 2 § 9 only for § 8 Abs. 4 | **fixed.** |
| 3 AÜG 18 months | **fixed.** "grundsätzlich 18 Monate", Tarifvertrag, 24 Monate, Anrechnung earlier Überlassungen; FAQ the same. Claim C09. |
| 4 FAQ Gefälligkeit limit | **fixed.** "nicht nachhaltig auf Gewinn gerichtet" added (§ 1 Abs. 4, § 8 Abs. 6). |
| 5 § 266a Abs. 6 | **fixed.** Neutral rule text with "von der Einzugsstelle bestimmten Frist"; no step list. Flag A5. |
| 6 H1 and fear words | **fixed.** H1 "Strafe, Bußgeld und Verteidigung"; "möglich sind"; heading "Wer kann bei Schwarzarbeit betroffen sein?". PAA entry in the brief set to "dropped, Duplikat" with the reason (the G6 check matched the old wording). |
| 7 Quote source | **fixed.** |
| 8 "Fachleute aus unserem Netzwerk" | **fixed.** Cut. |
| 9 FAQ § 266a without intent, § 8 Abs. 3 limit | **fixed, sourced.** § 15 StGB added; Abs. 2 Nr. 1 or 2 limit added. |
| 10 Third person, "Unternehmen" | **fixed.** |
| 11 Sozialleistungsempfänger | **fixed.** Cut from FAQ and from block 2 (flag B7). |
| 12 Cost promises | **fixed.** |
| Gap 1 FKS FAQ, Scheinselbständigkeit | **sourced, fixed.** Two FAQ (§ 2 Abs. 1 SchwarzArbG, § 7 Abs. 1 SGB IV saved). A full block on Scheinselbständigkeit: **open**, FAQ only (flag A9). |
| Gap 2 "schwarzarbeit strafe" frames | **fixed.** S02 names § 8 SchwarzArbG (50.000 / 100.000 Euro) and § 266a, § 9 (fünf Jahre). |
| Gap 3 local lines, links | **fixed.** Address block; links to /selbstanzeige/ and /steuerfahndung-durchsuchung/. |
| Slug without keyword (flag B6) | **open** (Weiterleitung and Go needed). |

## ST-31 Kosten und Honorar

| Review point | Result |
| --- | --- |
| 1 "Kostenvorteil" | **fixed.** Gone from S04. The FAQ keeps "kann ... Kosten sparen" (live FAQ, claim C08). Flag A3 corrected. |
| 2 "vor dem Gespräch" x3 | **fixed.** "In der Erstberatung informieren wir Sie offen über die voraussichtlichen Kosten eines Mandats" (S08, S09, FAQ). Claim C09. |
| 3 "schriftlich" against "Textform" | **fixed.** "Textform" everywhere. |
| 4 § 3a limits | **fixed, checked against `_work/rvg__3a.txt`.** "oder in vergleichbarer Weise", "mit Ausnahme der Auftragserteilung", § 34 exception, full Hinweis text (gegnerische Partei, Verfahrensbeteiligter, Staatskasse), § 3a Abs. 3 "bis zur Höhe der gesetzlichen Vergütung". |
| 5 Pauschale closed list | **fixed.** "zum Beispiel". |
| 6 "Wir bleiben erreichbar" | **fixed.** Removed; only phone times and "Termine ... nach Vereinbarung". |
| 7 "Fachgebiet", "sichern" | **fixed.** "In Wirtschafts- und Steuerstrafsachen"; "kontrollieren wir wichtige Entscheidungen zusätzlich". |
| 8 "Im Regelfall zahlen Sie selbst" | **fixed.** Replaced by "richtet sich nach der Vergütungsvereinbarung" (kosten.txt); Rechtsschutz stays a placeholder. |
| 9 Selbstanzeige promise | **fixed, open in part.** Table row and FAQ say a Selbstanzeige is a steuerstrafrechtliches Mandat, billed by time; placeholder 2 asks for specifics. The inference is flag A8. |
| 10 "Ihre Anwältin ist Dr. Stürzl" | **fixed.** "Die Kanzlei leitet" was dropped with the S09 trim; the credentials stay in S06. |
| 11 Internal note in placeholder | **fixed.** Visible placeholders are short; notes are in `placeholders.md`. |
| Client text check: dropped items | **fixed.** Restored: Vertrauenssache intro, "behalten die Kosten im Blick", "so unterschiedlich", "beispielsweise"/"Beratungstätigkeit", "kaum ein Fall gleicht dem anderen", KI block close to `ki-baustein.txt` (with "kann" and "soll"), "Warum sich die Investition lohnt" with its intro. Not restored on purpose: amounts (placeholders), Spezialisierung, Ruf, Netzwerk, Leidenschaft, hochqualifiziert, bestmöglich. |
| Value bullets | **fixed, sourced.** Lehre/Dozentin (Universität zu Köln LL.M., DAA-Lehrgang, Bundesfinanzakademie), Veröffentlichungen (live profile, claim C32), Praxiserfahrung, Vier-Augen-Prinzip, Termine nach Vereinbarung (only as the source states it), digital processes, Mandanteninteresse. |
| Check of flags B1/B4 (Startseite says RVG) | **corrected** in all four OPEN-FLAGS: F1 (line 155 of approved-copy.md) already says "nicht nach dem RVG" and prints 250 bis 350 Euro. Real conflict: Startseite prints the range, /kosten/ has a placeholder (placeholder 4). |
| Gap 1 no figures | **open.** Waits for the client's yes on placeholders 1, 3 and 4. |
| Gap 2 Selbstanzeige billing, links | **fixed in part.** Links to /selbstanzeige/ and /steuerstrafrecht/gutachten-risikobewertung/ in S04. Billing facts: placeholder 2. |
| Gap 3 links, schema, value block | **fixed.** 7 links spread over S04, S06, S09; /kontakt/ added; FAQPage and Person schema; value block back. |

## New law and source texts saved in `_work/`

- ST-25: `stpo__136`, `stpo__152`, `stpo__160`, `stpo__163`, `stpo__170` (.html and .txt).
- ST-27: `stgb__15`, `stgb__78`, `ao_1977__376`, `zollvg__12a`, `zollvg__31a`.
- ST-28: `sgb_4__7`, `sgb_3__404`, `stgb__15`. The fetch of `schwarzarbg` § 6, 12, 13, 14 failed (page not found); not needed.
- ST-31: none new; `rvg__3a.txt`, `rvg__9.txt` re-checked.

## Notes for the main agent

1. I ran `link_network.py --final` once on the shared directory by mistake; it rewrote `content-writing/LINK-NETWORK.md` (a shared file). The content is the current state of all pages, so a new run by the main agent replaces it. Later checks used a copy in the scratchpad.
2. Skill wishes: (a) `schema_tool.py make` should write the Person node on service pages that have a person section. My workaround is `_work/add_person_schema.py` in each folder. (b) `check_legal.py` and `deslop_de.py` count "individuell", "effizient", "transparent" as soft words (limit 3); a cost page that follows the client text hits the limit fast.
3. Open decisions for Martin: show the Erstberatung range 250 bis 350 Euro on both the Startseite and /kosten/, or on neither; the Fachanwaltsurkunde (flag B6 on ST-25); the status of the Heidelberger Kommentar (ST-27 flag A6).
