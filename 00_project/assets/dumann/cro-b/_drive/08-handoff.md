# Handoff — Startseite Dumann, Track B (Prototyp v1, Desktop)

Stand 2026-10-11. Pilot von Track B. Nichts ist live. Der Prototyp läuft nur lokal und trägt `noindex,nofollow`.

## 1. Pfade
- Prototyp: `00_project/assets/dumann/cro-b/07-prototype/index.html` (mit `assets/`). Generator `_build/build.py` und `_build/template.html`.
- Bewegung: `07-prototype/motion.md`. Gewicht: `07-prototype/perf.md`. Prüfdateien: `07-prototype/visual-check.md` (62 Punkte, 8 fixed, 0 open, dazu 15 Prüfer-Funde behoben), `self-check.md` (35 von 44).
- Konzept: `05-gpt-design-doc/concept/concept.md`. Design-Doc und Prompt: `05-gpt-design-doc/design-doc.md`, `prompt.txt`. Mockup: `06-gpt-assets/full-page-v1-final.png`. Slots: `06-gpt-assets/images/SLOTS.md`, Media: `06-gpt-assets/media/MEDIA-PLAN.md`.
- Text: `04-copy/approved-copy.md` (Copy v3). Brief: `00-brief-b/brief-b.md`. Element-Pool und Stimmen: `00-element-pool/`, `votes-summary.md`. Recherche: `02-data/`.
- Daten aus Track A: `02-data/dataset.md`, `brand.md`, `03-diagnosis/diagnosis.md`. Der Track-A-Lauf (Prototyp v2, Seite "Über mich") liegt in `../cro/`.

## 2. Text und Meta
- Title (59 Zeichen): Heilpraktikerin Berlin-Charlottenburg | Hildegard-Heilkunde
- Meta Description (152): Heilpraktikerin in Berlin-Charlottenburg: Hildegard-Heilkunde, Ernährungsberatung und Darmsanierung. 5,0 Sterne bei 9 Google Bewertungen. Termin buchen.
- H1: Ihre Heilpraktikerin in Berlin-Charlottenburg: Hildegard-Heilkunde, persönlich begleitet. (Varianten B und C im Text)
- Schema: `MedicalBusiness` im JSON-LD. Offen: `Person`, `FAQPage`, `sameAs`, Öffnungszeiten.
- `noindex,nofollow` vor dem Livegang entfernen.

## 3. Komponentenliste (Track B, mit Datei und Funktion)
| Komponente | Wo | Funktion |
| --- | --- | --- |
| Viriditas-Faden | `index.html`, Funktion `buildVine` und `drawVine`, Element `.vine` | baut einen SVG-Pfad über die ganze Seitenhöhe, steuert `stroke-dashoffset` nach Scroll-Anteil, schaltet Blätter und Blüte |
| Bild-Vorschau-Liste | Sektion 4, `#rows` und `#prev` | wechselt das Vorschaubild bei Hover und Fokus |
| Haftender Titel mit Schrittlinie | Sektion 5, `.sticky-t`, `#stepsv`, Funktion `steps` | Titel bleibt stehen, Linie füllt sich nach Scroll |
| Farbblock-Wechsel | Funktion `io2`, Klasse `body.dark` | wechselt Kopf (Creme zu Lila) und Faden, wenn das Abschlussband erreicht ist |
| X-ray-Schalter | `?xray=1` oder Taste `x` | Code-Ebenen rot, Bild-Ebenen blau |
| Reduced-Motion-Test | `?rm=1` | erzwingt die ruhige Fassung |

## 4. Marke
Echte Logo-Dateien (Icon als rundes Siegel, Wortmarke). Lila #783ca0, Dunkel #5b2d80, Creme #f8f3fb, Oliv #aabe1e nur für Buchungsbuttons. Cormorant Garamond, Poppins, Caveat (nur "seit 2002"). Siehe `02-data/brand.md`.

## 5. Bilder und Shoot-Liste
Echt: zwei Portraits, Logo. KI-Entwürfe aus Track A (ersetzen): fünf Themen-Symbole, sechs Leistungsbilder, Schmetterling (Hildegard-Teaser), Lavendel-Zeichnung (Abschluss). Shoot-Liste: Praxisraum und Eingang, Hildegard-Kräutergarten (Ort klären), Hände bei einer Anwendung, Heilpflanzen aus dem Garten, ein Foto je Leistung.

