# Prospect-Pipeline — automatische Review-Pages

Erzeugt aus Lead-Daten automatisch eine persönliche Analyse-Seite
(wie /review/tanja-neumann/) inkl. Local-Falcon-Scan, Vorher/Nachher-Karte,
On-Page-Audit, PageSpeed — und schickt dem Lead den Link per Mail.

## Voraussetzungen (.env im Repo-Root)
- PAGESPEED_API_KEY  ✅ vorhanden
- LF_API_KEY         ⬜ Local Falcon → Settings → API Access → Key kopieren
- RESEND_API_KEY     ⬜ gleicher Key wie in Supabase (nur für --send)

## Ablauf (2 Schritte pro Lead)
1. **Scan starten** (30 Sek): in der Local-Falcon-UI (Quick Scan) oder Claude/MCP —
   der Scan-START via REST braucht das On-Demand-Abo, das wir (noch) nicht haben.
2. **Generator laufen lassen** (Rest ist vollautomatisch):
```
node scripts/prospect-pipeline/generate.mjs \
  --report-key <key>            # ODER --place-id <ChIJ…> (nimmt neuesten Report)
  --firstname Anna --branch "Zahnarztpraxis" --domain praxis-muster.de \
  --email anna@praxis-muster.de --deploy --send
```
company/city/keyword werden automatisch aus dem Report abgeleitet (überschreibbar).
Ohne `--deploy` nur lokal; ohne `--send` keine Mail.
`--fixture fixtures/tanja.json --slug test-fixture` = Trockentest.

## Was automatisch passiert (live verifiziert 25.07.2026)
1. Report via LF Data-Retrieval-API (/v1/reports/:key/) — Location, SoLV/ARP,
   alle Wettbewerber, Scan-Bild. Im Tarif enthalten, KEINE Extra-Kosten.
2. PageSpeed mobil+desktop, On-Page-Audit (Title/Meta/H1/Schema/Alt/OG)
3. Seite aus template.html (statische Tokens + PROSPECT_DATA-JSON), Video = Platzhalter
4. Scan-Bild → public/review-assets/<slug>/ (PNG + WebP)
5. optional Build+Deploy, optional Resend-Mail an den Lead

## Wichtig
- template.html stammt von tanja-neumann — Design-Änderungen dort nachziehen.
- VOLL-Automatisierung (auch Scan-Start): entweder LF **On-Demand-API-Abo**
  ("Start Subscription" unter /api/) ODER später via MCP vom Dev-VPS.
- Supabase-Webhook → VPS → dieser Generator = Endausbau.
