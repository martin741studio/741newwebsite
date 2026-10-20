# Master-Prompt: Carousel (Instagram, 1080×1080 pro Slide, 741-CI)

> Wiederkehrendes Format für tägliche/regelmäßige Posts, z. B. aus NotebookLM-Inhalten
> (Playbooks, Guides, Recherche). Generator existiert: `07_social/templates/build_carousel.py`.

Erstelle einen Carousel im 741-CI aus einem Thema/Playbook.

**Input, den ich dir gebe:**
1. Thema + Quelle (z. B. „Local SEO Playbook aus NotebookLM", oder Text/Bullets, die ich paste)
2. Zielgruppe (Standard: lokale Betriebe / Heilberufler & Praxen, „du")
3. Optional: gewünschte Slide-Zahl (Standard 7–9) und eine echte Statistik

**Was du tust:**
1. Inhalt in Slides gliedern: **Cover → (optional Stat) → 5–7 Tipp-Slides (nummeriert) → CTA**.
   Jede Tipp-Slide = eine klare Aussage, 1 Kernsatz + 1 Satz Begründung, `<b>` fürs Wichtigste.
2. Nur den `CONFIG`-Block in `07_social/templates/build_carousel.py` anpassen
   (series, handle, slides[]). Slide-Typen: `cover` (title[]+hl-Index+sub), `stat` (big+lab[3]),
   `tip` (num+title+txt mit `<b>`), `cta` (title[]+sub+url).
3. Rendern: `python3 build_carousel.py <slug>` → PNGs in `07_social/output/<slug>/slide_N.png`.
4. Jede Slide mit Read prüfen: Text nicht abgeschnitten, Headline max. 2–3 Zeilen (sonst kürzen),
   Nummern-/Titel-Überlappung bei langen Tip-Titeln checken.
5. Alle Slides in Reihenfolge per SendUserFile schicken.

**Design-Regeln (im Generator, nicht ändern):**
- 741-CI: #111 Hintergrund, #fac118 Gelb, Anton-Headlines, DM Sans, Halftone-Textur.
- Topbar: Logo links, Serie + Slide-Zähler (`01 / 09`) rechts. Foot: „741.studio" + „SWIPE →".
- CTA-Slide = gelber Hintergrund, schwarzer Text, endet auf 741.studio + Handle.
- Erste Slide muss den Swipe wert sein (starker Hook), letzte Slide = ein klarer CTA.

**Content-Regeln:**
- „du", kein „Sie". Konkret, kein Agentur-Blabla (Ton wie das Praxis-Advertorial).
- Aus NotebookLM: Kernaussagen übernehmen, aber für Social zuspitzen (1 Idee pro Slide).
- Zahlen/Claims nur, wenn belegbar. Erfundene Statistiken vermeiden.
- CTA passend zum Thema (Local SEO → kostenloser Sichtbarkeits-Check).

**Hinweis NotebookLM:** Inhalt liegt in Martins Notebook (privat, Google-Login). Direktes
Auslesen per claude-in-chrome ist möglich, aber die SPA ist zäh — schneller ist, wenn Martin
die Kernpunkte/den generierten Text pastet und Claude daraus die Slides zuspitzt.
