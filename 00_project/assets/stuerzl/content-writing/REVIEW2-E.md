# REVIEW2-E: ST-43, ST-44, ST-45, ST-46, ST-49 (round 2, 2026-10-11, read only)
Checked: page.md, placeholders.md, schema.jsonld, claims.json, live texts, ext sources, nap.json, SoT, fixes file section 2. No en/em dash, no forbidden result word, no award or ranking text, no availability promise found in the five page.md files. Names of former colleagues: none in the five 05-final files except page-vorreview.md.

## ST-43 Kanzlei: VERDICT FIX FIRST
Round 1 (9 points): all CLOSED. Evidence: "Auf der Startseite sagt sie"; card cut; "gibt es zwei Notfallnummern"; Vier-Augen now in S07; "üblicherweise auf Grundlage einer Vergütungsvereinbarung"; claim C33 added; "bis zu ihrem Abschluss begleiten"; flags "offen"; schema.jsonld exists.
N1 S04 "ist es höchste Zeit, sich Rat zu holen." Why: urgency instruction without knowing the case (fixes rules 7, 8). Fix: cut, or "kann früher Rat sinnvoll sein".
N2 S03 "Das kann Zeit und Kosten sparen und die Reputation schonen." Why: outcome claim (§ 43b BRAO), flag A3 still open. Fix: cut the second half.
N3 S05 heading "Was sich nachprüfen lässt" over CV-only titles (no Kammer proof, flag A1). Why: promises proof that does not exist. Fix: heading "Qualifikationen im Überblick".

## ST-44 Team: VERDICT PASS (two notes, no rule break)
Round 1 (6 points): all CLOSED. Evidence: card without link; Mary card gone; "Wir sind überzeugt, dass kreative Verteidigungsansätze entstehen"; "Florentine Jilg, Organisation und IT"; "verlässliche Erreichbarkeit" gone; former names only in OPEN-FLAGS.md.
N1 S02 and S04 both say "Jedes Mandat betreuen üblicherweise zwei Anwältinnen oder Anwälte." Why: repeated; the answer block rests on unpublished kosten.txt. Fix: drop it from S02.
N2 S03 Jilg "Organisation und IT" while the live profile says "Wissenschaftliche Mitarbeiterin". Why: public conflict until the client decides (flag B4). Fix: client answer before go-live; align or remove her live profile.

## ST-45 Dr. Anja Stürzl: VERDICT FIX FIRST
Round 1 (6 points): all CLOSED. Evidence: "auf der Startseite"; "Das Team erklärt jeden Schritt"; "Die Kanzlei verbindet"; "Weitere Veröffentlichungen sowie Vorträge"; "Promotion an der LMU München (2017), Dissertation ... Peter Lang (2018)" (both sources saved and match); flags "offen". Answer block now 3 sentences.
N1 S07 "gemeinsam mit Tobias Schwartz", "gemeinsam mit Malte Cordes". Why: rule 11 says never name former colleagues; both co-wrote at the FGS/Rettenmaier stations. Fix: client confirms they are no ex-colleagues, else remove "gemeinsam mit ...".
N2 schema.jsonld Person: no Promotion, alumniOf, knowsAbout; TECH calls the Promotion "bereit" but the JSON has none. Fix: add or correct TECH (see cross-page item 4).
N3 S03 heading "Was sich nachprüfen lässt" (same as ST-43 N3). Fix: same.

## ST-46 Dr. Monika Glogger: VERDICT FIX FIRST
Round 1 (5 points): all CLOSED. Evidence: publications held; heading "Compliance bei STÜRZL Steuerstrafrecht"; "aus der Beratung durch eine Kanzlei" gone; former colleague only in OPEN-FLAGS.md.
N1 S06 "[von Kunde bestätigen: Veröffentlichungen von Dr. Glogger (Auswahl und Autorenname), einschließlich Dissertation]". Why: "Autorenname" is an internal hint in visible text (rule 12). Fix: "[von Kunde bestätigen: Veröffentlichungen von Dr. Glogger]".
N2 S03 "Zertifizierter Compliance Officer (Univ. Münster) seit 2024" under "nachprüfen"; not in nap.json, no proof. Fix: heading as N3 of ST-43; keep flag A1.
N3 schema.jsonld Person: "hasCredential": [] is empty although the title is in the text. Fix: omit the empty array, or add the credential to nap.json after the client confirms.

