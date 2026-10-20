# STÜRZL: Umsetzungs-Backlog (nur sammeln, NICHTS umsetzen)

Stand 09.10.2026. Beschluss Martin: Die Punkte aus der Wettbewerber-Analyse werden notiert, nicht umgesetzt. Wir sammeln die Daten, die wir für die schnelle Umsetzung in den nächsten Tagen brauchen. Das Audit läuft parallel weiter.
Quelle der Punkte: `stuerzl-wettbewerber-analyse-2026-10-09.md`, Abschnitt 4.
Regel: Jede Änderung braucht danach Martins Go einzeln.

## Quick Wins (Ziel: in den nächsten Tagen, sobald Daten und Go da sind)

| # | Maßnahme | Daten, die wir noch sammeln | Woher | Status |
|---|---|---|---|---|
| 1 | GBP-Kategorien (Frankfurt + München): Haupt "Anwalt für Steuerrecht", dazu Strafverteidiger | Aktuelle Kategorien beider Profile. Frage: Passen die Kategorien zur echten Praxis? | GBP-Zugang (Voss hat Zugang erteilt, Rolle prüfen) und Dr. Stürzl | offen |
| 2 | GBP: Leistungen, Beschreibung, Öffnungszeiten vereinheitlichen, UTM am Website-Link | Heutige Leistungen, Beschreibung, Zeiten. Verbindliche Zeiten der Kanzlei (09:00 / 09:30 / 09:00–18:00 widersprechen sich). | GBP + Frau Jilg | offen |
| 3 | GBP: Fotos (Frankfurt 15+, München 10+) | Echte Fotos, Einwilligung der Personen. Neue Räume am Untermainkai. | Frau Jilg / Kanzlei | offen |
| 4 | Adresse Untermainkai 26 (GBP, Website, Schema, Verzeichnisse) | Endgültige Bestätigung der Adresse. Wann ist der Umzug im Profil sinnvoll (Re-Verifizierung). Liste aller Einträge mit Alt-Adresse. | Frau Jilg; Sheet Tab 11 | offen |
| 5 | Website: Title, H1, Meta der Startseite | Entwurf mit Berufsrecht-Check. Frage: Fachanwalt-Titel ja oder nein? | Dr. Stürzl | offen |
| 6 | Website: sitemap.xml, robots-Zeile, 404 `/schwerpunkte`, 4 tote Links | Super-User-Zugang Joomla (Linkemann / Framotec) | WhatsApp an Linkemann (Entwurf liegt vor) | blockiert |
| 7 | Kontaktformular + Rückruf, Sticky-Call, Notfallblock | Notfallnummern bestätigen. Einwilligungstext (DSGVO, §203). Ziel: Portal-Tab "Anfragen" (Staging fertig). | Frau Jilg, Martin | Staging fertig |
| 8 | Bewertungen: ruhiger, einwilligungsbasierter Ablauf | Kanzlei-Wunsch zur Anonymität. Wie viele Bewertungen in den letzten 12 Monaten (Frankfurt, Abruf schlug fehl). | Dr. Stürzl; DataForSEO erneut | offen |
| 9 | Pressestimmen verlinken lassen (15 Erwähnungen) | Kontakte in den Redaktionen (LTO, JUVE, ZRI …), wer schrieb den Beitrag | Sheet Tab 12 | Liste liegt vor |
| 10 | Verzeichnisse reparieren (Infobel, Cylex, anwalt.de "RAK Köln") | Login-Wege, wer hat die Einträge angelegt | Sheet Tab 11 | offen |

## Seiten und Struktur (danach, Wochen 5–8)

