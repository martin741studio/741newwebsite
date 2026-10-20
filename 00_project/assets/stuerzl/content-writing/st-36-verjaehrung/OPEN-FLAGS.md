# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Ratgeber Verjährung, ST-36)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand 2026-10-11, nach der Korrekturrunde (REVIEW-G).

## A. Rechtsgrauzonen und Seitenspezifisches

| # | Stelle | Frage | Stand |
| --- | --- | --- | --- |
| A1 | S04: Beginn der Verfolgungsverjährung | Der Text zitiert jetzt § 78a StGB mit Satz 2 (Erfolg tritt später ein) nach gespeichertem Text. Wann eine Steuerhinterziehung beendet ist, nennt das Gesetz nicht. Rechtsprechung dazu (BGH, Beendigung) wurde nicht gelesen. Der Text sagt das offen. | Kanzlei ergänzt eine BGH-Aussage |
| A2 | S04: "bei 15 Jahren rechnerisch 37,5 Jahre" und "im Grundfall zehn Jahre" | Eigene Rechnung aus § 376 Abs. 3 AO und § 78c Abs. 3 Satz 2 StGB (Claim V06). | Kanzlei prüft |
| A3 | S04: "Für alle anderen Fälle bleibt es bei fünf Jahren" | Schluss aus dem Wortlaut von § 376 Abs. 1 AO (nur Nummer 1 bis 6) und § 78 Abs. 3 Nummer 4, Abs. 4 StGB. Ein besonders schwerer Fall nach § 370 Abs. 3 Satz 1 AO ohne Regelbeispiel Nummer 1 bis 6 behält danach fünf Jahre. Keine Rechtsprechung gelesen. | Kanzlei prüft |
| A4 | S04: Übergangsrecht zu § 376 AO | Gelesen: Art. 97 § 23 EGAO (`_work/gesetze/egao_art97_par23.txt`). Der Text regelt nur die Fassung des § 376 AO von 2008 (Gesetz vom 19.12.2008). Der Review nannte Art. 97 § 23 EGAO für den Stichtag 29.12.2020 der 15-Jahres-Frist. Das steht in dem gelesenen Text nicht. Eine Übergangsregel für die 15 Jahre wurde nicht gefunden und nicht behauptet. Der Text sagt nur, dass bei älteren Taten die damalige Fassung zählen kann. | Kanzlei klärt das Übergangsrecht |
| A5 | S04: Ruhen | § 78b StGB ist gespeichert. Genannt sind Abs. 3 (Urteil erster Rechtszug) und der Verweis auf weitere Ruhensgründe; § 376 Abs. 1 AO verweist auf § 78b Abs. 4. Abs. 1 Nummer 2 und Abs. 4 sind nicht ausgeführt. | Hinweis |
| A6 | S05: Rechenbeispiel (Erklärung 2022, Ende 2032) | Eigene Rechnung aus § 170 Abs. 2 Satz 1 Nummer 1 und § 169 Abs. 2 Satz 2 AO. Das Fristende nach Kalenderjahr ist nicht aus einem gespeicherten Text zu § 108 AO belegt. Claim V17. | Kanzlei prüft oder streicht |
| A7 | S05: § 170 Abs. 6 und 7 AO | Neu, nach gespeichertem Text. Zwei Sätze in einem verkürzt: nur der Beginn der Festsetzungsfrist, keine Einzelheiten zu den Drittstaaten. | Hinweis |
| A8 | S03, S05: Festsetzungsfrist "im Regelfall vier Jahre, für Verbrauchsteuern ein Jahr" | § 169 Abs. 2 AO gelesen. Sonderfälle (zum Beispiel Erbschaftsteuer, § 170 Abs. 5) sind nicht behandelt. | Hinweis |
| A9 | S05: § 171 AO | Genannt: Abs. 5 und Abs. 7. Weitere Hemmungsgründe stehen nur als Verweis auf § 171 AO. | Hinweis |
| A10 | FAQ "Wann fängt Steuerhinterziehung an?" | Die frühere Aussage "ab dem ersten Tag nach Fristablauf steht eine Hinterziehung im Raum" ist gestrichen (keine Norm). Neu: Vollendung bei Verkürzung (§ 370 Abs. 1 und 4 AO), Versuch (§ 370 Abs. 2 AO), Beginn der Verjährung (§ 78a StGB). | erledigt (Review A4) |
| A11 | FAQ Durchsuchung | Jetzt: Das Gesetz nennt die richterliche Anordnung (§ 78c Abs. 1 Nummer 4 StGB). Eine Durchsuchung ohne Richter bei Gefahr im Verzug wird nicht als unterbrechend behauptet. | erledigt (Review A6) |
| A12 | PAA "Wann verjähren Betrugsfälle?" | verworfen (off-offer): Betrug nach § 263 StGB gehört nicht zum Text. | erledigt |
| A13 | G2-Skript: Die Regel "Nr. 1" (Superlativ) trifft Gesetzeszitate und das Wort "gewinnen" (hier in "Gewinnen aus Kryptowerten"). Im Text steht "Nummer" und "Erträgen". | check_legal.py | Vorschlag an Skill |

