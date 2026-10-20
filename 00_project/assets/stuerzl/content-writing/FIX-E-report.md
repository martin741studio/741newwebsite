# FIX-E report: Stürzl pages ST-43, ST-44, ST-45, ST-46, ST-49

Date: 2026-10-11. Basis: `REVIEW-E.md`, `content-writing-stuerzl-fixes.md`, `content-writing-stuerzl-batch.md`, `nap.json`, `source-of-truth-2026-10-11.md`, `slugs.json`. Each page has a backup (`05-final/page-vorreview.md`), a new draft (`03-draft/draft-v3.md`) and a new package (`page.md`, `cms-blocks.txt`, `placeholders.md`, `schema.jsonld`, `measure-plan.md`). Nothing went to a site, a CMS, Drive or the portal.

## Summary

| ID | Page | Words now (before) | Bestand | G1 | G2 | G3 | G4 | G5 (lint) | G6 | Cleanse calls | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-43 | Kanzlei | 1179 (1170) | 1082 | pass | pass | pass | pass | pass | pass | 0 | ready for review |
| ST-44 | Team | 488 (409) | 259 | pass | pass | pass | pass | pass | pass | 0 | ready for review |
| ST-45 | Dr. Anja Stürzl | 890 (782) | 768 | pass | pass | pass | pass | pass | pass | 0 | ready for review |
| ST-46 | Dr. Monika Glogger | 492 (552) | 311 | pass | pass | pass | pass | pass | pass | 0 | ready for review |
| ST-49 | Veröffentlichungen | 1325 (1085) | none | pass | pass | pass | pass (2 long title sentences, warning) | pass | pass | 0 | ready for review |

Cleanse: no call in this round. The changes were small for ST-43 to ST-46. ST-49 is a list of citations, and a rival-model rewrite would change titles. `diff_claims.py diff` was therefore not needed. Cost: 0 USD (no DataForSEO call). One Firecrawl read of the BMF page (1 credit).

Common changes on all five pages:
- `nap_file` is now set in each `brief.json` (it was missing, so no `schema.jsonld` existed). `run_gates.py` now builds `05-final/schema.jsonld` (WebPage, BreadcrumbList, LegalService with both offices; Person on ST-45 and ST-46 from `nap.json`).
- Address block (three exact lines from the fixes file) at the end of each closing section.
- "LL.M." is the only spelling now (review cross-page point 10).
- No date for the Munich office on any page (decision 4). The four versions are in each OPEN-FLAGS file.
- OPEN-FLAGS status "Kanzlei bestätigt" is now "offen" (no client confirmation exists).
- Names of former colleagues stay only in `OPEN-FLAGS.md` of ST-44 and ST-46 (not in page.md TECH, not in placeholders.md, not in brief.json). The backup files `page-vorreview.md` keep the old text on purpose; delete them before the files go to the CMS team.
- Cost text uses the fixes-file decision: time-based billing, six-minute units, fee agreement in Textform. The Textform source is § 3a Abs. 1 Satz 1 RVG, stored in `st-43-kanzlei/_work/law/rvg__3a.txt`. No amount on any of the five pages.

## ST-43 Kanzlei

| Review point | Result |
| --- | --- |
| 1 Quote place "Kanzleiseite" | fixed: "Auf der Startseite" (claim C19 source corrected) |
| 2 "im Austausch mit den Finanzbehörden" | fixed: card cut; the lecturer role stays in S06 only; link to /publikationen/ moved to S06 |
| 3 Emergency numbers, heading "Persönlich erreichbar" | fixed: heading "Wege zu uns"; text "gibt es zwei Notfallnummern"; the 24/7 placeholder is gone; no hours promised |
| 4 Vier-Augen-Prinzip under "nachprüfen" | fixed: moved to S07; flag A10 (needs /kosten/ live in the same go) |
| 5 "schriftlich" | fixed: "üblicherweise auf Grundlage einer Vergütungsvereinbarung … in Textform"; Erstberatung "üblicherweise Pauschale"; amount placeholder removed (decision 3) |
| 6 "Wir erklären Ihnen jeden Schritt" | proven: new claim C33 (approved homepage, `approved-copy.md` line 33) |
| 7 "zügig und geräuschlos beenden" | fixed: "Verfahren, die sich nicht vermeiden lassen, bis zu ihrem Abschluss begleiten"; the firm phrase "möglichst geräuschlos und effizient" in S03 stays (flag A2) |
| 8 Flags marked "bestätigt" | fixed: "offen" |
| 9 TECH note, no schema | fixed: TECH text replaced; `schema.jsonld` exists |
| Cross-page 5 (founding wording) | fixed: "gründete sie im Dezember 2023 in Frankfurt am Main, heute gibt es Büros in Frankfurt am Main und München" (claim C03, sources SoT Tab 01 Z27 and LTO 01.12.2023) |
| Cross-page 7 (Hoppe) | fixed: "Thorben Hoppe … an beiden Standorten" in S06 and S08 (claim C32) |
| Text gap 1 (Wirtschaftsstrafrecht) | fixed with one sentence in S04; § 30/§ 130 OWiG now only named, with link (fixes decision 6) |
| Text gap 2 (FAQ), gap 3 (Kammer proof, reviews, awards, sameAs) | left open on purpose: type C brand page without PAA data; no client source for the rest (placeholders for reviews and awards stay) |

