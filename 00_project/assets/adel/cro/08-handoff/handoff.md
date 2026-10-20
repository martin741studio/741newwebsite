# Handoff — Startseite Rechtsanwältin Aydan Adel (Prototyp v1, Desktop)

Stand 2026-10-10. Für den späteren Rebuild-Workflow. Nichts ist live. Der Prototyp läuft nur lokal.

## 1. Pfade

- Prototyp: `00_project/assets/adel/cro/07-prototype/index.html` (mit `assets/`), Datei lokal öffnen oder `python3 -m http.server`
- Bewegung (Abweichungen von der Spezifikation): `07-prototype/motion.md`
- Prüfdateien: `07-prototype/visual-check.md` (41 Punkte, 9 fixed, 0 open), `07-prototype/self-check.md` (40 von 44)
- Mockup: `06-gpt-assets/full-page-v1-final.png`, Bilder `06-gpt-assets/images/`, Slots `06-gpt-assets/images/SLOTS.md`
- Design-Doc und Prompt: `05-gpt-design-doc/design-doc.md`
- Text: `04-copy/approved-copy.md`
- Diagnose: `03-diagnosis/diagnosis.md`. Daten: `02-data/dataset.md`, `02-data/brand.md`
- Screenshots: `07-prototype/screenshots/prototype-full-1440.png`, `prototype-first-viewport-1440.png`, Live-Seite vorher: `02-data/screenshots/`

## 2. Text und Meta (aus approved-copy.md)

- Title (58 Zeichen): Rechtsanwältin Bonn: Erbrecht & Familienrecht | Aydan Adel
- Meta Description (152): Rechtsanwältin Aydan Adel in Bonn-Beuel: Beratung im Erbrecht und Familienrecht, persönlich oder online. Erstberatung per WhatsApp, Telefon oder E-Mail.
- H1: Erbrecht. Familienrecht. Rechtsanwältin in Bonn. (Varianten B und C im Freigabetext)
- Schema: `Attorney` (JSON-LD im Prototyp, ohne aggregateRating, weil Eigenbewertungen für Rich Results nicht zählen). `sameAs`: LinkedIn und Instagram von ihrer eigenen Seite.
- Prototyp trägt `noindex,nofollow`. Vor dem Livegang entfernen.

## 3. Marke (kein Logo vorhanden)

