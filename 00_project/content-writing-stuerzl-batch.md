# Stürzl: Batch "alle restlichen Seiten" (Content Writing, 2026-10-11)

Auftrag von Martin (2026-10-11): „please create all other pages according to the sitetree.“ Das gilt als Go für die Outlines (Checkpoint 1) dieses Batches. Die fertigen Texte brauchen weiterhin Martins Freigabe (Checkpoint 2). Nichts geht live, nichts auf Drive, Portal oder ins CMS.

Dieses Dokument ist die gemeinsame Anweisung für alle Schreib-Agenten. Replies und Arbeitsdateien in STE (ASD-STE100). Seitentext für den Kunden: normales Deutsch.

## 1. Lies zuerst (in dieser Reihenfolge)

1. `~/.claude/skills/content-writing/SKILL.md` und alle Dateien in `~/.claude/skills/content-writing/references/` (copy-rules, legal-rules, fact-rules, seo-geo-rules, page-templates, blog-rules, voice-rules, de-tells). Das ist der Prozess. Die Skripte liegen in `~/.claude/skills/content-writing/scripts/`.
2. Referenzlauf: `/Users/martindrendel/741website/00_project/assets/stuerzl/content-writing/selbstanzeige/` mit `01-brief/brief.json`, `claims.json`, `gate-a0.md`, `03-draft/draft-v5.md` (Struktur Seller-Layer + Vertiefung), `OPEN-FLAGS.md`, `04-gates/gates.md`. Nimm Format und Tiefe dieser Seite als Maßstab. Von dieser Seite stammt die freigegebene Wortwahl.
3. Stimmprofil: `/Users/martindrendel/741website/00_project/assets/stuerzl/voice.md` (Sie, wir; Wendungen der Kanzlei; Wörter, die nicht übernommen werden).
4. Kundendaten: `assets/stuerzl/content-pool/01-client/client-baseline.md`, `client-input-2026-10-11.md`, `client-texte/` (kosten.txt, compliance.txt, ki-baustein.txt, pruefung-2026-10-11.md), `assets/stuerzl/cro/04-copy/approved-copy.md` (freigegebene Startseite: Telefonnummern, Büros, Nicht-Liste, Einwände).
5. Pool und Sitemap: `assets/stuerzl/content-pool/04-pool/pool.json` (Items je Seite), `05-sitetree/sitetree.json` (Elternseite, Geschwister, interne Links), `02-competitors/` (SERPs `serp-*.json`, Messwerte `metrics.json` mit Wörtern), `03-demand/` (volume.json, autocomplete.json).
6. Live-Website des Kunden (Stimme und Bestand). Rohtexte bereits gespeichert in `assets/stuerzl/content-writing/selbstanzeige/_work/live/` (home, kanzlei, faq, dr-anja-stuerzl, unternehmensvertretung, kontakt, leistungen, Verteidigung, Durchsuchung). Weitere Seiten mit `curl -sL -A "Mozilla/5.0" "https://stuerzl-steuerstrafrecht.de<Pfad>"` holen und Text ausziehen. Lies zu jeder Seite die Live-FAQ (`faq.txt`) nach Antworten zum Thema: Antworten der Kanzlei werden übernommen und gekürzt, nie ersetzt. Alle URLs: `content-pool/05-sitetree/own-urls.txt`.

## 2. Entscheidungen, die schon gelten

