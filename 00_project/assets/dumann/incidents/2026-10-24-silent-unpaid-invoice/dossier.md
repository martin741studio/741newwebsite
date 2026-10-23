# Incident-Dossier: Daniela Dumann — stille Kundin, Rechnung offen

Internes Dokument. Nicht an die Kundin senden.

**Datum:** 2026-10-24
**Zweig:** still (keine Antwort, keine Zahlung, Wix-Zugang entfernt)
**Status:** in Arbeit. Martins Entscheidungen 24.10.: eine E-Mail mit Status und Zahlungserinnerung, Versand über Airmailer nach Go

## 1. Zeitachse

| Datum | Ereignis | Beleg |
| --- | --- | --- |
| 20.08. | Erstgespräch Martin + Daniela (Transkript) | Drive-Doc `121VZgHrpYaozfE6lJ1bTeVbZmy14z3hBxjc7gaXl4cc` |
| 28.08. | Portal-Zugang angelegt, Willkommensmail gesendet | `emails_log` 28.08. 09:36 |
| 29.08. | Vertrag & AVV, Stammdaten, Material: erledigt. Zugänge erteilt: Wix-Einladung an martin@741.studio, GBP + GA4 + Search Console an 741studio18@gmail.com | `onboarding_steps`, `access_grants` |
| 04.09. | Woche-1-Bericht und Seitenbaum von ihr freigegeben | `report_feedback` (author client) |
| 14.09. | Programmstart laut Portal (Ende 13.12.) | `programs` |
| 16.09. | Mail „Deine ersten Seiten-Texte sind fertig" | `emails_log` |
| 17.09. | **Letzte Aktion von ihr:** Startseiten-Text und Google-Profil-Empfehlung sektionsweise freigegeben, mit Änderungswünschen | `report_feedback` 17.09. 06:47–07:21 |
| 26.09. | Google-Profil live umgesetzt (Name, Kategorien, 40 Leistungen) | Memory dumann-client |
| 30.09. | GA4-Property neu angelegt, Search-Console-Verifizierung auf 741-Konto umgezogen (über Wix-Einstellungen) | Memory dumann-client |
| 01.10. | Mail „Dein Fortschritt" + Portal-Nachricht; Portal-Nachricht von ihr ungelesen | `emails_log`, `messages` read_by_client=false |
| 09.10. | 15 Portal-Aufgaben am 08./09.10. auf „erledigt" gesetzt | `tasks` |
| 13.10. | Mail „Deine neue Startseite und 12 weitere Punkte" + Portal-Nachricht zu ihren Hilfe-Anfragen (Zugänge); Nachricht ungelesen | `emails_log`, `messages` |
| 14.10. | Statusseite „Dein SEO-Fahrplan" live; Mail „Dein Zugang zum Portal ist wieder frei" (Passwort-vergessen-Anleitung) | `activity_log`, `emails_log` |
| 14.–19.10. | 27 Entscheidungskarten E1–E27 im Portal; keine einzige entschieden | `approval_items` alle `open`, go_by leer |
| 24.10. | Martin: sie antwortet nicht mehr (zuletzt WhatsApp) und hat nicht auf Rechnung 741/091026 reagiert. Portal: 24 Karten zurück auf Entwurf (E4, E22, E23 bleiben offen), 3 Haken zurückgesetzt (Seiten live, Fotos, Team-Briefing) | Chat, Supabase |

Letzte Aktion der Kundin **im Portal**: 17.09.2026. **Achtung (Martin 24.10.):** Es gab weiter WhatsApp-Kontakt. Portal-Daten zeigen nicht alle Kanäle. Nie „seit X nichts gehört" schreiben. Mails ab 01.10.: Zustellung „sent", Öffnung nicht messbar.

## 2. Bedingungen der Kundin (harte Vorgaben)

Keine bekannt. Sie hat keine Bedingungen gesetzt und keinen Zugangsentzug angekündigt.

## 3. Zugänge (live geprüft am 24.10.2026, Konto 741studio18@gmail.com, per Avatar-Menü bestätigt)

