# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Ratgeber Krypto, ST-37)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand 2026-10-11, nach der Korrekturrunde (REVIEW-G).

## A. Rechtsgrauzonen und Seitenspezifisches

| # | Stelle | Frage | Stand |
| --- | --- | --- | --- |
| A1 | S03 bis S08: steuerrechtliche Aussagen | Quelle ist das BMF-Schreiben vom 6. März 2025 (BStBl I S. 658), § 23 EStG und das KStTG. Das Datum steht im gespeicherten Kopf (`_work/bmf-krypto-clean.txt`) und auf der Seite des BMF (`_work/bmf-seite-2026-10-11.md`). Die Seite kündigt Ergänzungen an. Bei der Suche (2026-10-11) wurde kein späteres Schreiben gefunden. Das beweist nicht, dass es keines gibt. Der sichtbare Text sagt: spätere Änderungen nicht ausgewertet. Das BFH-Urteil (14.02.2023, IX R 3/22) wird nur über das BMF-Schreiben genannt. Die Fachanwältin für Steuerrecht soll gegenlesen. | Kanzlei prüft |
| A2 | S03: "Die steuerliche Einordnung Ihres Einzelfalls nehmen wir hier nicht vor." | Die Kanzlei nennt allgemeine Steuerberatung nicht als Leistung (client-baseline, offene Frage 7). Der Satz grenzt ab. | Kanzlei bestätigt |
| A3 | S05: KStTG, erste Meldung | Die Frist "31. Juli 2027" ist eine Ableitung aus § 9 Abs. 1 (jährlich spätestens zum 31. Juli für den vorangegangenen Meldezeitraum), § 10 (Kalenderjahr) und § 21 (Pflichten erstmals für das Kalenderjahr 2026). Kein Text nennt das Datum. Gelesen auch: § 2 (Anwendungsbereich: Anbieter mit Bezug zu Deutschland) und § 13 (Weiterleitung an Landesfinanzbehörden oder Behörden anderer Staaten). Der Kreis der Anbieter im Einzelnen (§ 1, § 2 Abs. 2 bis 4) ist nicht ausgewertet. | Fachanwältin bestätigt das Datum |
| A4 | Influencer-Beitrag der Live-Seite (18.07.2025) | Handelt von Social-Media-Einnahmen, nicht von Krypto, und seine Zahlen sind nicht belegt. Nicht verwendet. | Kanzlei: Gibt es einen Krypto-Beitrag? |
| A5 | Keyword mit 20 Suchen | Wenig Daten, Pool-Priorität C, Status needs_client. Nischen-Vorschlag. | Martin entscheidet über Schreiben und Veröffentlichen |
| A6 | PAA "Wird Krypto bald besteuert?" | verworfen (nicht rechtssicher): Prognose zur Gesetzgebung. | erledigt |
| A7 | Mining, Staking, Lending, Hard Fork, Airdrop, NFT | Nur als Verweis auf die Sonderregeln im BMF-Schreiben. NFT und Liquidity Mining sind laut Ministerium noch nicht Gegenstand des Schreibens. | Hinweis |
| A8 | Zehn-Jahres-Frist (§ 23 Abs. 1 Satz 1 Nummer 2 Satz 4 EStG) | Der Text gibt den Wortlaut wieder (Einkunftsquelle in mindestens einem Kalenderjahr) und die Aussage des BMF-Schreibens Rn. 63 (keine Verlängerung bei Currency- und Payment-Token). Dass Staking und Lending diese Regel auslösen, steht in keinem gelesenen Text. Der Text sagt nur, dass das BMF-Schreiben dazu eigene Abschnitte hat. | Fachanwältin bestätigt oder ergänzt |
| A9 | FAQ "unter 600 Euro" | Beantwortet nur mit EStG-Text und BMF Rn. 53 (1.000 Euro, bis VZ 2023 600 Euro, Freigrenze). Eine Pflicht zur Angabe unter der Grenze wird nicht behauptet, weil keine Quelle dazu gelesen wurde. "Freigrenze: nichts bleibt steuerfrei, wenn die Grenze erreicht ist" ist ein Schluss aus dem Wortlaut. | Fachanwältin prüft |
| A10 | S04: Vorsatz | Die Kanzleidefinition ("billigend in Kauf nehmen") und der Satz "bleibt der Steuerpflichtige für die Angaben verantwortlich" sind gestrichen (Review A2). Neu: § 15 StGB und BGH 1 StR 416/08 Rn. 41 (gespeichert in `st-35.../_work/`). § 150 Abs. 2 AO steht als Pflicht zur wahrheitsgemäßen Angabe. | erledigt |
| A11 | S06: Selbstanzeige | Neu: 25.000 Euro je Tat (§ 371 Abs. 2 Satz 1 Nummer 3 AO), § 398a AO, "Straf- oder Bußgeldverfahren" nach Nummer 1 Buchstabe b. Wortlaut nach gespeichertem § 371. | erledigt (Review A6) |
| A12 | G2-Skript: Die Regel "Superlativ" trifft die Gesetzesformel "nach bestem Wissen und Gewissen" (§ 150 Abs. 2 AO). Der Text nennt nur "wahrheitsgemäß". | check_legal.py | Vorschlag an Skill |

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
- Wortzahl 1467 (Zielbereich bis 1300). Grund: Zehn-Jahres-Regel, Freigrenze, KStTG-Grenzen, 25.000 Euro. Kürzen möglich bei der Quellenliste.
- Ein CTA am Ende (Blog-Regel B9). Link zur Geldseite im ersten Drittel (Ende von S03) und am Ende (S10).