- Rechtsmodus **BRAO / UWG**. Anrede **Sie**. Sprecher **wir** (Person-Blöcke dritte Person, Zitate in ich-Form nur wörtlich von der Live-Seite). Keine Gedankenstriche (— und –). Haupt-CTA-Text überall: **Vertraulich anfragen**, Beruhigungszeile: „Nennen Sie uns nur Ihr Thema, keine Einzelheiten.“ Kein WhatsApp (§ 203 StGB, DSGVO).
- Verbotene Wörter (G2-Skript prüft): spezialisiert, Spezialist, Experte, Expertin, Expertise, führend, beste, Exzellenz, einzigartig, hart in der Sache, kostenlos, gratis, Festpreis, Straffreiheit als Versprechen, Strafe vermeiden, gewinnen, Angst-Wörter. Die Live-Seite benutzt einige davon selbst: **nicht übernehmen**, in `OPEN-FLAGS.md` des Laufs melden.
- Titel nur mit Beleg: Dr. Anja Stürzl: Fachanwältin für Steuerrecht seit 2021, Zertifizierte Beraterin für Steuerstrafrecht (DAA) seit 2022 (Lebenslauf). Titel anderer Personen nur, wenn die Live-Profilseite sie nennt. „Fachanwalt für Strafrecht“ nie.
- **Kostenmodell:** Zeitaufwand in Sechs-Minuten-Einheiten, Vergütungsvereinbarung, kein RVG, Vorschuss, Erstberatung gegen Pauschale, Vier-Augen-Prinzip (Quelle `kosten.txt`). Keine Beträge im Text. Beträge nur als `[von Kunde bestätigen: …]`. Die freigegebene Startseite sagt noch „RVG“: nicht übernehmen, im Flag melden.
- **Adressen und Kontaktdaten sind bestätigt** (Source of Truth des Kunden, Martin 2026-10-11; Korrektur einer früheren Fehlannahme dieser Datei). Frankfurt: Untermainkai 26, 60329 Frankfurt am Main (Umzug 05.10.2026), Post und Empfang Wilhelm-Leuschner-Straße 23, Tiefgarage Wilhelm-Leuschner-Straße 27-29 (Plätze 148 und 146), Telefon +49 69 298028870. München: Oberanger 32, 80331 München, Telefon +49 89 72444170. Telefonzeiten Montag bis Freitag 09:30 bis 14:30, Termine und Erstberatung auch außerhalb nach Vereinbarung. Notfallnummern 0160 3396513 und 0160 95945730 stehen öffentlich auf der Live-Kontaktseite. Daten: `assets/stuerzl/nap.json`, Text-Auszug des Sheets: `assets/stuerzl/source-of-truth-2026-10-11.md`. **Lies den Auszug, bevor du eine Tatsache als offen markierst.** Nur die Umstellung von Google-Profil und Live-Website wartet auf Martins Go (Veröffentlichung). Keine Öffnungszeiten ins Schema. Alte Adresse Wiesenhüttenstraße nie nennen.
- Bewertungen (anwalt.de 5,0 mit 79, Google 5,0 mit 14), Auszeichnungen, Rankings, Pressestimmen: **nicht freigegeben**. Nur als Platzhalter oder Hinweis. Mandanten-Zitate nie erfinden.
- Zahlen, Paragrafen, Fristen, Strafrahmen: **nur mit Gesetzestext**. Hole den Text von `https://www.gesetze-im-internet.de/<gesetz>/<norm>.html`, speichere ihn in `<lauf>/_work/` und zitiere nur, was dort steht. Für BRAO, StPO, StGB, AO, OWiG, ZollV, SchwarzArbG usw. Urteile und Literatur nur, wenn du die Quelle im Lauf gelesen und gespeichert hast. Sonst Aussage streichen.
- Seitentypen und Abschnitts-IDs: `references/page-templates.md`. Geldseiten (service) nutzen **Seller-Layer + Vertiefung**: Seller-Layer S01 bis S06 und S08 bis S09 schnell und scannbar (zusammen höchstens 550 sichtbare Wörter), die Tiefe steht in S07 als 3 bis 5 Akkordeon-Blöcke (`### Überschrift`, je 120 bis 220 Wörter). Lange Lehrtexte gehören in Ratgeber-Beiträge (ST-35, ST-36, ST-37) und werden verlinkt, nicht kopiert.
- Interne Links nur auf Seiten der Sitemap (`sitetree.json`), mit dem neuen Slug, falls vorhanden (z. B. /kosten/, /compliance/, /steuerfahndung-durchsuchung/, /standort-frankfurt/, /standort-muenchen/, /ratgeber/…), sonst mit dem Live-Pfad ohne /index.php/ nur wenn die Sitemap das so führt. Bereits geschrieben: /selbstanzeige/ (ST-14).
- Seite ST-00 Startseite: **nicht** schreiben (CRO-Text ist freigegeben). ST-15, ST-16, ST-17: nicht schreiben (in ST-14 aufgegangen). ST-50 Fallbeispiele: **nicht schreiben** (keine Daten, nur Blocker melden).

