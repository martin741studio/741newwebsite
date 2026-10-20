# Handoff: Über-mich-Seite Naturheilpraxis Daniela Dumann

Stand 2026-10-11. Für den separaten Rebuild-Workflow (Wix). Status: **Übergeben**, Freigabe durch Martin und Kundin steht aus. Der Run ist auf Martins Sonderregel ohne Stopp an den Checkpoints durchgelaufen.

## 1. Pfade

- Prototyp (Desktop 1440 px): `07-prototype/index.html`, Assets `07-prototype/assets/`, Schema `07-prototype/person-schema.json`, Screenshots `07-prototype/screenshots/`
- Mockup: `06-gpt-assets/full-page-v1-final.png`, Bild-Slots `06-gpt-assets/images/SLOTS.md`, erzeugte Bilder `06-gpt-assets/images/`
- Design-Doc und der eine Prompt: `05-gpt-design-doc/design-doc.md`
- Copy: `04-copy/approved-copy.md`
- Daten: `02-data/dataset.md`, Diagnose: `03-diagnosis/diagnosis.md`
- Drive: `Local SEO/Daniela Dumann/CRO Homepage/Über mich/`

## 2. Seitentexte für das CMS

- **URL:** `/ueber-mich` (neu). Die alte `/lebenslauf` wird nach Freigabe per 301 auf `/ueber-mich` geleitet. Der Menüpunkt „Über mich" (heute nur ein Obermenü, das auf die Startseite zeigt) verlinkt künftig auf diese Seite. Die Startseiten-Sektion „Über mich" verlinkt „Zum Lebenslauf" auf die neue Seite.
- **Title (57 Z.):** Daniela Dumann | Heilpraktikerin in Berlin-Charlottenburg
- **Meta Description (155 Z.):** Daniela Dumann, Heilpraktikerin in Berlin-Charlottenburg seit 2002 und Vizepräsidentin der Internationalen Gesellschaft Hildegard von Bingen. Termin buchen
- **H1:** Ich bin Daniela Dumann, Heilpraktikerin in Berlin-Charlottenburg seit 2002
- **Alt-Texte:** beschreibend, siehe `index.html` (Hero-Portrait, Beratung, Kräutergarten, Logo Viriditas). Die Wix-Alt-Texte im Dateinamen-Stil ersetzen.

## 3. Bilder und Shoot-Liste

- Echt: beide Portraits (Originale in `../01-input/`), Schmetterling und Lavendel von der Website, Logo Viriditas (Rand zugeschnitten, Logo unverändert), echtes Logo der Praxis.
- Erzeugt (ChatGPT, Gesicht aus den Portraits): `04-beratung.png` (Beratungsgespräch), `06-kraeutergarten.png` (Führung im Kräutergarten, 1536 px). **Shoot-Liste: beide durch echte Fotos ersetzen.** Das Kräutergarten-Foto ist nur 1,24-fach so groß wie seine Anzeige, ein echtes Foto in Originalauflösung ist dort besser. Das Foto zeigt eine Gruppe, die es so nicht gab: vor der Veröffentlichung mit Daniela klären, ob ein generiertes Bild an dieser Stelle gewünscht ist oder ob ein echtes Foto der Führung folgt.
- Gemalte Icons: Zweig, Schmetterling, Apfel, Blüte (Startseiten-Run), neu Kräuterbündel und Massagesteine.

## 4. Tracking-Spec

Primärkanal ist das Buchungsformular: Ereignis `booking_click` auf jedem Link zu `my.lemniscus.de` mit Parameter `section` (hero, ansatz, weg, bewertungen, warum, standort, abschluss), Ereignis `phone_click` auf jedem `tel:`-Link (hero, abschluss). Einrichtung selbst gehört nicht in diesen Workflow.

## 5. Person-Schema (E-E-A-T)

