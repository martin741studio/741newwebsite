# Recherche: dringender und vertraulicher Kontakt (Muster, kein Inhalt)

**Datum:** 2026-10-11
**Auftrag:** Muster für Notfall-Einstieg, vertraulichen Erstkontakt, Ablauf und zwei Standorte auf der Stürzl-Startseite.
**Gesehen:** 18 Websites (14 per Screenshot ausgewertet, 4 nur teilweise, siehe Grenzen).

| Gruppe | Websites |
|---|---|
| Straf- und Steuerstraf-Boutiquen (DE) | Park (park-wirtschaftsstrafrecht.de), Wessing & Partner (strafrecht.de), Kanzlei Wild (wild.legal), Müller Fischer (muellerfischer.de), KFDR (kfdr.de), Dr. Böttner (strafrecht-bundesweit.de), Schneider II Mick (strafrecht.berlin, Startseite und Notruf-Seite), Buchert Jacob Peter (dr-buchert.de), VONPELCHRZIM (pelchrzim.de/en), Feigen Graf (feigen-graf.de) |
| White-Collar international | Rahman Ravelli (rahmanravelli.co.uk), Kingsley Napley (Seite Criminal Litigation) |
| Dringend, aber ruhig (andere Branchen) | krisenchat.de, TelefonSeelsorge (telefonseelsorge.de), Privatklinik Bethanien (swissmedical.net), Precursor Security (Incident Response), Endida (Incident Response) |
| Zwei oder mehr Standorte, Familienrecht | Haibach Rechtsanwälte (haibach.com) |

Nur als Suchauszug gelesen, nicht per Screenshot: Böttner-Notfallseite (Nummer je Stadt), Gubitz & Partner (Kiel/Hamburg, Notnummern außerhalb der Bürozeiten), Withers (24-Stunden-Hotline), Höllwarth Wien (24/7-Notfallseite).

## Grenzen (ehrlich)

- Alle Bilder sind **Desktop 1440 px im Ruhezustand**. Keine mobile Ansicht gesehen.
- Cookie-Banner decken bei Park, Böttner, Haibach, Kingsley Napley, Bethanien und Precursor Teile des Heros ab.
- Reveal-Sektionen erscheinen leer (Müller Fischer, Endida). Was dort passiert, habe ich nicht gesehen.
- **Bewegung ist abgeleitet.** Nur zwei Punkte stammen aus dem Code: Wild setzt `globalViewTransitions` für htmx (Seitenübergänge). Precursor setzt gestaffelte `animation-delay`-Werte (1200 bis 1500 ms) auf die Siegel-Karten. Alles andere ist mit "abgeleitet" markiert.
- Wessing & Partner rendert im Scraper nur halb (fehlendes Bild, kaum Layout). Mein Urteil dort gilt nur für das Sichtbare.
- Firecrawl-Limit: Gubitz und Withers konnte ich nicht mehr scrapen.
- Bewertungszahlen aus Suchauszügen (z. B. "4,9 mit 1.762 Bewertungen") habe ich nicht geprüft.
- Alle Rechtsfragen (BRAO § 43b, BORA § 6, UWG, § 203 StGB) sind Hinweise für das Team, keine Rechtsprüfung.
- Zusätzliche Ausschnitte (`-foot.jpg`, `-form.jpg`) habe ich selbst aus den Vollbildern geschnitten. Alle Tiles liegen in `02-data/references/urgent/`.

## Elemente

Kürzel: S = klein (unter 0,5 Tag), M = mittel (bis 1,5 Tage), L = groß. Marken-Farben: Rot und Neon aus den Beispielen immer durch Salbei und Charcoal ersetzen. Der CTA ist nur #4E6F55.

