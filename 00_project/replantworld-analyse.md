# Replant World (replantworld.io) — Analyse
**Erstellt:** 2026-08-18 · 741 Studio
**Kontakt:** Philip "Phil" Dickenson (Gründer) — hat Martin die URL als Intro zu seiner Arbeit geschickt

---

## 1. Was sie anbieten

**Positionierung:** "Marketplace & AI Carbon Calculation Engine — a financial solution for people, biodiversity and climate."

Tree-NFT-Marktplatz mit Verifizierungs-Layer. Der Ablauf:

| Schritt | Was passiert |
|---|---|
| **Tree Capture** | Bäume werden beim Pflanzen fotografiert (ground-based dMRV), Experten-Review |
| **Nature Tech** | Jeder Baum bekommt Satelliten-Standort + Metadaten via **POPTech™** (Proof of Planting) |
| **Tree NFTs** | Verifizierte Bäume als unveränderliche NFT-Records |
| **Your Growth** | Mit dem Wachstum wächst der Impact — NFTrees können "retired" oder gehandelt werden |

**Zweiseitiger Marktplatz:** Sponsors (Käufer: Firmen/Privatpersonen) ↔ Planters (Indigene, lokale Communities, NGOs)

**Live-Daten auf der Startseite (ihr stärkstes Asset):**
- 40.473 minted trees · $46.238 planting cost · $40.265 CO₂ value · $86.503 NFT value
- Live **EU-ETS-Carbon-Preis-Chart** (€78–87)
- **IUCN Red List**: 29 Critically Endangered, 207 Endangered, 8.155 Vulnerable, 5.309 Data Deficient, 30.476 Least Concern
- **Artenmix ~75 Arten**: Tall-stilt mangrove 36,6 % · Balangeran 15,2 % · Pulai 12 % · Durian 6,6 % · True Mangrove 3,9 % · Petai 3,6 % · Langsat 3,0 % · Cashew 2,4 %

→ Artenliste stark **indonesisch** (Kalimantan Torfmoor + Mangroven), Kontakt **+62 881-0376-17294**, support@replantworld.io

---

## 2. Der Build (technisch)

| Punkt | Befund |
|---|---|
| Stack | **Next.js** (App Router, Turbopack), React SPA |
| Speed | TTFB ~1,07 s — ok |
| Chatbot | **Chatbase** AI-Chatbot eingebunden |
| Seitenzahl | **nur 5**: `/`, `/about`, `/nfts`, `/planters`, `/sponsors` |
| Auth | Login / Sign Up vorhanden |
| **Title-Tags** | ⚠️ **auf JEDER Seite identisch** — "Replant World - Tree NFT Marketplace" |
| Meta-Description | nur Startseite |
| H1 | Startseite 2 · `/nfts` **0** |
| **Schema.org** | ❌ **keins** |
| **Open Graph** | ❌ **keins** — geteilte Links ohne Vorschau |
| Canonical | ❌ keins |
| **robots.txt** | ❌ **existiert nicht** (404) |
| **sitemap.xml** | ❌ **existiert nicht** (404) |
| **Analytics** | ❌ **kein GA4, kein GTM, kein Pixel** |
| Content-Tiefe | 377–575 Wörter pro Seite |
| Social-Links | ⚠️ **Platzhalter** — instagram.com, linkedin.com, youtube.com **ohne Handles** |
| Blog/Ressourcen | ❌ /blog, /news, /resources, /faq, /calculator, /projects → **alle 404** |

---

## 3. Wie sie Reichweite bekommen — die ehrliche Antwort

**Praktisch keinen organischen Traffic.** Die Seite ist ein *Produkt*, keine *Traffic-Maschine*:
- Kein Sitemap + kein robots.txt → Google hat keine Crawl-Führung
- 5 Seiten mit identischen Titles → nichts zum Ranken
- Kein Schema/OG → keine Rich Results, jeder Share sieht kaputt aus
- Keine Analytics → sie sehen nicht, woher jemand kommt
- Social-Links tot → der naheliegendste Kanal ist nicht mal verdrahtet

**Realer Traffic heute:** Direkt/Netzwerk (Gründer, LinkedIn) · B2B-/NGO-Partnerschaften · WhatsApp (+62) · Chatbase-Chatbot · Web3-/Climate-Tech-PR
→ **100 % Push (Outbound/Netzwerk), ~0 % Pull (Suche/Content)**

---

## 4. Wettbewerb — wer wie Reichweite holt

| Plattform | Indexierte Seiten | Traffic-Motor |
|---|---|---|
| **Treedom** (Marktführer) | **~5.000+** (12 Child-Sitemaps) | Programmatic + UGC im großen Stil |
| **Evertreen** | **303** | Content + programmatic Projekte |
| **veritree** | **172** | B2B-Content + Resources-Hub |
| **Ecosapiens** | klein | Web3-/Community-getrieben |

**Treedoms Modell (die Blaupause):**
1. **UGC-Event-Seiten: ~5.000 URLs** — jeder Firmenkunde bekommt eine öffentliche Wald-Seite (`/organization/enel/event/enel-sustainability-day/`). **Die Kunden erzeugen das SEO** — und teilen die Seiten selbst.
2. **Programmatic Country-Pages** — `/countries/` in 5+ Sprachen
3. **Eigene Blog-Subdomain** — blog.treedom.net mit **1.090 Seiten**
4. Alles **×5 Sprachen** (en/it/es/de/fr)
5. **Gifting-Winkel** (`gift-a-tree`, `how-to-gift`, sogar `horoscope`) → Geschenk-Intent, stark saisonal