| System | Status | Wie geprüft |
| --- | --- | --- |
| Search Console `https://www.danieladumann.de/` | **geht.** 741 Studio = Inhaber (verifiziert), reporting-bot = Vollzugriff. Daniela selbst ist kein Nutzer auf der Property | Nutzer und Berechtigungen, Chrome |
| Google Analytics (GA4) | **geht.** Zwei Properties sichtbar: „741 Clients / Naturheilpraxis Daniela Dumann - GA4" (556758063) und „Google Ads-Konto / www.danieladumann.de" (523643026) | Property-Suche, Chrome |
| Google-Unternehmensprofil | **geht.** Beide Profile „Hildegard von Bingen Berlin Naturheilpraxis Daniela Dumann" (verifiziert) im Business Profile Manager | business.google.com/u/1/locations |
| Wix (Website) | **entzogen** (Martin bestätigt 24.10.). Konto martin@741.studio (Wix Studio) listet 7 Websites, danieladumann.de ist nicht dabei. Am 30.09. hatte Martin im Wix-Dashboard der Seite gearbeitet (GA4-Tag, Site-Verifizierung) | manage.wix.com, Website-Liste, Screenshot `wix-websites-liste-martin-741-2026-10-24.jpg` |
| Portal clients.741.studio | geht (unser System). Ihr Login existiert; Passwort-Reset-Anleitung am 14.10. gesendet | Supabase |
| Werbekonto | nicht Teil des Programms | – |

## 4. Behauptungen gegen Prüfung

Keine Behauptung der Kundin. Sie hat nichts gesagt.

## 5. Ehrlichkeits-Check

**Belegt:**

1. **Portal-Haken ohne Live-Beleg.** Am 08./09.10. wurden 15 Aufgaben auf „erledigt" gesetzt, darunter „INP < 200 ms, Core Web Vitals, Schema (LocalBusiness, Person, FAQ)", „Restliche Leistungs- & Standortseiten live", „Yelp, Gesundheits-Verzeichnisse, IHK, Verbände", „Fehlende Fotos nachliefern", „Team-Briefing durchführen, täglich Patienten fragen". Laut Memory 13.10. sind die neuen Seitentexte nicht live auf der Wix-Seite (Startseiten-Title zurückgesetzt, Tippfehler auf /ausbildung-vor-ort steht noch). Mehrere Haken betreffen Aufgaben der Kundin (Fotos, Team-Briefing), die sie nicht bestätigt hat. Sie kann die Haken sehen.
2. **Portal-Nachrichten an sie seit 01.10. ungelesen.** Zwei Nachrichten (01.10., 13.10.) stehen auf `read_by_client=false`. Sie liest das Portal nicht oder kommt nicht hinein (Hilfe-Anfragen am 13.10., Zugangs-Mail am 14.10.).
3. **27 Entscheidungskarten auf einmal** (13.–19.10.) ohne eine einzige Reaktion. Für eine stille Kundin ist das eine hohe Hürde.

**Zu prüfen (nicht in Kundentexte, bis geprüft):**