Datei `07-prototype/person-schema.json`, im `<head>` der Seite. Zu tun beim Rebuild:
- `image` ergänzen (Portrait-URL nach dem Wix-Upload).
- `worksFor`: heute ein eingebettetes LocalBusiness. Wenn die Startseite ein LocalBusiness-/MedicalBusiness-Schema mit `@id` hat, stattdessen `{"@id": "…"}` verwenden (die Startseite hat laut Scrape keines, siehe dataset 1.1).
- `sameAs` bewusst leer: nur geprüfte Profile mit korrekter NAP aus dem Citation-Audit aufnehmen. Facebook `hildegardvonbingenberlin` steht auf der Website, NAP dort nicht geprüft.
- Schema im Rich-Results-Test prüfen.
- Meta `robots noindex,nofollow` im Prototyp entfernen.

## 6. [FEHLT] und Entscheidungen vor dem Livegang

1. **Heilkräutergarten (Widerspruch auf der Website).** Die Startseite (Sektion „Über mich" des Startseiten-Runs, GBP-Text) nennt den Garten in der Schorfheide, die Seite Kräuterheilkunde sagt, er sei „in etwas anderer Form" in der Gartenarbeitsschule Schöneberg. Diese Seite nutzt nur Schöneberg. **Der Schorfheide-Satz im Prototyp der Startseite ist wahrscheinlich veraltet und muss geklärt und angepasst werden.**
2. **Freigabe der umformulierten Motivation** („Eigene schwere Erkrankungen haben mein Interesse an der Naturheilkunde geweckt.") durch Daniela. Original auf der Startseite enthält eine Wirkaussage („heilsame Wirkung") und sollte dort ebenfalls angepasst werden.
3. **Deutsche Originaltexte** der drei Google-Bewertungen.
4. **Echte Fotos** (Beratung, Kräutergarten).
5. **Mobilnummer 0170 6011182:** steht auf der Website, auf der Seite nicht verwendet. Entscheidung Martin.
6. **Parken** am Standort.
7. **Verbände:** vollständige Namen und, falls vorhanden, Mitgliederverzeichnis-Links für `sameAs`.
8. **Karte:** OpenStreetMap lädt beim Seitenaufruf, für den Livegang Einwilligung (Zwei-Klick-Lösung) nötig (DSGVO).
9. **Impressum und Datenschutz** sind Platzhalter, 5 „Mehr erfahren"-Links und „Kurse und Seminare ansehen" sind `#`-Platzhalter bis zum Rebuild der Behandlungsseiten.
10. **HWG-Aufräumen auf verlinkten Seiten:** `/kräuterheilkunde` enthält ein Wirkversprechen und Indikationszahlen. Vor dem Verlinken bereinigen.
11. **Sub-Entscheidung CTA-Text:** „Termin buchen" (Schritt, kein Nutzen), gleiche offene Entscheidung wie auf der Startseite.

## 7. Vorher und nachher

| | Ist-Zustand `/lebenslauf` | Prototyp |
| --- | --- | --- |
| Score (21 Items, max 42) | 11 | 39 |
| H1 und Title | „Über mich" / „Lebenslauf | …" | Name, Rolle, Stadt |
| Person-Schema | keines | ja, 6 Qualifikationen |
| Bewertungen, FAQ, Hinweisbox, CTAs | keine | 3 Bewertungen, 4 FAQ, Hinweisbox, CTA in 7 Abschnitten |

## 8. Offene Punkte für den Rebuild

Mobile Version (eigener späterer Workflow), Menü-Verlinkung, 301-Weiterleitung, interne Verlinkung von Startseite, Behandlungsseiten und Kursseiten auf die neue Seite, Wix-Umsetzung mit dem Seitentausch-Verfahren (neu bauen, alt offline, Slug übernehmen).

## 9. Learnings (auch in `rules.md`)

- Eine Behandlerinnen-Seite verwendet dieselbe Struktur wie die Startseite nur teilweise: Items für Einstiegsseiten entfallen, drei Seitentyp-Items kommen dazu (Name/Rolle/Stadt, Person-Schema, Werdegang).
- Widersprüche zwischen Seiten der Kundin immer im Dataset festhalten und die neuere, sicherere Aussage nehmen (hier der Garten).
- Eigene Fotos der Person bei der Arbeit fehlen fast immer: im Mockup als Foto-Slots einplanen, mit Porträts als Gesichtsreferenz erzeugen, auf die Shoot-Liste.
