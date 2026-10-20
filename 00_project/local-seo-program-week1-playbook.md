# Playbook: Local-SEO-Programm — Woche 1 (agent-abarbeitbar)

Destilliert aus dem ersten Durchlauf mit Praxis Suriya (14.–15.08.2026).
Ziel: Ein Agent kann Woche 1 für jeden neuen Programm-Kunden weitgehend selbst abarbeiten.
Referenz-Ergebnis: https://clients.741.studio/r/8dbd937730d2/praxis-suriya-woche1-2026-08.html

## Inputs (vor Start sammeln)
- Kundenname, Stadt, Nische/Wunsch-Positionierung, Website-URL, GBP-Name
- Drive-Kundenordner-ID, Portal `client_id` (Tabelle `clients` in 741-portal Supabase)
- Erst-Analyse-Sheet (falls vorhanden), Kickoff-Notizen
- Credentials: `.secrets/dataforseo.env` · `.env` (CLIENTS_FTP_*, LF_API_KEY) · Drive-MCP (741studio18@gmail.com) · Supabase-MCP (741-portal `galjmtozcgxcwtzkzbpi`)

## Harte Regeln (gelten für JEDEN Schritt)
1. **Nichts wird umgesetzt** (GBP/Website/etc.) — alles wird auf der Report-Seite gesammelt; Kunde gibt gebündelt frei. Auch mit Zugriff: nur notieren.
2. **Keine Auto-Ingestion ins Dashboard.** Scans laufen manuell, Ergebnisse als datierte Screenshots, erst nach Martins Freigabe sichtbar.
3. **Jede Behauptung braucht echte Daten** — nie aus Erst-Analyse/Website ableiten, immer live verifizieren (Reviews, Öffnungszeiten, Kategorien).
4. **Volumen-„0" = keine Daten, nicht keine Nachfrage** → Google-Autocomplete-Gegencheck, Themen-Baum bauen.
5. **HWG-Check bei Health-Kunden:** keine Erfolgs-/Heilversprechen; „kann / Ziel / unterstützen"; Review-Antworten neutral danken; HWG-Box auf die Seite.
6. **Review-Ziel = 2× Marktführer** (laufendes Jahr) + Etappe „überholen" (Leader+1).
7. **Keine Teamnamen** in Kundendokumenten — nur „741".
8. **Ansprache (Partner/Backlinks/Verzeichnisse) macht immer 741** — Kunde gibt nur frei + ergänzt eigenes Netzwerk.
9. **Keine Tool-Namen** auf der Kundenseite (kein „DataForSEO"/„Local Falcon" — stattdessen „Google-Daten", „Maps-Messung"). Methodik trotzdem erklären (warum diese Wettbewerber, welche Suchbegriffe, national vs. lokal).
10. Kunden-Ansprache „du", wenn Kunde selbst „du" nutzt — nie Sie-Variante anbieten.
11. Preise/Kassen/Parken etc. nie erfinden → gelbe `[von Kunde bestätigen]`-Platzhalter.
12. SEO-Wissensbasis konsultieren (Memory `seo-knowledge-base`, Drive-Ordner `1UXKKe4Tadl115MeaP_YbaQJavyop1vEJ`).

## Schritte

### 1 · Live-Verifikation der Erst-Analyse
- GBP live prüfen: Reviews (Anzahl + Sterne), Öffnungszeiten, Kategorien (Local Falcon `listAllLocalFalconLocations` query=<name> liefert Place-ID + Kategorien + Reviews sofort), Fotos, Posts, Buchungslink.
- Website prüfen (WebFetch): CMS/SEO-Plugin, H1-Struktur, Canonical, Schema, GA4, NAP, **komplette Leistungsliste** (Quelle für Services + Themenbaum-Abgleich).
- Jede Abweichung zur Erst-Analyse → „Korrekturen"-Box auf der Seite.