## ST-49 Publikationen: VERDICT FIX FIRST
Round 1 (10 points): 1 CLOSED ("4. September 2026, JUVE", matches juve.de 04.09.2026); 2 CLOSED (no date + placeholder); 3 CLOSED (webinar removed); 4 CLOSED ("Hier finden Sie die Fachbeiträge von Dr. Anja Stürzl"); 5 CLOSED ("Thema: Frauen im Wirtschafts- und Steuerstrafrecht"); 6 CLOSED (3 x "Titel gekürzt", 1 "Thema:"); 7 CLOSED ("So lesen Sie die Liste"); 8 CLOSED (jurisPR-StrafR 9/2020 listed); 9 PARTLY (see N4); 10 CLOSED ("19. und 20. November 2026").
N1 S01 "Die Liste führt nur Beiträge auf, die wir belegen können." and "jeweils mit Jahr und Quelle". Why: false. Capital and anwalt.de have no date; Fürstenberg, R&W, Köln lines have no year; "Steuerstrafrecht A-Z" has no confirmation; R&W page text unreadable (C35). Fix: cut both claims; hold the A-Z entry and the R&W line.
N2 S06 "9. Oktober 2024, ZRI online: STÜRZL Steuerstrafrecht eröffnet Büro in München" (plus LTO 10.10.2024 and 23.06.2025). Why: shows a 2024/2025 Munich start; SoT says "seit Anfang 2026"; breaks the no-Munich-date decision. Fix: Martin picks one wording; until then drop these lines.
N3 Three placeholders hold internal notes, e.g. "die Meldung der Kanzlei dazu trägt das Datum 6. August 2026" (rule 12). Fix: bare "[von Kunde bestätigen: Datum ...]"; notes stay in placeholders.md.
N4 LTO lines "Meldung der LTO-Redaktion, gezeichnet „sts/LTO-Redaktion“". Why: flag A2 ("Anzeige" on p12/p13) is unresolved, so the page states a fact it cannot prove. Fix: "Beitrag auf LTO" only, until the client confirms.
N5 Nine co-author names (Lachenmann, Körpinar-Häger, Schwartz, Kremer, Hammesfahr, Cordes, Lersch, Schauf, Grötsch). Why: rule 11, FGS-era colleagues likely. Fix: same decision as ST-45 N1.

## Cross-page problems
1. Munich date: ST-49 press lines contradict ST-43 to ST-46 (no date) and SoT; one wording needed for ST-42/43/49.
2. Co-author names (ST-45, ST-49) versus rule 11: one decision from Martin or the client for both pages.
3. "Was sich nachprüfen lässt" on ST-43, ST-45, ST-46 and "Kammer proof missing" (flag A1): rename or deliver proof.
4. Person schema NOT READY. nap.json people has only Stürzl and Glogger; Wimmer and Hoppe are missing (ST-44 cards, ST-47). Stürzl ready: name, jobTitle, worksFor, 2 credentials (no issuer). Missing: sameAs, image, alumniOf, doctorate, knowsAbout. Glogger ready: name, jobTitle, worksFor only; credentials empty. WebPage has no mainEntity link to Person; org sameAs empty.
5. /lea-wimmer/ is linked from ST-44 and ST-49, but ST-47 is not written: dead link at go-live. Hoppe has no slug (card without link, correct).
6. Vier-Augen and cost text (ST-43 S07, ST-44 S02/S04) need /kosten/ live in the same go.
7. Roles match for Stürzl, Wimmer, Hoppe. Glogger areas differ: ST-43 S06 omits Steuerstrafrecht (ST-44, ST-46 include it). Jilg role differs from her live profile.
8. Boilerplate: the same CTA text and "Nennen Sie uns nur Ihr Thema" block sit on all five pages. 5-gram overlap is near the 25 % limit: ST-44/ST-45 24 %, ST-45/ST-46 24 %, ST-43/ST-44 23 %.
9. Delete the page-vorreview.md files in 05-final before hand-over: ST-44 and ST-46 versions name Kellner, Laporte, Runhaar; 03-draft and 01-brief/gate-a0.md also carry them.
