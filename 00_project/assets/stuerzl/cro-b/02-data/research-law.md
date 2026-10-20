# Recherche Kanzlei- und Vertrauens-Websites: Gestaltungselemente für STÜRZL

Datum: 2026-10-11
Ziel: Wir suchen Elemente (Layout, Schrift, Bewegung, Interaktion). Wir übernehmen nie Inhalte, Bilder, Logos oder Code.
Tile-Ordner: `00_project/assets/stuerzl/cro-b/02-data/references/law/` (Dateien `<name>-t0.jpg` usw., Desktop 1440 px).

## Gesehene Websites (15)

| Kürzel | Website | Gruppe | Wie gesehen |
| --- | --- | --- | --- |
| drpb | https://drpb.ch (Burkhalter Rechtsanwälte, Bern, Zürich, Lausanne) | a, Awwwards-Liste "Swiss precision in law" | Screenshot, 6 Tiles, CSS und JS gelesen |
| wild | https://www.wild.legal (Kanzlei Wild, München, Steuerstrafrecht) | b, direkter Wettbewerber | Screenshot, 6 Tiles plus Übersichtsbogen `wild-sheet2.jpg`, CSS und JS gelesen |
| metzler | https://www.metzler.com/de (Bankhaus Metzler, Frankfurt) | c, Privatbank | Screenshot, 5 Tiles |
| lombard | https://www.lombardodier.com (Lombard Odier, Genf) | c, Privatbank | Screenshot, 5 Tiles (Cookie-Fenster verdeckt den Hero) |
| chipperfield | https://davidchipperfield.com (Architekturbüro, 5 Standorte) | c, Architektur | Screenshot, 4 von 18 Tiles |
| jga | https://jga.com.pl (JGA, Recht und Steuern, Katowice) | a, Awwwards-Liste | Screenshot, 6 Tiles, Skript-Liste gelesen |
| hafnia | https://hafnialaw.com (Hafnia Law Firm, Kopenhagen) | a, Awwwards-Liste | Screenshot, 5 Tiles |
| providentia | https://providentialaw.com (Providentia Law, Silicon Valley) | a, Awwwards-Liste | Screenshot, 4 Tiles |
| kralaw | https://www.kralaw.de (Krause und Kollegen, Berlin, Wirtschafts- und Steuerstrafrecht) | b | Screenshot, 5 Tiles |
| lilie | https://lilie-ihwas.legal (Lilie Ihwas, Frankfurt, Wirtschaftsstrafrecht) | b | Screenshot, 6 Tiles |
| roeh | https://www.roeh.com/en (ROEH, Recht und Steuern, Mexiko) | a, Awwwards-Liste, auch Anti-Referenz | Screenshot, 4 Tiles |
| gladica | https://www.gladica.law (GLADICA, Strafrecht, Berlin, Hamburg, Frankfurt) | b, Anti-Referenz | Screenshot, 5 Tiles |
| erb | https://kanzlei-erb.de (Erb und Becker, Gießen, Frankfurt) | b, Anti-Referenz | Screenshot, 4 Tiles (zum Teil schwarz, siehe Grenzen) |
| wessing | https://www.strafrecht.de/en (Wessing und Partner) | b | Screenshot, 5 Tiles (Bilder fehlen, siehe Grenzen) |
| ario | https://ario.law/en (Ario Law Firm, Awwwards-Liste) | a | Screenshot, 6 Tiles (nur Intro-Animation sichtbar, siehe Grenzen) |

## Grenzen