## 6. Tracking-Spezifikation (Einrichtung gehört nicht zu diesem Workflow)
Events mit Parameter `section` (hero, themen, leistungen, ablauf, ueber, bewertungen, standort, abschluss, kopf): `booking_click` für jeden Link auf `my.lemniscus.de`; `phone_click` für jeden `tel:`-Link. Zusätzlich für Track B: `vine_complete` (Faden erreicht die Blüte, nur zur Beobachtung) und `row_preview` (Zeile in Sektion 4 überfahren, Parameter `row`).

## 7. [FEHLT]-Liste (Martin klärt mit Daniela)
1. Die fünf Themen und die Wunschpatient:in bestätigen.
2. Methode in drei Sätzen und Motivation: Text von Daniela, Freigabe.
3. Ort des Hildegard-Kräutergartens (Schorfheide oder Schöneberg), echte Gartenfotos.
4. Hub-Seite "Hildegard-Heilkunde" und Seite der Schule Viriditas (Links `#`).
5. Link zum Google-Profil; deutsche Originaltexte der Bewertungen; Patientenstimmen (alle drei Zitate betreffen Kurse und Lehre).
6. Stornobedingungen (FAQ 4).
7. Karte mit Einwilligung, Parken, Barrierefreiheit, Öffnungszeiten.
8. Deutsche Übersetzung des Hildegard-Zitats prüfen ("O edelste Grünkraft, die du in der Sonne wurzelst" ist eine eigene Übersetzung).
9. Praxisfotos (siehe Shoot-Liste).
10. Sechs Leistungs-Links und drei Rechtslinks (Impressum, Datenschutz, Cookie) sind `#`. **Warnung:** Die Live-Unterseiten zu Leistungen enthalten HWG-Verstöße ("Präkanzerose", "Amethystsalbe … Neurodermitis", siehe Diagnose Punkt 22). Nicht verlinken, bevor die Texte geprüft sind.
11. Ist Lemniscus ein echter Kalender mit Verfügbarkeit oder nur ein Formular? (Dataset [FEHLT] 5)
12. Anzeigename der Bewertenden prüfen: "Scheila B." ist der Google-Anzeigename aus dem Track-A-Text, der volle Name im Dataset lautet anders.
13. Preis der homöopathischen Erstanamnese (60 bis 120 Minuten, 220 bis 380 €) steht jetzt in FAQ 1. Daniela bestätigt.
14. Leistungsnamen: "Ausleitung und Entgiftung", "für mehr Wohlbefinden", "Mineralstoffe und Belastungen sichtbar machen" wurden aus HWG-Gründen gestrichen. Martin entscheidet, ob Daniela sie zurückhaben will.

## 8. Hinweise für den Rebuild
- CMS ist Wix. Der Viriditas-Faden und die Bild-Vorschau-Liste brauchen eigenen Code (Wix-Velo oder Custom-Embed). Ohne diesen Code bleibt die Seite voll nutzbar (Test T5). Die sechs Zeilen und die Schrittleiste funktionieren auch ohne Skript.
- Schriften selbst hosten (DSGVO) statt Google Fonts.
- Das Bach-Zitat der Live-Seite nicht übernehmen (HWG).
- Zwei Zielgruppen trennen: Startseite für Patient:innen, die Schule bekommt eine eigene Seite (Teaser ist drin).
- Name im Google-Profil und auf der Seite angleichen (Option B ist gesperrt, 07.09.).

## 9. Learnings
- Der Element-Pool als Abstimmungsseite hat die Konzeptwahl entschieden: Martins Stimmen haben die Richtung (Faden) und die Komponenten festgelegt, ohne Fragebogen.
- `position:absolute` mit `height:100%` braucht einen positionierten Eltern-Container. Ohne `main{position:relative}` wurde die Ranke so hoch wie das Browserfenster (headless 16.000 px) und die Seite 15.684 px lang.
- Ein Bild, dessen Hintergrund nicht exakt der Seitenfarbe gleicht, zeigt auf Lila ein Rechteck, auch mit `mix-blend-mode:lighten`. Eine Randmaske (Radialverlauf) löst es.
- Instant-Sprünge im Scroll-Test überspringen Reveals. Reveals brauchen einen sequentiellen Durchlauf mit Wartezeit.
- `pbcopy` mit `LC_ALL=en_US.UTF-8` (Umlaute).
