# Dataset — Seite „Gespräch buchen“ me&you (Stand 2026-10-12)

Gemeinsame Fakten: `../../02-data/dataset.md` (Abschnitt 2.3 „Das Gespräch“, 4 Bewertungen, 7 Konflikte), `../../michael/02-data/dataset.md`.

## Quellen
- T1 Vorschau v2 `termin.html` (`page_termin` in `prototype-v2/build_v2.py`, 2026-10-12): Kicker „Kostenloses Gespräch · 30 Minuten · Online“, H1 „Finde heraus, wo du gerade Wirkung verlierst.“, Sub „30 Minuten mit dem Team von Michael Ehlers. Du bekommst eine ehrliche Einschätzung und einen Vorschlag für den nächsten Schritt. Kein Verkaufsdruck.“, drei Schritte (Termin wählen, Drei kurze Fragen, Gespräch per Video), Zeile Michael („Rhetoriktrainer seit über 30 Jahren · über 8.000 Teilnehmer · ERFOLG Magazin Top 100 Trainer“), Kalender rechts mit Kopf „Wähle deinen Termin · Zeitzone Berlin · nur die nächsten Tage buchbar“, Band „Das bringst du mit.“, drei FAQ. Screenshot `v2-termin-first-viewport-1440.png`.
- T2 Live-Seite https://www.meandyou.de/sichtbarkeit-termin (Firecrawl 2026-10-12, maxAge 0): „Was dich erwartet:“, „Simpel, aber klar: ein kurzes, klärendes Gespräch.“, drei Haken („Eine bewusste Einordnung deiner Situation“, „Eine erste klare Einschätzung deiner Außenwirkung“, „Gemeinsame Entscheidung über eine mögliche Zusammenarbeit“), Laptop-Mockup mit Michael, grauer Kasten für Calendly. Title „Sichtbarkeit Neu – VSL“. Footer: +49 15888367664, management@meandyou.de. Screenshots `live-sichtbarkeit-termin-*.png`.
- T3 Calendly-Event https://calendly.com/me-you/sichtbarkeit-neu (Firecrawl 2026-10-12): Name „Sichtbarkeit Neu“, „30 min“, Anbieter „Me & You“, robots noindex. Kalender zeigt den ganzen Monat. Zeitzone erkennt Calendly selbst beim Besucher (Firecrawl: Eastern Time, Headless-Chrome Bali: Zentralindonesische Zeit).
- T4 Ad-Funnel-Check 06.10.2026 (`00_project/meandyou-call-2026-10-05.md`): alle 8 aktiven Ads → /sichtbarkeit-neu (Video), Button „Kostenloses persönliches Gespräch buchen“ → /sichtbarkeit-termin. Calendly-Formular: Name, E-Mail, Telefon (Pflicht, mit SMS-Opt-in), Gäste. Keine Qualifizierungsfragen. Kalender den ganzen Monat offen. Bruch: Ad verspricht „kostenloses Training“, Seite bietet ein Gespräch.
- T5 Doc „No-Show senken: Umsetzungsplan“ (Drive 1LmfKEjT…, 08.10.2026): heute erscheinen 15 bis 20 % (No-Show 80 bis 85 %), Richtwert etwa 60 %. Phase 1 Buchungsstrecke: Ad und Seite angleichen, drei Pflichtfragen, buchbar nur 48 bis 72 Stunden im Voraus, eigene Bestätigungsseite mit Video von Michael. Zielwert als Schätzung: zuerst 40 %, später etwa 60 %. Offen: wer sendet die WhatsApp, Kaution ja/nein (Michael), wer filmt das Video. Zugänge Calendly und Framer noch nicht bei 741.
- T6 Doc „No-Show: Buchungsstrecke“ (Drive 1Z9zdhpj…, 08.10.2026): drei Pflichtfragen (1 „Wo wünschst du dir am meisten mehr Wirkung?“ Auswahl Meetings und Führung / Verkauf und Pitches / Bühne und Vorträge / Verhandlungen / Woanders; 2 „Was soll sich in den nächsten 3 Monaten konkret verändern?“ Freitext; 3 „Wann möchtest du an einem Seminar teilnehmen, wenn es passt?“ nächste 3 Monate / 3 bis 6 Monate / informiere mich erst). Zusatz am Telefonfeld „Wir melden uns per WhatsApp unter dieser Nummer.“ Calendly: nur die nächsten 3 Tage, Mindestvorlauf 4 Stunden, Weiterleitung auf Bestätigungsseite, Umbuchungslink in jeder Mail und WhatsApp, UTM von der Seite an Calendly. Bestätigungsseite: „Dein Termin steht, [Vorname].“, Schritt 1 WhatsApp beantworten, Schritt 2 Video von Michael (1 bis 2 Minuten), Schritt 3 ruhiger Ort, Stift und Papier, konkrete Situation, Schritt 4 Termin ändern, Button „Zum Kalender hinzufügen“. Video-Skript 60 bis 90 Sekunden.
- T7 Doc „No-Show: WhatsApp-Sequenz“ (Drive 1As1uLP2…, 08.10.2026): Absender ist die Person, die die Setter-Gespräche führt („[Name] vom Team von Michael Ehlers“). 5 Minuten nach Buchung WhatsApp mit Frage, 24 h vorher Insights, Termintag morgens mit Voice-Note von Michael, 1 h vorher, 15 min vorher Link zum Call. Bestätigungsmail-Text.
- T8 Freigegebene Startseiten-Copy S07 (`../04-copy/approved-copy.md`): „Erst ein Gespräch. Dann entscheidest du.“, drei Schritte (Termin wählen / Gespräch per Video / In Ruhe entscheiden), „Im Gespräch klärst du: wo du heute Wirkung verlierst, welches Seminar zu deiner Situation passt, welcher Ort und welcher Termin für dich gehen“, „Bring gern eine konkrete Situation mit“, Rückversicherung „Kostenlos, per Video. Lieber anrufen: +49 15888367664“.
- T9 Copy Deck R3, Block 08: „Ein Gespräch, 30 Minuten, kostenlos. Wir klären, wo du stehst und welches Format passt.“ Button „Gespräch buchen“.
- T10 Calendly-Hilfe (2026-10-12): UTM-Werte utm_source, utm_medium, utm_campaign, utm_content, utm_term werden nur gespeichert, wenn sie beim Laden in der Embed-URL stehen (help/how-to-source-track-your-calendly-embed-with-utm-parameters). Nach der Buchung sendet das Embed `calendly.event_scheduled` per postMessage an die Seite, mit Event- und Invitee-URI, ohne Name und Datum (help/advanced-calendly-embed-for-developers).
- T11 Beweise: ProvenExpert 250 Bewertungen, 227 mit 5 Sternen (C01). Freigegebene Zitate Startseite S08 (Michael B., Christin R., Peter Escher). Michael: seit 1990 (M01), über 8.000 Teilnehmer (C03), Lehrbeauftragter Universität St. Gallen (M02), laut ERFOLG Magazin Top 100 Trainer (C05).

