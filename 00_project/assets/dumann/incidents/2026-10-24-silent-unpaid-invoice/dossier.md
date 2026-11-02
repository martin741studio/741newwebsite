# Incident-Dossier: Daniela Dumann — stille Kundin, Rechnung offen

Internes Dokument. Nicht an die Kundin senden.

**Datum:** 2026-10-24
**Zweig:** still (keine Antwort, keine Zahlung, Wix-Zugang entfernt)
**Status:** Stufe 1 gesendet am 24.10.2026, Stufe 2 gesendet am 30.10.2026 (beide Martin, Airmailer). Frist für ihre Rückmeldung: Mi 04.11.2026. Arbeit an der Website ruht bis dahin. Erinnerungs-Task `dumann-frist-2026-11-04` prüft am 05.11. 09:00 (Berlin) nur lesend und bereitet Stufe 3 vor.

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
| 15.10. | Telefonat Martin + Daniela: sie will die Schließung von Profil B nicht, Martin stellt sie zurück und sagt ihr Bescheid | Martin 02.11. |
| 24.10. | Martin: sie antwortet nicht mehr (zuletzt WhatsApp) und hat nicht auf Rechnung 741/091026 reagiert. Portal: 24 Karten zurück auf Entwurf (E4, E22, E23 bleiben offen), 3 Haken zurückgesetzt (Seiten live, Fotos, Team-Briefing) | Chat, Supabase |
| 30.10. | Martin: weiter keine Antwort von ihr; sie hat ihm nur eine Mail weitergeleitet (Absender daniela.dumann@live.de, Inhalt nicht bekannt). Stufe-2-Mail „Deine Entscheidungen warten seit Wochen auf dich“ von Martin per Airmailer gesendet, Frist Mi 04.11., Arbeit an der Website ruht. Portal-Stand: letzter Login 28.08., 3 Karten offen, 0 entschieden | Chat (Dumann-Dashboard), Supabase, `nachricht-stufe2-2026-10-30.md` |

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

## 4. Behauptungen gegen Prüfung (Kündigungsmail 02.11.2026, Datei `kundin-nachricht-2026-11-02.md`)

