# Landingpage „KI-Website“ (Modell Praxis Hüwel) — Content v1

Stand 13.10.2026. Nur Inhalt, noch kein Design, nichts live. Sprache Sie (wie 741.studio DE). Rahmen: `00_project/prompts/direct-response-copy-prompts.md`. Keine Gedankenstriche im Seitentext.

## 0. Faktenbasis (nur das hier darf als Beleg auf die Seite)

| # | Fakt | Quelle |
| --- | --- | --- |
| F1 | Seite live seit 06.10.2026 unter www.praxis-huewel.de, gehostet auf GitHub Pages, Hosting-Kosten 0 € | Memory huewel-website-live-state; Konzept §6 "Kosten: null" |
| F2 | Geladen in Chrome am 13.10.2026: größtes Element nach 1,3 s, 6 Anfragen, 0 fremde Skripte, kein Layout-Springen (CLS 0) | Messung 741, Chrome, Standort Bali |
| F3 | Der Kunde ändert seine Seite per Chat mit seiner eigenen KI (ChatGPT, bestehendes Plus-Abo). Die KI ändert eine Kopie, nie die Live-Seite | `~/huewel-site/ANLEITUNG.md` |
| F4 | Feste Regeln für die KI: `AGENTS.md` (Frage-Protokoll vor jeder Änderung), `DESIGN.md` (gesperrte Farben, Schriften, Bausteine) | Memory huewel-repo-ai-rules |
| F5 | Automatische Prüfung bei jeder Änderung: blockt Löschungen, fremde Skripte, Schriften und iframes, kaputte Links und Bilder, SEO-Fehler, HWG-Risikowörter | `.github/workflows/pruefung.yml`, Memory huewel-repo-ai-rules |
| F6 | 741 gibt jede Änderung frei, bevor sie live geht. Jede Version bleibt gespeichert und lässt sich in wenigen Minuten zurückholen | ANLEITUNG.md "Gut zu wissen" |
| F7 | Einmalige Einrichtung für den Kunden: ca. 15 Minuten, zusammen mit 741, nichts zu installieren | ANLEITUNG.md Teil 1 |
| F8 | Formulare laufen über ein eigenes Backend (Supabase + Resend), Mails vom Praxis-Absender; Kontakte aus dem alten Tool (58) übernommen | Memory huewel-website-live-state, huewel-onlyinside-ersatz |
| F9 | Strukturierte Daten (JSON-LD) auf allen Seiten, Weiterleitungen aller alten Adressen (88), eigene 404-Seite | Memory huewel-website-live-state |

**[FEHLT] vor dem Livegang (Martin):**
1. Darf „Praxis Hüwel, Nürnberg“ als Referenz mit Namen genannt werden? (Hüwels Einverständnis)
2. Was kostete das alte Setup (ONLY INSIDE und andere Abos) pro Monat? Nur mit echter Zahl wird daraus ein Spar-Beleg.
3. Produktname: Arbeitstitel „KI-Website“. Alternativen siehe §9.
4. Ziel-URL: Vorschlag `/de/pages/ki-website.html` (+ EN später).
5. „24/7 Hilfe“: Die KI hilft rund um die Uhr. 741 prüft und gibt frei, aber nicht nachts in Minuten. Formulierung unten ist darauf abgestimmt; bitte bestätigen.
6. Newsletter und Kontakte im 741-Portal sind bei Hüwel auf Staging, noch nicht live. Darum stehen sie unten als „auf Wunsch“, nicht als fertige Funktion.

## 1. Hero Headline (10 Varianten)

