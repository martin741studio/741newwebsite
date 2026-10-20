# Master-Prompt: Landingpage „741 Sichtbarkeits-Stipendium" (Heilberufler & Praxen)

> Diesen Prompt 1:1 in eine Claude-Code-Session im Repo `~/741website` geben.

---

Baue die Bewerbungs-Landingpage für unser Gewinnspiel **„741 Sichtbarkeits-Stipendium"** — Zielgruppe: **Heilberufler & Praxen** (Physiotherapie, Heilpraktiker, Naturheilpraxis, Ergo/Logo, Osteopathie, Zahnärzte, Gesundheits-Coaches). Sprache: Deutsch, durchgehend **„du"**.

## Stack & Pflicht-Bausteine (nichts davon neu erfinden)

- Neue Seite: `04_site/de/pages/stipendium.html`, gebaut auf unserer Vite/Handlebars-Pipeline — exakt wie die bestehenden DE-Seiten.
- **Wiederverwenden, nicht nachbauen:** `{{> header }}` (DE-Variante wie auf `04_site/de/pages/local-seo.html`), `{{> footer }}`, `{{> consent }}`, `{{> partner-logos }}`, `weavy.css` + die `seo_*`-Klassen (`seo_section`, `seo_grid`, `seo_btn`, `seo_highlight`, `seo_tagline`, `seo_step_num`) aus `04_site/pages/local-seo.html`.
- CI: Gelb `#fac118` als Akzent, Rich Black, DM Sans — alles kommt aus weavy.css, keine neuen Farben/Fonts.
- **Formular → Supabase:** gleiche Pipeline wie `04_site/pages/sichtbarkeits-analyse.html` (Projekt `bgiljrygqvlgwsrjvhnp.supabase.co`, 741-leads). Lege eine eigene Tabelle `giveaway_entries` an: Name, Praxis-Name, Beruf/Nische (Dropdown), Stadt, E-Mail, Telefon (optional), Website/GBP-Link (optional), `referral_code` (eigener) + `referred_by` (aus URL-Param `?ref=`), Timestamp, Consent-Checkboxen. Resend-Notification an Martin wie bei advertorial_leads.
- **Tracking:** GA4/GTM mit Consent Mode v2 (wie überall live) + Meta Pixel; Events: `ViewContent` bei Load, `Lead` bei erfolgreichem Submit, eigenes Event `giveaway_share` beim Kopieren des Share-Links.
- Tonalität wie unser Praxis-Advertorial `04_site/pages/warum-google-nicht-die-beste-praxis-belohnt.html`: konkret, patientenbezogen, null Agentur-Blabla.

## Messaging (wichtig)

**NICHT** generisch „Website. Google. Local SEO." — sondern das Ergebnis für eine Praxis:

- Kern-Versprechen: **„Wir machen eine Praxis zur sichtbarsten ihrer Stadt. Komplett kostenlos."**
- Übersetzung in Praxis-Realität: gefunden werden, wenn jemand „Physiotherapie + Stadt" googelt → volle Terminkalender, Patienten die anrufen statt Karteileichen.
- Wert: 5.000 € — aber immer als das, was drinsteckt, nicht als Preisschild allein.
- Gewinner = **Live-Fallstudie**: Wir dokumentieren den Weg öffentlich Woche für Woche (das transparent als Teil des Deals framen — „du bekommst das Stipendium, wir zeigen deinen Weg").

## Sektionen (in dieser Reihenfolge)

1. **Hero — hier liegt die meiste Arbeit, mach sie richtig gut:**
   - Badge „GEWINNSPIEL · Teilnahme kostenlos" (Pflicht-Kennzeichnung, sichtbar above the fold)
   - H1 in Richtung: „Das 741 Sichtbarkeits-Stipendium: Wir machen deine Praxis zur sichtbarsten deiner Stadt."
   - Subline: Wert 5.000 €, 1 Gewinner-Praxis, komplett umgesetzt von uns — du bewirbst dich in 60 Sekunden.
   - Deadline/Countdown-Element (Datum als Variable, Ziehung Woche 8 = 05.–09.10.2026)
   - Primärer CTA scrollt zum Formular („Jetzt kostenlos bewerben")
   - **Proof direkt im Hero:** Mini-Strip mit echten Ergebnis-Zahlen unserer Health-Cases (z. B. „#85 → #1 Naturheilpraxis" · „Platz 1 Heilpraktiker Freiburg" · „0 → 100 % Top-3"), Optik wie die Maps-Pin/Rank-Badges unserer Review-Pages.
2. **Trust-Bar:** `{{> partner-logos }}`.
3. **„Was die Gewinner-Praxis bekommt"** — das Paket als konkrete Liste (Website-Relaunch/Optimierung, Google-Business-Profil-Aufbau, Local-SEO auf die wichtigsten Behandlungs-Keywords, Bewertungs-Setup, 90 Tage Begleitung), jede Zeile mit dem Patienten-Nutzen dahinter. Summe: Wert 5.000 €, keine Barauszahlung.
4. **Proof-Wall (Herzstück):** unsere 3 Health-Case-Studies mit echten Zahlen und Links auf die Case-Study-Seiten:
   - Bernd Laserstein, Heilpraktiker Freiburg → Platz 1 (`/case-studies/bernd-laserstein/`)
   - Veronika Schlirf, Naturheilpraxis → von #85 auf Platz 1 (`/case-studies/veronika-schlirf/`)
   - Maria Abel, Praxis → von 0 auf 100 % Top-3 (`/case-studies/maria-abel/`)
   - Aufbau wie die `.section-proof` unserer Review-Pages: echte Namen, echte Rank-Sprünge, Vorher/Nachher. Kein Stock-Material.
5. **„So läuft's ab"** — 3 Schritte mit `seo_step_num`: (1) Formular ausfüllen (60 Sek., kostenlos) → (2) Dokumentierte Ziehung am [Datum] per Los-Verfahren → (3) Gewinner-Praxis startet als Live-Fallstudie, alle anderen bekommen den Gratis-Sichtbarkeits-Check.
6. **Referral-Sektion:** Nach der Bewerbung bekommst du deinen persönlichen Share-Link. **Lädst du eine Kollegin/einen Kollegen ein und diese Praxis gewinnt, gewinnst du mit** (zweites Stipendium/gleichwertiger Preis — final aus den T&Cs übernehmen). Wichtig im Code: Share-Link = `stipendium?ref=CODE`, Teilen läuft NUR über die Teilnehmer selbst — die Seite verschickt nichts an Dritte, wir speichern nur den ref-Code (UWG §7).
7. **„Für wen ist das?"** — Nischen-Chips (Physio, Heilpraktik, Naturheilkunde, Ergo, Logo, Osteo, Zahnmedizin, Gesundheits-Coaching) + ein ehrlicher Satz, für wen es nichts ist (wer nächste Woche Ergebnisse erwartet).
8. **FAQ** (Accordion): Was kostet die Teilnahme? (Nichts, niemals.) · Was ist der Haken? (Keiner — der Gewinner wird öffentliche Fallstudie, das ist unser Marketing.) · Muss ich Kunde werden? (Nein.) · Wie wird gezogen? (Dokumentiertes Los-Verfahren am [Datum].) · Was passiert mit meinen Daten? (Nur fürs Gewinnspiel, Datenschutz-Link.) · Was bekommen Nicht-Gewinner? (Gratis-Sichtbarkeits-Check + befristeter Stipendiums-Tarif.)
9. **Finales Formular** (gleiche Felder wie oben definiert) mit CTA-Wiederholung + Micro-Trust („60 Sekunden · kostenlos · kein Abo, kein Haken").
10. **Teilnahmebedingungen** als eigener Abschnitt/eigene Unterseite, verlinkt aus Hero-Badge und Formular: Veranstalter (741 Digital Solutions LLC), Teilnahmeschluss, Los-Verfahren, Preiswert 5.000 €, keine Barauszahlung, Einverständnis Live-Fallstudie, Newsletter-Opt-in nur als separate, transparente Checkbox (keine Kopplung versteckt). Kennzeichnung „Anwaltliche Prüfung ausstehend" als HTML-Kommentar.

## Rechts-Leitplanken (nicht verhandelbar, aus dem Kampagnen-Sheet)

- Teilnahme **immer kostenlos**, Seite überall klar als **Gewinnspiel** gekennzeichnet
- Einladungen **nur teilnehmergetrieben** über den Share-Link — kein Feature bauen, das Eingeladene direkt anschreibt (UWG §7)
- Newsletter-Kopplung nur transparent (separate Checkbox, kein Pflichtfeld)
- T&Cs-Text als Entwurf markieren → finale Version anwaltlich prüfen lassen

## Abnahme

- Seite lokal bauen und im Browser verifizieren (Desktop + Mobile 375px), Screenshot zeigen
- Formular-Submit end-to-end testen (Testeintrag in `giveaway_entries`, Resend-Mail ankommen sehen, danach Testeintrag löschen)
- Lighthouse-Check: keine Layout-Shifts im Hero, Bilder optimiert