## 3. Ablauf je Seite (Skript-Skill, gekürzt)

Ordner: `/Users/martindrendel/741website/00_project/assets/stuerzl/content-writing/<st-id>-<slug>/` (z. B. `st-18-steuerfahndung-durchsuchung`). Unterordner wie im Skill: `01-brief/` (brief.json nach `content-writing-brief.schema.json`, claims.json, gate-a0.md), `02-outline/outline.md`, `03-draft/`, `04-gates/`, `05-final/` (page.md, cms-blocks.txt, placeholders.md), `_work/`, `_status.md`, `OPEN-FLAGS.md`, `_run.json`.

1. **Readiness und Blocker:** Pool-Item vorhanden, Keyword mit Volumen, Rechtsmodus, Stimmprofil. Ein Blocker (Seite ohne Daten) heißt: Seite nicht schreiben, im Bericht melden.
2. **A0-Gate:** Geldseiten voll (Bestand abholen und zählen mit `content-pool-skill/scripts/page_metrics.py`, SERP und PAA für das Keyword, mindestens 2 Wettbewerber-Messungen, alle SERP-Treffer durchprobieren). Nutze vorhandene SERPs/Metriken des Pools, wenn das Keyword passt. Sonst SERP per DataForSEO: `python3 /Users/martindrendel/741website/00_project/content-pool-skill/scripts/dfs.py serp/google/organic/live/advanced <payload.json> <out.json> --run-dir <lauf>/_work --cap 1.0` (Beispiel-Payload: `content-pool/02-competitors/serp-5-payload.json`, Land DE, Sprache de, location_code 2276). Kosten pro Seite höchstens 1 USD. Hub-, About-, Team-, Kontakt-, Person-, Presse-Seiten: Typ-C-Gate (Bestand und alle Kundentexte zum Thema, kein Benchmark).
3. **Brief und Claims:** `brief.json` und `claims.json` im Format der Referenzseite. Jede Zahl, jeder Paragraf, jeder Titel steht in claims.json mit Quelle und Datum.
4. **Outline:** `02-outline/outline.md` (Abschnitte, Überschriften mit bis zu 3 Varianten, Claims, Platzhalter, Entscheidungen für Martin). Weiter ohne Warten (Martins Go für diesen Batch).
5. **Entwurf:** `03-draft/draft-v1.md` im Seiten-Template. Bestand der Kanzlei und ihre FAQ-Antworten übernehmen und ausbauen, nie dünner als der Bestand, mindestens 70 % des Wettbewerber-Medians bei Geldseiten (Skript prüft). Wörter zählen nur mit `wordcount.py`.
6. **Gates:** `python3 ~/.claude/skills/content-writing/scripts/run_gates.py <lauf>` (Seite mit `--page`). Beheben bis alle grün sind. Das Skript prüft die Datei `05-final/placeholders.md` (alle gelben Platzhalter müssen dort stehen, Format der Referenzseite).
7. **Slop-Gate:** Lint ist in G5. Dann **höchstens 2** Cleanse-Aufrufe: `bash ~/.claude/skills/content-writing/scripts/cleanse_de.sh <entwurf> > cleansed.md 2> notes.txt`, danach `diff_claims.py diff` und `deslop_de.py`. Nur eine Cleanse-Fassung übernehmen, wenn der Diff besteht. Läuft codex nicht, melde das (G5 gilt dann als nicht bestanden).
8. **Paket:** `05-final/page.md` (Frontmatter wie Referenz, `flags: siehe OPEN-FLAGS.md`, FLAG-Kommentar über S01), `cms-blocks.txt` (`make_cms_blocks.py`), `placeholders.md`, `04-gates/gates.md`, `_status.md`, `OPEN-FLAGS.md` (Rechtsgrauzonen und Widersprüche mit Quelle), `_run.json` (client "STÜRZL Steuerstrafrecht", workflow "copy", page "<ST-ID> <Titel>", status "fertig, Freigabe offen", mode "Echt", last_run, result = Pfad zu page.md, note).
9. **Kein Reviewer-Aufruf:** Reviewer-Agenten startet der Hauptagent nach dem Batch.