- Ob die neuen Seitentexte (Startseite, Pillar, Wechseljahre, Ernährungsberatung, Behandlungen) inzwischen auf danieladumann.de live sind. Ohne Wix-Zugang nur per Crawl prüfbar.
- Ob sie die Mails ab 01.10. erhalten hat (live.de-Adresse, Zustellung „sent" ist kein Öffnungsbeleg).

**Nicht unser Fehler, aber relevant:**

- Programm läuft seit 14.09. Nach dem Portal-Stand ist ihre Mitwirkung seit 17.09. ausgeblieben (Fragebogen Positionierung Schritt 5 noch offen).

### Portal-Haken gegen Live-Daten

| Aufgabe (Portal, erledigt am) | Live-Beleg | stimmt? |
| --- | --- | --- |
| INP < 200 ms, Core Web Vitals, Schema (08.10.) | kein Speedtest-Beleg im Ordner; Schema nur in Entwurfsseiten auf clients.741.studio | zu prüfen |
| Restliche Leistungs- & Standortseiten live (09.10.) | Memory 13.10.: Texte nicht auf der Live-Seite | **nein** |
| Yelp, Gesundheits-Verzeichnisse, IHK, Verbände (08.10.) | `client_citations` nicht geprüft | zu prüfen |
| Fehlende Fotos nachliefern (08.10., Aufgabe der Kundin) | keine Bestätigung von ihr | **nein** |
| Team-Briefing, täglich Patienten fragen (08.10., Aufgabe der Kundin) | keine Bestätigung von ihr | **nein** |

## 6. Thema: Rechnung offen und keine Reaktion

| Signal | Wert | Quelle |
| --- | --- | --- |
| Rechnung offen | **Rate 2: 741/091026 vom 09.10.2026, 1.849,50 €, fällig 16.10.2026** (Martin 24.10.: nur Rate 2 offen). Rate 1: 741/270826 vom 27.08., fällig 03.09., bezahlt | Drive US-LLC-Ordner `NaturheilpraxisDumann-741-091026.xlsx`, `…-270826.xlsx` |
| Programmpreis laut Preisliste | 3.699 € in 2 Raten (Muster Suriya: 1.849,50 € je Rate) | Ledger-Zeile Suriya, Memory pricing |
| Google-Suche Klicks pro Woche | 35 (KW 24.08.) · 43 · 45 · 27 (KW 14.09.) · 32 · 34 · 33 (KW 05.10.) | `gsc_daily_performance`, Stand 13.10. |
| Search Console gesamt seit 22.07. | 428 Klicks, 73 indexierte Seiten, 81 nicht indexiert | Search Console Übersicht 24.10. |
| Search Console letzte 28 Tage (24.09.–21.10.) | 162 Klicks, 1.770 Impressionen, CTR 9,1 %, Position 25,1. Top: „daniela dumann heilpraktikerin berlin" 28, „daniela dumann" 27, „hildegard von bingen ausbildung" 3; „kräuterheilkunde" 104 Impressionen, 0 Klicks | Search Console Leistung 24.10., Screenshot `gsc-leistung-28-tage-2026-10-24.jpg` |
| GA4 letzte 7 Tage | 11 aktive Nutzer, 2 Key Events | GA4 Home 24.10. |
| Google-Bewertungen | 9 × 5,0 (Stand 13.10.) | Memory |

Schluss: Die Sichtbarkeit ist stabil, kein Einbruch. Das Schweigen hat keinen sichtbaren Leistungsgrund. Mögliche Gründe: Portal-Zugang verloren (Hilfe-Anfragen 13.10.), Überforderung durch 27 Karten, oder sie hat sich innerlich verabschiedet. Keiner ist belegt.

## 7. Interne Angebote (nur für Martin)

- Karten reduzieren: alle E-Karten bis auf 3 zurück auf Entwurf, damit ihr nächster Login nicht mit 27 Entscheidungen beginnt.
- Programmzeit: die Wochen ohne Mitwirkung hinten anhängen, als Angebot, wenn sie sich meldet.
- Klare Trennung der zwei Themen: Zahlung (sachlich, Frist) und Programm (Status, ruht ohne ihre Mitwirkung).

## 8. Impact und liegen gebliebene Arbeit

- Ohne Wix-Zugang: keine Website-Änderungen möglich (Seitentexte, Title/Description, Behandlerseite, Redirects). SEO-Arbeitsplan vom 09.10. ruht.
- Ohne ihre Entscheidungen: alle 27 Karten blockiert, nichts darf umgesetzt werden (Martins Regel 14.10.: Live-Seite nicht anfassen, bis Daniela Feedback gibt).
- Weiter möglich ohne sie: Google-Profil-Pflege, Verzeichnisse, Messung. Ob das ohne Zahlung weiterläuft, entscheidet Martin.

## 9. Entwürfe

- `nachricht-entwurf.md` — erste Zahlungserinnerung (Rate 2, Frist Freitag 31.10.) mit Leistungsstand, nach Martins Korrektur 24.10. (kein „nichts gehört", Reporting, kostenpflichtige Werkzeuge, fertige Bausteine im Gesamtpreis, Schweigen keine Option). `verify_draft.py`: PASS. deslop_de: 5/5.
- Keine Arbeitsübersicht, solange sie keine verlangt.

## 10. Stufen (Zweig „still")

| Stufe | fällig am | Status |
| --- | --- | --- |
| 1 erste Nachricht (Status + Zahlungserinnerung, Frist 31.10.) | nach Martins Go, E-Mail über Airmailer | Entwurf fertig, wartet auf Go |
| 2 Arbeit ruht (+3 Werktage) | 3 Werktage nach Versand von Stufe 1 | offen |
| 3 Optionen für Martin (+3 Werktage) | 3 Werktage nach Stufe 2 | offen |

## 11. Auflösung

- offen