- Ich habe nur Ruhezustände gesehen. Firecrawl zeigt keine Bewegung, kein Hover und keine Scroll-Effekte.
- Bewegung habe ich nur aus dem Code abgeleitet. Ich markiere sie im Text mit "(abgeleitet)". Das gilt für drpb, wild und jga.
- Bei drpb lese ich im Code: Alpine.js, `x-intersect.once` mit `startCounter()`, `progressiveImage()`, `startViewTransition`, `backdrop-filter: blur(10px)`.
- Bei wild lese ich im Code: htmx mit `globalViewTransitions`, UIkit-Animationen (`uk-kenburns`, `uk-slide-*`), keine Regel für `prefers-reduced-motion`.
- Bei jga lese ich in der Skript-Liste: GSAP, ScrollTrigger, Splide. Ich habe die Effekte selbst nicht gesehen.
- Bei den übrigen Seiten habe ich keine Bewegung geprüft.
- Ario zeigte nur den Lade-Bildschirm (blauer Verlauf, Wortmarke). Der Rest war schwarz. Ich kann Ario nicht bewerten. Ich führe es nur als Warnung.
- Erb war im Screenshot zum Teil schwarz (Seitenleiste, Cookie-Fenster). Den Text "Jeder Tag ohne professionelle anwaltliche Unterstützung ist ein verlorener Tag" habe ich aus dem Suchergebnis. Ich habe ihn nicht im Bild gesehen.
- Wessing hat Bilder und Logo nicht geladen. Ich bewerte dort nur die Struktur, nicht die Gestaltung.
- Ich habe nur Desktop (1440 px) gesehen. Mobil habe ich nicht geprüft.
- Land-book, Godly, Siteinspire, One Page Love und Behance habe ich nicht direkt geöffnet. Die Quelle (a) kommt aus der Awwwards-Kategorie "Law". Die Suche nach einem Notariat und einem Family Office ergab keine brauchbare Seite. Ich habe stattdessen Privatbank und Architektur genommen.
- Alle Rechts-Hinweise sind Hinweise für die Prüfung, keine Rechtsberatung. Die Kanzlei soll jeden Text vor der Veröffentlichung prüfen.

## Tabelle der Elemente

Abkürzungen: Aufwand S = klein (Stunden), M = mittel (ein bis zwei Tage), L = groß.
Alle Beispiele sind nur Vorlagen für Aufbau, Schrift und Rhythmus. Wir bauen alles mit unseren Farben, Fotos und Texten neu.

