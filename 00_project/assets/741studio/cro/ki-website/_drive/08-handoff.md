# Handoff — Landingpage 741 KI-CMS (Prototyp v3, Desktop)

Stand 2026-10-13. Status: v1 freigegeben (Martin, 13.10.2026). v3 setzt sein Feedback um (Hero = Produkt in Aktion, echtes Hüwel-Zitat, Vorher/Heute als Pflege-Ablauf, kein Symbolbild, Kontakte ohne Zahl) und wartet auf Freigabe. Nichts ist live. Der Prototyp läuft lokal und trägt `noindex,nofollow`.

## 1. Pfade
- Prototyp v2: `00_project/assets/741studio/cro/ki-website/07-prototype/v3/index.html` (+ `assets/`; v1 bleibt unter `07-prototype/index.html`, v2 unter `07-prototype/v2/`), gebaut mit `_build/build.py` aus der freigegebenen Copy (`content-writing/ki-website/05-final/page.md`), Stil `_build/style.css`, Bewegung `_build/motion.js`.
- Design-Doc und Prompt: `05-gpt-design-doc/design-doc.md`, `prompt.txt`, `make_prompt.py`. Mockup: `06-gpt-assets/full-page-v1-final.png`. Slots: `06-gpt-assets/images/SLOTS.md`.
- Prüfdateien: `07-prototype/v3/visual-check.md`, `v3/self-check.md` (36 von 40), `v3/motion.md`, Screenshots `07-prototype/v3/screenshots/`.

## 2. Text und Meta
- Freigegebene Copy: `04-copy/approved-copy.md` (v4; frühere Stände als approved-copy-v2.md und approved-copy-v3.md). CMS-Blöcke: `content-writing/ki-website/05-final/cms-blocks.txt`.
- Title: KI-Website mit KI-CMS, per Chat gepflegt | 741.Studio
- Meta: Mit dem 741 KI-CMS pflegst du deine Website per Chat. Eine Prüfung stoppt Fehler vor jeder Änderung. Hosting 0 €, Hilfe rund um die Uhr.
- H1: Deine Website mit KI-CMS: per Chat gepflegt, schnell geladen, ohne Baukasten-Abo
- Schema (im Prototyp-Head): Organization, Service "741 KI-CMS", Person Martin Drendel, WebPage. Kein FAQPage.

## 3. Bilder und Shoot-Liste
Alle Bilder echt: 741-Logo, Foto Martin Drendel (live auf 741.studio). Kein KI-Bild und keine Hüwel-Screenshots mehr (Martin mochte das Hüwel-Beispiel und das Symbolbild nicht). Das Hero-Fenster ist Live-HTML und als "Beispiel" beschriftet. Optional: echte Bildschirmaufnahme eines Chat-Ablaufs (ChatGPT/Codex) für die Chat-Karte im Hero.

## 4. Tracking
Event `booking_click` auf jedem CTA (6 Stück) mit Parameter `section` (hero, situationen, start, person, fallbeispiel, abschluss) — im Prototyp schon über `data-section` vorbereitet. Bestehende Events auf 741.studio: siehe Memory 741studio-analytics-conversions.

## 5. [FEHLT]
1. Einverständnis von Martin Hüwel, sein WhatsApp-Zitat „Hey, Dinge funktionieren einwandfrei und schnell, super Sache.“ zu veröffentlichen (Quelle des Wortlauts: Martin Drendel, 13.10.2026). Kein Platzhalter im Text mehr.

## 6. Rebuild-Hinweise
- Zielseite `04_site/de/pages/ki-website.html` im bestehenden Design-System: `{{> header_de }}`, `{{> footer_de }}`, `{{> consent }}` statt des Prototyp-Rahmens; Root-Schrift wie die Live-Seite (1vw-Regel, Memory mobile-fluid-root-and-header).
- Mobile-Version fehlt (Workflow nur Desktop) und gehört ins Rebuild.
- Offen aus dem Self-Check: "Start Now" im Kopf auf dieser Seite dunkel (Item 10), Martin hat das nicht gewählt.
- Interne Links: von website-design.html und der Startseite auf die neue Seite verlinken; Sitemap-Eintrag.
- Live nur nach Martins Go (Regel no-website-changes-without-go, erst Nachricht, dann Deploy).

## 7. Vorher/Nachher-Score
| | Score |
| --- | --- |
| Abkürzungs-Vorschau 13.10. (ohne Workflow) | 21 von 40 |
| Prototyp v1 | 34 von 40 |
| Prototyp v2 (Checkpoint 2) | 35 von 40 |
| Prototyp v3 (Feedback Martin) | 36 von 40 |