## ST-44 Team

| Review point | Result |
| --- | --- |
| 1 Link /thorben-hoppe/ | fixed: card without link (no slug in `slugs.json`); also removed from the TECH link list |
| 2 Card "Mary, Chief Barking Officer" | fixed: card and placeholder removed; return only with a "Bürohund" label and client go (flag A4) |
| 3 "verlässliche Erreichbarkeit" | fixed: half sentence cut (flag A7) |
| 4 "Nur wer … findet" | fixed: "Wir sind überzeugt, dass … entstehen" |
| 5 Florentine Jilg role | fixed: "Organisation und IT" per SoT Tab 01 Z46 and Tab 02 Z45 (claim C05); group heading "Organisation und Back-Office"; question about the live label "Wissenschaftliche Mitarbeiterin" in `placeholders.md` and flag B4. Roles of Stürzl, Wimmer (Standortleitung München), Glogger and Hoppe match the SoT and live profiles |
| 6 Former colleagues in TECH | fixed: names only in OPEN-FLAGS B1 |
| Text gap 1 | fixed: Hoppe "Rechtsgebiete: Strafrecht, Steuerrecht sowie Compliance" (live profile wording; flag A3 asks the firm) |
| Text gap 2 | fixed: e-mail and phone per lawyer (live profiles, nap.json; flag A8 asks the firm), address block |
| Text gap 3 | left open: no PAA data, no released photos; alt-text rule is in TECH |
| Cross-page 7 | fixed: "Thorben Hoppe ist an beiden Standorten tätig" in S04 |

## ST-45 Dr. Anja Stürzl

| Review point | Result |
| --- | --- |
| 1 Quote place "Kanzleiseite" | fixed: "auf der Startseite" |
| 2 "Sie erklären …" | fixed: "Das Team erklärt … steht Mandanten … zur Seite"; claim C25 added (approved-copy line 33) |
| 3 "Fachliche Kompetenz verbindet sie …" | fixed: "Die Kanzlei verbindet …" (and "verteidigt die Kanzlei") |
| 4 "vollständige Liste" | fixed: "Weitere Veröffentlichungen sowie Vorträge und Presseberichte" |
| 5 Basis for "Dr." | proven: Promotion LMU 2017 (Fürstenberg profile) and dissertation Peter Lang 2018, new claims C23 and C24; sources saved in `_work/ext/`; shown in S03 and S06; flag B7 asks the firm to confirm |
| 6 Flags marked "bestätigt" | fixed: "offen" |
| Gap: answer block 5 sentences | fixed: 3 sentences |
| Gap: local 70 | fixed: office links, /kontakt/ and address block in S10 |
| Gap: Person schema | done through `run_gates.py` (see below); `sameAs` empty, candidates listed in OPEN-FLAGS C7 |
| Gap: Kammer, awards, liftable question | left open: no chamber proof in the client material; awards stay a placeholder; no FAQ on a person page |

## ST-46 Dr. Monika Glogger

| Review point | Result |
| --- | --- |
| 1 Five titles and S03 bullet (byline "Werndl") | fixed: all publications held. S06 now has the JuWiSt membership (listed as hers in the live profile) and one placeholder. S03 bullet replaced by the JuWiSt membership. The Nomos 2019 dissertation stays held too. Question in `placeholders.md` |
| 2 "Das Profil nennt Veröffentlichungen …" | fixed: sentence removed with the list; heading "Mitgliedschaft und Veröffentlichungen" |
| 3 Heading "Wobei Dr. Glogger Unternehmen begleitet" | fixed: "Compliance bei STÜRZL Steuerstrafrecht" |
| 4 "und aus der Beratung durch eine Kanzlei" | fixed: second half cut |
| 5 Former colleague in TECH and placeholders.md | fixed: name only in OPEN-FLAGS B2 |
| Gap: Person schema | `worksFor` and `jobTitle` ready. `hasCredential` is empty because `nap.json` has no credential for her; the title is in the text and the live profile. `sameAs` empty (live LinkedIn link gives 404, SoT Tab 02 Z33) |
| Gap: personal work, photo | left open: no client source for her own mandates (question in `placeholders.md`); no released photo. /kontakt/ link and address block added |

## ST-49 Veröffentlichungen, Vorträge und Presse