| # | Ihre Behauptung | Geprüft? | Befund |
| --- | --- | --- | --- |
| 1 | „vereinbarte Geld-zurück-Garantie" | ja, Transkript 20.08. + Angebots-Vorlage | **Teilweise.** Martin hat im Erstgespräch 20.08. eine „100 % Geld-zurück-Garantie" genannt, ausdrücklich gebunden an die Ziele nach den 90 Tagen („wenn diese Ziele nicht eingehalten werden"; „wir wollen auf die ersten Ränge kommen, das ist meine Garantie"). Die 741-Angebotsvorlage bindet sie an die Top-3-Ziele nach 90 Tagen. Ein schriftliches Angebot vom 27.08. wurde in Drive und Repo **nicht gefunden** (Rechnung verweist darauf). Das Programm läuft bis 13.12.; die Garantie greift nach Ablauf, nicht in Woche 10. Ihre Mitwirkung ist seit 17.09. ausgeblieben (keine Freigaben, Website-Zugang entzogen). |
| 2 | „Beginn 27.08., jetzt 9. Woche" | ja | Rechnung 27.08., Portal-Start 14.09. (Woche 8 ab Portal-Start, Woche 10 ab Rechnung). Unerheblich. |
| 3 | „Ausdrücklicher Schwerpunkt: umsatzsteuerpflichtiger Bereich (Kurse, Vorträge, Seminare). Die Praxis war nicht Gegenstand." | ja, Transkript 20.08., Rechnungstext, ihre Freigaben | **Falsch als Schwerpunkt, richtig nur als Steuerzuordnung.** Im Gespräch 20.08. ging es um Praxis UND Kurse; sie selbst: „meine Praxis hat immer noch mehr Zeit als die Arbeit an den Kursen". Die Zuordnung auf der Rechnung („der Sichtbarkeit des umsatzsteuerpflichtigen Kurs- und Ausbildungsbereichs zugeordnet") kam aus ihrem Wunsch im Gespräch, die 19 % Vorsteuer ziehen zu können („es müsste was sein, was sich nur auf die Kurse bezieht"). Der Leistungstext derselben Rechnung nennt Google-Profil, Website-Struktur, Verzeichnisse, Themen-Unterseiten. Sie hat am 04.09. den Woche-1-Fahrplan (3 Standbeine: Praxis lokal, Hildegard-Wissen, Kurse & Ausbildung) und am 17.09. die Google-Profil-Empfehlung für die Praxis **selbst freigegeben**. |
| 4 | „Keine erkennbare Strategie, keine konkreten Maßnahmen für die Kurse" | ja, Portal | **Falsch.** Portal: 44 Aufgaben nach Woche und Spur, 5 freigegebene Berichte, Statusseite „Dein SEO-Fahrplan" (14.10.), 27 Entscheidungskarten. Konkret für Kurse/Ausbildung: Säule 3 im Seitenbaum (von ihr freigegeben, ihr Wunsch „eigene Seite Ernährungsberatung HvB" aufgenommen); Karten E16 Ausbildung Gesundheitsberater/in (720 Suchen/Monat), E17 Ausbildung Kräuterheilkunde, E18 Ausbildung Fastenleiter/in, E19 Ernährungstherapie (1.410/Monat), E7 beendete Kurstermine, E21 Kurse & Seminare; Google-Profil: Kategorie „Education center", 7 Ausbildungs-/Kurs-Leistungen, Einzugsgebiet DE/AT/CH/IT für die Ausbildungen (09.10.); Suchnachfrage „ernährungsberater ausbildung" 5.400 im Woche-1-Bericht und Sichtbarkeits-Report. Sie hat davon nichts entschieden und ab 17.09. nichts mehr freigegeben. |
| 5 | „Doppelte Google-Unternehmensprofile weiterhin ungelöst" | ja, live 02.11. (Maps + Profil-API) | **Richtig, und das ist unser Punkt.** Google Maps zeigt heute zwei Einträge an der Nithackstraße 24: „Daniela Dumann" (5,0, 10 Bewertungen, Heilpraktiker) und „Hildegard von Bingen Berlin Naturheilpraxis Daniela Dumann" (5,0, 2 Bewertungen, „Geschlossen · Öffnet Di um 09:00"). Profil B wurde am 09.10. per Schnittstelle auf „dauerhaft geschlossen" gesetzt; das ist bei Google **nicht angekommen**, B zeigt normale Öffnungszeiten. Profil B ist heute nicht mehr mit unserem Konto verbunden (Schnittstelle: „not connected to a Google account"). Zusätzlich: die Umbenennung von Profil A (26.09.) ist öffentlich nicht sichtbar, Maps zeigt weiter „Daniela Dumann"; die Schnittstelle meldet den neuen Namen und markiert A intern als Duplikat von B. Screenshot `maps-zwei-eintraege-2026-11-02.jpg`. |
| 6 | „Vorschlag, die Website durch eine neue zu ersetzen, nicht abgestimmt, nicht vorbereitet" | ja, Portal + Mails | **Verdreht.** Vorgeschlagen wurde ein neues Startseiten-Design als Entscheidungskarte E22 (13.10.) mit Vorschau-Link, plus Design-Vorschau v3 per Mail (09.10.). Nichts wurde ersetzt; Stufe-2-Mail 30.10.: „Deine Website selbst ist unverändert." Die Website-Struktur (Seitenbaum) und der neue Startseiten-Text wurden von ihr am 04.09. freigegeben; ihre Frage dazu: „wer überarbeitet?". Die Eignung der Website wurde vor Vertrag in der Analyse-Seite (22.07.) und im Gespräch 20.08. beurteilt. |
| 7 | „Rate 2 zunächst nicht bezahlt, Entwicklung abgewartet" | ja | Sie hat die Nichtzahlung nie angekündigt. Zwischen 16.10. (Fälligkeit) und 02.11. keine Nachricht von ihr trotz Mails 24.10. und 30.10. und WhatsApp (Martin: fünf Nachrichten). Gleichzeitig hat sie den Website-Zugang entzogen. |
| 8 | „Weitere drei Wochen später: Problem besteht, keine Verbesserung erkennbar" | ja | Ohne ihre Entscheidungen und ohne Website-Zugang ruhte die Website-Arbeit (Stufe 2 am 30.10. angekündigt). Google-Suche: 162 Klicks in 28 Tagen, stabil; Bewertungen 9 → 10. Der Doppel-Eintrag (Punkt 5) besteht wirklich. |
| 9 | „Rechnung vom 09.10. ist gegenstandslos" | – | Ihre Auslegung. Die Rate war am 16.10. fällig; die Leistung bis dahin ist erbracht (siehe Zahlungserinnerung 24.10.). Entscheidung Martin. |

