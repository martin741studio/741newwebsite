# Diagnose: Über-mich-Seite Daniela Dumann

Stand 2026-10-11. Grundlage: `02-data/dataset.md`. Bewertung nach `00_project/knowledge/cro-library/_derived/scorecard.md` (Desktop). Seitentyp Behandlerinnen-Seite: Items, die nur für den Einstieg über die Startseite gelten (3 Sub-Headline Situation zuerst, 9 „Dein erster Termin", 15 Situationen-Sektion, 16 Leistungskarten), zählen hier nicht. Dafür drei Seitentyp-Punkte (A1 bis A3) aus dem bewährten Behandlerinnen-Seiten-Muster (Skill `behandler-seite`, Pilot Praxis Hüwel) und dem Library-Muster P1 (Therapeutin: Foto, Name, Schwerpunkte, Zitat, Bewertungswand).

## 1. Bewertung der aktuellen Seite /lebenslauf

| # | Regel | Prio | Score | Beleg |
| --- | --- | --- | --- | --- |
| 1 | Hero in 5 Sekunden: wer, wofür, nächster Schritt | A | 0 | H1 „Über mich", direkt darunter eine Liste von Titeln. Kein nächster Schritt im Inhalt (dataset 1.1). |
| 2 | Headline nennt Ergebnis oder Rolle plus Stadt | A | 0 | Weder Name noch „Heilpraktikerin" noch Stadt in H1 oder Title (dataset 1.1). |
| 4 | Primärer CTA im ersten Bildschirm (1440×800) | A | 1 | „Termin buchen" nur im Kopf, klein, kein Telefon (dataset 1.1). |
| 5 | CTA-Text nennt Schritt und Nutzen | A | 1 | „Termin buchen", neutral (dataset 1.1). |
| 6 | Rückversicherung direkt unter dem CTA | A | 0 | Nicht vorhanden. |
| 7 | Zwei Beweisformen above the fold | A | 1 | Titel und Vorstand-Funktion sind Beweise, aber als nackte Liste ohne Gewichtung. Keine Bewertung, kein Foto im ersten Bildschirm. |
| 8 | Gesicht und Qualifikation im ersten Bildschirm | A | 1 | Portrait nur 375 px klein, mitten in der Liste, nicht im Blickfeld (dataset 1.1). |
| 10 | Eine CTA-Farbe, Blur-Test | A | 1 | Ein Button vorhanden, aber im Kopf ohne Gewicht. |
| 11 | CTA mindestens alle 2 Sektionen | A | 0 | Ein einziger CTA auf der ganzen Seite. |
| 12 | Bewertungen offen, Vorname, Google-Logo | B | 0 | Keine Bewertungen (dataset 1.1, 1.7). |
| 13 | Beweis-Überschrift trägt Nutzen | B | 0 | Keine Beweis-Sektion. |
| 14 | 3 bis 4 Beweisblöcke verteilt | B | 1 | Beweise liegen vollständig vor (Jahre, Vorstand, Schule, Mitgliedschaften), aber in einem Block. |
| 17 | FAQ mit echten Einwänden | B | 0 | Keine FAQ. |
| 18 | Standort: Karte, Adresse, ÖPNV, Zeiten | B | 1 | Adresse und Anfahrt im Fuß, keine Karte. |
| 19 | Abschluss = Mini-Hero | B | 0 | Seite endet mit Kontaktblock ohne Aussage. |
| 20 | Überschriften mit Aussage | C | 0 | „Über mich", „Schwerpunkte", „Privat" sind Labels. |
| 21 | Typografie und Hierarchie | C | 1 | Liste ohne Hierarchie, aber lesbar. |
| 22 | HWG | A | 1 | Die alte Seite selbst ist sauber, aber die Pflicht-Hinweisbox fehlt (dataset 1.9). |
| A1 | Name plus Rolle plus Stadt in Title, H1, Meta | A | 0 | Title „Lebenslauf | Hildegard von Bingen Naturheilkunde | Berlin", H1 „Über mich" (dataset 1.1). |
| A2 | Person-Schema mit hasCredential, worksFor, sameAs | A | 0 | Kein JSON-LD (dataset 1.1). |
| A3 | Werdegang belegt und lesbar (Timeline plus Qualifikationen-Überblick) | B | 1 | Alle Fakten da, aber ungeordnet (dataset 1.2). |

Summe Ist-Zustand: 11 von 42 Punkten (21 Items, je 0 bis 2).

## 2. Lücken (alle Items mit 0 oder 1), nach Wirkung geordnet

Priority A: Hero ohne Name/Rolle/Stadt (1, 2, A1), kein Gesicht im Blickfeld (8), kein CTA mit Rückversicherung (4, 5, 6, 11), Beweise nicht gewichtet (7), Person-Schema fehlt (A2), HWG-Hinweisbox fehlt (22).
Priority B: keine Bewertungen (12, 13), keine Beweisblöcke (14), Werdegang ungeordnet (A3), keine FAQ (17), keine Karte (18), kein Abschluss (19).
Priority C: Überschriften sind Labels (20), keine Hierarchie (21).

## 3. Idealer Ausgang (Plan)

Eine Seite, die in 5 Sekunden zeigt: „Daniela Dumann, Heilpraktikerin in Berlin-Charlottenburg seit 2002, Vizepräsidentin der Internationalen Gesellschaft Hildegard von Bingen". Sie zeigt ihr Gesicht, die vier stärksten Belege in einer Leiste, den Werdegang als lesbare Zeitleiste, ihre Haltung in eigenen Worten (HWG-sicher), ihre Lehre und Gesellschaft als Autorität, echte Bewertungen, die die Person beschreiben, eine FAQ mit den Fragen zur Person, die Pflicht-Hinweisbox und einen ruhigen Abschluss mit Buchung und Telefon.

Pattern-Wahl: Behandlerinnen-Seiten-Muster (Skill `behandler-seite`: Hero, Trust-Bar, Ansatz, Werdegang, Motivation, Hinweisbox, Final-CTA) mit P1-Stimmung (emotional, vertrauensbasiert, Person kaufen) und den visuellen Bausteinen der Startseiten-Prototypen v2 (gleiches Design-System, damit die beiden Seiten zusammenpassen).

## 4. Abschnittsplan (12 Sektionen) und Abdeckung des P0-Blueprints

| # | Abschnitt | Job | P0-Zeile |
| --- | --- | --- | --- |
| 1 | Hero | wer, was, wo, nächster Schritt | 1 Hero |
| 2 | Trust-Leiste (4 Belege plus Bewertung) | Vertrauen vor allem anderen | 2 Beweiswand (Kurzform) |
| 3 | Mein Ansatz (4 Karten) | Haltung und Arbeitsweise in Ich-Form | 6 Über die Behandlerin |
| 4 | Mein Weg (Zeitleiste plus Qualifikationen-Karte) | Werdegang belegt | 6 Über die Behandlerin |
| 5 | Meine Schwerpunkte (5 Karten, verlinkt) | zu den Behandlungsseiten führen | 4 Leistungen (Kurzform) |
| 6 | Lehre und Gesellschaft (Viriditas, Gesellschaft, Regionalgruppe, Garten) | Autorität und Gemeinschaft | 6 Über die Behandlerin |
| 7 | Bewertungen (3 offene Karten) | Vertrauen vor der Entscheidung | 7 Reviews |
| 8 | Warum dieser Weg (dunkles Band, persönliche Motivation, Privat) | Menschen kaufen von Menschen, HWG-defensiv | 6 Über die Behandlerin |
| 9 | Häufige Fragen zur Person (4 Fragen) | letzte Zweifel | 8 FAQ |
| 10 | Hinweisbox (HWG) | rechtliche Pflicht | nicht im Blueprint, Pflicht Behandlerinnen-Seite |
| 11 | Standort (Karte, Anfahrt) | Kann ich hinkommen | 9 Standort |
| 12 | Abschluss (Mini-Hero) | Buchung und Telefon | 10 Closer |

**Abdeckungs-Prüfung gegen die 10 Zeilen des P0-Blueprints:**

| P0 | Auf dieser Seite | Grund |
| --- | --- | --- |
| 1 Hero | ja (1) | |
| 2 Beweiswand | ja (2 und 7) | |
| 3 „Ist das etwas für dich?" | nein | Einstiegs-Sektion der Startseite. Eine Behandlerinnen-Seite beantwortet „Wer ist sie?", nicht „Passt das zu meiner Situation?". Die Startseite hat sie. |
| 4 Leistungen | Kurzform (5) | nur als Weiterleitung zu den Behandlungsseiten |
| 5 Dein erster Termin | nein, nur in FAQ und Abschluss | Ablauf steht in Startseite Sektion 5. Hier genügen Dauer und Preis in der Rückversicherungszeile und eine FAQ-Antwort. |
| 6 Über die Behandlerin | ja, Kern der Seite (3, 4, 6, 8) | |
| 7 Reviews 2 | ja (7) | |
| 8 FAQ | ja (9) | |
| 9 Standort | ja (11) | |
| 10 Closer | ja (12) | |

CTA in Abschnitt 1, 3 (unter den Karten), 4 (unter der Zeitleiste), 6, 8, 11 und 12 (Regel: mindestens jede zweite Sektion).

## 5. Offene Punkte aus der Diagnose

Siehe `02-data/dataset.md`, Abschnitt „Offene Punkte". Keine Rückfrage an die Kundin nötig für den Entwurf. Martin bekommt am Ende die Liste der Dinge, die vor einem Livegang zu klären sind.