| # | Headline |
| --- | --- |
| 1 | **Ihre Website ändern Sie ab heute per Chat, schnell, sicher und ohne Website-Abo (live in 1,3 Sekunden geladen)** ← 741 empfiehlt |
| 2 | Schreiben Sie, was sich ändern soll, und Ihre Website folgt, mit festen Regeln, die nichts kaputt machen lassen |
| 3 | Endlich unabhängig: Ihre Website gehört Ihnen, läuft ohne Baukasten-Abo und lässt sich in Minuten per KI ändern |
| 4 | Die schnellste Website Ihrer Branche, die Sie selbst pflegen, in 15 Minuten eingerichtet (0 fremde Skripte) |
| 5 | Nie wieder auf die Agentur warten: Texte, Seiten und Bilder per Chat ändern, geprüft vor jedem Livegang |
| 6 | Eine Website, die so einfach ist wie eine Nachricht schreiben, und so sicher, dass sie nicht kaputtgehen kann |
| 7 | Schluss mit Plugins, Updates und Abo-Rechnungen: Ihre KI-Website pflegt sich per Chat, 741 prüft jede Änderung |
| 8 | Ihre Website in Ihrer Hand, rund um die Uhr per KI änderbar, jede Version in Minuten zurückholbar |
| 9 | Werden Sie unabhängig von Technik und Abos, mit einer Website, die Sie per Chat steuern (Hosting 0 €) |
| 10 | Die Website, die mitdenkt: Sie schreiben den Wunsch, die KI setzt ihn um, die Prüfung schützt Design und Rankings |

## 2. Sub-Headline

**V1 (Schmerz zuerst):** Jede kleine Textänderung kostet Sie heute eine Mail, eine Rechnung oder einen Abend im Baukasten. Mit der 741 KI-Website schreiben Sie Ihren Wunsch in den Chat, die KI ändert eine Kopie, eine automatische Prüfung schützt Design und Rankings, und nach der Freigabe ist es live.

**V2 (Mechanismus):** Abhängig von Baukasten, Plugins und Agentur? Die einzige Website mit festen KI-Regeln und automatischer Prüfung bei jeder Änderung, damit Sie Texte und Seiten selbst ändern, kein Abo mehr zahlen und trotzdem nichts kaputt machen können.

## 3. Pain-Point-Sektion (PAS)

Liebe Praxisinhaberinnen und Praxisinhaber,

✓ Warten Sie Tage auf eine kleine Textänderung?
✓ Zahlen Sie jeden Monat für Baukasten, Plugins und Tools, die Sie kaum nutzen?
✓ Haben Sie Angst, beim Ändern etwas kaputt zu machen?

Sie sind nicht allein.

Die meisten Websites sind für Agenturen gebaut. Nicht für die Menschen, denen sie gehören.

Ein neuer Preis. Eine neue Leistung. Ein Urlaubshinweis.
Und jedes Mal: **warten, bezahlen, hoffen.**

Was Sie das kostet:
- Veraltete Texte, die Patienten und Kunden verunsichern
- Monatliche Abos für Funktionen, die eine gute Website gar nicht braucht
- Langsame Seiten voller Plugins, die Google nicht mag
- Abhängigkeit von einer Person oder einem Tool

**Sie brauchen keinen neuen Baukasten.**
Sie brauchen keine Programmierkenntnisse.
Und Sie brauchen keine weitere Monatsrechnung.

Sie brauchen eine Website, **die Sie per Chat ändern** und die sich selbst schützt.

Genau das haben wir für eine Heilpraxis in Nürnberg gebaut [FEHLT 1: Name nur mit Erlaubnis].
Seit Oktober 2026 live. Gemessen: Hauptinhalt nach 1,3 Sekunden geladen, kein einziges fremdes Skript.

## 4. Pain-Headlines (5, Formate gemischt)

| # | Format | Headline |
| --- | --- | --- |
| 1 | Frage | Warum zahlen Sie jeden Monat für eine Website, die Sie nicht selbst ändern können? |
| 2 | Reframe | Ihre Website ist nicht zu kompliziert. Sie ist nur für die falschen Menschen gebaut. |
| 3 | Warnung/Anleitung | Hören Sie auf, für Plugins zu zahlen, und ändern Sie Ihre Seite einfach per Chat. |
| 4 | Bold Claim | Eine Website braucht kein Baukasten-Abo. Sie braucht klare Regeln. |
| 5 | Frage + Lösung | Angst, etwas kaputt zu machen? Die Prüfung lässt es gar nicht zu. |