Wortmarke "Aydan Adel" in Newsreader 500 mit "RECHTSANWÄLTIN" in Manrope 600, Bronze (#9A5C08). Farben Tinte #0C1424, Papier #FBF9F5, Sand #F1EBE0, Bronze für alle Buttons. Das schwarze Linien-Symbol der Live-Seite wird nicht genutzt. Martin entscheidet, ob ein richtiges Logo folgt.

## 4. Bilder und Shoot-Liste

Beide Personenbilder (Hero, Über mich) sind KI-Entwürfe nach einem privaten Foto der Anwältin (Sonnenbrille, Urlaubsraum, nicht verwendbar). Das Gesicht ist erfunden, weil die Augen auf dem Foto verdeckt sind. Echte Fotos nötig:
1. Business-Porträt im Blazer (Hero)
2. Beratungssituation am Schreibtisch (Über mich)
3. Kanzleiraum oder Eingang mit Messingschild
4. Eingangsfoto Maarstraße 68 für den Standort
Die Alt-Texte der beiden Bilder sagen "Platzhalterbild (KI-Entwurf)". Die Karte ist ein gezeichneter Platzhalter. Echte Karte mit Einwilligung einbauen.

## 5. Tracking-Spezifikation

Ereignisse mit Parameter `section` (hero, kopf, situationen, ablauf, ueber-mich, bewertungen, faq, standort, abschluss, fuss, rail):
- `whatsapp_click` auf jedem `wa.me`-Link (11 Stück im Prototyp)
- `phone_click` auf jedem `tel:`-Link (Hero, Abschluss, Fuß)
- `email_click` auf jedem `mailto:`-Link (Abschluss, Fuß)
- `download_click` für die Vollmacht (PDF)
Vorbelegte WhatsApp-Texte: Hero, Kopf, Ablauf, Bewertungen, Standort, Abschluss, Fuß, Rail: "Guten Tag Frau Adel, ich möchte eine Erstberatung anfragen. Mein Thema: ". Situationen: "Guten Tag Frau Adel, ich habe ein Anliegen im Erbrecht oder Familienrecht und möchte eine Erstberatung anfragen. Mein Thema: ". Über mich: "Guten Tag Frau Adel, ich möchte Sie kennenlernen und eine Erstberatung anfragen. Mein Thema: ". FAQ-Link: "Guten Tag Frau Adel, ich habe eine Frage vor der Erstberatung: ". Einrichtung ist nicht Teil dieses Workflows.

## 6. [FEHLT]-Liste (Martin muss bei der Kundin klären)

1. **Kontaktkanal bestätigen.** Prototyp nutzt WhatsApp primär. Die Live-Seite sagt "bitte per E-Mail" (Startseite) und "Termine nach telefonischer Vereinbarung" (Kontakt). Frau Adel soll einen Hauptweg wählen.
2. **Dauer und Preis der Erstberatung.** Ohne Zahl bleibt die Kostenfrage offen. Für Verbraucher gibt es im RVG eine Kappungsgrenze. Eine "kostenlose Erstberatung" darf nur stehen, wenn sie stimmt.
3. **Fachanwaltstitel ja oder nein.** Die Seite nennt Fachanwaltslehrgänge 2018 und 2020 "mit besonderem Erfolg absolviert". "Fachanwältin" darf nur stehen, wenn die Kammer den Titel verliehen hat. Der Prototyp vermeidet den Begriff.
4. **Strafrecht und Verkehrsrecht bestätigen.** Die Live-Seite nennt "Vertretung vor allen Strafgerichten" und "auf jedem Rechtsgebiet behilflich". Strafrecht und "jedes Rechtsgebiet" sind im Prototyp nicht übernommen. **Verkehrsrecht (Unfallschadensregulierung) und Schadensersatz und Schmerzensgeld stehen im Prototyp**, weil die Live-Seite sie nennt. Die Bestätigung durch Frau Adel steht aus.
5. **Beratungssprachen.** Die Seite gibt es auf Deutsch, Englisch, Türkisch, Französisch. Es steht nirgends, in welchen Sprachen beraten wird. Die Mandantschaft ist laut Bewertungen international.
6. **Weitere Rechtsgebiete.** Bewertungen nennen Staatsangehörigkeits- und Einbürgerungsrecht, Verzeichnisse nennen Arbeitsrecht, Ausländer- und Asylrecht, Handels- und Gesellschaftsrecht. Bestätigung nötig, bevor Seiten dazu entstehen.
7. **Echte Fotos** (siehe Shoot-Liste).
8. **Link zum Google-Bewertungsprofil** (Platzhalter `#`).
9. **Datenschutzerklärung** und Cookie-Einstellungen im neuen Format. Hinweis zu WhatsApp als Mandatskanal und zur Datenverarbeitung durch den Anbieter aufnehmen.
10. **Karte mit Einwilligung** (Google Maps oder OpenStreetMap).
11. **Zustimmung zu den Bewertungs-Auszügen und Grauzonen:** Die Fachanwaltslehrgänge stehen als einer von fünf Belegen in der Beweis-Leiste (Wortlaut der Kundin, kein Titel). Falls der Titel nicht verliehen ist, kann dieser Beleg auf die Zeitleiste beschränkt werden. Bewertungs-Auszüge: (Anwaltswerbung, sachliche Mandantenstimmen sind erlaubt, Frau Adel soll die Auswahl sehen).
12. **Impressum-Format:** die Telefonnummer steht dort als "004917643523159". Gängige Form 0176 43523159.
13. **Leistungsunterseiten.** Die zwölf "Mehr erfahren"-Links im Prototyp haben noch kein Ziel.

## 7. Hinweise für den Rebuild

- **CMS Jimdo Creator.** Der Prototyp ist freier HTML-Code. Auf Jimdo ist das nur eingeschränkt umsetzbar. Rebuild-Workflow klärt: Wechsel des Systems oder Nachbau in den Jimdo-Grenzen. Das ist eine Entscheidung für Martin und die Kundin.
- **Rankings erhalten.** Die Seite rankt heute nur für Vollmacht-Begriffe, vor allem türkisch (vekaletname örnegi Platz 20, vekalet deutsch 53, vekaletname 80). Die Vollmacht-Seiten und die vier Sprachversionen dürfen nicht verloren gehen. Redirects für jede alte URL.
- **Keine Rankings** für Erbrecht, Familienrecht oder Bonn. Der neue H1 und die Leistungsseiten sind der SEO-Hebel (rechtsanwältin bonn 880, anwalt familienrecht bonn 390, anwalt erbrecht bonn 170).
- **Menü:** Leistungen, Ablauf, Über mich, Bewertungen, Fragen, Anfahrt. Die Über-mich-Seite der Live-Seite (/über-mich/) bleibt als eigene Seite, ihr Wortlaut ist in der Zeitleiste verwendet. Eine eigene CRO-Fassung dieser Seite ist möglich (Workflow Abschnitt 4b).
- **Korrekturen auf der Live-Seite, die die neuen Fakten fordern:** "spezialisierte Rechtsanwältin" ersetzen durch "mit Interessenschwerpunkt", "auf jedem Rechtsgebiet" und "Strafgerichte" prüfen, Kontaktweg vereinheitlichen, Impressum-Telefonformat, Cookie-Banner nicht über den ersten Bildschirm legen.
- **Sprachversionen** (EN, TR, FR) brauchen eine eigene Fassung des neuen Textes.

## 8. Vorher und Nachher

Scorecard 5 von 44 (Live-Seite) gegen 37 von 44 (Prototyp), nach strenger Neubewertung durch einen unabhängigen Prüf-Agenten. Prio A nicht auf 2: Item 2 (Headline ohne Ergebnis, Variante B oder C wählen), Item 8 (Gesicht ist KI-Entwurf, echtes Porträt nötig), Item 9 (Dauer und Preis der Erstberatung fehlen als Kundendaten).

## 9. Learnings (auch in `rules.md`)

Siehe Eintrag "Aydan Adel Startseite" in `00_project/knowledge/cro-library/_derived/rules.md`, Abschnitt 16.
