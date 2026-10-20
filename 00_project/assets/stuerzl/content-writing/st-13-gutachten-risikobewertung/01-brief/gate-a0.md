# Gate A0 (voll): Stürzl, Gutachten und Risikobewertung (ST-13)

Datum: 2026-10-11. Seitentyp A/B (Leistungsseite, Pool-Item ohne eigene Nachfrage; Sitetree-Keyword 'tax compliance'). Quelle der Pool-Daten: `content-pool/` (Lauf 2026-10-11).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth (Name, Leistungen, Anrede, Nicht-Liste) | ja | `client-baseline.md`, `approved-copy.md`, `voice.md`, `nap.json`, `source-of-truth-2026-10-11.md`, 2026-10-11. |
| 2 | Live-Bestand abgerufen und gezählt | ja | `/index.php/steuerstrafrecht/gutachten-risikobewertung`: 282 Wörter, 2×H1 ("Leistungen", "Steuerstrafrecht"), 0×H2. Ein Absatz zu präventiver Beratung, Rechtsgutachten, Compliance-Strukturen. `_work/bestand-metrics.json`, `_work/live/`, 2026-10-11. |
| 3 | Autocomplete-Themenbaum (mindestens 15) | teilweise | Für 'tax compliance' liegt kein Baum im Pool (Pool CP-SVC-011: `autocomplete_hits` 0, Basis "none"). Die SERP 'tax compliance' (20 Treffer, 4 PAA) vom 2026-10-11 ersetzt ihn. Kein Blocker: 0 heißt keine Daten, nicht keine Nachfrage (Regel F3). |
| 4 | Ziel-Keyword und Suchvolumen | ja | tax compliance 590; steuer compliance 20; compliance anwalt 70. `03-demand/volume.json`, DataForSEO 2026-10-11. Hinweis: das Volumen gehört im Pool zu CP-SVC-012 (ST-26). |
| 5 | SERP Top 10 für das Ziel-Keyword | ja | `_work/serp-tax-compliance.json` (neu abgerufen 2026-10-11, DataForSEO serp/google/organic/live/advanced, Kosten 0,0035 USD). Die SERP ist rein informativ: Steuerberater, Wirtschaftsprüfer, Lexika, Fachverlage. Eine Kanzlei-Leistungsseite steht dort nur auf Rang 11 (Steuerstrafrecht München). |
| 6 | Echte PAA-Fragen | ja | 4 Fragen aus der SERP: Aufgaben Compliance Officer (verworfen, off-offer), Beispiele Compliance-Management-System, Was bedeutet Tax Compliance, Compliance auf Deutsch (Duplikat). Im Brief unter `paa_questions`. |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 12 von 12 gelesen, Median **888,5** Wörter, 70-%-Untergrenze **622**. Liste unten. `_work/bench-metrics.json`, 2026-10-11. |
| 8 | Lokaler Fakt | nicht nötig | Bundesweite Themenseite. |

## Messreihe Wettbewerber ('tax compliance', SERP vom 2026-10-11)

| Wörter | Seite |
| --- | --- |
| 1597 | https://www.hlb-hussmann.de/steuerberatung-nuernberg/tax-compliance-management-system/ |
| 1583 | https://scheller-international.com/blog-beitraege/tax-compliance-system.html |
| 1557 | https://www.fachanwalt.de/ratgeber/tax-compliance-ein-muss-fuer-jeden-unternehmer |
| 1362 | https://www.tax-legal-excellence.com/anforderungen-an-ein-tax-compliance-system/ |
| 1115 | https://www.curacon.de/neuigkeiten/neuigkeit/tax-compliance-management-systeme |
| 1017 | https://schulz-beratung.de/mindestanforderungen-an-ein-tax-compliance-system/ |
| 760 | https://www.breidenbach-wp.de/tax-compliance-management-systeme/ |
| 659 | https://lueders-warneboldt.de/news/tax-compliance-management-system/ |
| 606 | https://www.roedl.com/insights/tax-compliance-system-2-punkt-0/ |
| 584 | https://www.fgs.de/news-and-insights/blog/detail/der-tax-compliance-officer-grundlagen-und-effekte-teil-1 |
| 455 | https://www.xn--steuerstrafrecht-mnchen-tpc.de/steuerlexikon/tax-compliance/ |
| 293 | https://www.sb-p.de/leistungen/tax-compliance/ |

Nicht gemessen (Behörde, Video, Datenbank): landkreis-pfaffenhofen.de, youtube.com, springer.com (Fachkapitel hinter Paywall), taxandbytes.de (Kategorie).

## Wortzahl-Urteil (vorab, Ziel)

Bestand 282 Wörter. Wettbewerber-Median 888. Untergrenze 622. Zielkorridor 900 bis 1.300 Wörter. Der Median stammt aus Informationsseiten über Tax-Compliance-Systeme, nicht aus Gutachten-Angeboten. Die Seite deckt nur ab, was die Kanzlei belegt anbietet (Risikobewertung, Gutachten) und nicht mehr.

## Konflikte im Bestand und bei Kundentexten

1. Live-Text nutzt "Spezialisierung" (Pillar-Kopf), nicht übernommen. "Verhindern" strafrechtliche Risiken (Live-ST-13) ist abgeschwächt auf "früh erkennen helfen" (Ergebnisaussage).
2. Tax-Compliance-Leistung: Der Compliance-Text der Kanzlei nennt "Steuer" nicht. Dr. Stürzl hat zu Tax Compliance veröffentlicht (Live-Profil). Ob die Kanzlei Tax-CMS prüft oder aufbaut, ist offen: Platzhalter 2.
3. Hauptkeyword 'tax compliance' steht im Sitetree bei ST-13 und ST-26 (Regel S6). Entscheidung in OPEN-FLAGS B3.

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden (Zeile 3 mit Ersatz). Keine Blocker.
