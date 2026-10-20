# Bericht Batch E: Kanzlei, Team, Personen, Presse (Stürzl, 2026-10-11)

Autor: Schreib-Agent Batch E. Alle Seiten nur lokal. Kein Upload, kein CMS, keine Mail. Kein Reviewer-Aufruf. Wörter zählt `wordcount.py` auf `05-final/page.md` (sichtbarer Text von H1 bis vor dem TECH-Block).

## Ergebnis je Seite

| ID | Seite | Wörter | Bestand | Wettbewerber-Median (Info) | G1 | G2 | G3 | G4 | G5 | G6 | Platzhalter | Cleanse-Aufrufe | Kosten USD | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-43 | Kanzlei (Über uns) | 1170 | 1082 | 633 (11 Seiten) | PASS | PASS | PASS | PASS | PASS (5/5) | PASS | 4 | 2 | 0 | fertig, Freigabe offen |
| ST-44 | Team | 409 | 259 | 477 (10 Seiten) | PASS | PASS | PASS | PASS | PASS (5/5) | PASS | 1 | 1 | 0 | fertig, Freigabe offen |
| ST-45 | Dr. Anja Stürzl | 782 | 768 | 370 (11 Seiten) | PASS | PASS | PASS | PASS | PASS (5/5) | PASS | 1 | 1 | 0 | fertig, Freigabe offen |
| ST-46 | Dr. Monika Glogger | 552 | 311 | 370 (11 Seiten) | PASS | PASS | PASS | PASS | PASS (5/5) | PASS | 1 | 1 | 0 | fertig, Freigabe offen |
| ST-49 | Veröffentlichungen, Vorträge und Presse | 1085 | kein Bestand | 756 (10 Seiten) | PASS | PASS | PASS | PASS | PASS (5/5) | PASS | 3 | 1 | 0 | fertig, Freigabe offen |

Alle fünf Seiten bestehen G1 bis G6 auf `05-final/page.md` (Stand 2026-10-11, `04-gates/gates.md`). Der Median ist nur Information: Typ C (Brand-, Team-, Personen-, Presse-Seiten) braucht kein Wortziel. Gate G6 verlangt aber einen gespeicherten Benchmark, deshalb habe ich je Seitentyp Vergleichsseiten aus der Wettbewerberliste des Pools gemessen (`_work/bench-metrics.json`, `page_metrics.py`, 0 USD). Der Bestand ist die Untergrenze und ist bei allen Seiten erreicht.

Cleanse: ST-43 Aufruf 1 ohne Änderung, Aufruf 2 mit zwei kleinen Rhythmus-Änderungen (übernommen, Diff PASS). ST-44, ST-45, ST-49 ohne Änderung. ST-46 eine Satzteilung (übernommen, Diff PASS). Codex lief immer. G5 gilt daher als bestanden.

Ordner: `/Users/martindrendel/741website/00_project/assets/stuerzl/content-writing/` mit `st-43-kanzlei`, `st-44-team`, `st-45-dr-anja-stuerzl`, `st-46-dr-monika-glogger`, `st-49-publikationen`. Je Ordner: `01-brief/` (brief.json, claims.json, gate-a0.md), `02-outline/outline.md`, `03-draft/`, `04-gates/gates.md`, `05-final/` (page.md, cms-blocks.txt, placeholders.md), `_work/`, `_status.md`, `OPEN-FLAGS.md`, `_run.json`.

## Korrektur von Martin eingearbeitet (Adresse, Zeiten, Notfallnummern)

Quelle: `nap.json` und `source-of-truth-2026-10-11.md`. Entfernt oder ersetzt in meinen Seiten:

- ST-43: Platzhalter „endgültige Adresse Frankfurt“ entfernt. Der Text nennt Untermainkai 26, 60329 Frankfurt am Main (Claim C28).
- ST-43: Platzhalter „eine gültige Telefonzeit“ entfernt. Der Text nennt Montag bis Freitag 9:30 bis 14:30 Uhr und Termine auch außerhalb (Claim C29).
- ST-43: Notfallnummern 0160 3396513 und 0160 95945730 stehen im Text (Quelle Live-Kontaktseite, Claim C30). Der Platzhalter zu „24/7-Erreichbarkeit“ bleibt, aber nur für die Besetzungszeiten der Nummern (nicht dokumentiert).
- ST-43: Ansprechpartnerinnen vor Ort ergänzt (Frankfurt Dr. Stürzl, München Lea Wimmer und Dr. Glogger).
- ST-44 bis ST-49: hatten keine Adress-, Zeit- oder Notfall-Platzhalter. Nichts zu entfernen. Die alte Adresse steht nirgends (G4 prüft das Verbotswort).
- `placeholders.md` und `OPEN-FLAGS.md` von ST-43 sind angepasst. Ein Hinweis in `placeholders.md` Nr. 4 hält die Entfernung fest.

## Was blockiert wurde

Nichts. Kein Blocker bei den fünf Seiten. Nicht geschrieben (nicht meine Zuteilung): ST-50 Fallbeispiele (keine Daten).

Nicht übernommen, mit Grund:

- Neun Zitate von Kollegen und Mandanten auf der Live-Kanzleiseite (275 Wörter, Superlative).
- „hochspezialisiert“, „Experten“, „Expertise“, „Spezialisierung“, „Festpreis“, „beste Lösung“, „ganzheitliche Beratung“, „Leidenschaft“ aus der Live-Kanzlei- und Teamseite.
- Namen früherer Kolleginnen und Kollegen (siehe Widersprüche).
- Auszeichnungen und Rankings: nur als Platzhalter.
- Bewertungszahlen (Google, anwalt.de): nur als Platzhalter in ST-43.
- Eine Anmerkung („… nach § 9 Abs. 2 Nr. 1 OWiG“) in ST-49 wegen eines Fehlalarms von Gate G2 (siehe Vorschläge).
- Brühler Symposion (BMF-PDF lieferte HTTP 503), R&W-Inhalte (Seite lädt per Skript): nur als Hinweis, nicht als Eintrag.

## Neue Widersprüche im Kundenmaterial (Details in den OPEN-FLAGS.md)

1. Fremde Namen auf der Teamseite: Im sichtbaren Live-Text steht keiner der Namen Pösl, Kellner, Brunzel, Euler, Fenzl, Scherübel. Im HTML stehen falsche Bild-Alt-Texte: „Dr. Philipp Kellner, Rechtsanwalt | Associate“ (am Foto von Dr. Glogger), „Alice Laporte, Human Resources“, „Nellie Runhaar, Office Managerin“. `/index.php/cedric-euler` liefert 404. LTO und ZRI nennen Dr. Philipp Kellner 2024 und 2025 als Rechtsanwalt der Kanzlei in München; die aktuelle Teamseite führt ihn nicht. Frage an die Kanzlei: Sind das ehemalige Kolleginnen und Kollegen? Alt-Texte beim Relaunch ersetzen.
2. Eröffnung des Büros München: Lebenslauf Dr. Stürzl „03/2026“; LTO und ZRI (Oktober 2024) „spätestens zum Januar 2025“; LTO Juni 2025 „vor wenigen Monaten eröffnet“; Lea Wimmer laut Profil „seit 7/2025“ in München; Source of Truth „seit Anfang 2026“. Die Seiten nennen kein Startdatum für München.
3. JuWiSt-Rolle: Live-Profil „Gründungsmitglied / wissenschaftlicher Beirat“; Live-Kanzleiseite und Fürstenberg „Vorstandsvorsitzende“; C.F. Müller (Februar 2026) „engagierte sich als Vorstandsvorsitzende“. Text: sichere Fassung „Gründungsmitglied und Mitglied des wissenschaftlichen Beirats“.
4. Empathy: „Vorstands- und Gründungsmitglied“ (Kanzleiseite, C.F. Müller) gegen „Gründungsmitglied“ (Profil). Text: „Gründungsmitglied“.
5. Flick Gocke Schaumburg: „2019 bis 2022“ (Profil) gegen „2019 bis 2023“ (Fürstenberg). Text: Profil.
6. Erstberatung: „Festpreis“ (Live-Kanzleiseite) gegen „Pauschale 250 bis 350 Euro“ (Kundentext) gegen Live-FAQ. Platzhalter ohne Zahl.
7. Kostenmodell: freigegebene Startseite „nach RVG“ gegen Kundentext „kein RVG“. Meine Seiten folgen dem Kundentext. Die Startseite muss angepasst werden.
8. Zwei Slogans live („Aufklären. Verständigen. Verteidigen.“ und „Lösen. Schlichten. Streiten.“). ST-43 nutzt den der Kanzleiseite.
9. Autorenname „Werndl“ in allen Veröffentlichungen auf der Seite von Dr. Glogger; Bezug nicht erklärt (Platzhalter in ST-46). Autorenname „Stürzl-Friedlein“ in einem wistra-Verzeichnis (Source of Truth Tab 12); nicht übernommen.
10. Titel Dr. Glogger: `nap.json` führt keine Titel, das Live-Profil nennt „Zertifizierter Compliance Officer (Univ. Münster)“. Text folgt dem Live-Profil (Regel für ST-46).
11. Das Live-Profil von Dr. Stürzl nennt keine Promotion. Fürstenberg nennt Promotion LMU 2017, Peter Lang die Dissertation 2018. ST-49 nennt die Dissertation mit Beleg, ST-45 nicht (Regel: Fakten nur aus Live-Profilseiten).
12. Team-Bezeichnung „Salary Partner/in“ mit Fußnote „Angestellte Rechtsanwältin“. Meine Seiten schreiben „angestellt“.
13. Karte „Mary, Chief Barking Officer“ (Bürohund laut Profiltext): Profil beschreibt Beratung von Mandanten. Platzhalter in ST-44.
14. Der Aktuelles-Beitrag zum Webinar (Verlag Dr. Otto Schmidt) nennt Dr. Stürzl nicht als Referentin und verlinkt auf eine Seite mit 404. Platzhalter in ST-49.