## 5. Value Props (6 echt einzigartige, nicht 8)

Nur 6 sind belegbar einzigartig. Generika wie „modernes Design“ oder „mobil optimiert“ lasse ich weg, weil jeder Wettbewerber sie behauptet.

1. Ändern per Chat mit der eigenen KI (F3)
2. Feste KI-Regeln für Design und Inhalte (F4)
3. Automatische Prüfung bei jeder Änderung, inklusive HWG-Wortliste für Gesundheitsberufe (F5)
4. Freigabe durch 741 und Rückkehr zu jeder Version in Minuten (F6)
5. Kein Baukasten, keine Plugins, Hosting 0 € (F1, F2)
6. Eigene Formulare und Kontakte ohne Fremd-Tool (F8)

## 6. Value-Prop-Headlines

| # | Kern-Differenzierer | Headline |
| --- | --- | --- |
| 1 | Ändern per Chat | Schreiben Sie Ihren Wunsch in den Chat und sehen Sie Ihre Website folgen, ganz ohne Technik |
| 2 | Feste KI-Regeln | Ändern Sie Texte und Seiten frei, während feste Regeln Ihr Design zuverlässig schützen |
| 3 | Prüfung bei jeder Änderung | Veröffentlichen Sie mit ruhigem Gewissen, weil jede Änderung automatisch auf Fehler geprüft wird |
| 4 | Freigabe und Rückweg | Probieren Sie Neues ohne Risiko, denn jede Version lässt sich in Minuten zurückholen |
| 5 | Ohne Abo, ohne Plugins | Sparen Sie Baukasten- und Plugin-Abos und gewinnen Sie eine Seite, die in 1,3 Sekunden lädt |
| 6 | Eigene Formulare | Erhalten Sie Anfragen direkt von Ihrer Website, ohne Ihre Daten einem weiteren Tool zu geben |

## 7. Primary CTA (5 Varianten)

| # | CTA |
| --- | --- |
| 1 | **Kostenlos prüfen, ob Ihre Website umziehen kann** ← 741 empfiehlt |
| 2 | Zeigen Sie mir, wie ich meine Seite per Chat ändere |
| 3 | Meine KI-Website anfragen |
| 4 | Kostenlose Potenzialanalyse für meine Website |
| 5 | Erst sehen, dann entscheiden: Demo anfragen |

## 8. Seitenaufbau (Vorschlag, Reihenfolge)

1. **Hero:** Headline 1, Sub-Headline V1, CTA 1, Beweis-Zeile „Live seit Oktober 2026 · 1,3 s geladen · 0 fremde Skripte“
2. **So funktioniert es (3 Schritte):** Wunsch in den Chat schreiben → KI ändert eine Kopie, die Prüfung läuft → 741 gibt frei, live in ein bis zwei Minuten
3. **Pain-Sektion** (PAS, §3)
4. **Was die Prüfung blockt:** Liste aus F5, als Schutzschild visualisiert
5. **Value Props** (6 Karten, §6)
6. **Vorher / Nachher:** altes Setup (Baukasten, Abos, Warten) gegen KI-Website. Zahlen nur mit [FEHLT 2]
7. **Für wen:** Bestandskunden (Umzug der bestehenden Seite) und Neukunden
8. **Hilfe:** „Ihre KI hilft rund um die Uhr. 741 prüft jede Änderung und ist für Sie da, wenn die KI nicht weiterkommt.“ [FEHLT 5]
9. **FAQ:** Brauche ich Technikwissen? Was kostet die KI? Was passiert, wenn ich etwas falsch mache? Wem gehört die Website? Kann ich Seiten selbst anlegen?
10. **Abschluss-CTA** mit Rückversicherung „Kostenlos und unverbindlich“

## 9. Namensvorschläge für das Produkt
| Name | Gedanke |
| --- | --- |
| **741 KI-Website** | klar, suchbar ← 741 empfiehlt |
| Chat-Website | beschreibt die Bedienung |
| Website per Chat | wörtlich, gut für Headlines |