| ID | Element | Was es für den Besucher tut | Beispiel und wo | Abschnitt unserer Seite | Aufwand | Risiko-Hinweis | Tile |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L1 | Schwebende Kopfleiste aus Milchglas über dem Hero-Foto: Wortmarke links, 6 Links rechts, abgerundete Ecken, Foto scheint weich durch | Navigation bleibt sichtbar, aber nimmt dem Foto nichts weg. Wirkt leicht und ruhig. | drpb.ch, Hero. `backdrop-filter: blur(10px)` im CSS gelesen | Hero, ganze Seite | S | Gering. Text in der Leiste braucht genug Kontrast (Charcoal auf hellem Glas). | drpb-t0.jpg |
| L2 | Vollbreites Hero-Foto mit sehr heller, dünner Serif-Überschrift unten links, weicher Farbverlauf als Schutz für den Text | Zeigt echte Menschen in echter Altbau-Umgebung. Die Überschrift liegt ruhig im Bild, kein Button drängt. | drpb.ch, Hero (zwei Zeilen, Satzpunkte als Rhythmus) | Hero | M | Überschrift darf nichts versprechen (BORA § 6, UWG). Der Verlauf soll Salbei-Grau sein, nicht Dunkel. | drpb-t0.jpg |
| L3 | Leistungsraster 3 mal 2 ohne Fotos: helle Flächen mit weichen, unscharfen Farbflecken, zentrierter Serif-Titel | Sechs Felder auf einen Blick. Kein Icon, kein Lärm. Der Besucher findet sein Thema schnell. | drpb.ch, Abschnitt "Worauf wir uns fokussieren" | Leistungen | M | Titel nur sachlich nennen (zum Beispiel "Selbstanzeige"). Kein Wort wie "Spezialist" ohne Nachweis (§ 43c BRAO). | drpb-t1.jpg, drpb-t2.jpg |
| L4 | Große Serif-Ziffern in einer Reihe (3, 1, 100) mit kleiner Beschriftung daneben. Die Zahlen zählen beim Eintritt in das Sichtfeld hoch (abgeleitet aus `x-intersect.once` und `startCounter()`) | Zahlen geben Halt, ohne zu schreien. Die Schrift trägt das Element, nicht eine Grafik. | drpb.ch, "Wer wir sind" | Beweis-Leiste | S | Nur prüfbare Fakten: Standorte, Jahre seit Gründung, Zahl der Anwälte. Keine Erfolgsquoten, keine Fallzahlen. | drpb-t2.jpg |
| L5 | Fünf Stufen als Reihe: große Serif-Zahl oben, kurzer zentrierter Text darunter, keine Linien, keine Kästen | Zeigt einen Weg mit Anfang und Ziel. Passt zu einem Ablauf in 5 Schritten. | drpb.ch, "Was uns bewegt" (dort Jahreszahlen 1922 bis 2026). Wir nutzen sie als Schritt 1 bis 5. | Ablauf | S | Der Ablauf muss die echte Arbeitsweise zeigen. Keine Frist oder Dauer ohne Prüfung nennen. | drpb-t3.jpg |
| L6 | Zentrierte Absatz-Aussage in Serif (28 bis 32 px), kleine Überzeile darüber, viel Weißraum | Gibt dem Besucher einen ruhigen Satz zum Lesen. Ideal für die Haltung zu Vertraulichkeit. | drpb.ch, "Unser Netzwerk" | Vertraulich | S | Gering. Keine Schweige-Versprechen, die rechtlich mehr sagen als die Verschwiegenheitspflicht (§ 43a BRAO). | drpb-t4.jpg |
| L7 | Schmales Akkordeon mit dünner Haarlinie und feinem Plus-Zeichen, mittig in 6 Spalten | Antworten liegen offen, aber nicht laut. Wenig Platz, gut lesbar. | drpb.ch, "Was uns auszeichnet" | FAQ | S | Gering. Antworten sachlich halten, keine Erfolgsaussage zu Selbstanzeige oder Verfahren. | drpb-t5.jpg |
| L8 | Seitenwechsel mit Überblendung statt hartem Neuladen (abgeleitet aus `startViewTransition` bei drpb und `globalViewTransitions` bei wild) | Der Wechsel zwischen Seiten fühlt sich ruhig an. Bei Standort-Unterseiten bleibt der Kopf stehen. | drpb.ch und wild.legal, beim Klick auf einen Link | ganze Seite | M | Aus dem Code abgeleitet, nicht gesehen. Muss `prefers-reduced-motion` achten. Wild hat dazu keine Regel (Lücke). | drpb-t0.jpg |
| L9 | Kopf als volle Farbfläche in Salbei-Grau: Wortmarke groß in der Mitte, Burger links, Sprache rechts, darunter die Kanzlei-Zeile | Der erste Eindruck ist die Marke, nicht ein Menü. Sehr ruhig. | wild.legal, Hero | Hero | M | Wild ist ein Wettbewerber in München und nutzt ein ähnliches Salbei-Grau. Wir müssen uns klar absetzen (Foto, Schrift, Raster). Wortmarke nie nachbauen, nur die echte Datei. | wild-t0.jpg |
| L10 | Ganzflächiges Foto direkt unter dem Kopf, Person von oben, lange Schatten, kein Text im Bild | Ein starkes, ruhiges Bild ohne Text. Der Blick bleibt bei der Person. | wild.legal, Hero | Hero | M | Schatten-Motiv bei Wild ist eine Bild-Idee des Wettbewerbs. Wir nehmen nur das Prinzip "ein Bild, kein Text". Wir nutzen unsere eigenen Fotos. | wild-t0.jpg, wild-t1.jpg |
| L11 | Mehrzeilige Überschrift in Versalien mit gestaffeltem Einzug (erste Zeile rechts versetzt) | Gibt dem Satz einen Rhythmus wie ein Gedicht. Man liest Wort für Wort. | wild.legal, Satz unter dem Foto | Hero | S | Der Wild-Satz "Es ist immer zu früh, um aufzugeben" ist ein Gefühlsversprechen. Nur das Layout nehmen, nicht den Ton. Versalien brauchen viel Zeilenabstand. | wild-t1.jpg |
| L12 | Outline-Button in Pillenform mit dünner Linie ("Vereinbaren Sie jetzt einen Termin"), nach jedem Block wiederholt | Ein klarer Weg, immer an der gleichen Stelle, ohne Druck. Keine Signalfarbe. | wild.legal, nach Hero, Anwältin, Leistungen | ganze Seite, Abschluss | S | Gering. Auf Weiß mit Charcoal-Linie gut lesbar. Beim Hauptbutton in Salbei #4E6F55 füllen, damit der Besuch eine klare Hauptaktion hat. | wild-t3.jpg, wild-t5.jpg |
| L13 | Jeder Abschnitt hat eine eigene ruhige Flächenfarbe (Salbei, Creme, Rosé, Mint) in Streifen | Die Seite hat einen Rhythmus. Der Besucher sieht, wo ein Thema endet. | wild.legal, ganze Seite | ganze Seite | S | Bei Wild sind es 5 Töne. Wir nehmen nur 3: Weiß, Creme #F4F1EC, Salbei-Tint #E4EBE5. Mehr wird bunt. | wild-sheet2.jpg |
| L14 | Drei große Kacheln mit gestapeltem Versal-Titel, Wörter getrennt (QUALIFI-KATION), Fläche in Beige | Drei Themen als Karten mit starkem Typo-Bild. Kein Foto nötig. | wild.legal, "Anwältin" | Leistungen | M | Trennstriche in Titeln stören das Lesen. Nur für 3 kurze Wörter nutzen. Kein "Qualifikation"-Block, der Fachanwalts-Titel ohne Nachweis zeigt. | wild-t4.jpg |
| L15 | Referenzen-Block: Rankings als Textzeilen mit Jahr und runden Siegeln, ein Zitat im Streifen | Zeigt Belege. Für uns nur als Aufbau-Idee. | wild.legal, "Referenzen" | Bewertungen | S | HOHES Risiko. Rankings und "Beste Anwälte" sind Werbung mit Auszeichnungen (UWG, BORA § 6). Nur belegbare Quelle, Jahr und Kriterium nennen. Kein Siegel ohne Lizenz. Bei Wild stehen "Top Kanzlei" und "Top Anwalt". Das übernehmen wir nicht. | wild-sheet2.jpg |
| L16 | Feste Seitenleiste in Markenfarbe: Burger oben, darunter drei Sektions-Punkte als Strahlen-Symbol, der aktive Punkt ist hell (Scroll-Wechsel abgeleitet aus GSAP und ScrollTrigger in der Skript-Liste) | Der Besucher weiß immer, wo er auf der Seite ist. Hilft bei langer Seite. | jga.com.pl, Hero | ganze Seite | M | Die Seitenleiste nimmt auf dem Handy Platz. Mobil nur oben als Fortschrittslinie zeigen. Punkte nie als Dekoration ohne Funktion. | jga-t0.jpg |
| L17 | Porträt-Foto im Anschnitt, versetzt vor einem tiefen Farbblock, rechts daneben große Serif-Zeile und Pfeil-Link "Poznaj cały zespół" | Das Gesicht steht im Mittelpunkt. Der Farbblock gibt Tiefe, ohne Schatten. | jga.com.pl, Team-Abschnitt | Über Dr. Stürzl | S | Gering. Foto muss echt sein (Dr. Stürzl im Altbau). Farbblock in Salbei #4E6F55 oder Charcoal. | jga-t1.jpg, jga-t2.jpg |
| L18 | Drei Spalten mit Bild oben, Haarlinie als Rahmen, Titel auf dem Bild, Fläche darunter für Text | Klare Karten. Jede Spalte hat ein Thema und ein Bild. | jga.com.pl, "Prawo, Podatki, Księgowość" | Leistungen | S | Die Stock-Bilder bei JGA (Hände, Akten) wirken austauschbar. Bei uns nur echte Fotos oder Typo. | jga-t1.jpg |
| L19 | Großes Zitat in Serif (Anführungszeichen in Markenfarbe, 6 Zeilen), Name und Firma darunter, drei Punkte als Navigation | Ein einziges Zitat pro Bildschirm. Das ist ruhiger als drei Zitate in einer Reihe. | jga.com.pl, Referenz | Bewertungen | S | Mandantenzitate nur mit Einwilligung. Kein Fallbezug, kein Ergebnis, keine Steuerstrafsache nennen (§ 43a BRAO, BORA § 6). Bei Strafrecht kaum nutzbar. Besser: Google-Bewertungen als Beleg. | jga-t4.jpg |
| L20 | Kontakt-Fuß: Karte links in der halben Breite, rechts zwei Adressblöcke mit Telefon und Mail, darunter dunkler Fuß in Tiefgrün | Alles zum Kontakt an einer Stelle. Klar getrennt nach Einheit. | jga.com.pl, Fuß | Standorte | S | Karte lädt Drittanbieter-Daten. Erst nach Einwilligung laden (Consent). Zwei Blöcke für Frankfurt und München. | jga-t5.jpg |
| L21 | Große organische Kreisform in Salbei-Tint hinter Überschrift und Karten, Rand läuft aus dem Bild | Bricht die Rechtecke auf und gibt Wärme. Wirkt wie eine Bühne für den Inhalt. | metzler.com/de, "Was können wir für Sie tun?" | Leistungen, ganze Seite | M | Gering. Form darf nicht wie ein Wasserzeichen oder Logo wirken. Eine Form pro Seite genügt. | metzler-t2.jpg |
| L22 | Display-Serif mit übergroßem Anfangsbuchstaben in Salbei-Tint und handgezogener Linie darunter | Gibt einer Zeile eine persönliche Handschrift. Wirkt warm und menschlich. | metzler.com/de, Überschrift "Was können wir für Sie tun?" | Leistungen, Ablauf | S | Pinsel-Linie nicht übertreiben. Eine Betonung pro Seite. Bei Newsreader den Initial per CSS `::first-letter` bauen. | metzler-t2.jpg |
| L23 | Kennzahlenband in tiefer Markenfarbe mit weißen Serif-Ziffern (12 Generationen, 10 Standorte, 100 %), Satz darüber | Ein dunkler Streifen mit drei Zahlen trägt Vertrauen und teilt die Seite. | metzler.com/de, unter dem Hero | Beweis-Leiste | S | Nur prüfbare Zahlen. Band in Charcoal #323335 statt Oliv. Keine Prozent-Angaben zu Erfolg. | metzler-t1.jpg |
| L24 | Vier Karten in 2 mal 2: kleine Zeile oben ("Lösungen für Unternehmen"), Serif-Titel, ein Satz, runder Pfeil-Button unten rechts | Der Besucher wählt seine Rolle. Jede Karte führt zu einem Weg. | metzler.com/de, "Was können wir für Sie tun?" | Mandanten | S | Karten benennen Rollen (Privatperson, Geschäftsführer, Compliance). Titel nicht als Zusage formulieren. | metzler-t2.jpg |
| L25 | Gruppenporträt im Anschnitt mit kleiner Bildunterschrift (Name und Rolle) in der Ecke | Ehrliche Vorstellung der Person. Die Unterschrift macht das Foto glaubhaft. | metzler.com/de, Hero | Über Dr. Stürzl | S | Gering. Rolle genau nennen (Rechtsanwältin). Keinen Fachanwaltstitel zeigen, wenn er nicht belegt ist. | metzler-t1.jpg |
| L26 | Ein Satz groß am Fuß des Hero-Bildes, kleine Slide-Punkte darunter, Outline-Pill "watch our manifesto" | Ein ruhiger Satz statt einer Wand aus Text. Der Besucher kann bei Bedarf weiterblättern. | lombardodier.com, Hero | Hero | M | Karussell versteckt Inhalt. Für gestresste Besucher einen festen Satz zeigen. Cookie-Fenster in der Mitte verdeckte den Hero. Das Fenster klein halten (unten). | lombard-t0.jpg |
| L27 | Vier Spalten auf dunklem Band, getrennt durch Haarlinien, je ein Satz und ein weißer Pill-Link | Vier Wege zum nächsten Schritt. Sauber, ohne Kästen. | lombardodier.com, unter dem Hero | Leistungen | S | Band in Charcoal #323335, nicht in Schwarz. Pill-Link in Weiß auf Charcoal. | lombard-t1.jpg |
| L28 | Versetzter Bild-Feed: Bilder in verschiedener Breite, mittig, links, rechts, darunter kleine Zeile mit Kategorie, Datum und Titel | Die Bilder atmen. Jede Position hat Weißraum. Es ist kein Raster, aber ruhig. | davidchipperfield.com, Start | Standorte | M | Für Frankfurt und München: zwei Schwarzweiß-Stadtbilder versetzt, mit Unterzeile (Stadt, Adresse). Kein Pseudo-Archiv. | chipperfield-t0.jpg, chipperfield-t1.jpg |
| L29 | Sehr schlanke Kopfleiste: Name links, vier Links, Suche rechts, feine Schrift in Grau, kein Hintergrund | Die Leiste tritt zurück. Das Bild bleibt im Mittelpunkt. | davidchipperfield.com, Kopf | ganze Seite | S | Für eine Seite mit Notfall-Bedarf braucht es zusätzlich einen klaren Kontakt-Link rechts. Telefonnummer sichtbar. | chipperfield-t0.jpg |
| L30 | Vertikale Reiter mit Zahl und senkrechter Beschriftung (03, 02, 01) neben einem Foto | Schritte als schmale Spalten. Der aktive Schritt öffnet sich mit Text. | hafnialaw.com, Karriere-Abschnitt | Ablauf | M | Senkrechte Schrift ist schwer zu lesen. Für 3 kurze Wörter okay. Auf dem Handy als normale Liste. | hafnia-t3.jpg |
| L31 | Drei Schritte mit Foto, Nummer, Serif-Titel und drei Stichpunkten ("01 Application", "02 The First Interview") | Einfacher Prozess mit klaren Kriterien. Bild gibt Stimmung. | hafnialaw.com, Rekrutierung | Ablauf | S | Stichpunkte nur zu dem, was wir tun. Keine Zeitangabe wie "binnen 24 Stunden", wenn wir sie nicht halten. | hafnia-t4.jpg |
| L32 | Anfahrts-Text je Standort (Auto, Parkplatz, Metro vom Flughafen) auf dunkler Fläche neben der Adresse | Zeigt, wie man ankommt. Nimmt dem Besucher die Unsicherheit vor dem ersten Termin. | hafnialaw.com, Kontakt | Standorte | S | Für Frankfurt und München je ein Absatz (Bahn, Auto, Parken). Nur geprüfte Angaben. | hafnia-t4.jpg |
| L33 | Schmale Randspalte links mit kleinem Versal-Titel und Haarlinie ("FACHGEBIETE", "RECHTSANWÄLTE"), Inhalt rechts in einer Lesespalte | Gibt Ordnung wie ein Fachbuch. Der Text bleibt kurz und lesbar. | kralaw.de, Start | Leistungen | S | Gering. Randspalte auf dem Handy über den Inhalt legen. | kralaw-t0.jpg, kralaw-t2.jpg, kralaw-t4.jpg |
| L34 | Historische Zeichnung (Straßenszene, Kanzleisitz um 1920) statt Foto, mit Quellenzeile darunter | Gibt der Kanzlei Herkunft und Ort, ohne Stock-Foto. | kralaw.de, Start | Standorte, Über | M | Bildrechte klären (dort steht ein Rechtehinweis). Bei uns: gemeinfreie Frankfurter oder Münchner Ansicht, mit Quelle. | kralaw-t0.jpg |
| L35 | Drei Fotos in einer Reihe: Raum, Fassade, Personen am Fenster, gleiche Höhe, kleine Lücken | Zeigt Ort, Haus und Menschen. Gibt ein Gefühl für den Besuch. | lilie-ihwas.legal, unter dem Intro | Über Dr. Stürzl, Standorte | S | Gering. Passt zu unserem Altbau-Büro. Fotos nur echte, hell, ohne Dunkel-Filter. | lilie-t1.jpg |
| L36 | Schachbrett aus 2 mal 2: abwechselnd Foto und dunkle Textfläche mit Titel, kurzer Linie und Absatz | Jeder Schwerpunkt hat Bild und Text zugleich. Abwechslung ohne Karten. | lilie-ihwas.legal, "Tätigkeitsschwerpunkte" | Leistungen | M | Texte bei Lilie sind lang. Wir kürzen auf 2 Sätze. Dunkle Fläche in Charcoal, nie Schwarz. | lilie-t3.jpg, lilie-t4.jpg |
| L37 | Mehrstufiges Kontaktformular mit Auswahl-Chips ("Worum geht es?", Schritt 1 von 3) | Der Besucher beginnt mit einem Klick, nicht mit einem leeren Feld. Die Hürde sinkt. | roeh.com/en, Fuß | Abschluss | M | Im ersten Schritt keine Angaben zum Sachverhalt abfragen. Hinweis zu Datenschutz und Mandatsgeheimnis. Chips neutral nennen (Selbstanzeige, Durchsuchung, Betriebsprüfung, Unternehmen). | roeh-t3.jpg |
| L38 | Standort-Reiter: Tabs je Stadt, darunter Karten mit Name, Adresse, Beschreibung und Link "Go to Google Maps", Pfeile zum Blättern | Der Besucher wählt seine Stadt und sieht sofort den Ort. | roeh.com/en, "Global Presence" | Standorte | M | Zwei Tabs: Frankfurt, München. Kein Karussell mit 10 Karten. Maps-Link erst nach Einwilligung. | roeh-t3.jpg |
| L39 | Zeilenliste: links Titel in Versalien, rechts Text, jede Zeile mit farbiger Oberlinie | Lässt vier Zusagen untereinander lesen. Ruhig und klar. | providentialaw.com, "Expertise, Innovation and Cost-Efficiency" | Vertraulich | S | Zeilentitel nicht als Superlativ ("Best", "Leading"). Beispiele: Verschwiegenheit, Ablauf, Erreichbarkeit. Linie in Salbei #8DA38E. | providentia-t2.jpg |
| L40 | Segment-Tabs über den Leistungen (Criminal Law, Traffic Law, Employment Law, Tax Law), aktiver Tab dunkel, darunter drei Karten | Der Besucher filtert nach seiner Lage. Weniger Text auf einmal. | gladica.law, "Our Practice Areas" | Mandanten, Leistungen | M | Nur das Tab-Muster nehmen (Privatperson, Unternehmen). Gladica nutzt dort Wörter wie "Highest Level". Das ist bei uns nicht erlaubt. | gladica-t2.jpg |