### 2 · Wettbewerber + Faktoren
- Suche `heilpraktiker/<kategorie> <stadt>` + `<kategorie>praxis <stadt>` (WebSearch) → Top 2–3 benennen, Auswahl auf der Seite begründen.
- Echte Review-Zahlen via `searchForLocalFalconBusinessLocation` (Achtung: Timeouts → Retry mit anderem Wortlaut oder `listAllLocalFalconLocations`).
- Faktor-Analyse je Wettbewerber: Keyword im Namen? Exact-Match-Domain? Reviews/Rating? Alter/Citations? Kategorien? GBP-Aktivität (Posts/Q&A)? Behandlerzahl? → Tabelle „Warum sie vor dir liegen" + „Unser Konter" je Faktor.
- DR/Backlinks: **DataForSEO `backlinks/summary/live` funktioniert** (verifiziert 31.08., ~0,024 $/Target) — eigene Domain + Top-3-Wettbewerber ziehen: rank, backlinks, referring_domains, dofollow-Anteil, first_seen (= Link-Alter!). **Gotcha: nur EIN Target pro Call** („You can set only one task at a time") → loopen. Ahrefs-MCP `public-domain-rating-free` geht NICHT (Insufficient plan) — nicht versuchen. Destillieren: Autoritäts-Gap, wer ist einholbar (90 Tage), Beweis-Sätze („X hat riesige Domain, aber 0 Reviews → nur Y % SoLV → Reviews schlagen Links in Maps").

### 3 · Suchvolumen + Themenbaum
- DataForSEO `keywords_data/google_ads/search_volume/live` (location_code 2276, language de). Script-Muster: Scratchpad `suriya-kw2.cjs`; Keyword-Mix: lokal breit + Nische/Symptom national + Nachbarstadt-Kombis.
- Autocomplete-Gegencheck: `suggestqueries.google.com/complete/search?client=firefox&hl=de&gl=de&q=<seed>` + Alphabet-Soup → Themen-Baum, 4 Cluster (Bildung national / Kauf-Intent / Zielgruppen-Beleg / Lokal-Maps).
- Je Cluster: „Website heute" (✓/△) + Aktion + Warum. National vs. lokal IMMER labeln.

### 4 · Baseline-Scans (alle Service-Keywords)
- Place-ID aus `listAllLocalFalconLocations`. Je Keyword: `runLocalFalconScan` 7×7, 5 km, google (49 Credits/Scan; nie retrien — queued!).
- Poll via `getLocalFalconReport` mit fieldmask `keyword,arp,solv,found_in,image,heatmap`.
- Grid-PNGs laden → FTP `clients.741.studio/r/<hash>/scans/<datum>-<kw-slug>-grid.png` (Datum im Dateinamen, nie überschreiben).
- `scans`-Tabelle (741-portal): eine Row je Messung mit JSON (keyword, date, arp, solv, found_in, Wettbewerber-Werte, Bild-URLs, approved_by_martin).
- Auf der Seite: Sektion „Ranking-Tracking — datierte Messungen": Übersichtstabelle (Keyword / Ø Position / Top-3-Fläche / Bedeutung) + datierte Karten-Cards + 90-Tage-Ziele.