## B. Offene Punkte für alle Ratgeber-Seiten

| # | Punkt | Quelle | Stand |
| --- | --- | --- | --- |
| B1 | Autorin oder Autor und Freigabe: offen. Pool und Sitetree führen `needs_client`. Berufsrecht-Check (BRAO, UWG) vor Veröffentlichung. Ohne Prüfung bleibt der Status "Vorschlag, wartet auf Abstimmung mit der Kanzlei". | pool.json, sitetree.json | Platzhalter in `05-final/placeholders.md` |
| B2 | Titel von Dr. Stürzl stammen aus ihrem Lebenslauf, nicht aus einem Kammernachweis. | approved-copy.md | Kanzlei bestätigt |
| B3 | Die Live-Seite benutzt Wörter, die dieser Text bewusst nicht übernimmt: "Spezialisierung", "Expertise", "exzellent", "Festpreis", "hart in der Sache". Die Live-FAQ schreibt außerdem "Worst Case Szenario" und "Ihre Freiheit steht auf dem Spiel". Das ist Angst-Wortschatz (Regel LR16) und steht hier nicht. | Live-FAQ, voice.md | Nur Hinweis |
| B4 | Das Stimmprofil `voice.md` ist ein Entwurf. Blog-Beiträge sprechen als "wir" mit Anrede Sie. Die Blog-Regel B4 sieht Ich-Form der Autorin vor. Das hängt an Punkt B1. | blog-rules.md, voice.md | Offen |
| B5 | Rechtsgrenze: Die Beiträge geben allgemeine Information und keine Einschätzung des Einzelfalls (Regel B7). Der Hinweis steht am Ende. | blog-rules.md | erledigt im Text |
| B6 | `schema.jsonld` liegt als Entwurf in `05-final/`. Autorenname und Veröffentlichungsdatum sind darin leer, weil Platzhalter nicht ins Markup dürfen (G6b). Nach der Freigabe Name in `brief.json` (byline) und Datum im Frontmatter eintragen und `schema_tool.py make` neu starten. Das Entwurf-Markup darf vorher nicht live gehen. | schema_tool.py | Offen bis B1 |
| B7 | Telefonnummern im Abschluss stammen aus nap.json (Source of Truth Tab 00). Keine Adresse, keine Öffnungszeiten im Text. | nap.json | bestätigt |

## C. Korrekturrunde 2026-10-11 (REVIEW-G, FIX-G-report.md)

- Sicherung vor der Änderung: `05-final/page-vorreview.md`. Neuer Entwurf: `03-draft/draft-v3.md`, Endfassung `05-final/page.md`.
- Rivalen-Cleanse: nicht gelaufen. Der codex-Aufruf endete mit "usage limit" (Exit 1, Neustart frühestens 17:20 laut Meldung). G5 besteht nur im Lint (5/5). Ein Cleanse-Aufruf ist offen und darf einmal nachgeholt werden (danach `diff_claims.py diff`).
- Wortzahl 1490 (Zielbereich bis 1300). Grund: Beginn nach § 78a mit Satz 2, Obergrenze mit Vorbehalt § 78b, Beispiel, § 170 Abs. 6 und 7, Fragen. Kürzen möglich beim Beispiel und bei der Quellenliste.
- Ein CTA am Ende (Blog-Regel B9). Link zur Geldseite (Selbstanzeige) im ersten Drittel (S03) und am Ende (S10). Link zu ST-37 in S06.