## Anti-Referenzen

1. **GLADICA (gladica.law).** Handwerklich sauber, aber falsch für uns.
   - Im Kennzahlen-Block steht eine Waage (Justitia) im Hintergrund. Das ist bei uns verboten.
   - Die Kopfleiste hat zwei Buttons: "Book Appointment" und ein koralles "Call Now". Der Besucher steht unter Druck.
   - Unter dem Hero läuft ein Band mit Logos von Fernseh- und Zeitungsmarken. Das sieht nach Medienpräsenz aus und ist ohne klaren Beleg riskant.
   - Der Text nennt "500+ Clients with 5-Star Reviews", "10.000+ Clients", "Criminal Defense Where Others Fall Short" und "Expertise at the Highest Level". Das sind Superlative und Erfolgsbilder (UWG, BORA § 6).
   - Eine Balkengrafik "Client Inquiries on the Rise" wirkt wie ein SaaS-Produkt, nicht wie eine Kanzlei.
   - Tiefblaue Karten mit roten Icons erinnern an einen Notruf-Dienst.
2. **Kanzlei Erb und Becker (kanzlei-erb.de).** Schwarz mit Orange.
   - Die Seitenleiste ist schwarz mit orangen Linien und orangem Kontakt-Button. Das ist der "dunkle Thriller-Look" aus unserer Verbotsliste.
   - Eine orange Sprechblase "Hier Online-Anfrage stellen" hängt über dem Inhalt.
   - Laut Suchergebnis steht auf der Seite "Jeder Tag ohne professionelle anwaltliche Unterstützung ist ein verlorener Tag" und ein 24-Stunden-Notruf. Das ist Angst-Ton. (Aus dem Suchtext, nicht im Bild gesehen.)
   - Die Portraits sind Schwarzweiß-Anzugfotos vor weißem Verlauf. Sie wirken austauschbar und kühl.
