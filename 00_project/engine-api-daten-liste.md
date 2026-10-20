# Content Engine — API- & Daten-Liste für die Voll-Automatisierung

Stand 2026-08-08 · Was pro Engine-Stufe gebraucht wird, was wir **haben** ✅ und was **fehlt** ❌.
Ziel: Feed → Empfehlung → Generierung → Publish → Messung läuft ohne Handarbeit.

---

## Stufe 1 · Integration (Website des Kunden verbinden)

| Was | Wofür | Status |
|---|---|---|
| FTP/SFTP-Zugang | Statische Sites (wie 741.studio) direkt beschreiben | ✅ 741.studio (`agent_deploy`) · ❌ pro Kunde einsammeln (läuft über Portal-Onboarding „Website/Hosting/CMS") |
| WordPress REST API + Application-Password | Artikel/Seiten als Entwurf oder live pushen (häufigster Kunden-Fall) | ❌ pro Kunde; Prozess: Admin-Account aus Onboarding → App-Passwort erzeugen |
| Wix / Shopify / Webflow API-Keys | Nur falls Kunde eines davon nutzt | ❌ bei Bedarf pro Kunde |
| Supabase (Engine-Datenhaltung) | Templates, Generierungen, Status, Kunden | ✅ Projekt `741-portal` (Frankfurt), Tabellen `content_templates` + `content_generations` existieren |

## Stufe 2 · Feeds (Keywords, Wettbewerber, Suchvolumen)

| Was | Wofür | Status |
|---|---|---|
| **DataForSEO API** | Suchvolumen, Keyword-Ideen, SERP-/Wettbewerber-Daten DACH — der Kern-Feed | ⚠️ Konto laut Spec vorhanden — **Key muss in die Pipeline** (app_secrets) |
| Local Falcon API | Maps-Ranking-Grids (Baseline + Verlauf) | ✅ Key in .env; Scan-START braucht On-Demand-Abo oder Start via MCC/UI (bekannte Einschränkung) |
| Google Search Console API | Echte Suchanfragen + Impressionen der Kunden-Domain (bester Gratis-Feed) | ✅ Service-Account `reporting-bot`, 741.studio verifiziert · ❌ pro Kunde: Property-Einladung (Prozess existiert) |
| GA4 Data API | Conversion-/Traffic-Daten | ✅ 36 Client-Properties angebunden |
| Apify (Scraping) | Wettbewerber-Content, Verzeichnis-Checks | ✅ MCP verbunden |

## Stufe 3 · KI-Empfehlungen + Generierung

| Was | Wofür | Status |
|---|---|---|
| **Anthropic API Key** | DER fehlende Kern-Baustein: `generate-article` (Artikel/Seiten schreiben) + `run-visibility` (AI-Sichtbarkeit) + Empfehlungs-Logik | ❌ **FEHLT — wichtigster nächster Schritt** (in `app_secrets` als `anthropic_api_key`) |
| Kunden-Stammdaten (business/services/cities JSON) | Ohne echte Lokal-/Leistungsdaten keine einzigartigen Seiten | ✅ Format definiert (`04_site/_pseo/<kunde>/`), 741-Pilot befüllt · pro Kunde: kommt aus Portal-Onboarding (Stammdaten-Sheet + Fragebogen) |
| Bild-Quelle | Bilder in Artikeln | ✅ Kundenfotos aus Portal-Materialien · ❌ optional Pexels/Unsplash-API für Stock |

## Stufe 4 · Publish (automatisch veröffentlichen)

| Was | Wofür | Status |
|---|---|---|
| Renderer/Generator | Body + Shell → fertige Seite | ✅ gebaut: `05_scripts/build_pseo_741studio.py` (Shell-Ansatz, pro Kunde kopierbar) |
| Staffel-Logik (Batch-Publishing) | Nicht 300 Seiten an Tag 1 (Spam-Signal) | ✅ konzeptionell (Playbook) · ❌ Scheduler-Automation (pg_cron vorhanden, Job fehlt) |
| Sitemap-Update + GSC-Submit | Indexierung anstoßen | ❌ kleiner Baustein: sitemap.xml erweitern + GSC-API-Submit (Service-Account kann das) |

## Stufe 5 · Messung & Nachsteuern

| Was | Wofür | Status |
|---|---|---|
| GSC API (Coverage, Impressionen, Position je URL) | „Indexiert? Rankt? Verdicken oder prunen?" | ✅ für 741.studio · pro Kunde nach Einladung |
| Local Falcon Trend-Reports | Maps-Wirkung | ✅ |
| Reporting-Cron (monatlich je Kunde) | Automatischer Report ins Portal + Mail | ✅ Mail-Engine existiert (Resend + pg_cron) · ❌ Report-Job selbst |

## Betrieb / Infrastruktur

| Was | Status |
|---|---|
| Supabase 741-portal (DB, Auth, Edge Functions, Cron) | ✅ läuft |
| Resend (Mail) | ✅ läuft |
| n8n (komplexere Workflows, WhatsApp) | ❌ geplant — kommt mit dem Dev-VPS |
| Keepalive beider Supabase-Projekte | ✅ GitHub Action täglich |

---

## Die 3 Beschaffungs-Prioritäten (in dieser Reihenfolge)

1. **Anthropic API Key** → schaltet Artikel-Generierung + AI-Sichtbarkeit frei (beides fertig verdrahtet). ~Minuten Arbeit, sofortiger Effekt.
2. **DataForSEO-Key in die Pipeline** → echte Keyword-/Volumen-Feeds statt Bauchgefühl; Grundlage der „Empfehlungen"-Stufe.
3. **Pro-Kunde-Standard im Onboarding ergänzen:** WordPress-App-Passwort (bzw. FTP) als eigener Zugangs-Punkt — dann kann die Engine ab Tag 1 publizieren.

*Pilot-Beweis (heute live, noindex): 741.studio/local-seo-nuernberg · /local-seo-fuerth · /webdesign-erlangen*
