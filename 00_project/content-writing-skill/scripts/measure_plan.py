#!/usr/bin/env python3
"""Write the 30/60/90-day measurement plan for one page (gate G6d, after launch).

    python3 measure_plan.py <run_dir> [--publish YYYY-MM-DD]

Output: <run_dir>/05-final/measure-plan.md. Evidence (Ahrefs 2025): new pages need weeks to months; judge by trend, not by rank 1.
"""
import argparse
import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_json  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("run_dir")
ap.add_argument("--publish")
a = ap.parse_args()
run = Path(a.run_dir)
b = load_json(run / "01-brief/brief.json")
pub = datetime.date.fromisoformat(a.publish) if a.publish else None
def dt(n): return str(pub + datetime.timedelta(days=n)) if pub else f"Veröffentlichung + {n} Tage"
kw = [f"{k['kw']} ({k.get('volume')})" for k in b.get("keywords_cluster", [])] or [b.get("keyword_primary", "")]
t = f"""# Messplan: {b.get('client')} · {b.get('page_slug') or b.get('url_slug')}

Quelle der Zahlen: Google Search Console (Seite + Hauptanfrage). Zugang: [FEHLT: GSC-Zugang für den Dienstkonto-Bot, siehe Client-Status].
URL: {b.get('url_slug')}. Hauptkeyword: {b.get('keyword_primary')}. Cluster: {', '.join(kw)}.
Veröffentlicht am: {pub or '[offen, nach Freigabe und Go]'}.

| Zeitpunkt | Messen | Urteil |
| --- | --- | --- |
| Vor Veröffentlichung | Baseline: Impressionen, Klicks, Position der alten Seite für das Cluster (28 Tage). Zahl der Anfragen über die Seite. | Zahlen festhalten |
| {dt(30)} | Indexiert? (URL-Prüfung). Erste Impressionen? Anzahl Anfragen, für die die Seite eingeblendet wird. | Nicht indexiert nach 30 Tagen: Sitemap, interne Links und Canonical prüfen |
| {dt(60)} | Durchschnittliche Position für das Hauptkeyword, Trend der Impressionen, Zahl der rankenden Anfragen. | Trend nach oben: weiter. Flach: Vertiefung und interne Links ergänzen |
| {dt(90)} | Klicks, Klickrate, Anfragen über Formular und Telefon. Vergleich mit der Baseline. | Nach Trend urteilen, nicht nach Platz 1. Entscheidung: behalten, ausbauen, zusammenlegen |
| {dt(180)} | Stabile Position, Zahl der rankenden Anfragen, Anfragen pro Monat. Quartals-Prüfung (KICK: behalten, verbessern, zusammenlegen, löschen). | Autorität braucht 3 bis 12 Monate: nach Trend urteilen |
| {dt(365)} | Jahres-Prüfung: Rechtsstand, Zahlen, Quellen, Titel. Prüfdatum nur bei echter Prüfung ändern. | Aktualisieren oder zusammenlegen |

**KI-Sichtbarkeit (monatlich, Quartals-Audit):** 10 bis 30 feste Fragen (Prompt-Set) in den KI-Antworten prüfen, ob die Kanzlei oder die Seite genannt wird. Vorschlag aus dem Cluster: {', '.join('"'+q['q']+'"' for q in b.get('paa_questions', []) if q.get('status')=='answered')} und je Leistung "Anwalt für <Thema> in <Stadt>". Ergebnis in eine Tabelle: Datum, Frage, genannt ja/nein, Quelle.

**Vor der Veröffentlichung (Index-Eignung):** noindex und Vorschau-Banner entfernt, Canonical auf die eigene URL, Seite in der Sitemap, keine blockierende robots-Regel. Core Web Vitals der Seite: LCP unter 2,5 s, INP unter 200 ms, CLS unter 0,1.

Zusätzlich außerhalb dieser Seite (korreliert am stärksten mit KI-Sichtbarkeit): neue Erwähnungen der Kanzlei im Web und Verweise von anderen Seiten. Tracking im Backlink-Workflow.
Prüfdatum des Inhalts: alle 12 Monate oder bei Gesetzesänderung (Rechtsstand auf der Seite aktualisieren, Datum nur bei echter Änderung).
"""
(run / "05-final/measure-plan.md").write_text(t, encoding="utf-8")
print(run / "05-final/measure-plan.md")