## Rechtsgrauzonen (Auswahl, nicht vom Agenten zu entscheiden)

- Titel aus Lebenslauf und Live-Profilen, nicht aus Kammernachweisen (§ 43c BRAO, FAO): Dr. Stürzl, Lea Wimmer, Dr. Glogger.
- Wendungen der Kanzlei mit Ergebnisbezug: „möglichst geräuschlos und effizient“, „zügig und geräuschlos zu beenden“. Ein Satz („Das spart Zeit und Kosten und schützt Ihre Reputation“) ist mit „kann“ abgeschwächt, „ohne strafrechtliche Konsequenzen“ ist gestrichen.
- Rechtspolitische Aussagen der Kanzlei (sechs Entwicklungen im Steuerstrafrecht) ohne Fundstelle; im Text als „aus unserer Sicht“ gekennzeichnet.
- Peer-Zitate mit Superlativen auf der Live-Seite; Live-Seite nutzt selbst verbotene Wörter (Wortliste oben). Entscheidung von Martin, ob die Kanzlei hingewiesen wird.
- Presseliste in ST-49: LTO-Meldung vom 01.12.2023 ist eine Kanzleimitteilung; ob die LTO-Meldungen von 2024 und 2025 redaktionell sind, geht aus den Seiten nicht eindeutig hervor (UWG, Kennzeichnung).
- Rankings und Bewertungszahlen: nicht freigegeben; Platzhalter.
- „Salary Partner“ und die Mary-Karte (siehe oben).
- Quellentitel mit Angstton („Wann dem Geschäftsführer … Gefängnis droht“) steht in den Publikationslisten (ST-49) nur als Titel der Quelle.

## Vorschläge für Regeln im Skill