## 5. Ehrlichkeits-Check

**Belegt (Stand 02.11.):**

0. **Doppel-Eintrag bei Google besteht öffentlich weiter, auf ihren Wunsch.** Martin (02.11.): Der Antrag an Google (Profil B als Duplikat schließen) wurde gestellt (09.10.). In einem Telefonat danach sagte Daniela, sie wolle das nicht, es solle zurückgestellt werden. Martin hat es zurückgestellt und ihr Bescheid gegeben. Telefonat am 15.10.2026 (Martin 02.11.). Heute: zwei Einträge sichtbar, Profil B offen und nicht mehr mit unserem Konto verbunden, neuer Name auf A nicht veröffentlicht. **Martin 02.11.: an Google wird nichts mehr geändert, solange sie nicht zahlt.**
0b. **Überschrift (Martins Punkt 02.11.):** Als Martin die Seite auf ihren Wunsch auf den Ursprung zurückstellte, sagte sie, diese Überschrift habe sie nie gehabt. Es war ihre ursprüngliche. Seine Empfehlung war auf die gesuchten Begriffe optimiert; „Naturheilverfahren" lehnte sie als nicht existent ab, obwohl danach gesucht wird. Nicht in ihrer Mail, deshalb nicht in der Antwort.
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
- `nachricht-stufe2-2026-10-30.md` — Stufe 2: Frist Mi 04.11., Arbeit ruht, Liste des Vorbereiteten, 3 offene Karten, Login-Weg, Gespräch als Alternative. Kein Rechnungsthema (Martins Vorgabe: klarer Ton, kein „easy“). `verify_draft.py --final`: PASS. deslop_de: 5/5. Gesendet 30.10. (Martin, Airmailer).
- Keine Arbeitsübersicht, solange sie keine verlangt.

## 10. Stufen (Zweig „still")

| Stufe | fällig am | Status |
| --- | --- | --- |
| 1 Zahlungserinnerung + Status (Frist 31.10.) | 24.10.2026 | gesendet von Martin (Airmailer), geloggt in emails_log + activity_log |
| 2 Arbeit ruht (+3 Werktage) | Mi 29.10.2026 | gesendet 30.10.2026 von Martin (Airmailer, martin@741.studio), Frist für sie Mi 04.11. **Bounce 30.10. 07:54:** Microsoft lehnt die Absender-IP 185.2.31.101 (741.studio-Hosting) ab, Fehler 550 5.7.1 S3150. Mail nicht angekommen. **Erneut gesendet 30.10. von 741studio18@gmail.com (Gmail, Martin), gleicher Text, BCC martin@741.studio. Kein Bounce bekannt.** Hinweis: Mails von martin@741.studio an live.de/outlook/hotmail scheitern, bis der Hoster die IP entsperren lässt; die Stufe-1-Mail vom 24.10. ging evtl. denselben Weg (nicht geprüft) |
| 3 Optionen für Martin (+3 Werktage) | Do 05.11.2026 (Tag nach der Frist) | offen; Task `dumann-frist-2026-11-04` prüft Login/Karten/Nachrichten und legt nur interne Optionen vor |

## 11. Auflösung

- offen