**Evertreen:** 177 News + 91 Projekte + 24 Baumarten-Seiten + **CO₂-Rechner** (`/co2-calculator`) + Zertifizierungs-LPs (verra-carbon-credits)

**veritree:** wenig Seiten, aber scharfer B2B-Title ("Tree Planting Company **for Businesses**") + Resources-Hub

---

## 5. Suchvolumen — das Kernproblem

### 🚨 "tree nft" = **10 Suchen/Monat** — ihre gesamte Positionierung

| Keyword | US /Mo | UK /Mo | CPC |
|---|---|---|---|
| carbon footprint calculator | **8.100** | — | $4,47 |
| carbon credits | **5.400** | 1.900 | $8,98 / €18,87 |
| carbon offset | 2.900 | 1.600 | $12,12 |
| esg reporting | 2.900 | — | $17,90 |
| carbon removal | 880 | — | $1,21 |
| corporate sustainability | 720 | — | **$48,17** |
| voluntary carbon market | 390 | 260 | $9,84 |
| buy carbon credits | 320 | 170 | $15,54 |
| verra carbon credits | 320 | — | $6,26 |
| mangrove restoration | 260 | — | **$28,20** |
| biodiversity credits | 210 | 210 | $21,36 |
| plant a tree gift / gift a tree | 420 | — | $7,37 |
| tree planting company | 210 | — | $18,17 |
| carbon offsetting companies | 70 | 110 | **$75 (UK)** |
| **tree nft** | **10** | **10** | — |

**Kategorie gesamt: ~23.000/Mo (US), ~28.000/Mo (US+UK).**
Bei CPCs von $18–75 entspricht das bei 500 organischen Besuchern/Monat auf Buyer-Intent-Terms **$9.000–37.000/Monat Ad-Äquivalent**.

---

## 6. Die Lücke in einem Satz

> Replant World hat die **besten Daten** der Kategorie (Live-Carbon-Preis, 40k Bäume, IUCN-Status, 75 Arten) und zeigt sie auf **5 Seiten, die Google nicht mal richtig crawlen kann** — während Treedom jeden von 5.000 Kunden in eine indexierte Landingpage verwandelt.

### Ungenutzte Assets, die sie bereits besitzen
| Asset | Der Zug |
|---|---|
| Artendaten (75 Arten) | 75 programmatische Seiten ("Balangeran", "mangrove restoration" @ $28 CPC) |
| Planter-/Projektdaten | Per-Projekt-Seiten (Evertreen hat 91) |
| **Sponsor-Daten** | **Treedom-Style Brand-Forest-Seiten** — höchster Hebel, Kunden teilen selbst |
| **AI Carbon Calculation Engine** | **Öffentlicher CO₂-Rechner** → zielt auf 8.100/Mo, exakt Evertreens Playbook |
| Live-EU-ETS-Preis | Öffentliche Carbon-Preis-Tracker-Seite → wiederkehrende Besuche + Link-Magnet |
| IUCN-Daten | Biodiversitäts-Content — hat sonst niemand in der Tiefe |

### Sofort-Fixes
Sitemap · robots.txt · unique Titles · Schema · OG-Tags · **GA4** (aktuell komplett blind)

---

## 7. Strategische Empfehlung

1. **Sprache umstellen** von "Tree NFT" auf **Carbon / Biodiversity Credits** (10/Mo → 28.000/Mo Kategorie)
2. **Den Rechner ausliefern**, den sie schon gebaut haben (AI Engine → öffentlicher CO₂-Rechner)
3. **Arten- + Sponsor-Daten in Seiten verwandeln** (Treedom/Evertreen-Playbook)

---

## 8. Gesprächsführung mit Phil (er hat die URL als Intro geschickt)

**Nicht** mit dem Audit einsteigen — er hat es als Vorstellung seiner Arbeit geschickt, nicht zur Bewertung.

**Opener (gesendet):** Bezug auf konkrete Details (Live-Carbon-Preis, Artenmix, Balangeran/Mangroven) + Indonesien-Verbindung (Martin 10 Jahre, Canggu) + POPTech als "harter Teil" anerkennen → offene Frage nach seiner Journey.

**Fragen-Arc:**
1. Ursprung/Stage: Wie lange baust du schon? Solo oder Team? Funded/bootstrapped?
2. **"Wo kommen deine Sponsoren heute her?"** ← die wichtigste Frage, verrät die ganze Akquise-Realität
3. Vision: Wo soll es in 12 Monaten sein? Verifizierungs-Standard oder Marktplatz?
4. Constraint: Was hält es gerade wirklich auf?
5. Erst dann: Machst du Marketing selbst — willst du dabei Hilfe?

**Was NICHT in Gespräch 1:** Das NFT-Positionierungsproblem (10 Suchen/Mo). Er hat die Firma danach benannt — das ist Zweitgespräch-Material, und nur wenn er sagt, dass er wachsen will.

**Signale lesen:**
| Er sagt… | Situation | Zug |
|---|---|---|
| "Netzwerk/Konferenzen/Partnerschaften" | Sales-led, keine Distribution | Die echte Öffnung — als Wachstum framen |
| "pre-revenue / validieren" | Früh, kein Budget | Freund sein, langes Spiel |
| "funded / raising" | Budget da, braucht Traction | Stärkster Fit |
| "eher Mission-Projekt" | Kein Skalierungswunsch | Nicht pitchen, Beziehung halten |
| "Marketing ist abgedeckt" | Anderer besitzt es | Peer bleiben, später wieder |

**Tools-Hinweis:** Ahrefs = "Insufficient plan" → keine Backlink-/Traffic-Zahlen verfügbar. Alle Zahlen oben aus direktem Crawling + DataForSEO (IP-Whitelist beachten, ändert sich).
