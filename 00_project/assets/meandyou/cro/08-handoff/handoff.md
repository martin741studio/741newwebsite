# Übergabe — me&you Website (Michael Ehlers), CRO-Prototypen

Stand 2026-10-12. Gemeinsame Übergabe für alle Seiten des Neuaufbaus. Teil 1 enthält die vier fertigen Seiten. Stimmen, FAQ und Gespräch buchen laufen parallel und kommen als Teil 2 dazu.

## 0. Status
| Seite | Slug | Prototyp | Raster vorher → jetzt | Freigabe Martin |
|---|---|---|---|---|
| Startseite | `/` | `cro/07-prototype/index.html` | 20 → 37 von 42 | Copy 11.10., Prototyp 12.10. („sehr gut“, Google-Kachel S02 entfernt) |
| Seminare | `/seminare` | `cro/seminare/07-prototype/index.html` | 11 → 37 | Copy + Prototyp 12.10. |
| Michael | `/michael` | `cro/michael/07-prototype/index.html` | 15 → 39 | Copy + Prototyp 12.10. |
| Was ist Rhetorik | `/rhetorik` | `cro/rhetorik/07-prototype/index.html` | 14 → 38 | Copy + Prototyp 12.10. |
| LP Replayers (Persona) | Vorschlag `/schlagfertigkeit-lernen` (Entscheidung offen) | `cro/lp-replayers/07-prototype/v2/index.html` (Community-Version) | 18 → 42 von 44 | Copy + Prototyp 12.10. |
| LP Overlooked (Persona) | offen (z. B. `/lp-overlooked`) | `cro/lp-overlooked/07-prototype/index.html` | 19 → 47 von 48 | Copy + Prototyp 12.10. |
| LP Undersold (Persona) | Vorschlag `/rhetorik-seminar-fuehrungskraefte` (Entscheidung offen) | `cro/lp-undersold/07-prototype/index.html` | 15 → 40 von 44 | Copy + Prototyp 12.10. |

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

## LP Undersold (Persona-Seite, Teil 3)
- Quelle: Content Pool `content-pool/04-pool/pool.json` (page_tag `lp:undersold`), Text `cro/lp-undersold/04-copy/approved-copy.md`, 1.440 Wörter (Untergrenze 836).
- Slug offen. Vorschlag der Session: `/rhetorik-seminar-fuehrungskraefte`. Die Startseiten-Karte „Dein Unternehmen ist größer …“ verlinkt die Seite (lokal und v4 umgesetzt).
- Ein Button im Inhalt, weit unten („Gespräch buchen“, `utm_source=lp-undersold`, `utm_content` header, abschluss, footer). Keine Dringlichkeit, keine Preise.
- Schema: drei Course mit allen elf Terminen, ohne Preis. Michael erst als `instructor`, wenn der Kunde bestätigt, dass er jedes Seminar leitet.
- GPT-Bilder ersetzen: Hero (Terrasse Mallorca, Gruppe) und Gruppe auf der Terrasse. Shoot-Liste: echte Terrassen-Gruppe, echte Fotos je Ort.
- Offene Kundendaten: Seminarnamen, Person im Gespräch, Mallorca-Termine 2027, Übernachtung und Verpflegung, leitet Michael jedes Seminar, Bundle-Termine, Zitate von Unternehmern, 1:1-Coaching und Medientraining (ja/nein), sameAs-Profile.
- Telefonnummer klären: Seite +49 15888367664, Google-Profil +49 160 96600322.

## LP Replayers (Persona-Seite)
- **Stand 12.10. abends: Community-Version freigegeben.** CTA überall „Community beitreten“ → Skool `talk-to-me-9409/about?utm_source=lp-replayers&utm_content=<abschnitt>`, Event `community_click`, kein „Gespräch buchen“ auf dieser Seite (auch Header). Preis 39 €/Monat von Martin bestätigt (12.10.); gelbe Marken entfernt. Skool-Button zeigte $44: Kunde prüft die Skool-Einstellung. Skool-Text enthält Ergebnisversprechen (UWG): Kunde soll entschärfen. Video-Training nur noch als stiller Textlink (führt selbst zur Gesprächsbuchung: Entscheidung offen).
- Ursprüngliche Gesprächs-Version (v1, `07-prototype/index.html`) bleibt nur zum Vergleich.
- Text `cro/lp-replayers/04-copy/approved-copy.md`, 1.698 Wörter (Untergrenze 1.083). Pool-Items CP-1nn.
- Ein Button pro Bildschirm: Der Header-Button blendet sich aus, solange ein Abschnitts-Button sichtbar ist. Soft-CTA kostenloses Training `/sichtbarkeit-neu?utm_source=lp-replayers`. Event `training_click` wie auf `/rhetorik`.
- Offene Kundendaten: Inhalt, Länge und Anmeldung des Video-Trainings, Übungen von Michael im Wortlaut, Michaels Satz zu „Worte kommen zu spät“, Buchtitel, Bezugsquelle und Cover, Podcast-Cover-Freigabe, Name des Schlagfertigkeits-Seminars, Einwilligung Zitat-Namen.
- Interne Links ergänzen: Textlink von `/rhetorik` und aus der FAQ.

