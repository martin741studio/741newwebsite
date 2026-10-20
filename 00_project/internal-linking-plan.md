# 741.Studio – Internal-Linking-Plan (DE + EN)

> Stand 2026-08-08. Ziel: Themen-Silos bilden, Link-Equity gezielt auf Money-Pages lenken, Verweildauer erhöhen, Google die Themen-Autorität zeigen.

## Ausgangslage (verifiziert)

- **29 Blogbeiträge** (identische Slugs unter `/pages/blog/` **und** `/de/pages/blog/`).
- **Die Beiträge haben 0 interne Links im Fließtext** – nur die Canonical-Selbstreferenz. Das ist der größte, schnellste Hebel.
- **Der `/de/pages/blog/` ist eine 1:1 englische Dublette** (kein `lang`, englische Titel). → Duplicate-Content-Risiko; es gibt aktuell **keinen** echten deutschsprachigen Blog für den DACH-Markt.
- Blog-Themen = **Bali/englischer Markt**. Der deutsche Teil der Website sind die Service-Seiten + Case-Studies.

## Grundregeln (für jede Umsetzung)

1. **3–6 kontextuelle Links pro Beitrag**, im Fließtext, nicht als Linkliste am Ende.
2. **Beschreibender Ankertext** (keyword-nah, natürlich) – nie „hier klicken". Ziel-Keyword der Zielseite als Anker.
3. **Silo-Prinzip:** innerhalb eines Themenclusters dicht verlinken; über Cluster hinweg nur gezielte „Brücken".
4. **Jeder Beitrag verlinkt mind. 1× auf eine Money-Page** (Service/Angebot) – dorthin fließt die Equity.
5. **Money-Pages verlinken nach unten** auf ihre 2–4 stärksten Cluster-Beiträge (Themen-Autorität).
6. **Case-Studies** als Beweis von Money-Pages + passenden Beiträgen verlinken; Case-Study zurück auf die Service-Seite.

---

# TEIL 1 — ENGLISCH (Bali-Blog) — Hauptpotenzial

## Cluster A · Web Design / Development
**Pillar (Hub):** `/pages/bali-web-design.html` (Money-Page)
**Content-Pillar-Beitrag:** `web-design-bali.html`

Spokes: `website-design-bali`, `web-designer-bali`, `web-development-bali`, `web-designer-canggu`, `best-web-design-bali`, `best-website-design-bali`, `best-web-designer-bali`, `best-web-development-bali`, `best-web-design-agency-bali`, `premium-web-development-studio-bali`, `web-design-cost-bali`, `web-development-pricing-bali`, `webflow-vs-wordpress`

| Von | → Nach | Ankertext (Vorschlag) |
|---|---|---|
| jeder A-Beitrag | `/pages/bali-web-design.html` | „custom web design in Bali" / „our Bali web design service" |
| jeder A-Beitrag | `web-design-bali.html` (Content-Pillar) | „high-performance website engineering" |
| `web-design-cost-bali` | `web-development-pricing-bali` | „detailed web development pricing" |
| `web-design-cost-bali` | `seo-retainer-price-bali` | „ongoing SEO retainer costs" (Brücke → B) |
| `webflow-vs-wordpress` | `web-development-bali` | „bespoke custom development" |
| `best-web-design-agency-bali` | alle 4 `best-web-*` | „see how we compare as a web design agency" |
| `web-designer-canggu` | `web-designer-bali` | „web designer for all of Bali" |
| `/pages/bali-web-design.html` | `web-design-bali`, `webflow-vs-wordpress`, `web-design-cost-bali` | „read our guide to …" |

## Cluster B · Local SEO
**Pillar (Hub):** `/pages/bali-local-seo.html` (Money-Page)
Spokes: `best-local-seo-bali`, `seo-agency-bali`, `seo-retainer-price-bali`

