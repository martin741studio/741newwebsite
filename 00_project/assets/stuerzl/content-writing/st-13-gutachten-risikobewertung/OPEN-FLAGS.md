# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Gutachten und Risikobewertung ST-13)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand 2026-10-11, nach der Korrekturrunde (REVIEW-B, `content-writing-stuerzl-fixes.md`). Die Vorversion steht in `05-final/page-vorreview.md`. Fragen an die Kanzlei stellen wir erst, wenn sie alles zur Bestätigung bekommt.

## A. Rechtsgrauzonen (BRAO / UWG), nicht vom Agenten zu entscheiden

| # | Stelle im Text | Frage | Aktueller Stand |
| --- | --- | --- | --- |
| A1 | Title, H1 und Meta | "Tax Compliance" ist aus Title, H1 und Meta entfernt. Das Keyword versprach ein Angebot (Tax-CMS), das der Kundentext nicht belegt. Title und H1 lauten jetzt "Gutachten und Risikobewertung im Steuerstrafrecht". | Platzhalter 1. Sobald die Kanzlei das Angebot bestätigt, kann "Tax Compliance" zurück in Title, H1 und Meta (Martin entscheidet). |
| A2 | S05: Titel und Veröffentlichungen (Kapitel "Tax Compliance", Aufsatz GmbH-Steuerpraxis 2022) | Aus Lebenslauf und Live-Profil, nicht aus Kammernachweis. Mit-Autor Tobias Schwartz genannt. Das sind Titel von Veröffentlichungen, kein Leistungsversprechen. | Kanzlei bestätigt. |
| A3 | S07 Block 1 und 2, FAQ: Unterschied § 153 AO und Selbstanzeige | Aussage der Kanzlei aus Live-FAQ, ohne Rechtsprechung. Im Text als "nach Auffassung der Kanzlei" gekennzeichnet. Das Wort "selbstanzeigesicher" ist gestrichen (fixes Punkt 8); der Text sagt "mit Blick auf die Anforderungen des § 371 AO". § 153 Abs. 1 AO steht mit den Bedingungen "Steuerpflichtiger" und "vor Ablauf der Festsetzungsfrist". | Text steht so. Kanzlei prüft, ob sie ihr eigenes Wort doch wünscht (Martin entscheidet einmal für alle Seiten). |
| A4 | S07 Block 3 und FAQ: Geldbußen "bis zu einer Million Euro" (§ 130 Abs. 3 OWiG) und "bis zu zehn Millionen Euro" (§ 30 Abs. 2 OWiG) | Wörtlich aus dem Gesetz, aber hohe Zahlen können als Angstmittel wirken. § 130 Abs. 1 OWiG steht jetzt mit "vorsätzlich oder fahrlässig" und der Bedingung "mit Strafe oder Geldbuße bedroht". § 30 OWiG nennt "juristische Person oder Personenvereinigung" und die Gruppen der leitenden Personen. Die Überschrift nennt nur noch den Inhaber (kein § 9 OWiG). | Text steht so. Kanzlei prüft. |
| A5 | FAQ "Was bedeutet Tax Compliance?" | Erste Hälfte aus dem Compliance-Text der Kanzlei (Wortsinn), zweite Hälfte eine Bezeichnung ohne Quelle. Die Definition in S02 ist gestrichen. | Platzhalter 2: Definition in der Wortwahl der Kanzlei. |
| A6 | S07 Block 5: "Eine Aussage über den Ausgang eines späteren Verfahrens ist damit nicht verbunden." | Abgrenzung zur Ergebnisaussage, eigene Formulierung. | Text steht so. |
| A7 | **Die Live-Seite selbst** sagt, Rechtsgutachten "verhindern" strafrechtliche Risiken und verspricht "bestmögliche Beratung" (Pillar-Kopf) | Ergebnisaussage und Superlativ, § 43b BRAO / UWG. | Nicht übernommen. Martin entscheidet über den Hinweis an die Kanzlei. |
| A8 | S07 Block 4: "Unserer Erfahrung nach werden an kleine und mittelständische Unternehmen immer höhere Anforderungen ... gestellt" | Als Erfahrung der Kanzlei gekennzeichnet (wie auf der Live-Seite), nicht als allgemeine Tatsache. | Kanzlei bestätigt. |

## B. Widersprüche im Kundenmaterial und offene Entscheidungen

| # | Widerspruch | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Vergütung: freigegebene Startseite "RVG oder Vereinbarung", Kundentext "kein RVG, nach Zeitaufwand". | `approved-copy.md` gegen `kosten.txt` | Diese Seite folgt dem Kundentext und den drei Kernsätzen aus dem Fix-Auftrag, keine Beträge. |
| B2 | Erstberatung: Live-Kanzleiseite "Festpreis", Live-FAQ andere Sätze, Kundentext "Pauschale". | `kanzlei.txt`, Live-FAQ, `kosten.txt` | Platzhalter für den Betrag entfernt. Die Seite sagt "üblicherweise gegen Pauschale". Der Betrag steht nur auf /kosten/ (ST-31). |
| B3 | Kannibalisierung (Regel S6): Das Sitetree gibt "tax compliance" an ST-13 und ST-26. | `sitetree.json`, `pool.json`, `serp-tax-compliance.json` | ST-13 trägt jetzt "gutachten und risikobewertung" (Navigationsbegriff, kein Volumen belegt) als Hauptkeyword im Brief. "tax compliance" bleibt offen, bis die Kanzlei das Angebot bestätigt. ST-26 nutzt "compliance beratung". Martin entscheidet. |
| B4 | Der Compliance-Text der Kanzlei nennt "Steuer" nicht. Die Seite /compliance/ (ST-26) ist geschrieben und steht in slugs.json. | `compliance.txt` | Link bleibt. |
| B5 | Pfad wechselt nicht (/steuerstrafrecht/gutachten-risikobewertung/), nur /index.php/ entfällt. Weiterleitung nötig, nicht live ändern (Page-Swap-Regel). | `slugs.json` | Offen für den Livegang. |
| B6 | Vorschläge aus REVIEW-B: Prüfzeile mit Dr. Stürzl, Person-Schema, Tabelle "§ 153 AO oder § 371 AO", Block "Was eine Risikoprüfung umfasst" (Schritte). | REVIEW-B, `schema_tool.py` | Nicht umgesetzt: Prüfzeile und Schritte brauchen die Kanzlei (Angebot unbestätigt), Person-Schema gibt es nur auf Personenseiten. Martin entscheidet. |