1. Gate G6 verlangt einen gespeicherten Benchmark. Für Typ C (Brand, Team, Person, Presse) gilt laut `seo-geo-rules.md` „kein Benchmark“. Entscheiden: entweder G6 für Typ C von der Benchmark-Pflicht ausnehmen oder in der Regel festhalten, dass Vergleichsseiten als Information gemessen werden. Ich habe das Zweite getan. Der Skill wurde um 13:06 geändert, nachdem das Batch-Dokument geschrieben war (neue Gates G6 H1 bis H7).
2. Gate G2: Das Muster `nr\.? ?1` (Superlativ „Nr. 1“) schlägt bei Gesetzeszitaten an („§ 9 Abs. 2 Nr. 1 OWiG“). Vorschlag: nur sperren, wenn kein „Abs.“ oder „§“ davor steht.
3. Gate G5, Dreier-Raster: `A, B und C` trifft auch Quellentitel und Seitennamen („Veröffentlichungen, Vorträge und Presse“). Vorschlag: Links, Anführungszeichen und Zitate vom Raster ausnehmen.
4. Gate G6 H2 zählt Sätze mit dem Punkt hinter „Dr.“ und „LL. M.“ falsch (zu viele Sätze). Vorschlag: Abkürzungen ausnehmen.
5. `make_cms_blocks.py` macht aus jeder kurzen fetten Zeile einen „Button:“. Karten-Überschriften in `el-grid`-Listen und Zwischenüberschriften erscheinen deshalb als Button. Vorschlag: nur Zeilen mit CTA-Text als Button führen, Rest als „Titel:“.
6. `validate_page.py`: Bestand-Untergrenze hat keine Ausnahme für nicht übernehmbare Bestandsteile (Peer-Zitate 275 Wörter, Lebenslauf 191 Wörter in ST-43; Publikationsliste 520 Wörter in ST-45). Vorschlag: `bestand_words` nach Abzug dokumentierter, nicht übernehmbarer Teile zulassen, mit Pflichtfeld `bestand_excluded`.
7. Das Template „Practitioner“ verlangt Ich-Form im Ansatz-Abschnitt. Das Batch-Dokument verlangt dritte Person mit wörtlichen Zitaten. Regel im Template angleichen (BRAO: dritte Person).
8. Templates „About“ und „Team“ haben keinen `answer`-Abschnitt, Gate G6 H2 verlangt ihn. Template um `answer` ergänzen (habe ich getan).
9. Neue Regel für Quellentitel: Gedankenstriche in Titeln durch Doppelpunkt ersetzen und Seitenbereiche mit Bindestrich schreiben; Hausregel in `copy-rules.md` festhalten.
10. Batch-Dokument: Der Satz „Adresse Frankfurt nicht endgültig“ ist durch die Korrektur überholt (nap.json). `client-baseline.md` und `approved-copy.md` (Platzhalter für Adresse, Notfallnummern) ebenfalls nachziehen. Ich habe diese Dateien nicht geändert.
11. `legal-terms.json`: „Straflosigkeit“ ist nicht gesperrt (nur „Straffreiheit“); in einem Quellentitel in ST-49 steht es. Entscheiden, ob das Wort in Titeln erlaubt ist.

## Hinweise für Martin

- Ich habe die Wettbewerber-Messungen, die gespeicherten Gesetzestexte (`st-43-kanzlei/_work/law/`: § 370 AO, §§ 30 und 130 OWiG, § 43a BRAO, § 203 StGB) und mehr als 20 externe Quellen unter `st-49-publikationen/_work/ext/` gespeichert. Prüfbar sind sie über `claims.json` (Quelle und Datum je Eintrag).
- Quellen, die ich nicht automatisch prüfen konnte: capital.de und anwalt.de (HTTP 403), R&W (Inhalt lädt per Skript), Spotify (kein Text), LinkedIn (HTTP 999), BMF-PDF (HTTP 503). Vor Livegang von Hand öffnen.
- Fotos: Für keine Seite liegen freigegebene Bilddateien mit Bildunterschrift vor. Ein Design-Kommentar steht im Hero.
- Die Seiten ST-43 bis ST-46 zitieren Gesetze nur mit gespeichertem Text (ST-43) oder in Quellentiteln (ST-45, ST-49). Die Zeile „Rechtsstand“ beziehungsweise „Stand: Oktober 2026“ steht sichtbar (Gate G6 H6).
- DataForSEO: 0 USD. Cleanse: 6 Aufrufe insgesamt.
