# Demand: Dr. Stephan Meyer, "Doctor Change" (agent A, 2026-10-12)

Quelle der Angebote: stephanmeyer.com Menü und /services/, /coach/, /trustedadvisor/ (curl). Angebote: Executive Coaching, psychologisches Coaching (Unternehmer, Vorstände, Investoren), Keynotes, Trusted Advisor (Berater im Monatspaket), Heilige-Kuh-Workshop, Vision-to-Reality-Workshop, Business Wargaming. Sitz Wurzbach (Thüringen), Kunden bundesweit und online.

## 1. Suchvolumen (Deutschland, Google Ads, pro Monat)
Evidenz: `evidence/dfs-volumes-ads.json` (Kosten 0,09 USD).

| Suchbegriff | Volumen | CPC (EUR/USD laut Ads) | Art |
|---|---|---|---|
| führungskräfte coaching | 2.900 | 10,06 | national, Hauptangebot |
| business coach | 2.900 | 5,15 | national |
| veränderungsmanagement | 390 | 5,26 | national |
| psychologisches coaching | 390 | 5,14 | national |
| change management beratung | 260 | 17,63 | national |
| executive coach | 210 | 6,94 | national |
| executive coaching | 210 | 6,94 | national (Google fasst beide Schreibweisen zusammen, gleiche Zahl) |
| change management coach | 90 | 7,62 | national |
| business coach jena | 10 | 2,30 | Dienstleistung + Stadt |
| business coach erfurt | 10 | keine Angabe | Dienstleistung + Stadt |
| executive coach erfurt | Google gibt keine Zahl heraus | | Dienstleistung + Stadt |
| coaching saalfeld | Google gibt keine Zahl heraus | | Dienstleistung + Stadt |
| business coach gera | Google gibt keine Zahl heraus | | Dienstleistung + Stadt |
| executive coaching kosten | Google gibt keine Zahl heraus | | Kosten |

Zusammengefasste Varianten: "executive coach" und "executive coaching" = ein Thema (210). "führungskräfte coaching" und "business coach" haben je 2.900 und sind die zwei grössten Nachfrage-Begriffe.

## 2. Gap-Keyword mit Stadt (für den Karten-Scan)
**Vorschlag: "business coach jena", 10 Suchen pro Monat.** Alternative mit gleicher Zahl: "business coach erfurt" (10).
- Echtes Hauptangebot: ja (Business- und Executive-Coaching steht auf /coach/ und /services/).
- Nachfrage: ja, aber sehr klein (10 pro Monat). Alle anderen Stadt-Begriffe (Erfurt "executive coach", Saalfeld, Gera) haben keine Zahl. Das heisst: Nachfrage unter der Messgrenze.
- Seine Seite steht nicht in den organischen Top 20 für "business coach jena" (Evidenz: `evidence/dfs-serp-2.json`, Standort Jena, depth 20; stephanmeyer.com kommt nicht vor). Die SERP hat ein local_pack und eine KI-Übersicht; die Karten-Plätze liefert dieser Endpunkt nicht, der Scan entscheidet.
- Ehrliche Einschätzung für den Orchestrator: Es gibt genau einen Stadt-Begriff mit Nachfrage pro Stadt, und er ist klein. Der Scan zeigt ein echtes Loch auf der Karte in Jena, beweist aber keine grosse Nachfrage. Sein Geschäft ist national und online. Die Hauptaussage der Seite sollte der nationale Begriff tragen, der Scan ist Beleg für die lokale Lücke, nicht der Haupthebel.

## 3. Bester nationaler Begriff für die Textabschnitte
**"führungskräfte coaching", 2.900 pro Monat, Wettbewerb LOW** (Evidenz: `evidence/dfs-volumes-ads.json`). Zweiter Begriff: "business coach" (2.900). Seine Seite steht nicht in den Top 20 (Evidenz: `evidence/dfs-serp-1.json`, Deutschland, depth 20; stephanmeyer.com kommt nicht vor).

## 4. Wettbewerber-Anbieter für den Seitenlängen-Check (keine Verzeichnisse)
Evidenz: `evidence/dfs-serp-1.json`, `evidence/dfs-serp-2.json`.
1. https://www.fuehrungskompetenzen.com/fuehrungskraefte-coaching/ (national, Platz 6)
2. https://www.kommunikationswerk.de/fuehrungskraefte-coaching/ (national, Platz 13)
3. https://coach-und-mentor.de/ (national, Platz 8)
4. https://dianawalther-action.coach/business-coach-jena/ (Jena, Platz 10)
5. https://www.vorwerg.de/personalentwicklung/coaching/ (Jena, Platz 17)
Ausgeschlossen als Verzeichnis oder Akademie: coach-liste.de, trustlocal.de, haufe-akademie.de, ihk.de, tuev-nord.de, greator.com.

## 5. Namenssuchen
- "doctor change" (Evidenz: `evidence/dfs-serp-name.json`): Die Marke ist nicht auffindbar. Alle 8 organischen Treffer sind englische Seiten über Arztwechsel (Mayo Clinic, HealthPartners, Reddit, Quora). stephanmeyer.com und seine Marke kommen nicht vor.
- "stephan meyer change management" (Evidenz: `evidence/dfs-serp-name2.json`): Auf Platz 1 und 2 steht `stephanmeyer.biz` (Seiten "Transformation & Change" und "Kontakt"), nicht `stephanmeyer.com`. Seine eigene Seite stephanmeyer.com/de/coach/ steht erst auf Platz 8. Dazwischen: complicated.life (Therapeuten-Verzeichnis), Xing (Platz 4), navitalglobal.com, redner-veraenderung-psychologie.de (seine Keynote-Seite, Platz 6), brainguide.de, Pressemeldung einpresswire.com (Platz 11). Offen: Ob stephanmeyer.biz zu ihm gehört oder ein Namensvetter ist, belegen diese Daten nicht. Das muss Agent B / der Orchestrator an der Seite prüfen, bevor es in die Seite kommt.

## 6. Schädliche Links (Spam-Score ab 60)
- **63 von 1.139 verweisenden Domains** haben einen Spam-Score von 60 oder mehr (5,5 %). Evidenz: `evidence/dfs-refdomains-spam.json` (total_count 63) und `evidence/dfs-backlinks-summary.json` (referring_domains 1.139; 1.331 Links; Domain-Rang 141; Spam-Score des ganzen Profils 47).
- Beispiele: backlinksguide.com (75), wheretobuybest.link (80), rank-seo-now.shop, bestnz-poker-casinoslot.com, betwinnermirror.com, realwinningonlinecasino.online (je 70). Fast alle Domains tragen "backlinks", "checker", "casino" oder ".shop" im Namen: gekaufte SEO-Linkmüll-Seiten.

## Kosten
Gesamt 0,1513 USD (Ledger `cost_ledger.jsonl`): Volumen 0,09, SERP je 0,0035 / 0,0035 / 0,002 / 0,002, Backlinks-Summary 0,024, Referring-Domains 0,0263. Kein Task-Status 40101 aufgetreten.