| ID | Element | Was es für den Besucher tut | Beispiel und Ort | Sektion bei uns | Aufwand | Risiko-Hinweis | Tile |
|---|---|---|---|---|---|---|---|
| U1 | Schmale Notfall-Leiste ganz oben: Label plus Nummer links, Sprachwahl rechts | Die Nummer ist sofort da und stört nichts. Kein Banner, kein Pop-up. | Park, oberste Leiste der Startseite | Notfall-Streifen | S | "24 Stunden" nur sagen, wenn es stimmt (UWG, Irreführung). Keine Farbe, die nach Alarm aussieht. | park-t0.jpg |
| U2 | Ankündigungsleiste mit messbarer Zusage: "Aktiver Vorfall? Jetzt anrufen" plus durchschnittliche Abholzeit | Nennt die Wartezeit. Das nimmt Unsicherheit vor dem Anruf. Der Satz ist ein Fakt, kein Appell. | Precursor, Leiste über der Navigation (Quelle: roter Punkt, hier Salbei) | Notfall-Streifen | S | Zusage nur mit echten Zahlen. Keine Erfolgs- oder Ergebnisversprechen. Nicht rot, nicht blinkend. | precursor-t0.jpg |
| U3 | Notfall als gleichwertiger Eintrag in einer Hilfsleiste (Mail, Telefon, Termin, Kontakt, Notfalldienst) | Ruhig und immer auffindbar. Wirkt wie Service, nicht wie Alarm. | Bethanien, Leiste über dem Header | Notfall-Streifen oder ganze Seite | S | Wenn "Notfall" nur ein Link unter vielen ist, kann er untergehen. Nummer direkt sichtbar machen. | bethanien-t0.jpg |
| U4 | Anlässe in Alltagssprache direkt neben der Nummer (Festnahme, Durchsuchung der Wohnung, Praxis oder Geschäftsräume) als kurze Liste | Besucher erkennen ihre Lage und wissen, dass die Nummer für sie gilt. | Schneider II Mick, Seite Notruf, erster Block | Notfall-Streifen (Aufklapp-Teil) | S | Nüchtern formulieren. Keine Steigerung, keine Angstwörter. Wir nutzen "Durchsuchung läuft gerade?" ohne Bild dazu. | sm-notruf-t0.jpg |
| U5 | Ehrliche Erreichbarkeitszeile: was nachts gilt, was zu Bürozeiten gilt | Besucher wissen, wann jemand abnimmt und wann zurückgerufen wird. Das schafft Vertrauen. | Schneider II Mick, Notruf-Seite (Nacht und Büro getrennt). Wild, Fußzeile (Mo bis Fr 9 bis 18 Uhr und nach Vereinbarung) | Notfall-Streifen | S | Muss mit der echten Organisation übereinstimmen. Keine Bereitschaft versprechen, die es nicht gibt. | sm-notruf-t1.jpg, wild-foot.jpg |
| U6 | Drei kurze Verhaltensregeln mit Verb vorn und je einer Erklärzeile | Gibt in der Lage sofort etwas Konkretes. Senkt Panik, ohne zu dramatisieren. | Schneider II Mick, Notruf-Seite ("Dulden", "Anrufen", "Schweigen") | Notfall-Streifen (Aufklapp-Panel) | M | Quelle nutzt ein Warndreieck: weglassen. Inhalt vom Anwalt freigeben lassen. Allgemeiner Hinweis, keine Einzelberatung. | sm-notruf-t1.jpg |
| U7 | Eigene Notfallnummer je Standort, auf einer eigenen Notfall-Seite | Besucher in der Nähe rufen den Ort an, der zu ihnen passt. Beide Orte gleich wichtig. | Böttner, Seite Notfallkontakt (Nummer je Stadt, nur Suchauszug). Park, Fußzeile (Emergency je Ort) | Notfall-Streifen und Standorte | S | Nur sinnvoll, wenn beide Nummern wirklich besetzt sind. | park-foot.jpg |
| U8 | Ruhiger Satz in Serifen-Schrift, darunter die Nummer in Headline-Größe | Die Nummer ist der größte Text der Seite, aber der Ton bleibt weich. | TelefonSeelsorge, Hero links | Hero | S | Der Satz "Sie sind nicht allein" ist emotional. Für Stürzl neutral halten (Lage benennen, nicht trösten). Newsreader passt zur Serifen-Wirkung. | telefonseelsorge-t0.jpg |
| U9 | Kanal-Kacheln: Telefon, Chat, E-Mail, Kompass, Vor-Ort als gleich große Kacheln mit Icon und Pill-Label | Besucher wählen den Kontaktweg, der zu ihrer Lage passt. Kein Weg wird bevorzugt versteckt. | TelefonSeelsorge, unter der Nummer | Hero oder Formular/Abschluss | M | Für uns: Anruf, Rückruf, Formular, E-Mail. **Kein WhatsApp** für Mandatsdaten. Icons ohne Schloss. | telefonseelsorge-t0.jpg |
| U10 | Drei Fakten-Chips unter der Headline (erreichbar, kostenlos, für wen) | Beantwortet die drei ersten Fragen, bevor jemand sie stellt. | krisenchat, Hero | Hero | S | "Kostenlos" ist bei Anwälten eine Preisaussage (RVG, BORA). Nur Fakten, die stimmen: z. B. Orte, Rückruf, Vertraulichkeit. | krisenchat-t0.jpg |
| U11 | Zwei Hero-Buttons: Anruf als Haupt-CTA, "Ablauf ansehen" als zweiter Weg | Wer noch nicht anrufen will, bekommt ohne Druck den Ablauf. | Precursor, Hero (roter Button plus dunkler Button) | Hero | S | Rot der Quelle ersetzen. Haupt-CTA nur in #4E6F55. Zweiter Button als Outline. | precursor-t0.jpg |
| U12 | Primärer Button plus kleiner Text-Link darunter "Informationen zur Terminvereinbarung" | Erklärt den Ablauf an der Stelle der Entscheidung. | Müller Fischer, Hero (Link teils vom Pop-up verdeckt) | Hero | S | Kein Risiko. Link muss auf den Ablauf-Block springen, nicht auf eine Fremdseite. | muellerfischer-t0.jpg |
| U13 | Hero-Aussage in zwei Sätzen: wer wir sind, dann Reichweite ("innerhalb und außerhalb des Verfahrens, bundesweit") | Zeigt früh, dass man auch ohne laufendes Verfahren kommen kann, und dass die Reichweite national ist. | KFDR, Hero | Hero | S | "International" und "bundesweit" nur, wenn belegbar. Keine Superlative. | kfdr-t0.jpg |
| U14 | Fakten-Punktzeile aus vier Kurzaussagen, danach versetzt eingeblendete Siegel-Karten | Eine Zeile Beleg statt eines Wandbilds. Die Siegel erscheinen ruhig nacheinander. | Precursor, Band unter dem Hero. Bewegung aus dem Code (animation-delay 1200 bis 1500 ms), Wirkung nicht live geprüft | Beweis-Leiste | S | Keine Fallzahlen oder Erfolgsquoten (BORA § 6, UWG). Nur Titel, Orte, Verschwiegenheit. Reveal nur einmal (CRO-Motion-Regel). | precursor-t1.jpg, precursor-t0.jpg |
| U15 | Zwei Siegel als kleine Bild-Badges am unteren Rand des Heros, neben dem Text | Beleg direkt am ersten Blick, ohne eigenen Block. | Müller Fischer, Hero unten links | Beweis-Leiste | S | Siegel nur mit Quelle und Jahr und nur mit gültiger Lizenz. Wording "TOP" der Quelle nicht übernehmen (Spitzenstellung, UWG). | muellerfischer-t0.jpg |
| U16 | Auszeichnungen rein typografisch in vier Spalten: Quelle, Titel, Jahr | Ruhige Belegzeile ohne Logo-Chaos. Quelle und Jahr stehen da. | VONPELCHRZIM, Fußzeile | Beweis-Leiste | S | Quelle zeigt Superlative ("beste", "TOP"). Wir schreiben Titel und Quelle neutral. Methode der Quelle verlinken. | pelchrzim-foot.jpg |
| U17 | Titelzeilen direkt unter dem Namen (Fachanwalt für X, Fachanwalt für Y, Zertifizierung) | Titel stehen am Gesicht. Kein Extra-Block nötig. | KFDR, Personenkarten | Beweis-Leiste | S | Titel exakt nach FAO und nur mit Nachweis. Zertifikat-Angaben prüfen (UWG). | kfdr-t2.jpg |
| U18 | Situations-Karten "Was beschäftigt Sie?" mit Titel und zwei Zeilen Text je Karte | Besucher finden ihren Fall über die Lage, nicht über Rechtsbegriffe. Auch Kingsley Napley sortiert die Navigation "nach Situation". | TelefonSeelsorge, Block "Was macht Ihnen Sorgen?" | Mandanten | M | Quelle nutzt Fotos leidender Menschen: nicht übernehmen. Nur Text-Karten. Keine Fallbeispiele (§ 203 StGB). | telefonseelsorge-t1.jpg |
| U19 | Selbsttest in drei Fragen ("Haben Sie eine Vorladung erhalten? Werden Sie verdächtigt?") als Aufzählung | Besucher erkennen sich wieder und wissen: das ist mein Fall. | Schneider II Mick, Startseite, erster Textblock | Mandanten | S | Fragen neutral halten. Keine Aussicht auf Ausgang. Quelle schreibt daneben "beste Strafverteidigung": nicht übernehmen. | schneidermick-t1.jpg |
| U20 | Ablauf als horizontale Pipeline: vier Schritte mit Nummer, kleinem Icon und Titel | Zeigt den ganzen Weg auf einen Blick. Passt zu unseren vier Schritten. | Precursor, Block "Incident Response Process" | Ablauf | M | Icons ohne Schloss, Waage, Hammer. Nur Ziffern oder neutrale Linien-Icons. | precursor-t3.jpg |
| U21 | Zeitleiste "Die ersten 60 Minuten" mit relativen Zeitmarken (0:00, 0:05, 0:30, 1:00) | Macht den Ablauf nach dem Anruf greifbar. | Precursor, dunkle Karte | Ablauf | M | Zeitangaben müssen real sein. Keine Ergebnis-Zusage. Dunkle Karte in Charcoal statt Marine. Bewegung abgeleitet (Marken ruhig einblenden). | precursor-t2.jpg |
| U22 | FAQ-Akkordeon mit den Sorgenfragen der Besucher ("Bleibe ich anonym?", "Ruft ihr die Polizei?", "Wie lange muss ich warten?") | Beantwortet die Angst vor dem ersten Schritt, ohne dass jemand fragen muss. | krisenchat, Block "Du hast Fragen zum Chat?" | Vertraulich | M | Antworten juristisch freigeben lassen. Aussagen zu Verschwiegenheit nur nach § 43a BRAO und § 203 StGB. Bewegung abgeleitet (Aufklappen). | krisenchat-t2.jpg |
| U23 | Begrüßungstext der Leitung mit einem Satz zu Diskretion, Foto daneben | Ein Mensch spricht direkt. Wirkt ruhig und verbindlich. | Bethanien, Abschnitt "Willkommen" | Vertraulich | S | Quelle sagt "absolute Diskretion": Superlativ, nicht übernehmen. Besser: Verschwiegenheit als Berufspflicht benennen. | bethanien-t3.jpg |
| U24 | Mehrstufiges Formular mit großen Ziffern 1 bis 4 links, Ort-Wahl als erstem Schritt, dann Thema als Ankreuzfeld, Button "Weiter" | Klein starten, Schritt für Schritt. Der Ort ist die erste, gleichwertige Entscheidung. Es gibt keinen Freitext für Falldaten. | Haibach, Block "Terminanfrage" | Formular/Abschluss | M | Genau das Muster "Formular ohne Falldaten": nur Thema, Ort, Rückweg. Kein Freitext (§ 203 StGB). Datenschutz-Hinweis am Absenden. | haibach-t4.jpg, haibach-form.jpg |
| U25 | Formular mit Kontextzeile ("Sie kontaktieren das Team Strafrecht") und Verweis auf die Dringend-Nummer mitten im Hinweistext | Besucher sehen vor dem Absenden, wer liest und was bei Eile gilt. | Kingsley Napley, "Contact us in confidence" | Formular/Abschluss | S | Die Quelle hat ein Freitextfeld (2000 Zeichen). Das lädt zu Falldaten ein. Bei uns weglassen. | kingsleynapley-foot.jpg |
| U26 | Kontaktband: große Zeile "Kontaktieren Sie uns" mit nur einem Button, darunter Standort-Spalten | Ein klarer Abschluss ohne Ablenkung. | Feigen Graf, Fußbereich | Formular/Abschluss | S | Quelle zeigt oben "marktführende Spezialkanzlei": nicht übernehmen. Nur den Aufbau. | feigengraf-foot.jpg |
| U27 | Zwei gleich breite Spalten, je Ort mit Adresse, Telefon, **eigener Notfallnummer**, E-Mail, über einem Foto der Empfangshalle | Beide Orte sind exakt gleich gebaut. Beide Notfallnummern sind sichtbar. | Park, Fußzeile (Dortmund und Hamburg) | Standorte | S | Nur Nummern angeben, die besetzt sind. Foto echt, kein Stock. | park-foot.jpg |
| U28 | Dunkles Kontaktband: E-Mail oben, dann je Stadt eine Zeile mit Telefon-Icon (München, Frankfurt) | Schnell lesbar, jede Stadt gleich gesetzt. | KFDR, Band über der Fußzeile | Standorte | S | Fax-Zeilen weglassen. Telefonnummer klickbar (`tel:`). | kfdr-foot.jpg |
| U29 | Karte mit gestapelten Standort-Schaltern links unten; darunter Fußzeilen-Spalten je Ort | Besucher wählen den Ort und die Karte folgt. | Müller Fischer, Fußbereich. Reaktion der Karte abgeleitet | Standorte | M | In der Quelle ist ein Ort dunkel hervorgehoben. Das gewichtet ungleich. Bei uns beide gleich oder keiner aktiv. | muellerfischer-foot.jpg |
| U30 | Stilisierte Deutschlandkarte mit Städtepunkten und Namens-Etiketten | Zeigt "bundesweit" und die Orte in einem Bild. | Böttner, Block Standorte | Standorte | M | Reichweite nur behaupten, wenn sie stimmt. Karte als Illustration kennzeichnen. Cookie-Wall der Seite nicht kopieren. | boettner-t3.jpg |
| U31 | Standort-Zeilen mit Karte links und Daten rechts, je Ort gleich gebaut | Jeder Ort bekommt Platz und Karte. Anfahrt ist sofort klar. | Haibach, Block "Kontakt" | Standorte | M | Karten laden Drittanbieter-Inhalte: Einwilligung oder statisches Bild nutzen. | haibach-form.jpg |
| U32 | Beide Städte schon in der ersten Zeile der Seite ("Ihre Experten in X und Y") | Orte sind vor dem Scrollen klar. | Müller Fischer, Mikrozeile ganz oben | Standorte oder ganze Seite | S | Reihenfolge der Orte wechseln lassen oder alphabetisch halten, damit kein Ort "erster" ist. | muellerfischer-t0.jpg |
| U33 | Fester Pill-Button unten rechts im Blickfeld ("Zum Chat") | Kontakt bleibt erreichbar, ohne die Seite zu überdecken. | krisenchat. Position aus dem Screenshot, "fest" abgeleitet | ganze Seite | S | Bei uns: "Rückruf anfragen" oder "Anrufen". Nicht pulsieren. Auf Mobil nicht über Cookie- oder Formular-Buttons legen. | krisenchat-t0.jpg |
| U34 | Zwei schmale Rand-Tabs am rechten Bildschirmrand (Telefon, E-Mail) | Immer da, nimmt wenig Platz. | Buchert Jacob Peter, rechter Rand. Verhalten nicht geprüft | ganze Seite | S | Farben der Quelle (Cyan, Magenta) sind zu laut. Bei uns Salbei und Charcoal. | buchert-t0.jpg |
| U35 | Weiche Überblendung zwischen Seiten statt hartem Sprung | Seitenwechsel wirkt ruhig, nicht abrupt. | Wild. Aus dem Code gelesen (htmx `globalViewTransitions: true`), Wirkung nicht live gesehen | ganze Seite | M | `prefers-reduced-motion` beachten. Nur kurze Überblendung, kein Slide. | wild-t0.jpg |