## LP Overlooked (Persona-Seite)
- Text `cro/lp-overlooked/04-copy/approved-copy.md`, 1.608 Wörter (Untergrenze 1.193). Pool-Items CP-2nn. Nur „Gespräch buchen“ (9 Links mit eigenem `utm_content`).
- Hero-Foto ist ein GPT-Bild (Michael am Glastisch): vor Go-Live durch echtes Foto ersetzen.
- Offene Kundendaten: Einwilligung Zitat (AfO), Satz und Übung je Methodenschritt, Seminarnamen, Name und Extras des Online-Kurses, Person im Gespräch, Logo-Rechte, Rückerstattungsregel.

## Einheitlich klären (alle Persona-Seiten)
- Formulierung ERFOLG Magazin: Overlooked „Ausgabe 2017“, Replayers Vergangenheit, übrige Seiten Gegenwart. Eine Fassung für alle Seiten.
- Slugs der drei Persona-Seiten. Die Startseiten-Karten verlinken alle drei (lokal und v4 umgesetzt).

## Round Table 12.10. umgesetzt (13.10.)
- Neuer Haupt-Button „Optionen ansehen“ → neue Seite `/optionen` (`cro/optionen/`, Text `04-copy/copy.md`, Slop-Check 5/5). Die Seite zeigt fünf Wege: kostenloses Video-Training, Community Talk to ME (44 US-Dollar/Monat), Online-Kurs, Seminare, Gespräch. Event `options_click`, `utm_source=optionen`.
- Umgestellt auf allen Seiten außer Replayers (Community), Gespräch buchen und Optionen. Abschnitte, die das Gespräch selbst erklären (`utm_content` ablauf, gespraech, kosten; Undersold abschluss), behalten „Gespräch buchen“.
- Umsetzung im Site-Build (`cro/site-build/assemble.py`), die Prototyp-Quellen der Einzelseiten sind unverändert. Beim echten Bau den Button-Text in den Seitenquellen ändern.
- Livegang bleibt vorerst auf clients.741.studio (Entwurf C, v4). Deploy nur mit `deploy/ftp-v4-safe.mjs` (erster Lauf 13.10. erfolgreich, 5:32 min, Seite blieb erreichbar).

## Änderung 13.10. abends (Pauspapier)
- „Optionen ansehen“ führt immer zur Terminseite `/gespraech-buchen`, nicht auf eine eigene Optionen-Seite. Begründung Pauspapier: das Gespräch ist das Einzige, was zählt. Event wieder `booking_click`.
- Die Seite `/optionen` ist offline. Quelle bleibt in `cro/optionen/`, falls sie später gebraucht wird.
- Die Mikrotexte unter den Buttons sind wieder die Gesprächs-Texte („30 Minuten, kostenlos, per Video …“).

## Rechtliche Seiten gebaut (19.10., Martin: Entwurf C ist die Basis, kein Framer)
- Neue Seiten `/impressum`, `/datenschutz`, `/agb` in Entwurf C, Quelle `cro/impressum/`, `cro/datenschutz/`, `cro/agb/` (Design aus `cro/rechtliches_build.py`, Text 1:1 aus den Live-Seiten kopiert, Quelle `cro/rechtliches_quelltext.py`). Keine CRO-/Content-Writing-Gates, da reiner Gesetzestext ohne Marketing-Anteil.
- Einzige inhaltliche Änderung: Impressum nennt jetzt **Tarek Port als Geschäftsführer** statt „Vertretungsberechtigt: Michael Ehlers". Stand-Datum im Impressum auf 19.10.2026 gesetzt (einziges geändertes Faktum). Datenschutz und AGB unverändert, eigenes Stand-Datum 08.09.2025 bleibt.
- Footer-/Nav-Links auf allen Seiten zeigen jetzt lokal auf `impressum.html` / `datenschutz.html` / `agb.html` statt extern auf meandyou.de (Umsetzung in `cro/site-build/assemble.py`).
- Offener Fund (nicht behoben, nicht gefragt): Der Footer-Adressblock auf allen Seiten zeigt weiter „Institut Michael Ehlers GmbH, Landsknechtstraße 50, 96103 Hallstadt" (deutsche GmbH) während das Impressum „Me&You Communication FZCO" in Dubai nennt. Zwei verschiedene Firmen. Gleiches gilt für das JSON-LD-Schema jeder Seite (`name: "Institut Michael Ehlers GmbH"`).

## Firmen-Konflikt gelöst (19.10., Martin: Me&You Communication FZCO überall)
Fußzeile und Schema aller 13 Seiten nennen jetzt „Me&You Communication FZCO", Dubai Silicon Oasis, DDP, Building A1, Dubai, VAE — statt „Institut Michael Ehlers GmbH", Hallstadt. Umsetzung global in `cro/site-build/assemble.py`. Nicht angefasst: die FAQ-Antwort auf der Michael-Seite „Wo sitzt sein Institut?" nennt weiter „Institut Michael Ehlers GmbH … Hallstadt bei Bamberg" — das ist Michaels reales Trainings-Institut (eigene Adresse laut institut-ehlers.de), eine andere Sache als der Website-Betreiber und bewusst unverändert.
