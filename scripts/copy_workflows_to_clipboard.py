import subprocess

markdown_table = """| Befehl / Trigger | Was der Workflow ist |
|---|---|
| `/cro-homepage <Name>, <URL>, <GBP>, <Kanal>` | **CRO Homepage (Track A)**: Erstellt einen validierten High-Converting Startseiten-Prototyp (Fokus: Conversion, Hooks, Hero, Lead-Kanal WhatsApp/Call). |
| `/cro-track-b <Kunde> <URL>` | **CRO Track B (Design-intensiv)**: Hochwertige Showpiece-Showcase-Seiten mit maßgeschneiderter Markenästhetik, Animationen und tiefer visueller Differenzierung. |
| `/un-burning <Kunde>` | **Un-Burning (Entbündelung)**: Bereinigt Altlasten, segmentiert unklare Sammelangebote in eigenständige, hochprofitable Leistungspakete und schützt die Markenidentität. |
| `/maps-playbook <Kunde>` | **Get the phone to ring (Maps Growth Playbook)**: Systematische Optimierung des Google Business Profils (Kategorien, Attribute, Belege, Fotos, lokale Relevanz) zur Steigerung lokaler Anrufe. |
| Chat: `Starte Maps-Audit für <Kunde>` | **Client Audit (Maps-Readiness)**: Tiefenanalyse der digitalen Ausgangslage (Google Maps, Website-Speed, On-Page SEO, Citations) mit Scorecard (0–100) vor Kickoff. |
| `/content-pool <Kunde>` | **Content Pool**: Erstellt einen datengestützten Themenpool (Suchvolumen, Intent, Fragen, Cluster) für Blogs und Leistungsunterseiten inklusive HTML/Excel-Export. |
| `/content-write <Kunde> <Seite/Thema>` | **Content Writing**: Schreibt conversion-starke, rechtskonforme und YMYL-sichere Seitentexte und Fachartikel in der authentischen Stimme des Kunden. |
| `/collab-content <Kunde> <Partner-Domain>` | **Backlink-Kollaboration (Co-Marketing & Gastbeitrag)**: Gegenseitige Backlink- und Relevanz-Kollaboration zwischen zwei Firmen (z. B. Bali Healing x Ayurvedagram Bali). Erstellt Synergie-Pool und zwei wechselseitige Gastartikel. |
| `/backlink-dach <Kunde>, <Stadt>, <Budget>` | **Backlink DACH (Verzeichnisse & Verbände)**: Identifiziert und priorisiert themen- und ortsrelevante Backlink-Möglichkeiten (Verbände, lokale Medien, Partner) im DACH-Raum. |
| Chat: `Prüfe Citation-Status für <Kunde>` | **Citation-Modul (NAP & Verzeichnisse)**: Überwacht und synchronisiert Name, Adresse, Telefonnummer (NAP) über Verzeichnisse (BrightLocal, Gelbe Seiten etc.) im Kundenportal. |
| `/automation-build <Kunde> <Automation>` | **Automation Build**: Konzipiert, baut und testet Integrations- und Funnel-Automationen (Zapier, Make, n8n, KlickTipp) mit Sicherheitsstufen L0–L6. |
| `/tracking <mode> <Kunde>` | **Proof Tracking & Quartal**: Wöchentliche Performance-Karten (Metrics, Leads, Warnings R1–R6) sowie Vorbereitung des quartalsweisen War-Room-Reviews. |
| `/client-roadmap <Kunde>` | **Client Roadmap & Goal Engine**: Steuert Kundenprojekte entlang harter Meilensteine (M1–M4) mit automatischer Zielüberprüfung und Pre-Flight-Prüfung. |
| Chat: `Review-Page für <Name>, <URL>, <Maps>` | **Prospect Review-Page (Mini)**: Generiert eine interaktive Video- und Audit-Review-Landingpage für Pitches an Interessenten (z. B. nach Kaltakquise). |
| Chat: `Sales Call Prep für <Prospect>` | **Sales Call Prep**: Erstellt ein vertrauliches Vorbereitungsdossier (Wettbewerbsanalyse, Schwachstellen, Pitch-Angle) für Martins Erstgespräche. |
| `/sales-pitch <Prospect>` | **Sales Call & High-Ticket Pitch Architecture**: Strukturiert und steuert den 60-Minuten-Abschluss-Call (Min 00–60), NEPQ-Tiefendiagnose, 3-Tier Offer Stack (1.999 / 3.699 / 7.999 €) mit Leistungsgarantie und Einwand-Matrix. |
| Chat: `cal.com-Buchung einfügen` | **Booking-Sequenz (WhatsApp-Funnel)**: Generiert eine 3-stufige personalisierte WhatsApp-Nachrichten-Sequenz nach Terminbuchung zur Minimierung von No-Shows. |
| Chat: `Starte Morning Grill` | **Morning Grill**: Strukturierte Morgen-Routine zur Priorisierung von Tageszielen, Blockern und anstehenden Kunden-Milestones. |
| Chat: `Starte Evening Check-out` | **Evening Check-out**: Tagesabschluss zur Protokollierung erledigter Aufgaben, Dokumentation von Erkenntnissen und Vorbereitung der Night Shift. |
| Chat: `Starte Night Shift` | **Night Shift**: Autonome Hintergrund- und Batch-Ausführung von Audits, Datenaggregationen und Code-Scans über Nacht auf dem Server. |
| Monitor / Telegram: `Canary Alert` | **Canary (Ausfall-Wächter)**: 24/7-Monitoring für Zaps, Server und kritische Kunden-APIs mit automatischer Alarmierung über den 741-Telegram-Bot. |
| `/client-access-lockout <Kunde>, <Tool>` | **Kunde entzieht Zugang (Incident Recovery)**: Notfall-Protokoll zur Beweissicherung, Erstellung eines Leistungsnachweises (PDF) und Schutz bei Vertragsstreitigkeiten. |
| Chat: `Ziele & Datenarchitektur abgleichen` | **Ziel-Datenarchitektur**: Gleicht Kundenziele und Meilensteine zwischen Supabase, Google Drive und lokalen Roadmaps ab. |
| `/workflow-create <id>` oder Chat: `Starte Workflow-Architektur` | **Workflow-Architektur & Creator (Meta-System)**: Entwickelt, testet und installiert neue cybernetische 741-Workflows (Step 0.0 Inputs Grill bis Checkpoint 2, Checklisten-Enforcement, Scorecard ≥ 80 %, Skill-Installation). |
"""

p = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
p.communicate(markdown_table.encode("utf-8"))
print("Successfully primed clipboard with updated markdown table!")