## Anti-Referenzen

### A1. Endida (Incident Response), `endida-t0.jpg`
**Was nicht stimmt:** Ein Banner in vollem Alarmrot. Dazu "Unter aktivem Angriff? Jetzt Notfall-Hotline anrufen" in Versalien. Die Headline sagt "Sie wurden angegriffen" und färbt ein Wort rot. Ein roter Notfall-Button im Header und einer im Hero. Drei Nummern nebeneinander.
**Warum es bei Stürzl scheitert:** Das ist genau der Ton, den wir vermeiden: Alarmrot, Angstwörter, Druck. Wer unter Stress anruft, braucht Ruhe, keinen Sirenen-Effekt. Der Gegenentwurf ist U1/U2 in Salbei mit einem Satz Fakt.

### A2. Wessing & Partner (strafrecht.de), `wessing-t0.jpg`, `wessing-t3.jpg`
**Was nicht stimmt:** Hero ist ein zerfallender Kendo-Kämpfer mit Schwert. Das ist Kampf-Bildsprache. Die Seite nennt "Notfall" nur als kleinen Link in der Fußzeile, ganz unten. In den gesehenen Tiles gibt es keine Nummer im ersten Bildschirm und kein Formular. Das Layout wirkt kalt und leer (Einschränkung: der Scraper hat die Seite nur halb gerendert).
**Warum es bei Stürzl scheitert:** Der Notfall-Einstieg ist versteckt. Das Bild steht für Angriff, nicht für Schutz. Hier fehlen U1 und U8.

