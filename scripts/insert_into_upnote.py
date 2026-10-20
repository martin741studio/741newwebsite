import os
import subprocess
import time

html_content = """<h2>741 Studio — Workflow-Übersicht & Befehle</h2>
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 14px; border: 1px solid #d0d7de;">
  <thead>
    <tr style="background-color: #f6f8fa; text-align: left;">
      <th style="padding: 10px 14px; border: 1px solid #d0d7de; width: 38%;">Befehl / Trigger</th>
      <th style="padding: 10px 14px; border: 1px solid #d0d7de; width: 62%;">Was der Workflow ist</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/cro-homepage &lt;Name&gt;, &lt;URL&gt;, &lt;GBP&gt;, &lt;Kanal&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>CRO Homepage (Track A)</b>: Erstellt einen validierten High-Converting Startseiten-Prototyp (Fokus: Conversion, Hooks, Hero, Lead-Kanal WhatsApp/Call).</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/cro-track-b &lt;Kunde&gt; &lt;URL&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>CRO Track B (Design-intensiv)</b>: Hochwertige Showpiece-Showcase-Seiten mit maßgeschneiderter Markenästhetik, Animationen und tiefer visueller Differenzierung.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/un-burning &lt;Kunde&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Un-Burning (Entbündelung)</b>: Bereinigt Altlasten, segmentiert unklare Sammelangebote in eigenständige, hochprofitable Leistungspakete und schützt die Markenidentität.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/maps-playbook &lt;Kunde&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Get the phone to ring (Maps Growth Playbook)</b>: Systematische Optimierung des Google Business Profils (Kategorien, Attribute, Belege, Fotos, lokale Relevanz) zur Steigerung lokaler Anrufe.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">Chat: Starte Maps-Audit für &lt;Kunde&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Client Audit (Maps-Readiness)</b>: Tiefenanalyse der digitalen Ausgangslage (Google Maps, Website-Speed, On-Page SEO, Citations) mit Scorecard (0–100) vor Kickoff.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/content-pool &lt;Kunde&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Content Pool</b>: Erstellt einen datengestützten Themenpool (Suchvolumen, Intent, Fragen, Cluster) für Blogs und Leistungsunterseiten inklusive HTML/Excel-Export.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/content-write &lt;Kunde&gt; &lt;Seite/Thema&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Content Writing</b>: Schreibt conversion-starke, rechtskonforme und YMYL-sichere Seitentexte und Fachartikel in der authentischen Stimme des Kunden.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/collab-content &lt;Kunde&gt; &lt;Partner-Domain&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Co-Marketing & Backlink Collaboration</b>: Plant und schreibt synergetische Kooperations-Gastartikel (Client & Partner) zum gegenseitigen Backlink- und Relevanzaufbau.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/backlink-dach &lt;Kunde&gt;, &lt;Stadt&gt;, &lt;Budget&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Backlink DACH</b>: Identifiziert und priorisiert themen- und ortsrelevante Backlink-Möglichkeiten (Verbände, lokale Medien, Partner) im DACH-Raum.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">Chat: Prüfe Citation-Status für &lt;Kunde&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Citation-Modul (NAP & Verzeichnisse)</b>: Überwacht und synchronisiert Name, Adresse, Telefonnummer (NAP) über Verzeichnisse (BrightLocal, Gelbe Seiten etc.) im Kundenportal.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/automation-build &lt;Kunde&gt; &lt;Automation&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Automation Build</b>: Konzipiert, baut und testet Integrations- und Funnel-Automationen (Zapier, Make, n8n, KlickTipp) mit Sicherheitsstufen L0–L6.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/tracking &lt;mode&gt; &lt;Kunde&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Proof Tracking & Quartal</b>: Wöchentliche Performance-Karten (Metrics, Leads, Warnings R1–R6) sowie Vorbereitung des quartalsweisen War-Room-Reviews.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/client-roadmap &lt;Kunde&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Client Roadmap & Goal Engine</b>: Steuert Kundenprojekte entlang harter Meilensteine (M1–M4) mit automatischer Zielüberprüfung und Pre-Flight-Prüfung.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">Chat: Review-Page für &lt;Name&gt;, &lt;URL&gt;, &lt;Maps&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Prospect Review-Page (Mini)</b>: Generiert eine interaktive Video- und Audit-Review-Landingpage für Pitches an Interessenten (z. B. nach Kaltakquise).</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">Chat: Sales Call Prep für &lt;Prospect&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Sales Call Prep</b>: Erstellt ein vertrauliches Vorbereitungsdossier (Wettbewerbsanalyse, Schwachstellen, Pitch-Angle) für Martins Erstgespräche.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/sales-pitch &lt;Prospect&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Sales Call &amp; High-Ticket Pitch Architecture</b>: Strukturiert und steuert den 60-Minuten-Abschluss-Call (Min 00–60), NEPQ-Tiefendiagnose, 3-Tier Offer Stack (1.999 / 3.699 / 7.999 €) mit Leistungsgarantie und Einwand-Matrix.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">Chat: cal.com-Buchung einfügen</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Booking-Sequenz (WhatsApp-Funnel)</b>: Generiert eine 3-stufige personalisierte WhatsApp-Nachrichten-Sequenz nach Terminbuchung zur Minimierung von No-Shows.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">Chat: Starte Morning Grill</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Morning Grill</b>: Strukturierte Morgen-Routine zur Priorisierung von Tageszielen, Blockern und anstehenden Kunden-Milestones.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">Chat: Starte Evening Check-out</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Evening Check-out</b>: Tagesabschluss zur Protokollierung erledigter Aufgaben, Dokumentation von Erkenntnissen und Vorbereitung der Night Shift.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">Chat: Starte Night Shift</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Night Shift</b>: Autonome Hintergrund- und Batch-Ausführung von Audits, Datenaggregationen und Code-Scans über Nacht auf dem Server.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">Monitor / Telegram: Canary Alert</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Canary (Ausfall-Wächter)</b>: 24/7-Monitoring für Zaps, Server und kritische Kunden-APIs mit automatischer Alarmierung über den 741-Telegram-Bot.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/client-access-lockout &lt;Kunde&gt;, &lt;Tool&gt;</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Kunde entzieht Zugang (Incident Recovery)</b>: Notfall-Protokoll zur Beweissicherung, Erstellung eines Leistungsnachweises (PDF) und Schutz bei Vertragsstreitigkeiten.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">Chat: Ziele &amp; Datenarchitektur abgleichen</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Ziel-Datenarchitektur</b>: Gleicht Kundenziele und Meilensteine zwischen Supabase, Google Drive und lokalen Roadmaps ab.</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">/workflow-create &lt;id&gt;</code> oder <code style="background-color: #f0f3f6; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, monospace; font-size: 13px;">Chat: Starte Workflow-Architektur</code></td>
      <td style="padding: 8px 12px; border: 1px solid #d0d7de;"><b>Workflow-Architektur &amp; Creator (Meta-System)</b>: Entwickelt, testet und installiert neue cybernetische 741-Workflows (Step 0.0 Inputs Grill bis Checkpoint 2, Checklisten-Enforcement, Scorecard ≥ 80 %, Skill-Installation).</td>
    </tr>
  </tbody>
</table>
"""

html_path = "/tmp/upnote_workflows.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Set clipboard to HTML and plain text
applescript_clipboard = f"""
set f to POSIX file "{html_path}"
set the clipboard to {{«class HTML»:(read f as «class HTML»), Unicode text:(read f as «class utf8»)}}
"""
subprocess.run(["osascript", "-e", applescript_clipboard], check=True)
print("Dual clipboard primed successfully!")

# Open new note in UpNote and paste
paste_script = """
open location "upnote://x-callback-url/note/new"
delay 0.8
tell application "UpNote" to activate
delay 0.4
tell application "System Events"
    keystroke "v" using command down
end tell
"""
subprocess.run(["osascript", "-e", paste_script], check=True)
print("Pasted into UpNote successfully!")
