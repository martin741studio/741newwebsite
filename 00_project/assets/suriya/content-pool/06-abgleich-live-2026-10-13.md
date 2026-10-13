# Abgleich Content-Pool ↔ Live-Seite — Praxis Suriya, 2026-10-13

Basis: Content-Pool-Lauf 2026-10-11 (`04-pool/`, `05-sitetree/`), Live-Prüfung per curl am 2026-10-13. Grill-me mit Martin am 2026-10-13. Nichts davon ist live umgesetzt. Jede Live-Änderung braucht Martins Go pro Änderung.

## Schon erledigt (live geprüft)
- Startseiten-H1 "Naturheilpraxis in Ingelheim für Migräne & Nervensystem" (CP-LOC-001).
- MedicalBusiness-Schema mit Name "Praxis Suriya" (CP-LOC-008, Name ok).
- Bewertungs-Widget live, zeigt 12 Bewertungen (CP-AUT-004).
- /praxis-fuer-naturheilkunde-ingelheim/ leitet 301 auf / und steht nicht mehr in der Sitemap.
- /ganzheitliche-schmerztherapie/ zeigt nur noch 95 €.

## Entscheidungen
| # | Punkt | Befund 13.10. | Entscheidung |
| --- | --- | --- | --- |
| 1 | Preis Einzelsitzung | /nacken-schulter/ 85 € + 95 €; /kosten-abrechnung/ 80 € (plus 100/120/240 €) | **Coralie entscheidet im Dashboard.** Erstes echtes Freigabe-Element: 95 € ("741 empfiehlt", steht so auf /ganzheitliche-schmerztherapie/) gegen 85 €. Aktives Ja Pflicht (Preis). |
| 2 | HWG-Altseite | /suriya-praxis-fuer-naturheilkunde-ingelheim/ live (200), Krankheitsbilder-Liste, Sie-Form, 0 GSC | **301 → /** (Martin ja). Live nach Go. |
| 3 | /behandlungsangebot-2/, /praxis-suriya-ingelheim-nervenregulation-vagusnerv-akupunktur-ayurveda/ | live (200), 0 GSC, doppelt | Empfehlung 741: 301 → /behandlungsangebot/ bzw. /nervensystem-vagus-beruhigen/. Martin war unsicher → wartet auf Go. |
| 4 | /meinayurvedaangebot/ | live (200), 214 Impr., 2 Klicks | Empfehlung 741: 301 → /ayurveda-ingelheim/ 2 Wochen nach Punkt 2/3, Rankings vorher/nachher messen. /ayurveda-therapie/ (WP 1511) unberührt. Wartet auf Go. |
| 5 | Klick-zum-Anrufen | 0 tel:-Links auf 10 geprüften Seiten; Konkurrenz 7/11 | **Umsetzen** (Martin ja): tel:+491747411087 auf allen Seiten, Anruf-Klick als Event messen. Live nach Go. |
| 6 | Analysen | /migraene-analyse-ingelheim/ und /suriya-cranio-neuro-analyse/ beide live | **Zusammenlegen** (Martin ja, Go zum Zusammenlegen lag schon vor): Texte vergleichen, Fehlendes in Cranio-Neuro-Analyse übernehmen, 301. Live nach Go. |
| 7 | "Wer behandelt dich?" | auf keiner Leistungsseite | **Umsetzen** (Martin ja): Kurzblock mit verifizierten Stationen (Erlaubnis Wiesbaden 2010, Diplom Ayurveda 2012, CMD-Fortbildung 2016) auf den Leistungsseiten. Live nach Go. |
| 8 | Bewertungen | 12, Marktführer 37 | **WhatsApp-Vorlage + QR-Karte** für Coralie (Martin ja). Coralie antwortet selbst auf Bewertungen. Keine Anreize. |
| 9 | Gutschein-Weg | nur FAQ-Erwähnung | Nicht jetzt (Martin nicht gewählt). |

## Bewusst nicht nötig
Neue Ortsseiten · große Konkurrenz-Keywords (Bioresonanz, Kinesiologie, Thai-Massage; nicht im Angebot) · mehr Text (über dem Konkurrenz-Median) · mehr Blog-Beiträge.

## Vorlage Bewertungsbitte (Coralie an Patientin, nach dem Termin)
Hallo [Name], danke für deinen Besuch heute in meiner Praxis. Wenn du dich bei mir gut aufgehoben gefühlt hast, freue ich mich sehr über eine kurze Google-Bewertung. Das hilft anderen Menschen, mich zu finden: https://g.page/r/CdYiMAEOs1KiEBM/review
Herzliche Grüße, Coralie

## Umsetzung (Stand 13.10.)
Details und genaue Änderungen: `07-umsetzung-2026-10-13.md`.
- WP-Zugang per MCP gibt 401 (Benutzer von Coralie neu angelegt). Neues Anwendungspasswort von Martin nötig.
- 2, 5, 6, 7: vorbereitet, nichts live. 2 und 6 brauchen zusätzlich Coralies Bestätigung (ihre Vorgabe vom 13.10.: keine Seitenadressen ändern).
- 8: QR-Karte fertig in `00_project/assets/suriya/bewertungen/`, wartet auf Martins Freigabe zum Weitergeben.