## 4. Grenzen

- Schreibe nur in deinen Seitenordnern und in deine Berichtsdatei. Ändere keine bestehende Datei (voice.md, pool.json, sitetree.json, Skill-Dateien, Referenzlauf, Registry). Wünsche dazu gehören in den Bericht.
- Keine Uploads, keine E-Mails, keine Änderungen an einer Website. Keine Aufrufe an Kunden.
- Erfinde nichts. Fehlt eine Tatsache: gelber Platzhalter `[von Kunde bestätigen: …]` und Zeile in `placeholders.md`. Nenne nie Methodenquellen (Hormozi und andere).
- Zähle Kosten: DataForSEO höchstens 1 USD je Seite, Cleanse höchstens 2 Aufrufe je Seite.

## 5. Bericht

Schreibe `/Users/martindrendel/741website/00_project/assets/stuerzl/content-writing/BATCH-<Buchstabe>-report.md`: Tabelle je Seite (ID, Seite, Wörter, Bestand, Wettbewerber-Median, Gates G1 bis G5, Platzhalter, Cleanse-Aufrufe, Kosten USD, Status) plus: was blockiert wurde, neue Widersprüche im Kundenmaterial, Vorschläge für Regeln im Skill, Rechtsgrauzonen. Antwort an den Hauptagenten: 15 Zeilen, STE.

## 6. Zuteilung

### Batch A: Akut und Verteidigung

| ID | Seite | Typ | Status | Live-Pfad / neuer Slug | Keyword (Sitetree) | Pool-Items | Bestand (Wörter) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ST-18 | Steuerfahndung und Durchsuchung (Akutseite) | service | Neu | /steuerfahndung-durchsuchung/ | steuerfahndung anwalt | CP-SVC-007 | None |
| ST-12 | Verteidigung im Steuerstrafverfahren | service | Überarbeiten | /index.php/steuerstrafrecht/verteidigung-im-steuerstrafverfahren | steuerstrafverfahren | CP-SVC-006 | 276 |
| ST-19 | Durchsuchungsbegleitung und Schulung (für Unternehmen) | service | Überarbeiten | /index.php/steuerstrafrecht/durchsuchungsbegleitung-schulung |  | CP-SVC-008 | 223 |
| ST-29 | Verteidigung von Privatpersonen | service | Überarbeiten | /index.php/verteidigung-von-individualpersonen |  | CP-SVC-017 | 211 |

### Batch B: Säule, Gutachten, Hub, FAQ

| ID | Seite | Typ | Status | Live-Pfad / neuer Slug | Keyword (Sitetree) | Pool-Items | Bestand (Wörter) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ST-11 | Steuerstrafrecht (Säulenseite) | service | Überarbeiten | /index.php/steuerstrafrecht | anwalt steuerstrafrecht | CP-SVC-005 | 217 |
| ST-13 | Gutachten und Risikobewertung | service | Überarbeiten | /index.php/steuerstrafrecht/gutachten-risikobewertung | tax compliance | CP-SVC-011 | 282 |
| ST-10 | Leistungen (Übersicht) | hub | Überarbeiten | /index.php/leistungen | anwalt steuerstrafrecht | CP-SVC-001 | 152 |
| ST-32 | FAQ | faq | Überarbeiten | /index.php/faq | steuerstrafverfahren | CP-SVC-004, CP-SVC-024 | 2555 |

### Batch C: Unternehmen und Compliance

| ID | Seite | Typ | Status | Live-Pfad / neuer Slug | Keyword (Sitetree) | Pool-Items | Bestand (Wörter) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ST-21 | Unternehmensvertretung | service | Überarbeiten | /index.php/unternehmensvertretung |  | CP-SVC-016 | 291 |
| ST-26 | Compliance | service | Neu | /compliance/ | tax compliance | CP-SVC-012 | None |
| ST-20 | Wirtschaftsstrafrecht | service | Überarbeiten | /index.php/sonstiges-wirtschaftsstrafrecht | anwalt wirtschaftsstrafrecht | CP-SVC-013 | 142 |
| ST-23 | Ordnungswidrigkeiten | service | Überarbeiten | /index.php/ordnungswidrigkeiten | steuerordnungswidrigkeit | CP-SVC-018 | 229 |