| Von | → Nach | Ankertext |
|---|---|---|
| jeder B-Beitrag | `/pages/bali-local-seo.html` | „local SEO service in Bali" |
| `seo-agency-bali` | `best-local-seo-bali` | „how to rank #1 in the Google Maps local pack" |
| `seo-retainer-price-bali` | `seo-agency-bali` | „what an SEO agency actually does" |
| `best-local-seo-bali` | `reputation-management-bali` | „reviews are a ranking factor" (Brücke → C) |
| `best-local-seo-bali` | `web-design-bali` | „a fast website supports rankings" (Brücke → A) |
| `/pages/bali-local-seo.html` | `best-local-seo-bali`, `seo-agency-bali`, `seo-retainer-price-bali` | „learn more about …" |

## Cluster C · Reputation / Review Removal
**Pillar (Hub):** `reputation-management-bali.html`
Spokes: `google-review-removal-bali`, `best-google-review-removal-bali`, `remove-bad-google-reviews`, `right-to-be-forgotten-2026`

| Von | → Nach | Ankertext |
|---|---|---|
| jeder C-Beitrag | `reputation-management-bali` (Pillar) | „full reputation management" |
| jeder C-Beitrag | `/pages/bali-local-seo.html` | „clean, optimized Google Business Profile" |
| `google-review-removal-bali` | `remove-bad-google-reviews` | „the legal dispute process step by step" |
| `best-google-review-removal-bali` | `google-review-removal-bali` | „how review removal works" |
| `reputation-management-bali` | `best-local-seo-bali` | „turn a clean profile into #1 rankings" (Brücke → B) |
| `right-to-be-forgotten-2026` | `remove-bad-google-reviews` **und** `scrub-photo-metadata` | Brücke C ↔ E |

## Cluster D · Automation / n8n
**Pillar (Hub):** `best-automation-agency-bali.html`
Spokes: `n8n-developer-bali`, `n8n-whatsapp-automation`

| Von | → Nach | Ankertext |
|---|---|---|
| jeder D-Beitrag | `best-automation-agency-bali` (Pillar) | „our automation agency work" |
| `n8n-whatsapp-automation` | `n8n-developer-bali` | „certified n8n developer" |
| `n8n-developer-bali` | `n8n-whatsapp-automation` | „WhatsApp automation in practice" |
| jeder D-Beitrag | Booking (`calendly.com/martin-233/15-minute-meeting`) | „book a free automation audit" |
| `n8n-developer-bali` | `web-development-bali` | „custom development that ties it together" (Brücke → A) |

## Cluster E · Privacy / Security / Decentralization (Top-of-Funnel-Autorität)
**Pillar (Hub):** `serverless-p2p-digital-life.html`
Spokes: `decentralized-vpn-dvpn`, `scrub-photo-metadata`, `secure-data-wiping`, `right-to-be-forgotten-2026`

| Von | → Nach | Ankertext |
|---|---|---|
| jeder E-Beitrag | `serverless-p2p-digital-life` (Pillar) | „build a resilient, private digital life" |
| `decentralized-vpn-dvpn` | `serverless-p2p-digital-life` | „go fully serverless" |
| `secure-data-wiping` | `scrub-photo-metadata` | „scrub metadata before sharing" |
| `right-to-be-forgotten-2026` | `reputation-management-bali` | „manage what shows up about you" (Brücke → C) |

**Brücken-Übersicht (Cross-Cluster, sparsam):** A↔B (Speed↔Ranking), B↔C (Reviews↔Ranking), C↔E (RTBF↔Privacy), A↔D (Dev↔Automation).

---

# TEIL 2 — DEUTSCH (Service-Seiten-Mesh + Case-Studies)

> Es gibt **keine echten deutschen Blogbeiträge** – daher hier zuerst das Verlinken der bestehenden DE-Seiten, dann die Empfehlung, einen DACH-Blog aufzubauen.

## 2a · Bestehende DE-Seiten verlinken