3. **ROEH (roeh.com/en).** Konzernton.
   - Der Hero zeigt dunkle Glasfassaden bei Sonnenuntergang. Die Überschrift läuft als Laufschrift aus dem Bild. Der Besucher kann sie nicht in Ruhe lesen.
   - Das Cookie-Banner ist rot-korallenfarben. Rot ist bei uns als Alarm-Farbe verboten.
   - Der Fließtext verspricht "results that matter" und "outcomes that materially advance your business objectives". Das ist ein Ergebnis-Versprechen.
   - Der Kontaktblock ist schwarz.
   - Gut ist dort nur der Standort-Reiter (L38) und das Chip-Formular (L37).

Hinweis: Lilie Ihwas ist gemischt. Die Fotos sind stark (L35, L36). Der Block "Auszeichnungen" mit JUVE-Zitaten wie "Top Verteidigerin" ist für uns nicht erlaubt. Der Aufbau mit Elementor ist flach. Wessing und Partner konnte ich wegen fehlender Bilder nicht bewerten.

## Top 5 für Stürzl

1. **L2 mit L1: Hero-Foto mit dünner Serif-Überschrift und Milchglas-Leiste (drpb).** Das helle Foto von Dr. Stürzl im Altbau passt genau zu diesem Aufbau. Newsreader ist eine Serif wie dort. Die Leiste lässt das Foto frei. Der Hero hat einen einzigen Gedanken und keinen Druck.
2. **L24: Vier Karten für "Mandanten" (metzler).** Der Besucher wählt seine Rolle: Privatperson, Geschäftsführer, Compliance. Die runden Pfeil-Buttons sind klein und ruhig. Das Muster ist rechtlich unkritisch, wenn die Titel sachlich bleiben.
3. **L5: Ablauf in fünf Schritten mit großen Serif-Ziffern (drpb, mit L31 von hafnia).** Gestresste Besucher wollen wissen, was nach dem ersten Anruf passiert. Große Zahlen und kurze Texte geben das. Das Element braucht kein Foto und keine Bewegung.
4. **L17: Porträt versetzt vor einem Salbei-Block (jga).** Der Block gibt dem echten Foto Tiefe. Er nutzt unsere Markenfarbe. Er zeigt Dr. Stürzl als Person, ohne Titel-Werbung.
5. **L38: Standort-Reiter Frankfurt und München (roeh, mit L28 von chipperfield).** Zwei Städte sind ein Kern der Marke. Ein Reiter mit Adresse, Anfahrt (L32) und einem Schwarzweiß-Stadtbild macht beide Orte greifbar. Wir nehmen nur zwei Tabs und kein Karussell.