### Batch D: Begleitdelikte und Kosten

| ID | Seite | Typ | Status | Live-Pfad / neuer Slug | Keyword (Sitetree) | Pool-Items | Bestand (Wörter) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ST-25 | Korruptionsstrafrecht | service | Überarbeiten | /index.php/korruptionsstrafrecht |  | CP-SVC-019 | 227 |
| ST-27 | Zollstrafrecht | service | Überarbeiten | /index.php/zollstrafrecht | zollstrafrecht | CP-SVC-014 | 147 |
| ST-28 | Schwarzarbeit, Sozialversicherung und Arbeitnehmerüberlassung (Arbeitsstrafrecht) | service | Überarbeiten | /index.php/arbeitsstrafrecht | schwarzarbeit strafe | CP-SVC-015 | 148 |
| ST-31 | Kosten und Honorar | cost | Neu | /kosten/ | anwaltskosten selbstanzeige | CP-SVC-003, CP-BRD-006 | None |

### Batch E: Kanzlei, Team, Personen, Presse

| ID | Seite | Typ | Status | Live-Pfad / neuer Slug | Keyword (Sitetree) | Pool-Items | Bestand (Wörter) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ST-43 | Kanzlei (Über uns) | about | Überarbeiten | /index.php/kanzlei |  | CP-BRD-005, CP-BRD-003 | 1082 |
| ST-44 | Team | team | Überarbeiten | /index.php/team |  | CP-BRD-004 | 259 |
| ST-45 | Dr. Anja Stürzl | practitioner | Überarbeiten | /index.php/dr-anja-stuerzl | anja stürzl | CP-AUT-001, CP-AUT-010 | 768 |
| ST-46 | Dr. Monika Glogger | practitioner | Überarbeiten | /index.php/dr-monika-glogger |  | - | 311 |
| ST-49 | Veröffentlichungen, Vorträge und Presse | press | Neu | /publikationen/ |  | CP-AUT-004, CP-AUT-003 | None |

### Batch F: Kontakt und Standorte

| ID | Seite | Typ | Status | Live-Pfad / neuer Slug | Keyword (Sitetree) | Pool-Items | Bestand (Wörter) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ST-40 | Kontakt und Anfahrt | contact | Überarbeiten | /index.php/kontakt |  | CP-LOC-002, CP-LOC-003, CP-SVC-020, CP-LOC-006 | 255 |
| ST-41 | Standort Frankfurt | location | Neu | /standort-frankfurt/ | anwalt steuerstrafrecht frankfurt | CP-LOC-004 | None |
| ST-42 | Standort München | location | Neu | /standort-muenchen/ | anwalt steuerstrafrecht münchen | CP-LOC-005 | None |
| ST-33 | Aktuelles | news | Überarbeiten | /index.php/aktuelles |  | - | 338 |

### Batch G: Ratgeber (Vorschläge)

| ID | Seite | Typ | Status | Live-Pfad / neuer Slug | Keyword (Sitetree) | Pool-Items | Bestand (Wörter) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ST-34 | Ratgeber Steuerstrafrecht (Wissens-Hub) | hub | Vorschlag | /ratgeber/ | steuerhinterziehung strafe | CP-AUT-009 | None |
| ST-35 | Steuerhinterziehung: Strafe und Strafrahmen | blog | Vorschlag | /ratgeber/steuerhinterziehung-strafe/ | steuerhinterziehung strafe | CP-SVC-021 | None |
| ST-36 | Verjährung der Steuerhinterziehung | blog | Vorschlag | /ratgeber/verjaehrung/ | steuerhinterziehung verjährung | CP-SVC-022 | None |
| ST-37 | Krypto und Steuerhinterziehung | blog | Vorschlag | /ratgeber/krypto/ | krypto steuerhinterziehung | CP-SVC-023 | None |

### Hinweise zu einzelnen Seiten

