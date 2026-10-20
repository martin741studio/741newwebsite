# Übergabe — me&you Website (Michael Ehlers), CRO-Prototypen

Stand 2026-10-12. Gemeinsame Übergabe für alle Seiten des Neuaufbaus. Teil 1 enthält die vier fertigen Seiten. Stimmen, FAQ und Gespräch buchen laufen parallel und kommen als Teil 2 dazu.

## 0. Status
| Seite | Slug | Prototyp | Raster vorher → jetzt | Freigabe Martin |
|---|---|---|---|---|
| Startseite | `/` | `cro/07-prototype/index.html` | 20 → 37 von 42 | Copy 11.10., Prototyp 12.10. („sehr gut“, Google-Kachel S02 entfernt) |
| Seminare | `/seminare` | `cro/seminare/07-prototype/index.html` | 11 → 37 | Copy + Prototyp 12.10. |
| Michael | `/michael` | `cro/michael/07-prototype/index.html` | 15 → 39 | Copy + Prototyp 12.10. |
| Was ist Rhetorik | `/rhetorik` | `cro/rhetorik/07-prototype/index.html` | 14 → 38 | Copy + Prototyp 12.10. |

Alle Prototypen: Desktop 1440 px, `noindex,nofollow`, nur lokal. Gemeinsames Design-System: CSS und JS stehen in `cro/07-prototype/build.py` (Startseite). `seminare/`, `michael/` und `rhetorik/` importieren es und ergänzen nur ihre eigenen Bausteine. Text je Seite: `04-copy/approved-copy.md` (Title, Meta, H1 im Frontmatter bzw. TECH-Block).

## 1. Seitenstruktur, URLs, Redirects
| Neu | Alt (meandyou.de) | Aktion |
|---|---|---|
| `/` | `/` | ersetzen (Page-Swap: neu bauen, alt offline, Slug übernehmen) |
| `/seminare` | keine eigene Seite | neu |
| `/michael` | keine | neu |
| `/rhetorik` | keine | neu |
| `/gespraech-buchen` | `/seminare-termin` | neu (Teil 2); 301 von `/seminare-termin` |
| `/sichtbarkeit-neu` | bleibt | Ziel des Soft-CTA auf `/rhetorik` |
| — | `/videokurs/start` | bleibt (Online-Kurs, nicht Teil dieses Laufs) |

**Interne Links, die nach dem Bau stimmen müssen:**
- Startseite S06 Format-Karten → `/seminare#frei-sprechen`, `/seminare#ruhig-bleiben`, `/seminare#mit-sprache-fuehren` (Anker existieren jetzt auf der Seminarseite).
- Alle Seiten: Menü Seminare, Michael, Was ist Rhetorik, Stimmen, FAQ; Footer „Termine“ → `/seminare#termine`.
- Im Prototyp zeigen Links noch auf die Vorschau `clients.741.studio/meandyou/v2/…`. Beim Bau durch relative Pfade ersetzen.

## 2. Tracking
Primärer Kanal: Buchung über die Terminseite (Calendly „Sichtbarkeit Neu“).
- Event `booking_click` auf jedem Link nach `termin.html` bzw. `/gespraech-buchen`, Parameter `page` = `utm_source` und `section` = `utm_content`.
- Die Links tragen die Parameter schon: Startseite `utm_source=startseite` (hero, situationen, michael, seminare, ablauf, stimmen, termine, abschluss, header, footer) · Seminare `seminare` (hero, einstieg, format-ruhig, format-fuehren, format-bundle, ablauf, termine, gespraech, abschluss, header, footer) · Michael `michael` (hero, werdegang, methode, medien, seminare, gespraech, abschluss, header, footer) · Rhetorik `rhetorik` (header, footer, abschluss-textlink).
- Event `training_click` auf `/rhetorik`: Links nach `/sichtbarkeit-neu?utm_source=rhetorik&utm_content=` (hero, ethos, methode, lernen, training, video, abschluss).
- Event `phone_click` auf `tel:+4915888367664`.
- Die Terminseite muss die UTM-Parameter an Calendly weitergeben (Teil 2).