| # | Maßnahme | Daten, die wir noch sammeln |
|---|---|---|
| 11 | Säulenseite Steuerstrafrecht, Seite Steuerfahndung/Durchsuchung, Selbstanzeige | Fachliche Inhalte von Dr. Stürzl und Dr. Glogger. Echte Fälle ohne Mandantenbezug. |
| 12 | München-Seite | Ansprechpartnerin (Lea Wimmer), Anfahrt, Leistungen am Standort, Ist München im Paket? |
| 13 | Zusammenlegen der 9 dünnen Seiten, Redirects | Welche URLs ranken oder haben Links (GSC fehlt noch). |
| 14 | Interne Verlinkung, Menü "Steuerstrafrecht" | Heutige Link-Struktur (Crawl liegt vor). |
| 15 | Zwei Ratgeber-Artikel | Autor und Freigabe. |

## Daten, die uns noch fehlen (zuerst besorgen)

1. **Zugänge:** GBP-Rolle prüfen, Search Console, Google Ads, Hosting und Domain, Joomla Super User.
2. **Kundenantworten:** Fachanwalt-Titel, München im Paket, endgültige Adresse und Zeiten, Notfallnummern, Du/Sie.
3. **Messdaten:** München-Scan (Local-Falcon-Credits, Go), erneuter Abruf der Frankfurter Bewertungen, Scan 30 Tage nach Umsetzung.
4. **Wettbewerber vertiefen:** GBP-Leistungen und Beschreibungen der Top-Profile (nur über Maps im Browser lesbar), Heindl und ROSE & PARTNER in München.

## Audit läuft parallel

Offene Audit-Punkte: Search Console Daten, München-Wettbewerber vertiefen, GBP-Audit nach Zugang, Safari-Traffic prüfen, Kanzleisoftware (Antwort Frau Jilg), SEO-Bibliothek (Export läuft) auswerten.
| 16 | Disavow hochladen (Gruppe A, 37 Domains) | Search-Console-Zugang; Gruppe C geprüft; Frage an Kanzlei: Wurden Links gekauft? | offen |

## Local Falcon: Keyword-Auswahl (Martin, 09.10.2026)

Raster 7×7, 5 km, je Standort Frankfurt und München, Keywords ohne Stadt. Monatlicher Lauf, 10 Scans = 490 Credits.

| # | Keyword | Wichtigkeit |
|---|---|---|
| 1 | anwalt steuerstrafrecht | WICHTIG (Martin) |
| 2 | anwalt steuerhinterziehung | WICHTIG (Martin) |
| 3 | steuerfahndung anwalt | WICHTIG (Martin) |
| 4 | selbstanzeige anwalt | Zusatz |
| 5 | anwalt wirtschaftsstrafrecht | Zusatz |

Nicht in die Kampagne: Ads- und Seitenbegriffe ohne Local Pack, Stadt-Varianten, "steueranwalt", "strafverteidiger", Fachanwalt-Begriffe, Ratgeber-Begriffe.
Die Kampagne von Martin hat heute zu viele Keywords. Abgleich mit seinem Stand steht aus.
Keyword-Datei: `assets/stuerzl/keywords/keywords-frankfurt-2026-10-09.xlsx` (Blatt "Local Falcon Auswahl").

## Befunde 09.10.2026 (ProvenExpert-Frage)
- **Titel geklärt (öffentlich belegt):** Dr. Anja Stürzl ist seit 2021 Fachanwältin für Steuerrecht und seit 2022 Zertifizierte Beraterin für Steuerstrafrecht (DAA). Quellen: LTO, Fachseminare von Fürstenberg, R&W Fachkonferenzen. Vor Veröffentlichung von Dr. Stürzl bestätigen lassen. "Fachanwalt für Strafrecht" ist nicht belegt.
- **anwalt.de:** Kanzlei-Profil zeigt 5,0 bei 79 Bewertungen (Google Frankfurt nur 14). Das ist ein starkes Signal und eine Quelle, die KI-Plattformen zitieren. Nutzen und prüfen, ob Profil-Angaben und Adresse aktuell sind.
- **ProvenExpert:** Für die Kanzlei in zwei Suchen kein Profil gefunden (kein Beweis für Abwesenheit). Kein Treffer in den Local-Falcon-Berichten. ProvenExpert steht in unserer 44er-Verzeichnisliste. Niedrigere Priorität als anwalt.de.