- **ST-18 Akutseite (neu):** Keyword „steuerfahndung anwalt“ / „steuerfahndung durchsuchung“. Aufbau „Was tun in der ersten Stunde“: ruhig, klar. Notfallnummern nur als Platzhalter mit den Live-Werten. Keine Verhaltens-Rechtsberatung für den Einzelfall; allgemeine Hinweise nur mit Gesetz (z. B. Beschuldigtenrechte § 136 StPO, Durchsuchung § 102 ff. StPO, § 399 AO, § 404 AO) und Quelle. Die Live-FAQ hat Antworten zu Schweigerecht und Ablauf: übernehmen.
- **ST-31 Kosten (neu):** Grundlage `kosten.txt` (758 Wörter, Kundentext). Wörter wie „besonders hohe Spezialisierung“, „ausgezeichneter Ruf“, „Leidenschaft“ nicht übernehmen (BRAO). Beträge nur als Platzhalter. Rechtsschutz: Platzhalter. KI-Baustein (`ki-baustein.txt`, CP-BRD-006) als Abschnitt mit Prüfhinweis (Datenschutz, Berufsrecht).
- **ST-26 Compliance (neu):** Grundlage `compliance.txt` (370 Wörter). Steuer-Compliance-Bezug fehlt im Kundentext: nicht erfinden, als Frage an die Kanzlei in den Flags. „Haftung vermeiden“ und ähnliche Ergebnisaussagen vermeiden.
- **ST-32 FAQ:** Die Live-FAQ (2.555 Wörter) bleibt inhaltlich. Aufgabe: eine saubere Seite mit einer H1, Gruppen als H2, Fragen als H3, kurzen Direktantworten (40 bis 60 Wörter, CP-SVC-024) über der langen Antwort, rechtlich geprüft. Der Kostenteil der FAQ soll entfallen (Kanzlei-Wunsch): Verweis auf /kosten/. Selbstanzeige-Teil: Verweis auf /selbstanzeige/.
- **ST-10 Leistungen (Hub):** Pool CP-SVC-001: künftig 6 starke Bereiche statt 9 mit sauberen Überschriften. Karten mit Link auf die Kind-Seiten.
- **ST-41, ST-42 Standorte:** Ortsregel: Nachfrage, Einzugsgebiet und ein echter lokaler Fakt mit Quelle sind Pflicht. Lokale Fakten nur aus der Live-Kontaktseite (Anfahrt, Parken, ÖPNV) und gelesenen Quellen. Fehlt ein Teil, schreibe die Seite als Entwurf mit Flag. München: Ansprechpartnerin Lea Wimmer (Standortleitung laut Sitetree), Dr. Monika Glogger (Live-Kontaktseite). Leistungen vor Ort: Platzhalter.
- **ST-43 bis ST-46:** Fakten nur von den Live-Profilseiten. Die Team-Seite nennt auf der Live-Seite Namen ehemaliger Kolleginnen/Kollegen (Pösl, Kellner, Brunzel, Euler, Fenzl, Scherübel): nicht übernehmen, Frage an die Kanzlei in die Flags. Auszeichnungen und Rankings: nur als freigabepflichtiger Platzhalter.
- **ST-45 Dr. Stürzl:** Struktur aus `references/page-templates.md` Abschnitt 4. Das Zitat „Jedes Mandat und jeder Mandant ist anders.“ und „Effektive Strafverteidigung ist nicht zwingend ‚laut‘ und ‚konfrontativ‘.“ stehen auf der Live-Seite.
- **ST-34 bis ST-37 (Ratgeber, Vorschläge):** Blog-Template und `blog-rules.md`. Status im Frontmatter: „Vorschlag, wartet auf Abstimmung mit der Kanzlei“. Autorenzeile als Platzhalter (wer schreibt, offen). Pflicht: jede rechtliche Aussage mit gespeichertem Gesetzestext (§ 370 AO, § 376 AO, § 78 StGB, § 169 AO usw.). Keine Einzelfall-Einschätzung. Krypto (ST-37): Steuerrecht zu Kryptowerten nur mit gelesenen Quellen (BMF-Schreiben, § 23 EStG), sonst kurz halten und flaggen.
- **ST-33 Aktuelles:** Nur einen Einleitungsabsatz (Typ news-hub), die Beitragsliste erzeugt das CMS.