## Aktuelle Seiten (Messung)
| Punkt | v2 termin.html (T1) | Live /sichtbarkeit-termin (T2) |
|---|---|---|
| Kalender im ersten Bildschirm 1440 | ja, rechts | grauer Kasten, Kalender lädt spät |
| Navigation | nur Logo (gut) | nur Logo |
| Wer führt das Gespräch | „Team von Michael Ehlers“, Rundbild Michael (wirkt, als spräche man mit Michael) | Laptop-Mockup mit Michael (gleicher Eindruck) |
| Ablauf | 3 Schritte | 3 Haken |
| Beweis neben dem Kalender | nur Zeile unter Michael | keiner |
| Telefon | nur im Footer | nur im Footer |
| Nach der Buchung | Calendly-Standardseite im Rahmen | Calendly-Standardseite |
| UTM | nicht weitergereicht | nicht weitergereicht |
| Falsche Angaben | „Zeitzone Berlin“ (Calendly zeigt Besucher-Zeitzone), „nur die nächsten Tage buchbar“ (heute ganzer Monat), „Drei kurze Fragen“ (Formular hat heute keine) | keine |

## Konflikte und Regeln
| # | Fund | Behandlung |
|---|---|---|
| K1 | v2 verspricht „Drei kurze Fragen“ und „nur die nächsten Tage buchbar“. Calendly hat heute weder Fragen noch ein kurzes Fenster (T3, T4). Calendly-Einstellungen ändern wir nicht | Text nennt beides nur mit Platzhalter `[von Kunde bestätigen: …]`, bis Pauspapier Calendly umstellt. Entscheidung E2 |
| K2 | Gesprächspartner ist der Setter, nicht Michael (Memory 08.10.). Name unbekannt | „ein Mitglied aus Michaels Team“ + `[von Kunde bestätigen: Name und Rolle der Person im Gespräch]`. Michael-Foto nur mit Text „Michael Ehlers leitet die Seminare“, nicht als Gesprächspartner |
| K3 | „Kein Verkaufsdruck“ (T1) ist eine Zusage, die wir nicht prüfen können | ersetzt durch Tatsache: „Ob und wann du ein Seminar buchst, entscheidest du danach.“ (T8) |
| K4 | Telefon: Website +49 15888367664, Google-Profil +49 160 96600322 (`nap.json`) | Seite nutzt +49 15888367664 (Auftrag, T2, T8) |
| K5 | Google-Sterne | nie auf dieser Seite (Regel). Nur ProvenExpert |
| K6 | „seit über 30 Jahren“ gegen „25 Jahre“ auf der Live-Seite | „seit 1990“ (M01, belegt) |
| K7 | Calendly-Embed setzt Cookies. v2 blendet das Calendly-Cookie-Banner aus (`hide_gdpr_banner=1`) | Entscheidung E5: nur ausblenden, wenn die Einwilligung der Website Calendly abdeckt |
| K8 | Bestätigungsseite per Calendly-Weiterleitung braucht eine Calendly-Einstellung | Bestätigung als Zustand auf derselben Seite über `calendly.event_scheduled` (T10). Keine Calendly-Änderung |
| K9 | Ad verspricht Training, Seite ein Gespräch (T4) | Diese Seite sagt klar: Gespräch, 30 Minuten, kostenlos. Ad-Abgleich gehört zu den Ads (Pauspapier), nicht in diesen Lauf |
| K10 | Kaution offen (T5, Michael) | nichts auf der Seite |