Vorhandene DE-Seiten: `local-seo.html`, `website-design.html`, `google-maps-fix.html`, `google-ads-1/2/3.html`, `meta-ads-1/2.html`, `about.html`, `faq.html` (alle unter `/de/pages/`), plus `/pages/growth-plan-de.html`, `/pages/sichtbarkeits-analyse.html`.
DE-Case-Studies: `veronika-schlirf`, `astrid-lengauer`, `bernd-laserstein`, `maria-abel`.

| Von | → Nach | Ankertext |
|---|---|---|
| `de/…/local-seo` | `de/…/google-maps-fix` | „Google-Maps-Ranking reparieren" |
| `de/…/local-seo` | `case-studies/veronika-schlirf`, `astrid-lengauer` | „Ergebnis aus der Praxis: Platz 15 → 1" |
| `de/…/local-seo` | `/pages/sichtbarkeits-analyse.html` | „kostenlose Sichtbarkeits-Analyse" |
| `de/…/local-seo` | `/pages/growth-plan-de.html` | „unser 90-Tage-Programm" |
| `de/…/google-maps-fix` | `de/…/local-seo` | „vollständige Local-SEO-Betreuung" |
| `de/…/website-design` | `de/…/local-seo` + Case-Studies | „damit die Website auch gefunden wird" |
| `de/…/google-ads-1/2/3` | `de/…/meta-ads-1/2` | „Meta-Ads als zweiter Kanal" (Cross-Sell) |
| `de/…/google-ads-*` + `meta-ads-*` | `de/…/local-seo` | „organische Sichtbarkeit als Fundament" |
| `de/…/about` | Case-Studies + `local-seo` | „Ergebnisse für Kunden" |
| `de/…/faq` | `local-seo`, `website-design`, `growth-plan-de` | jeweils themenpassend |
| jede DE-Case-Study | passende Service-Seite + `sichtbarkeits-analyse` | „so machen wir das" / „kostenlose Analyse" |

## 2b · Empfehlung: echten DACH-Blog aufbauen (Priorität)

Der `/de`-Blog sollte **nicht** die englischen Bali-Artikel spiegeln (Duplicate Content). Stattdessen 6–10 deutsche Beiträge für die Zielgruppe (Praxen/Coaches/Heilberufler). Vorschläge (Slug → Ziel-Money-Page):

| Vorgeschlagener Beitrag | verlinkt auf |
|---|---|
| `local-seo-fuer-praxen` (Pillar) | `de/…/local-seo`, alle Spokes |
| `google-unternehmensprofil-optimieren` | `de/…/local-seo`, `google-maps-fix` |
| `mehr-google-bewertungen-bekommen` | `de/…/local-seo` |
| `warum-google-nicht-die-beste-praxis-belohnt` (existiert schon als Seite!) | `de/…/local-seo`, Case-Studies |
| `google-ads-vs-local-seo-fuer-praxen` | `de/…/google-ads-1`, `de/…/local-seo` |
| `website-die-patienten-bringt` | `de/…/website-design`, Case-Studies |

> Hinweis: `warum-google-nicht-die-beste-praxis-belohnt.html` liegt bereits unter `/pages/` – idealer erster DACH-Blog-Anker; von `de/…/local-seo` darauf verlinken und umgekehrt.

---

## Umsetzungs-Reihenfolge (Impact zuerst)

1. **EN Blog → Money-Page-Links** (Cluster A & B zuerst – höchstes kommerzielles Volumen).
2. **EN Hub-and-Spoke** innerhalb A, B, C.
3. **DE Service-Mesh + Case-Study-Links** (2a).
4. **`/de`-Blog-Dublette lösen:** entweder `noindex`/`canonical` auf die EN-Version **oder** durch echte deutsche Beiträge ersetzen (2b).
5. Cluster D & E + Brücken.

## Technische Umsetzung
Links werden im Body-HTML der jeweiligen Datei gesetzt (relative Pfade, z. B. `href="/pages/bali-web-design.html"`). Header/Footer sind Partials – dort **nicht** anfassen. Nach den Edits `npm run build` + `npm run deploy`.
