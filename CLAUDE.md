# 741website: Arbeitsregeln

## Stil
Antworten und Dokumente in ASD-STE100 Simplified Technical English: kurze aktive Sätze, ein Gedanke je Satz, gleiche Wörter für gleiche Dinge. Ausnahme: E-Mails, Nachrichten, Blogposts und Seitentexte in normaler Prosa. Pfade, Funktionsnamen, Preise und Zahlen bleiben exakt.

## Nachrichten zum Versenden
In einem ```text-Block, Bullets mit "•", Nummerierung mit "1.". Der Stop-Hook `slop_gate` prüft diese Blöcke mit dem Slop-Lint. Nur 5/5 geht raus. Lint- und Cleanse-Schleife: Skill `slopmonster`.

## Gates (Hooks erzwingen sie, hier steht nur das Warum)
- FTP-Deploys, Novamira-Writes, Porkbun, Claude-Config: nur mit Go. Ein getipptes "Go" oder eine Karten-Option mit dem Wort "Go" setzt den Marker (Hook `live_change_gate`).
- Destruktive Shell- und SQL-Befehle blockt `destructive_guard`. INSERT und UPDATE auf Live-Tabellen trotzdem nur nach eigener Bestätigung von Martin.
- Alles, was auf Martin wartet, ist eine AskUserQuestion-Karte, nie eine Prosa-Liste. Details in `~/.claude/CLAUDE.md`.

## Kunden-Seiten
- Body-Copy für Kundenseiten (Abschnitt, Artikel, Blogpost, auch "nur ein Absatz") entsteht nur im Skill `content-writing`. Der Skill ist `disable-model-invocation`, Martin startet ihn mit `/content-writing`. Copy gilt erst als fertig mit einem Lauf in `00_project/workflow-registry/registry.json`.
- Seitenstruktur und Startseiten laufen über `/cro-homepage`, jede Leistungsseite einzeln.
- WordPress-Felder, die Kunden selbst editieren (Überschriften, Textboxen): keine HTML-Tags oder Inline-Styles. Styling über Widget-Einstellungen, Unterfelder oder CSS-Klassen am Container. Zwei gewollte Ausnahmen: das kursive "&" in Baskerville als Inline-Span in Überschriften, und Badge-Pills wie "live von Google" in der Reviews-Überschrift.
- Vor Arbeit an Talkinfive, Praxis Suriya oder Stürzl: `python3 .claude/skills/client-roadmap/scripts/get_roadmap.py <client>` ausführen und den aktiven Meilenstein nennen. Aufgaben bleiben im aktiven Meilenstein. Kisser hat kein roadmap.json.

## Marketing-Daten (Supabase `execute_sql`)
Tabellen per `list_tables`. Fallstricke:
- `gsc_daily_performance` enthält Tageswerte für Klicks, Impressionen, CTR, Position. Nie sagen, GSC-Zeitreihen fehlen.
- `meta_campaigns` sind nur Agentur-Leads. Kunden-Ads stehen in `google_campaigns` und `v_paid_campaigns`.
- Map-Rankings `geo_grid_scans` · Citations `brightlocal_audits`, `client_citations` · Backlinks `client_backlinks` · Leads `leads`, `site_form_submissions` · Kunden-Deliverables `client_drive_assets`.
