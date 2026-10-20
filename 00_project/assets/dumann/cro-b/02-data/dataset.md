> Aus dem Track-A-Lauf übernommen (`../cro/`), gilt unverändert für Track B. Stand 2026-10-11.

# Dataset — Naturheilpraxis Daniela Dumann

Stand: 2026-10-11. Quelle jeder Zeile angegeben. Nichts erfunden; `[FEHLT: …]` wo Daten fehlen.

## 1.1 Aktuelle Startseite: Text, Sektionen, CTAs, Bilder

Quelle: Firecrawl-Scrape https://danieladumann.de, 2026-10-11.

- **Title:** „Heilpraktikerin Berlin-Charlottenburg | Daniela Dumann" (44 Z.)
- **Meta Description:** „Heilpraktikerin in Berlin-Charlottenburg: Ernährungsberatung, Fasten, Darmsanierung und Aderlass nach Hildegard von Bingen. Termine nach Vereinbarung." (143 Z.)
- **H1:** „Heilpraktikerin in Berlin-Charlottenburg – Naturheilkunde nach Hildegard von Bingen"
- **Sektionsreihenfolge (Desktop + Mobil identisch):**
  1. Hero: H1 über unscharfem Blumenfoto-Hintergrund, keine Subline, kein CTA im Bild. Runder Button „Kurse & Seminare" verlinkt zu `/kurse-seminare` (kein Buchungs- oder Kontakt-CTA)
  2. Intro-Absatz (105 Wörter) + Hildegard-von-Bingen-Zitat
  3. 4 Service-Kacheln: Aderlass Therapie, Darm Sanierung, Ernährungsberatung & Fasten, Pflanzenheilkunde (je Bild + Titel + Link „Zur Therapie"/"Zu den Behandlungen")
  4. 4 weitere Service-Kacheln: Oligoscan & Mikronährstoffe, Schilddrüsen Behandlung, Homöopathie, Massagen & Anwendungen
  5. „Mein Ansatz" — Fließtext + Dr.-Edward-Bach-Zitat „Es gibt keine echte Heilung ohne eine Veränderung der Lebenseinstellung …" ⚠️ HWG-Grauzone, siehe 1.9
  6. „Über mich" — Kurztext + echtes Portraitfoto + 1 Kundenstimme ohne Namen/Quelle („Ein wunderbares ganzheitliches Konzept …" — H.)
  7. Kontaktformular (Vorname/Nachname/E-Mail/Telefon/Nachricht)
  8. Newsletter-Anmeldung
  9. Footer: NAP, Anfahrt (Bus/S-Bahn/Autobahn), Facebook-Link, Impressum/Datenschutz