Nächste Kandidaten: L12 (Outline-Pill-CTA), L35 (Foto-Reihe Raum, Fassade, Personen), L4 (Serif-Ziffern mit Hochzählen, nur mit prüfbaren Zahlen).

## Drei Ideen für ein "Signature"-Moment

**S1: Zwei Städte, ein Schalter.** Ein ruhiger Umschalter "Frankfurt | München" sitzt im Hero oder im Abschnitt Standorte. Beim Klick wechselt das Schwarzweiß-Stadtbild per Überblendung (L8, abgeleitet). Adresse, Anfahrt und Sprechzeit wechseln mit. Der Rest der Seite bleibt stehen. Quellen: Standort-Reiter (roeh, L38), versetzte Bilder (chipperfield, L28), View Transitions (drpb und wild, abgeleitet). Das passt zu zwei Büros und Mandanten im ganzen Land. Risiko: gering, wenn beide Orte gleich stark gezeigt werden.

**S2: Farbband-Weg durch die Seite.** Jeder Abschnitt hat eine eigene ruhige Fläche: Weiß, Creme, Salbei-Tint, Charcoal. Eine große Salbei-Kreisform läuft durch ein bis zwei Abschnitte und bricht das Raster (L21). Der Besucher spürt beim Scrollen einen ruhigen Wechsel wie Atem. Quellen: Farbband pro Abschnitt (wild, L13), Kreisform (metzler, L21), Kennzahlenband (metzler, L23). Risiko: Wild setzt dieses Prinzip schon ein. Wir halten uns mit 3 Tönen, Serif-Schrift und eigenen Fotos klar ab.