### A3. Schneider II Mick (strafrecht.berlin), `schneidermick-t3.jpg`, `sm-notruf-t1.jpg`
**Was nicht stimmt:** Seitenleiste mit über zehn Auszeichnungen als Textliste (Wirtschaftswoche, Handelsblatt, Stern, Focus, Capital und mehr). Im Text steht "Verteidigung ist Kampf" und "beste Strafverteidigung". Die Notruf-Seite nennt im Meta-Text eine andere Nummer (0171) als im Seitentext (0177). Zwei Nummern für denselben Dienst schaden dem Vertrauen.
**Warum es bei Stürzl scheitert:** Zu viel Beleg auf einmal wirkt wie Werbung und kollidiert mit UWG (Spitzenstellung). Der Kampf-Ton passt nicht zur ruhigen Linie. **Gut daran:** die Inhalte von U4, U5, U6. Nur anders verpacken.

### Kleinere Warnzeichen (nicht als eigene Anti-Referenz)
- Müller Fischer: Pop-up für ein Buch über dem Hero (`muellerfischer-t0.jpg`). Stört den Erstkontakt.
- Feigen Graf: Hero-Zitat "marktführende Spezialkanzlei" (`feigengraf-t0.jpg`). UWG-Risiko.
- Böttner: Cookie-Wall vor dem Inhalt und "Schlüssel zum Erfolg" im Text (`boettner-t0.jpg`, `boettner-t2.jpg`). Ergebnisversprechen.
- VONPELCHRZIM: Tabelle mit Mandatsbeschreibungen in der Fußzeile (`pelchrzim-foot.jpg`). BORA § 6 und § 203 StGB. Auch WhatsApp-Symbol bei den Kontaktdaten: bei uns nicht für Mandatsdaten.
- Park: Liste mit vielen Firmennamen (Überschrift nicht gesehen, wirkt wie eine Referenzliste) (`park-foot.jpg`, oberer Teil). Mandantennennung nur mit Einwilligung.
- Haibach: Mandantenzitat im Carousel (`haibach-t3.jpg`) und starkes Rot. Zitat nur mit Einwilligung, Ton sehr laut.