- **CTAs gesamt:** „Termin buchen" (Header-Link zu `http://my.lemniscus.de/pss/21c5c780-26ba-4f11-8885-9a1d09a0c241`) nur auf Desktop sichtbar, siehe 1.3. „Kontakt" (Header, scrollt zum Formular). Kein WhatsApp-Link auf der ganzen Seite. Kein Telefon-Link im sichtbaren Content (nur im Footer als Text, nicht klickbar verifiziert).
- **Bilder:** 1 Hero-Hintergrund (Blumenfoto, unscharf), 1 runder Button mit mittelalterlicher Buchmalerei (nicht die Praxis), 8 Service-Kacheln (gemischt: Naturfotos ohne Praxisbezug, siehe 1.10), 1 echtes Portraitfoto bei „Über mich" (klein, unten).
- **Alt-Texte:** durchgehend Dateiname-Stil mit Keyword-Wiederholung („Aderlass Therapie Hildegard von Bingen Berlin Daniela Dumann Naturheilkunde"), kein beschreibender Alt-Text.

## 1.2 Screenshots

- Mobil 390×844, Hero: siehe `02-data/screenshots/` (im Chat gezeigt, nicht als Datei exportiert — Browser-Tool liefert Bild nur inline). Zusammenfassung: Hero zeigt nur Logo, Headline, „Kurse & Seminare"-Button. Kein CTA, kein Telefon, keine Bewertung sichtbar.
- Desktop 1440 px, Hero: Logo + Headline + „Termin buchen"-Button oben links, überlappt sichtbar mit dem Logo-Schriftzug (Layout-Fehler, siehe 1.3).

## 1.3 Mobile-Check

- **Scrolls bis zum ersten CTA:** auf 390 px ist im Hamburger-Menü kein Buchungslink vorhanden (Menüpunkte: Über mich, Therapien, Kurse & Seminare, Blog, Downloads, Kontakt). Der einzige erreichbare „CTA" ist der runde „Kurse & Seminare"-Button im Hero — das ist kein Termin-CTA, sondern ein Link zu Kursen. Das Kontaktformular liegt nach 6 vollen Bildschirmen (Scorecard-Item 4 = 0).
- **Layout-Fehler Desktop:** „Termin buchen"-Button überlappt den Logo-Schriftzug „Naturheilpraxis" sichtbar (Screenshot-Zoom bestätigt).
- **Cookie-Banner + Newsletter-Block:** auf Mobil blockiert ein eingebetteter Newsletter-Abschnitt mit großem X-Icon (kein Lightbox-Close, Teil des Seitenflusses) einen Großteil der ersten Bildschirme beim Scrollen — wirkt wie ein Popup, ist aber eine echte Sektion.
- **Buchungslink `my.lemniscus.de`:** im DOM auf Desktop vorhanden (Firecrawl + Live bestätigt), auf Mobil im Hamburger-Menü NICHT vorhanden → auf Mobil faktisch unerreichbar ohne Scrollen zum Footer-Telefon oder zum Formular.

## 1.4 Site-Struktur

Quelle: Firecrawl-Map + Google-Sitemap-Crawl vom 09.10.2026 (Team-Memory, 34 Seiten). Hauptnavigation: Über mich (+ Lebenslauf), Therapien (9 Unterseiten), Kurse & Seminare (12 Unterseiten), Blog, Downloads. Traffic nach GSC (90 Tage, Stand 30.09.2026): Top-Seiten nach Impressionen /behandlungen (325), /lebenslauf (302), /blog (271). `[FEHLT: aktuelle GSC-Zahlen seit 30.09. nicht neu gezogen, da Service-Account noch keinen Zugriff hat — Zahlen sind 11 Tage alt]`.

## 1.5 Suchnachfrage

**Update 2026-10-11, später am selben Tag:** Martin hat die IP-Whitelist für DataForSEO freigeschaltet, Live-Abruf jetzt erfolgreich (`search_volume/live`, location 2276, language de). Ersetzt die vorherige Schätzung.

| Keyword | Volumen/Mon | Wettbewerb | CPC | Quelle |
| --- | --- | --- | --- | --- |
| heilpraktiker berlin | **1.600** | LOW | 1,45 € | DataForSEO live 2026-10-11 |
| ernährungsberatung berlin | **1.600** | MEDIUM | 2,43 € | DataForSEO live 2026-10-11 |
| darmsanierung berlin | **90** | MEDIUM | 1,48 € | DataForSEO live 2026-10-11 |
| ernährungsberatung berlin charlottenburg | 30 | MEDIUM | 2,15 € | DataForSEO live 2026-10-11 |
| hildegard von bingen berlin | 50 | LOW | — | DataForSEO live 2026-10-11 (bestätigt: kein starker Praxis-Zielbegriff, siehe SERP-Check unten) |
| heilpraktiker/-in berlin charlottenburg | kein Volumen getrackt (zu long-tail) | — | — | DataForSEO live 2026-10-11, aber Autocomplete bestätigt die Suche real (siehe unten) |
| hildegard von bingen (national, ohne Ortsbezug) | 27.100 | — | — | DataForSEO (13.09.2026, älter) — fast ausschließlich Kirche/Bistum-Suchvolumen, nicht praxisrelevant |
| ernährungsberater ausbildung | 5.400 (HIGH) | — | — | DataForSEO (13.09.2026, älter) — nur für die Ausbildungs-/Kurs-Seiten relevant, nicht für die Praxis-Startseite |

**Live-SERP-Check „heilpraktiker berlin charlottenburg" (Google, 2026-10-11):** danieladumann.de erscheint NICHT auf Seite 1 der organischen Ergebnisse und NICHT im lokalen 4er-Pack (Soulhouse Berlin Charlottenburg, Manuela Lemke, Angela Käßner, Betty Timpe). Reale Konkurrenz-Domains auf Seite 1: betty-timpe.de, heilpraktikerberlin.com, heilpraktiker-seiffert.de, petra-butschko.de, natura-heilpraxis.de, manu-lemke.de.
**People Also Ask (echt, aus der SERP):** „Was kostet 1 Std Heilpraktiker?" · „Bei welchen Beschwerden zum Heilpraktiker?" · „Wird ein Heilpraktiker von der privaten Krankenkasse bezahlt?" → direkte FAQ-Kandidaten.

**Fazit für den Hero:** „heilpraktiker berlin" (1.600/Mon, LOW) ist der stärkste reale Kopfbegriff. „Charlottenburg" hat kein eigenes messbares Volumen, bleibt aber als Geo-Signal im Text/H1 wichtig (Autocomplete-real, Local-Pack-Relevanz). „Hildegard von Bingen" bestätigt sich erneut als schwacher Ziel-Suchbegriff für die Startseite.

## 1.6 Aktuelle Rankings

**Update 2026-10-11:** Live-Abruf `ranked_keywords/live` für danieladumann.de erfolgreich (63 rankende Keywords gesamt). **Zentraler Befund: die Domain rankt für KEIN einziges Praxis-/Patienten-Keyword** (kein „heilpraktiker berlin", kein „ernährungsberatung berlin", kein „darmsanierung berlin" in den Top-63). Alle 63 Rankings liegen auf Ausbildungs-/Kurs-/Blog-Inhalten:

| Keyword | Volumen | Position | Rankende URL |
| --- | --- | --- | --- |
| kräuterheilkunde | 320 | 15 | /ausbildung-kraeuterheilkunde |
| hildegard von bingen darmsanierung | 170 | 25 | /ausbildung-darmheilkunde |
| ausbildung kräuterheilkunde | 170 | 43 | /ausbildung-kraeuterheilkunde |
| ausbildung fastenleiter | 170 | 49 | /ausbildung-fastenleiterin |
| fasten nach hildegard von bingen | 320 | 69 | /hildegard-fasten |
| hildegard von bingen fasten | 480 | 70 | /hildegard-fasten |
| oligoscan | 260 | 63 | /oligoscan |

Vollständige Liste: alle 63 Treffer betreffen Ausbildungen (Kräuterheilkunde, Fastenleiter, Darmheilkunde), Kräuterlexikon-Blogposts oder einzelne Leistungs-Fachbegriffe (Oligoscan, Schilddrüsenmassage) — **keiner davon ist ein Begriff, mit dem jemand gezielt eine Heilpraktikerin für sich selbst sucht.** Das bestätigt und verschärft den Befund aus Schritt 2 der Diagnose: die Website ist organisch praktisch unsichtbar für neue Patient:innen, sichtbar nur für Ausbildungsinteressent:innen.

## 1.7 GBP-Fakten

Quelle: Google Maps Live-Check, 2026-10-11, Place-ID `ChIJwdcWYxZRqEcR8RDtWZzHMgI` (Keeper-Profil, Team-Entscheidung 26.09.2026).

- **Name:** Hildegard von Bingen Berlin Naturheilpraxis Daniela Dumann
- **Bewertung:** 5,0 ★ (9 Bewertungen)
- **Kategorie:** Heilpraktiker (alternative practitioner) + 7 Nebenkategorien (Naturopathic practitioner, Nutritionist, Health counselor, Education center, Homeopath, Alternative medicine practitioner, Massage therapist)
- **Adresse:** Nithackstraße 24, 10585 Berlin-Bezirk Charlottenburg-Wilmersdorf
- **Telefon:** +49 30 36430358
- **Website:** danieladumann.de
- **Öffnungszeiten:** nicht hinterlegt („Add hours" — Team-Entscheidung 26.09.: bewusst offen gelassen, passt zu „Termine nach Vereinbarung")
- **Fotos:** 7
- **Eröffnungsdatum (hinterlegt):** 15.07.2002 (passt zur Heilpraktiker-Prüfung 03.05.2002)
- **GBP-Performance (Local Falcon, Jul–Sep 2026):** 501 Impressionen (Juli 148, August 171, September 182, +23 % Trend)
- **Lokale Sichtbarkeit (Local Falcon Scan 01.10.2026):** „heilpraktiker charlottenburg" SoLV 0 % (5 von 49 Rasterpunkten gefunden), „ernährungsberatung charlottenburg" SoLV 0 % (1 von 49). ARP (durchschnittliche Rang-Position) 14–21.

## 1.8 Bewertungssprache

Quelle: Google Maps Reviews, 2026-10-11, eingeschränkte Ansicht (nicht eingeloggt). 3 von 9 Bewertungen mit Volltext gesehen, 6 weitere nur als Zahl sichtbar — `[FEHLT: 6 weitere Bewertungstexte, Google zeigt ohne Login nur eine begrenzte Auswahl]`.

Auffällig: **alle 3 sichtbaren Bewertungen sprechen über Danielas Ausbildungen/Kurse, keine über eine Behandlung als Patientin.** Das deckt sich mit dem GBP-Namen (Trainerin/Ausbilderin-Positionierung).

- „Ms. Dumann, as a lecturer, possesses extensive knowledge of Hildegard von Bingen's medicine, combined with many years of experience with patients. She conveys this knowledge in her training courses with such conviction and confidence …" — Scheila Beatriz da Silva-Hofmann, vor 1 Jahr
- „I can wholeheartedly recommend Daniela Dumann! My keen interest in Hildegard von Bingen's healing methods led me to discover Daniela and her work. I've already completed her training in 'Nutritional Therapy' and 'Fasting Guide' …" — Karin Siebert, vor 2 Jahren
- „Daniela conveyed the principles of Hildegard medicine to us with depth, heart, and soul. Daniela's practice is an enriching and rewarding experience for any interested therapist and a haven for all those interested in Hildegard medicine." — Dagmar Jarvis, vor 6 Tagen

**Top-Phrasen (aus den 3 sichtbaren Reviews):** „extensive knowledge", „many years of experience", „with conviction and confidence", „wholeheartedly recommend", „depth, heart, and soul", „enriching and rewarding experience". Alle auf Englisch übersetzt von Google — Originalsprache vermutlich Deutsch, `[FEHLT: deutsche Originaltexte]`.

## 1.9 Bestehende 741-Daten (Portal, NAP, frühere Entwürfe)

Quelle: `client_locations` (nap_status=locked), Memory `dumann-client`, Portal-Reports.

- **Kanonisches NAP:** Naturheilpraxis Daniela Dumann (Rechtsform), GBP-Name „Hildegard von Bingen Berlin Naturheilpraxis Daniela Dumann". Nithackstraße 24, 10585 Berlin-Charlottenburg. Tel 030 36430358, Mobil 0170 6011182. **E-Mail: praxis@danieladumann.de** (verifiziert, nicht office@).
- **Preise (von /behandlungen, live verifiziert 2026-10-11):** Erstanamnese/Erster Besprechungstermin (60 Min) **220 €**. Allgemeine Beratung und Behandlung je angefangene Stunde **150 €**. Homöopathische Erstanamnese (60–120 Min) 220–380 €. Abrechnung nach GebüH, private/Zusatzversicherte können teilweise Erstattung bekommen (keine Garantie, Gebührensätze von 1985).
- **Hausbesuche:** explizit NICHT mehr angeboten („Hausbesuche kann ich derzeit leider nicht mehr anbieten", Zitat von /behandlungen, 2026-10-11 live verifiziert). Die Footer-Zeile „nach Vereinbarung und Hausbesuche" ist veraltet und widerspricht dem. Für den Prototyp gilt: keine Hausbesuche erwähnen.
- **E-E-A-T (von /lebenslauf, live verifiziert):** Diplom-Sozialpädagogin (FH) seit 1985 · Heilpraktikerin seit 2002 · Psychologische Beraterin seit 2011 · Tanz- und Bewegungspädagogin seit 2013 · Entspannungstherapeutin seit 2018 · Vorstand Internationale Gesellschaft Hildegard von Bingen seit 2015, **Vizepräsidentin seit 2023** · Ausbildung bei Dr. Wighard Strehlow, Gudrun/Peter Germann (Phytaro Heilpraktikerschule Dortmund) · Medizinischer Arbeitskreis Internationale Hildegard Gesellschaft Engelberg (Schweiz) seit 2004 · Schilddrüsenpraktikerin-Ausbildung bei Dr. Berndt Rieger seit 2019 · Gründerin **Viriditas – Schule für Naturheilweisen** seit 2021 · Mitglied Fachverband Freie Heilpraktiker, FET, MeGeMit.
- **Besonderes Asset:** eigener **Hildegard Kräutergarten in der Schorfheide** (physischer Garten mit Hildegard-Heilpflanzen, für Seminare/Workshops genutzt) — einzigartiges, noch nicht prominent genutztes E-E-A-T-Element.
- **⚠️ HWG-Funde auf der bestehenden Website (nicht auf der Startseite, aber auf verlinkten Seiten, als Kontext für die Diagnose):** „Präkanzerose-Test (Untersuchung auf Vorstufen einer Krebserkrankung)" nennt Krebs direkt · „Amethystsalbe … leistet hervorragende Dienste bei Neurodermitis" ist ein Wirkversprechen · lange Krankheitslisten als „Schwerpunkte bei der Behandlung von …" formuliert · „Selbstheilungskräfte werden aktiviert" bei mehreren Massagen. Das Hero-Zitat „Es gibt keine echte Heilung ohne eine Veränderung der Lebenseinstellung …" (Dr. Edward Bach) ist eine Fremdaussage in Zitatform, grenzwertig (Heilungsbegriff), wird im neuen Hero nicht übernommen.
- **GA4:** Property „Naturheilpraxis Daniela Dumann – GA4", Measurement-ID G-3NTQVLCFG0, seit 30.09.2026 live, noch keine Historie.
- **GSC (90 Tage, Stand 30.09.2026, aus Wix-Dashboard übernommen):** 7.485 Impressionen (−47 %), 361 Klicks (−31 %) — Rückgang liegt vor Programmstart.
- **Wix-eigenes Analytics (90 Tage, Stand 30.09.2026):** 586 Sitzungen (+11 %), 321 Unique Visitors (+11 %). Quelle: Google organisch 200 (+18 %), Wix-E-Mail 138 (+55 %), Direct 133 (−27 %).
- **Booking-Link (bestätigt, Live-Check + Firecrawl 2026-10-11):** `http://my.lemniscus.de/pss/21c5c780-26ba-4f11-8885-9a1d09a0c241` — externes Terminbuchungssystem (Lemniscus), auf Desktop im Header als „Termin buchen" verlinkt, auf Mobil nicht erreichbar (siehe 1.3).

## 1.10 Brand-Visuals → siehe `brand.md`

## Kontaktkanal (von Martin am Start festgelegt)

**Primär: Buchungsformular** (`http://my.lemniscus.de/pss/21c5c780-26ba-4f11-8885-9a1d09a0c241`). Sekundär: Telefon 030 36430358 (allgemeine Sprechstunde) bzw. Mobil 0170 6011182. Kein WhatsApp-CTA für diesen Kunden — die Workflow-Vorlage "WhatsApp" wird im Prototyp durch "Termin buchen" (Lemniscus-Link) ersetzt, nach Regel 6/Operating Rule 10 (Kontaktkanal ist nicht immer WhatsApp).

## [FEHLT]-Liste (für Martin)

1. ~~DataForSEO-IP-Whitelist~~ — erledigt 2026-10-11, Martin hat die IP freigeschaltet. Zeilen 1.5/1.6 jetzt mit Live-Daten.
2. 6 weitere Google-Bewertungstexte (nur 3 von 9 ohne Login sichtbar).
3. Deutsche Originaltexte der Bewertungen (aktuell nur Google-Übersetzung ins Englische sichtbar).
4. Frischer GSC-Export seit 30.09.2026 (Service-Account-Zugriff fehlt noch, siehe Memory).
5. Ob der Lemniscus-Buchungslink echte freie Termine zeigt oder nur ein Kontaktformular ist — nicht getestet (keine Testbuchung ohne Zustimmung).