**S3: Der Faden durch den Ablauf.** Eine dünne Linie mit Salbei-Punkten folgt dem Besucher am Rand der Seite (L16, jga). Im Abschnitt Ablauf füllt sich die Linie bei Schritt 1 bis 5, die Zahlen stehen in großer Serif (L5, drpb). Die Linie endet beim Abschluss-Button. Der Besucher sieht, wo er ist und was als Nächstes kommt. Bewegung ist nur eine Linie (abgeleitet aus GSAP und ScrollTrigger bei jga, nicht gesehen). Mit `prefers-reduced-motion` entfällt der Effekt. Risiko: gering. Der Ablauf muss die echte Arbeitsweise zeigen und darf keine Dauer versprechen.

## Zusammenfassung (5 Zeilen)

1. 15 Websites gesehen (12 Kanzleien, 2 Privatbanken, 1 Architekturbüro). Davon 3 Anti-Referenzen: GLADICA, Erb und Becker, ROEH.
2. 40 Elemente (L1 bis L40) mit Abschnitt, Aufwand, Risiko und Tile-Datei in der Tabelle.
3. Beste Quellen für unseren Ton: Metzler (Salbei-Fläche, Serif, 2 mal 2 Karten), Burkhalter (Hero, Ziffern, Ablauf), JGA (Porträt vor Farbblock), Wild (Farbband, Pill-CTA; aber Wettbewerber).
4. Top 5: L2 mit L1, L24, L5, L17, L38. Drei Signature-Ideen: Städte-Schalter, Farbband-Weg, Ablauf-Faden.
5. Grenzen: nur Ruhezustände und Desktop gesehen, Bewegung nur aus Code abgeleitet, Ario, Erb und Wessing nur teilweise lesbar, Land-book, Godly, Siteinspire und Behance nicht geöffnet.