| Review point | Result |
| --- | --- |
| 1 JUVE date | fixed: "4. September 2026" (JUVE page `_work/ext/p3.html`, 04.09.2026 12:05). The 10.09. is the firm's post date (in flag A3). Title of the source replaced by the topic line "Thema: Frauen im Wirtschafts- und Steuerstrafrecht" (also covers point 5) |
| 2 Capital date | fixed: no date in the line; placeholder with the firm's post date (capital.de gives HTTP 403) |
| 3 Webinar Otto Schmidt | fixed: entry removed; question in `placeholders.md`; flag A8 |
| 4 "Fachbeiträge unserer Kanzlei" | fixed: H1 "… rund um Dr. Anja Stürzl", intro "Fachbeiträge von Dr. Anja Stürzl", meta changed, one sentence on pre-2023 works from earlier stations. Page title keeps the brand "| STÜRZL" |
| 5 JUVE ranking title, "Kluge Köpfe im Strafrecht" | fixed: topic line for JUVE; the C.F. Müller line now reads "Interview … in Ausgabe 34 des Verlagsnewsletters" |
| 6 Titles with "droht/Gefängnis/Strafen drohen" | fixed: one entry as topic line, three as shortened titles with "(Titel gekürzt)". Full titles are in OPEN-FLAGS A5 if the firm wants them back. Source titles of media pieces ("Steuerfallen lauern …") stay verbatim as citations with link |
| 7 Altered titles | fixed: new section "So lesen Sie die Liste" explains dash-to-colon changes, corrected typos, "Titel gekürzt" and "Thema:" lines. The ZWH typo correction stays flagged (A6) |
| 8 jurisPR-StrafR 9/2020 | fixed: entry added. G2 gives no hit for "Nr. 1 OWiG" in the current script, so no script change is needed |
| 9 LTO items and "Anzeige" | fixed: each LTO item is labelled by type (Kanzleimitteilung, external content / editorial item signed "sts/LTO-Redaktion"). The word "Anzeige" appears on all LTO pages, but the HTML does not show whether it marks the article or an ad slot; the firm must confirm (flag A2) |
| 10 "20. November 2026" | fixed: "19. und 20. November 2026" with note on the Kongresstag; talk is shared with Dr. Stefan Rolletschke (Referenten page) |
| Text gap 1 (topic index, links) | fixed: new section S03 "Beiträge nach Themen" with links to /compliance/, /selbstanzeige/, /unternehmensvertretung/, /ordnungswidrigkeiten/, /steuerstrafrecht/ |
| Text gap 2 (JSON-LD, years) | `schema.jsonld` built (WebPage, BreadcrumbList, LegalService). Article and ScholarlyArticle per entry not built (dates and authors not checked per entry). Undated entries (anwalt.de, Capital) carry placeholders |
| Local 45 | fixed: address block |
| Section IDs | changed: S03 new, old S03 to S07 are now S04 to S08. Brief sections updated |

## Special rules from Martin: check

1. Dr. Glogger publications: held on ST-46; ST-49 links only Lea Wimmer's profile now. Done.
2. ST-49: titles marked or exact; JUVE date 4 September 2026; unverified dates are placeholders; LTO relabelled; fear-word titles shortened or replaced by topic lines. Done.
3. ST-44: Mary removed, /thorben-hoppe/ dropped, roles aligned with the Source of Truth. Done.
4. Munich date: no date on any of the five pages. Done.
5. Person pages: `worksFor` and credentials in TECH and OPEN-FLAGS; `sameAs` empty with a note; `schema_tool.py make` ran through `run_gates.py`. Done. Open: `nap.json` has no credential for Dr. Glogger.

## Decisions for the main agent or Martin

1. `nap.json`: add Dr. Glogger's credential "Zertifizierter Compliance Officer (Univ. Münster)" (2024) after the firm confirms it. Then `hasCredential` is filled.
2. Hoppe has no slug in `slugs.json` (ST-48 empty). The Team card has no link. ST-47 (/lea-wimmer/) is not in this batch but is linked from ST-44 and ST-49.
3. Direct e-mail addresses on the ST-44 cards come from the live profiles. The firm should confirm them.
4. Vier-Augen-Prinzip (ST-43, ST-44) and the cost text need /kosten/ live in the same go.
5. Munich opening date: one version must be chosen before ST-42, ST-43 and ST-49 go live.
6. Link-count warnings (more than 8 text links): ST-43 (15), ST-45 (13), ST-49 (10). The fixes file allows more for Kanzlei and hub pages. ST-45 is a person page: trim if you want it at 8.
7. I ran `link_network.py` twice, which rewrites `LINK-NETWORK.md` in the shared folder. The file is generated, but it is outside my five folders. Its last result shows no failure for ST-43 to ST-49 (the open failure is ST-33, not in this batch).
8. The BMF page for the Brühl symposium (4 September 2025) was read through Firecrawl without the PDF text. Dr. Stürzl is not named there. She is not listed on ST-49. Note in `_work/ext/bmf-bruehler-seite.md`.