## 3. Offene Kundendaten (gelb markiert)
| # | Punkt | Seiten | Quelle des Konflikts |
|---|---|---|---|
| 1 | Seminarnamen für Rhetorik I, II, III und Bundle | Startseite, Seminare | Copy Deck: noch beim Kunden |
| 2 | Name und Rolle der Person im Gespräch | alle | Funnel: Setter, nicht Michael |
| 3 | Übernachtung und Verpflegung (Sales-Checkliste) | Startseite, Seminare | Freigabe Kunde offen |
| 4 | Bundle: Termine, Ort, Plätze | Seminare | keine Quelle |
| 5 | Leitet Michael jedes Seminar selbst? | Michael, Rhetorik | institut-ehlers.de nennt zwei lizenzierte Trainer |
| 6 | Wortlaut Motto „Wer etwas zu sagen hat, sollte es sagen können.“ | Michael | nur englisch belegt |
| 7 | Inhalt und Länge des Video-Trainings (Wistia: 29:39 min) | Rhetorik | Vorschlag „rund 30 Minuten“ |
| 8 | Braucht das Video eine Anmeldung? | Rhetorik | /sichtbarkeit-neu zeigt keine |

**Konflikte für Martin oder Kunde:**
- AGB Storno (bis 8 Wochen, 30 %) gegen Sales-Checkliste (Gutschein). Seiten folgen den AGB.
- Mallorca-Termine 2027: PDF (22.–25.4., 23.–26.9.) gegen Live-Seite (29.4.–2.5., kein September). Seiten folgen der Live-Seite.
- „5 Bücher“ (Copy Deck) gegen neun Bücher (Michaels eigene Seite). Seiten sagen neun.
- Rhetorik 4 Mexico ohne Inhalte: nicht auf den Seiten.
- Krisenkommunikation und Inhouse laufen über institut-ehlers.de: erwähnt, nicht verlinkt.

## 4. Bilder und Shoot-Liste
**Echte Fotos im Einsatz:** Michael Magazin, Tür, Café, Olive, Sakko (Startseiten-Bestand); von institut-ehlers.de: Stuhl (Mai 2026), weißes Hemd, Gruppenfoto mit Zertifikaten (April 2023); Wistia-Standbild des Trainings-Videos; Video-Stimmen-Standbilder.
**Rechte klären:** Fotos von institut-ehlers.de (Nutzung auf meandyou.de), Einwilligung der Personen auf dem Gruppenfoto.
**GPT-Bilder (ersetzen durch echte Fotos):** Startseite Finca-Band, Situationen (2), Format-Karten (3), Abschluss-Terrasse; Seminare Einstieg-Gruppe, VR-Band, Bundle-Pitch. Ortsfotos: Pexels (Credits in `07-prototype/assets/city-credits.txt`).
**Shoot-Liste:** 1) Gruppe im Seminarraum mit sprechender Person, 2) VR-Training im Einsatz, 3) Videoanalyse am Bildschirm, 4) Get Together am Abend, 5) Michael beim Feedback in der Gruppe, 6) Seminarorte mit echter Location (Mallorca, Barcelona).
**Video-Stimmen:** Poster mit eingebrannten Untertiteln → andere Standbilder aus Wistia wählen.
**Fehlende Logo-Dateien:** ARTE, WELT TV (Michael-Seite nennt sie nur im Text).

## 5. Schema
Startseite: WebPage, EducationalOrganization, Person, EducationEvent je Termin (ohne Preis). Seminare: Course je Format mit CourseInstance (Ort, Datum). Michael: ProfilePage + Person (hasCredential, affiliation getrennt Uni und SGMI, sameAs 4 Profile). Rhetorik: Article mit Autor Michael, about → Wikipedia. Kein FAQPage. `sameAs` der Organisation bleibt leer, bis Profile geprüft sind.

## 6. Vor Go-Live
`00_project/website-security-checklist.md` · `noindex` entfernen · Telefonnummer klären (Seite +49 15888367664, GBP +49 160 96600322) · Impressum, Datenschutz, AGB verlinkt · Consent für Wistia und Calendly.

## Startseite: offene Marken
- [FEHLT: Freigabe Übernachtung]
- [von Kunde bestätigen: Name und Rolle der Person im Gespräch]
- [von Kunde bestätigen: Seminarname]