### 5 · Report-Seite (das zentrale Freigabe-Dokument)
- EIN self-contained HTML, 741-CI (#fac118, DM Sans, Logo als data-URI), Muster: `/tmp/suriya-week1.html` bzw. Live-Referenz oben.
- Sektionen in dieser Reihenfolge: Korrekturen → Wettbewerbs-Vergleich + Faktor-Tabelle → Suchvolumen (echte Zahlen) → Warum-diese-Spitze (Herleitung!) → Themen-Baum → Top-5-Fokusse (Aktuell→Verbesserung→Warum) → Plan A–D (GBP/Website/NAP+Backlink-Box/Positionierung) → E Fertige Texte → F Ranking-Tracking → G Partner → H Methode → Footer.
- Status-Badge: „Vorschlag — zur Sammel-Freigabe durch <Kunde>".
- **Freigabe-JS** einbauen: pro Sektion „✓ Passt"/„💬 Kommentar" + global „Alles freigeben" → POST auf Supabase `report_feedback` (anon key, client_id, report_slug); Trigger erzeugt `admin_notifications`. Code-Muster im Suriya-Report.

### 6 · Fertige GBP-Texte (Sektion E)
- Beschreibung ≤750 Zeichen (Zeichen zählen!), 6 Services mit Kurztext (Quelle: Website-Leistungen — Quelle auf der Seite nennen), 8 FAQ, Review-Antwort-Vorlagen.
- Review-Antwort-Formel: **Dank + exakte Leistung + Ort + Marke** (KI liest Antworten als Quelle). Bebilderte Patientinnen-Anleitung (Wer/Wo/Wie, 3–4 Screenshots, QR) als eigener 1-Seiter spezifizieren.
- Öffnungszeiten-Hinweis: so lang ansetzen wie telefonisch erreichbar (außerhalb der Zeiten weniger Sichtbarkeit).

### 7 · Partner-Liste (Sektion G)
- 25+ komplementäre Betriebe (KEINE direkten Wettbewerber): Frauen-Gesundheit/Hebammen/Gyn, Physio/Osteo, Yoga/Pilates/Gym, Ernährung, Apotheken. Quellen: Local Falcon Business-Suche (echte Ratings) + WebSearch.
- Backlink-Daten checken: wer verlinkt den Kunden SCHON → als „Verlinkt dich schon" markieren (Beweis, dass das Modell funktioniert).
- 4 Modelle: Backlink-Tausch · Auslage/Flyer+QR · Affiliate beidseitig · gemeinsame Workshops.
- Text-Regel: 741 kontaktiert; Kunde gibt frei + ergänzt Netzwerk.

### 8 · Methoden-Konzept (Sektion H)
- Vorbild: sabrinagritzmacher.com — Muster: EINE benannte Methode, Bildungs-first-Seite (Bildung → Nutzen-Liste → Methode als Bild → Testimonials → eigene Story → Call).
- 3 Namensvorschläge (einer = Praxisname-Methode als Empfehlung; einer aus bestehendem Begriff des Kunden; einer ergebnisnah als Programm-Name). Empfehlung: Methode (Marke) + Programm (Produkt) kombinieren.
- 3 Phasen aus den ECHTEN Leistungen destillieren + 9-Block-Programmseite + Ranking-Verzahnung (Ziel-Keyword, GBP-Service, Post-Serie, Lead-Magnet).

### 9 · Deploy + Portal
- FTP: `node`-Script mit basic-ftp (CLIENTS_FTP_* aus `.env`), Ziel `clients.741.studio/r/<12-hex-hash>/<kunde>-woche1-<jahr-monat>.html`. Hash: `openssl rand -hex 6`.
- Portal: INSERT `client_reports` (client_id, title, period_label, storage_path=volle URL) — Report-Viewer lädt URLs direkt. NUR nach Martins Go.
- Drive: Link-Doc in den Kundenordner (`create_file`, text/plain → Google Doc).
- Jede Zwischenversion an Martin senden (SendUserFile) — Feedback einarbeiten, gleiche URL überschreiben.

### 10 · Übergabe an den Kunden
- Kurze „du"-Nachricht (Martin sendet) + Martin nimmt Loom-Erklärvideo auf (Report ist viel Info).
- Kunde: ① GBP-Einladung an 741studio18@gmail.com (Anleitung im Portal `access_grants.guide`) ② Freigabe/Kommentare direkt auf der Seite.
- Danach: Umsetzung + zweite Messung nach ~2 Wochen (nur nach Freigaben).

### 11 · Mess- & Monitoring-Plan (Local-Falcon-Aktivitäten, auf die Seite!)
Als eigener Block in Sektion F — Kunde muss den Messrhythmus sehen (Retention). Immer ohne Tool-Namen formulieren:
| Messung | LF-Funktion | Rhythmus |
|---|---|---|
| Maps-Ranking (alle Service-Keywords) | Geo-Grid-Scan google | alle 2 Wochen (nach Umsetzungen) |
| KI-Sichtbarkeits-Check | Scans chatgpt/gemini/gaio/aimode (SAIV + zitierte Quellen → Content-Steuerung) | monatlich |
| Bewertungs-Analyse | Reviews Analysis (Velocity, Sentiment, genannte Leistungen) | monatlich |
| Wettbewerber-Vergleich | Competitor Reports (vs. Top 2) | monatlich |
| Quartals-Trend | Trend Reports (Verlaufskurve, Strategie-Gespräch) | alle 3 Monate |
| Profil-Wächter | Falcon Guard (ungewollte GBP-Änderungen) | dauerhaft, ab GBP-Zugriff |
| Apple-Maps-Check | Apple-Scan / Eintrag anlegen | 1× Basis |
NICHT nutzen: Falcon Agent (Auto-Posts/Auto-Replies) — Content machen wir selbst (HWG, eigene Texte).
Alles manuell zum Stichtag + Martins Freigabe vor Portal-Sichtbarkeit (Regel 2).

## Tool-Rezepte & Datenquellen (Stand 31.08.2026 — verifiziert an Suriya + Maria Brasse)

**Reihenfolge immer: erst vorhandene Daten ausschöpfen, dann neue (kostenpflichtige) erheben.**

### Quelle 0 · Die Prospect-Review-Page (WIRD OFT VERGESSEN!)
- Liegt unter `04_site/review/<slug>/index.html`. **Die Detail-Daten stecken in `window.PROSPECT_DATA` im `<script>`-Block** — NICHT nur den sichtbaren Text extrahieren (Text-Extraktion wirft die Scripts weg und zeigt Platzhalter wie „58/100", die JS später überschreibt!).
- Enthält: Place ID, Scan-Baseline (Datum!), gbpAudit/websiteAudit/citationAudit je Element mit Status, competitors mit Sichtbarkeits-%, quickWins, roadmap, growthMetrics.
- Alte Scans dazu: `listLocalFalconScanReports` mit `placeId=<aus PROSPECT_DATA>` → `report_key` → `getLocalFalconReport` (s. u.). **Kostet nichts — vorhandene Reports lesen ist frei.**

### Quelle 1 · Live-Website (kostenlos, Python/curl)
Ein Script, eine Seite: Title, Meta-Description, alle H1s, JSON-LD-Blöcke (welche @type? LocalBusiness fehlt?), GA4 (`G-XXXX`)/GTM (`GTM-`), Yoast/RankMath, WordPress-Marker, OG-Tags (og:image fehlt oft!), Canonical, `<img>` ohne alt, Ladezeit. Impressum separat laden → NAP (Name/Adresse/Tel/Mail) + Navigation → komplette Leistungsliste (= Basis für Services + Themenbaum-Abgleich).

### Quelle 2 · Local Falcon (MCP-only, Bearer; Scans kosten Credits — Reports lesen ist frei)
- `listLocalFalconScanReports {placeId, fieldmask:"reports.*.report_key,reports.*.date,reports.*.keyword,reports.*.arp,reports.*.atrp,reports.*.solv,reports.*.grid_size"}` — IMMER zuerst, spart Credits.
- `getLocalFalconReport {reportKey, fieldmask:"report_key,date,keyword,arp,atrp,solv,found_in,unique_competitors,insights.osolv,rankings.by_solv,places.*.name,places.*.solv,places.*.arp,places.*.rating,places.*.reviews,places.*.url,places.*.categories"}` → **voller Wettbewerbs-Datensatz** (alle ~30 Anbieter mit SoLV/ARP/Reviews/Domain/Kategorien) aus EINEM alten Scan. Das ist die Wettbewerbs-Vergleichs-Tabelle.
- `searchForLocalFalconBusinessLocation {term, proximity}` für einzelne Wettbewerber-Daten. **Gotcha: Timeouts bei Marken-Namen ohne Kategorie-Wort** („ShuiGuru" → 3× Timeout). Timeout ≠ „kein GBP"! Retry mit anderem Wortlaut oder Place ID aus Quelle 0 nutzen.
- Neue Scans (`runLocalFalconScan`, 7×7=49 Credits): NUR nach Martins Go, nie retrien (queued).

### Quelle 3 · DataForSEO (Login `.secrets/dataforseo.env`, Basic-Auth)
- **Suchvolumen:** `keywords_data/google_ads/search_volume/live`, POST `[{keywords:[...bis 25+], location_name:"Germany", language_name:"German"}]` — ~0,09 $ für 25 Keywords. Keyword-Mix: Money-Terms national + je Nische-Cluster 3–5 Begriffe + Lokal-Terme. Ergebnis nach Volumen sortieren, Cluster-Summen bilden.
- **Backlinks:** `backlinks/summary/live`, EIN Target pro Call (loopen!), ~0,024 $/Target. Eigene Domain + Top-3-Wettbewerber.
- „0/None" = keine Daten, nicht null Nachfrage → Regel 4 (Autocomplete-Gegencheck). Aber: wenn der ganze Cluster 0 zeigt UND Autocomplete nur 5 Varianten liefert → ehrlich als „Mission, kein SEO-Kanal" einordnen (Beispiel Maria: „feng shui schule").

### Quelle 4 · Google Autocomplete (kostenlos)
`https://suggestqueries.google.com/complete/search?client=firefox&hl=de&gl=de&q=<seed>` — je Cluster 3–5 Seeds (auch mit Leerzeichen am Ende für neue Vervollständigungen). Ziel: **80–100+ echte Varianten gesamt**, je Cluster gezählt. Auswerten auf: Money-Signale („kosten", „in der nähe"), Stadt-Muster (→ spätere pSEO-Chance), Long-Tail-Dichte je Cluster (reichster Cluster = Content-Prio).

### Quelle 5 · Portal-DB (741-portal, REST + `standup.env`-Login)
`clients`, `programs`, `tasks`, `onboarding_steps`, `access_grants`, `client_reports` — Ist-Stand des Kunden prüfen, Review-Page via `client_reports` verlinken (title, period_label, storage_path=volle URL).

## Detailtiefe-Benchmarks (daran wird der Report gemessen)
1. **Wettbewerb:** ALLE Anbieter aus dem Scan (25–30), nicht nur die Top 3. Tabelle: SoLV, ARP, Reviews, Backlinks/Ref-Domains + first_seen, Kategorien(-anzahl!), Positionierung, Nischen-Seiten ja/nein.
2. **Beweis-Sätze aus Rohdaten** — jede Strategie-Aussage braucht ihren Zahlen-Beleg im Format „X → Y, deshalb Z" (z. B. „Arndt: 10 Reviews → 66,7 % SoLV → 10–15 Reviews bewegen diesen Markt").
3. **Jede Zahl mit Datum + Quelle** (Scan-Datum, Abfrage-Datum). Nie Platzhalter aus HTML übernehmen.
4. **Autocomplete: 80+ Varianten**, je Cluster: Queries · „Website heute" (✓/△/✗) · Aktion · Warum.
5. **Faktor-für-Faktor-Konter:** je Top-Wettbewerber-Faktor eine konkrete Gegenmaßnahme.
6. **Ehrlichkeit:** Lieblings-Nischen ohne Volumen klar als Mission/Direktvertrieb labeln; „Ehrlicher Stand"-Box mit der unbequemen Zahl.
7. **Texte fertig, nicht skizziert:** Beschreibung ≤750 Zeichen (zählen!), alle Services, 6–8 FAQ (Pflicht: Kosten-Frage), Review-Vorlagen, Anleitungs-Aufbau. Unbekanntes als gelbe `[von Kunde bestätigen]`.

## Abnahme-Checkliste (vor „fertig" — jede Zeile abhaken)
☐ Quelle 0 gelesen (PROSPECT_DATA + alte Scans)? ☐ Korrekturen-Box (Erst-Analyse vs. live)? ☐ Voller Wettbewerbs-Datensatz (alle Scan-Anbieter)? ☐ Backlink-Vergleich (eigene + Top 3)? ☐ Suchvolumen echt + Cluster-Summen? ☐ Herleitungs-Tabelle „Warum diese Spitze"? ☐ Themenbaum 80+ Varianten? ☐ Top-5-Fokusse? ☐ A–D-Tabellen mit Prio/Ist/Ziel/Wer? ☐ E-Texte komplett? ☐ F Baseline + Ziele + Monitoring-Plan? ☐ G Partner (echte Betriebe oder klar als Woche-2 markiert)? ☐ H Methode (3 Namen + Empfehlung + Phasen + Seitenblöcke)? ☐ I Säulen? ☐ Vollständigkeits-Check-Tabelle gegen Referenz-Report (Suriya) im Dokument? ☐ Offene Punkte mit Credit-/Go-Bedarf explizit?

## Offene Automatisierungs-Kandidaten (für den späteren Agent-Run)
- Scan-Batch: alle Service-Keywords in einem Rutsch scannen + Bilder + DB + Seiten-Sektion generieren
- Report-Seiten-Generator: Sektionen aus JSON-Config statt Hand-HTML (analog Review-Page-config.js-Muster)
- Autocomplete-Themenbaum als wiederverwendbares Script (liegt: Scratchpad `suriya-topictree.cjs` — ins Repo übernehmen)
- report_feedback-UI als Snippet-Template für alle Reports
- Money Prompt Set (10–30 KI-Test-Prompts) je Kunde + monatlicher AI-Visibility-Check