## Top 5 für Stürzl

1. **U1 plus U2 plus U5: Notfall-Streifen** als schmale Leiste mit einem Faktsatz, der Nummer und einer ehrlichen Erreichbarkeitszeile. Salbei, kein Rot. Wirkt sofort und bleibt ruhig.
2. **U9: Kanal-Kacheln** (Anruf, Rückruf, Formular, E-Mail) direkt unter der Nummer im Hero. Besucher wählen selbst. Kein WhatsApp.
3. **U20 plus U21: Ablauf** als vier Schritte mit relativer Zeitmarke. Beantwortet "Was passiert, wenn ich anrufe?" in einem Blick.
4. **U24 plus U25: Formular ohne Falldaten** mit Ziffern-Stepper, Ort als Schritt 1, Thema als Ankreuzfeld und Kontextzeile mit Dringend-Verweis. Kein Freitext.
5. **U27 plus U30: Standorte** als zwei gleich gebaute Spalten mit eigener Notfallnummer, dazu eine Deutschlandkarte mit zwei Punkten für "bundesweit".

Knapp dahinter: **U22** (FAQ mit Sorgenfragen) für die Sektion "Vertraulich". Sie fehlt in der Top 5 nur, weil der Inhalt juristisch freigegeben werden muss.

## 3 Mikrotext-Strukturen für einen ruhigen Notfall-Einstieg (nur Aufbau, keine Wörter)

1. **Lage, Handlung, Erreichbarkeit** (Notfall-Streifen): Zeile 1 benennt die Lage im Präsens und ohne Wertung. Zeile 2 sagt, wer abnimmt und was als Nächstes passiert. Zeile 3 zeigt Nummer und Zeitraum. Quellen: Schneider II Mick (Notruf-Seite), Precursor (Leiste).
2. **Wer liest, was fehlt bewusst, wie kommt die Antwort** (Formular-Rahmen): Satz 1 nennt das Team, das die Anfrage liest. Satz 2 sagt, welche Angaben wir nicht brauchen (keine Falldaten). Satz 3 nennt den Rückweg (Rückruf, Zeit) und den Dringend-Weg. Quelle: Kingsley Napley (Kontextzeile), Haibach (Themen-Ankreuzfelder).
3. **Ziffer, Akteur plus Verb, Ergebnis für Sie, Zeitrahmen** (Ablauf-Schritt): Ziffer steht groß. Danach ein Satz mit klarem Subjekt und Verb. Dann ein Halbsatz zum Ergebnis für den Besucher. Dann ein relativer Zeitrahmen. Quelle: Precursor (Pipeline und Zeitleiste), krisenchat (Ziffern).

## 3 Ideen für zwei Standorte mit gleichem Gewicht

1. **Umschalter ohne Vorauswahl (Toggle).** Ein Segment "Frankfurt | München" in Kontaktband und Formular. Im Ruhezustand sind beide Orte sichtbar, kein Ort aktiv. Ein Klick tauscht Nummer, Adresse und Zeiten. Muster: Müller Fischer (Karten-Schalter) und Haibach (Ort als Formular-Schritt 1). Lehre aus Müller Fischer: kein Ort dunkel hervorheben. Tabs sind die schwächste Variante, weil sie einen Ort verbergen.
2. **50/50-Split mit eigener Notfallnummer und einer Linie dazwischen.** Zwei gleich breite Spalten, gleiche Zeilenfolge (Adresse, Telefon, Notfall, Zeiten, Anfahrt). Zwischen den Spalten steht eine dünne vertikale Linie. Muster: Park (Fußzeile), KFDR (Nummern je Stadt).
3. **Kartenpaar mit Verbindungslinie.** Eine ruhige Deutschlandkarte mit zwei gleich großen Punkten und Etiketten, dazu eine dünne Linie von Punkt zu Punkt und ein Satz zur Reichweite. Dazu zwei kleine Ausschnitt-Karten je Ort für die Anfahrt. Muster: Böttner (Deutschlandkarte), Haibach (Karte je Ort). Die Verbindungslinie ist unsere Anpassung, in den Beispielen nicht gesehen.

## Kurzfassung

1. 18 Websites gesehen (14 per Screenshot, 4 nur per Suchauszug), Desktop 1440 px, Ruhezustand.
2. 35 Elemente (U1 bis U35) in 9 Sektionen, mit Aufwand, Risiko und Tile.
3. 3 Anti-Referenzen (Endida, Wessing & Partner, Schneider II Mick) plus 6 kleine Warnzeichen.
4. Top 5: Notfall-Leiste, Kanal-Kacheln, Ablauf mit Zeitmarke, Formular ohne Falldaten, zwei gleich gebaute Standorte.
5. Bewegung ist fast überall abgeleitet. Nur Wild (View Transitions) und Precursor (gestaffeltes Einblenden) sind aus dem Code belegt.
