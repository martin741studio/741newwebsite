#!/usr/bin/env python3
"""Build the client-tab prototype "Ergebnisse" (v2) for the tracking workflow from real data files.

Usage: python3 build_prototype.py   (reads ./data/*.json + ./template.html, writes ./suriya-ergebnisse-prototype.html)
Read-only: no network, no portal, no upload. Every number carries a source link.
"""
import json
from html import escape as e
from pathlib import Path

HERE = Path(__file__).parent
J = lambda f: json.loads((HERE / "data" / f).read_text())
weeks = J("suriya-weekly.json")
reviews = J("suriya-reviews-2026-10-12.json")
scans = J("suriya-scans-2026-08.json")
comp = J("suriya-competitors-2026-08.json")
comp_rev = J("suriya-competitor-reviews-2026-10-12.json")
serp = J("suriya-serp-2026-10-12.json")
guards = J("suriya-guards-2026-10-12.json")["guards"]

PLACE = "ChIJCasDQHi-vUcR1iIwAQ6zUqI"
GBP_LINK = f"https://www.google.com/maps/search/?api=1&query=Praxis+Suriya&query_place_id={PLACE}"
FEE_MONTH = 3699 / 3
LOCKED = ["heilpraktiker ingelheim", "migräne behandlung", "schmerztherapie ingelheim", "akupunktur ingelheim", "naturheilpraxis ingelheim"]

BASE = [w for w in weeks if "2026-06-29" <= w["week"] <= "2026-09-21"]
avg = lambda k: sum(w[k] for w in BASE) / len(BASE)
act = lambda w: w["calls"] + w["web"] + w["routes"]
BASE_ACT = sum(act(w) for w in BASE) / len(BASE)
LAST = next(w for w in weeks if w["week"] == "2026-09-28")


def de(n, d=0):
    return f"{n:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def dm(iso):
    y, m, d = iso[:10].split("-")
    return f"{d}.{m}."


def usdate(s):
    m, d, y = s.split(" ")[0].split("/")
    return f"{int(d):02d}.{int(m):02d}.{y}"


def src(url, label="Quelle öffnen"):
    return f'<a class="srcl" href="{e(url)}" target="_blank" rel="noopener">{label} ↗</a>'


def short(name):
    return name.replace("Heilpraktiker Ingelheim I ", "").split(" - ")[0].split(", ")[0].strip()


def is_me(p):
    return p.get("place_id") == PLACE


# ---------- chart ----------
def chart():
    ws = [w for w in weeks if w["week"] >= "2026-06-29"]
    W, H, pl, pr, pt, pb = 760, 250, 40, 44, 16, 34
    iw, ih = W - pl - pr, H - pt - pb
    n, amax, vmax = len(ws), 32, 260
    bw = iw / n * 0.62
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Kontakte über Google pro Woche und Aufrufe des Profils" class="chart">']
    for t in (0, 10, 20, 30):
        y = pt + ih - t / amax * ih
        o.append(f'<line x1="{pl}" x2="{W-pr}" y1="{y:.1f}" y2="{y:.1f}" class="grid"/><text x="{pl-8}" y="{y+4:.1f}" class="ax" text-anchor="end">{t}</text>')
    for t in (0, 100, 200):
        y = pt + ih - t / vmax * ih
        o.append(f'<text x="{W-pr+8}" y="{y+4:.1f}" class="ax ax-v">{t}</text>')
    pts = []
    for i, w in enumerate(ws):
        x = pl + (i + 0.5) * iw / n
        if w["week"] == "2026-09-21":
            mx = pl + (i + 3 / 7) * iw / n
            o.append(f'<line x1="{mx:.1f}" x2="{mx:.1f}" y1="{pt}" y2="{pt+ih}" class="mark"/><text x="{mx+4:.1f}" y="{pt+10}" class="ax">Umbau 24.09.</text>')
        y0 = pt + ih
        partial = w["week"] == "2026-10-05"
        for k, cls in (("routes", "s-routes"), ("web", "s-web"), ("calls", "s-calls")):
            h = w[k] / amax * ih
            if h > 0:
                o.append(f'<rect x="{x-bw/2:.1f}" y="{y0-h:.1f}" width="{bw:.1f}" height="{h:.1f}" rx="2" class="{cls}{" partial" if partial else ""}"><title>{dm(w["week"])}: {w[k]}</title></rect>')
                y0 -= h
        pts.append((x, pt + ih - w["views"] / vmax * ih, w))
        if i % 2 == 0 or partial:
            o.append(f'<text x="{x:.1f}" y="{H-12}" class="ax" text-anchor="middle">{dm(w["week"])}</text>')
    o.append('<polyline fill="none" class="views" points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y, _ in pts) + '"/>')
    for x, y, w in pts:
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" class="views-dot"><title>{dm(w["week"])}: {w["views"]} Aufrufe</title></circle>')
    o.append("</svg>")
    return "\n".join(o)


# ---------- section 2: competitors ----------
def comp_tables():
    out = []
    for kw in LOCKED:
        c = comp.get(kw)
        if not c:
            continue
        top = c["top"][:4]
        if not any(is_me(p) for p in top):
            me = next((p for p in c["top"] if is_me(p)), None)
            if me:
                top = top[:3] + [me]
        rows = []
        for i, p in enumerate(top):
            t3 = round(float(p["solv"] or 0) * 49 / 100)
            arp = float(p["arp"] or 21)
            rank = "nicht unter 20" if arp >= 21 else de(arp, 1).replace(",0", "")
            maps = f"https://www.google.com/maps/search/?api=1&query={e(short(p['name']))}&query_place_id={p['place_id']}"
            rows.append(f'<tr class="{"me" if is_me(p) else ""}"><td>{"<b>Du</b> · " if is_me(p) else ""}{e(short(p["name"]))}</td><td class="num">{t3} von 49</td><td class="num">{rank}</td><td class="num">{p["reviews"]} · {de(float(p["rating"]),1)} ★</td><td class="num">{len(p.get("categories") or {})}</td><td><a class="srcl" href="{maps}" target="_blank" rel="noopener">Profil ↗</a></td></tr>')
        out.append(
            f'<div class="card ctab"><div class="ctab-h"><b>„{e(kw)}“</b><span>Messung {usdate(c["date"])} · <span class="admin-only">{src(c["public_url"], "Originalbericht (nur 741)")}</span></span></div>'
            f'<div class="tablewrap"><table><thead><tr><th>Praxis</th><th>Platz 1–3 an</th><th>Ø Platz</th><th>Bewertungen</th><th>Kategorien</th><th></th></tr></thead><tbody>{"".join(rows)}</tbody></table></div></div>'
        )
    return "\n".join(out)


def review_race():
    rows = [{"name": "Du (Praxis Suriya)", "now": reviews["total_reviews"], "aug": 12, "me": True, "link": GBP_LINK}]
    for c in comp_rev:
        rows.append({"name": short(c["name"]), "now": c["reviews_2026_10_12"], "aug": c["reviews_2026_08_15"], "me": False, "link": c["map_link"]})
    rows.sort(key=lambda r: -r["now"])
    mx = max(r["now"] for r in rows)
    out = []
    for r in rows:
        w = r["now"] / mx * 100
        d = r["now"] - (r["aug"] or r["now"])
        out.append(f'<div class="race{" me" if r["me"] else ""}"><div class="rn">{e(r["name"])} <a class="srcl" href="{e(r["link"])}" target="_blank" rel="noopener">↗</a></div><div class="rb"><span style="width:{w:.0f}%"></span></div><div class="rv"><b>{r["now"]}</b> <em>{"+" if d >= 0 else ""}{d} seit 15.08.</em></div></div>')
    return "\n".join(out)


# ---------- section 3: maps ----------
def maps_rows():
    rows = []
    for s in sorted(scans, key=lambda s: -(s["solv"] or 0)):
        top3 = round((s["solv"] or 0) * 49 / 100)
        rank = "nicht unter den ersten 20" if s["arp"] in (None, 21) else de(s["arp"], 1).replace(",0", "")
        locked = "fester Begriff" if s["keyword"] in LOCKED else "Zusatz"
        rep = f"https://localrankingtracker.com/scan-report/{s['report_key']}/948fe1232e0a3b9/"
        rows.append(
            f'<tr><td><b>{e(s["keyword"])}</b><br><small>{locked}</small></td><td class="num">{top3} von 49</td><td class="num">{rank}</td>'
            f'<td class="num">{s["found_in"]}</td><td>{dm(s["date"])}2026<br><span class="admin-only">{src(rep, "Bericht (nur 741)")}</span></td>'
            f'<td><a href="{s["grid_image"]}" target="_blank" rel="noopener"><img src="{s["grid_image"]}" alt="Kartenbild {e(s["keyword"])}" loading="lazy"></a></td></tr>'
        )
    return "\n".join(rows)


# ---------- section 4: serp ----------
def serp_rows():
    rows = []
    for kw in LOCKED:
        k = serp["keywords"][kw]
        pos = f'Platz {k["organic_position"]}' if k["organic_position"] else "nicht unter den ersten 100"
        page = (k["url"].replace("https://suriya-praxis.de", "") or "/") if k["url"] else "–"
        page = "Startseite" if page == "/" else page
        extra = []
        if "local_pack" in k["features"]:
            extra.append("Karte mit 3 Praxen" + (" (du dabei)" if any("Suriya" in (x or "") for x in k["local_pack"]) else " (ohne dich)"))
        if "ai_overview" in k["features"]:
            extra.append("KI-Antwort von Google")
        rows.append(f'<tr><td><b>{e(kw)}</b></td><td class="num">{pos}</td><td>{e(page)}</td><td>{e(", ".join(d.replace("www.", "") for d in k["top3"]))}</td><td>{e(" · ".join(extra))}</td><td>{src(k["check_url"], "Suche öffnen")}</td></tr>')
    return "\n".join(rows)


# ---------- section 6: guards ----------
def guard_rows():
    lab = {"ok": ("g", "in Ordnung"), "warn": ("a", "beobachten"), "bad": ("r", "nicht lesbar" )}
    out = []
    for g in guards:
        cls, txt = lab[g["status"]]
        out.append(f'<tr><td><span class="dot {cls}"></span> <b>{e(g["name_de"])}</b></td><td><span class="chip {cls}">{txt}</span></td><td>{e(g["detail"])}</td><td>{src(g["source"])}</td></tr>')
    return "\n".join(out)


# ---------- section 8: quarterly ----------
Q = [
    ("Mitbewerber & Markt", [("Wer hat aufgeholt und warum?", "sammeln", "nach der 2. Maps-Messung"), ("Wer hat verloren oder ist verschwunden?", "sammeln", "Vergleich der Top 10 je Messung"), ("Wer ist neu dazugekommen?", "sammeln", "neue Praxen in den Top 10"), ("Welche Verweise anderer Websites kamen dazu (bei dir und den Mitbewerbern)?", "sammeln", "Stand zur Quartalsrunde"), ("Passen wir uns an den neuen Markt an?", "entscheiden", "in der Runde"), ("Haben unsere letzten Schritte gewirkt?", "entscheiden", "erste Runde = Ausgangswert")]),
    ("Grenzen des Wachstums", [("Wo sind wir schon fast überall vorne?", "gesammelt", "ayurveda 47/49, akupunktur 45/49 Punkte"), ("Welche Seiten bekommen Aufrufe, aber keine Klicks?", "sammeln", "braucht wieder Zugriff auf die Google-Suchdaten"), ("Ab welcher Entfernung wirst du schwächer?", "gesammelt", "heilpraktiker: an allen 49 Punkten sichtbar, an 38 unter den ersten 3"), ("Hast du freie Termine für mehr Patientinnen?", "frage", "Frage an dich vor der Runde")]),
    ("Kürzen & Verdoppeln", [("Welche Inhalte kürzen oder zusammenlegen?", "sammeln", "Seiten ohne Klicks in 90 Tagen"), ("Was verdoppeln wir?", "sammeln", "Seiten und Begriffe, die wachsen"), ("Welche Seiten überarbeiten statt neu schreiben?", "sammeln", "Seiten, die Plätze verlieren")]),
    ("Neue Orte & Leistungen", [("Gibt es Nachfrage in neuen Orten (Bingen, Mainz, Wiesbaden)?", "sammeln", "Routen-Anfragen und Orte deiner Anfragen"), ("Passen die Anfragen zu deinen Terminen?", "sammeln", "startet mit dem Bereich „Anfragen“"), ("Lohnt ein zweiter Standort oder ein zweites Profil?", "entscheiden", "nur mit Nachfrage-Daten"), ("Lohnt eine neue Leistung?", "entscheiden", "Nachfrage aus der Themen-Liste")]),
    ("Plan für einen neuen Standort (nur wenn ja)", [("Standort prüfen", "vorlage", "Nachfrage, Mitbewerber, Erreichbarkeit"), ("Sauber bestätigen lassen statt riskanter Wege", "vorlage", "echte Adresse, Video-Bestätigung"), ("Einträge in Verzeichnissen vorbereiten, bevor das Profil bestätigt ist", "vorlage", "Liste der Verzeichnisse"), ("Bewertungen verteilen und Kosten durchrechnen", "vorlage", "Bewertungen je Standort × Kosten je Termin")]),
    ("Saison & Markt (2–3 Quartale voraus)", [("Welche Aktionen planen wir für die nächsten Monate?", "sammeln", "Suchnachfrage der letzten 24 Monate"), ("Anzeigen und Suchbegriffe feiner einstellen?", "gesammelt", "„migräne behandlung“: Suche zeigt Ratgeber und KI-Antwort, du bist nicht unter 100"), ("Was ändert sich in der Region und bei deiner Wunsch-Patientin?", "sammeln", "öffentliche Daten zur Region"), ("Was ändern Google und KI-Assistenten?", "gesammelt", "KI-Antwort bei 2 von 5 Begriffen (12.10.); ChatGPT nannte dich am 15.08. an 7 von 9 Punkten")]),
]
CHIP = {"gesammelt": ("g", "Daten da"), "sammeln": ("a", "wird gesammelt"), "entscheiden": ("b", "zur Entscheidung"), "frage": ("b", "Frage an dich"), "vorlage": ("n", "Vorlage bereit")}


def quarter():
    out = []
    for title, items in Q:
        li = "".join(f'<li><span class="chip {CHIP[s][0]}">{CHIP[s][1]}</span> <b>{e(q)}</b><br><small>{e(n)}</small></li>' for q, s, n in items)
        out.append(f'<div class="card qcard"><h3>{e(title)}</h3><ul>{li}</ul></div>')
    return "\n".join(out)


rv_2026 = [r for r in reviews["reviews"] if r["date_created"].startswith("2026")]
leader = max(comp_rev, key=lambda c: c["reviews_2026_10_12"])
repl = {
    "{{LAST_RANGE}}": "28.09.–04.10.2026",
    "{{ACT_LAST}}": str(act(LAST)), "{{CALLS_LAST}}": str(LAST["calls"]), "{{WEB_LAST}}": str(LAST["web"]), "{{ROUTES_LAST}}": str(LAST["routes"]),
    "{{ACT_BASE}}": de(BASE_ACT), "{{VIEWS_LAST}}": str(LAST["views"]), "{{VIEWS_BASE}}": de(avg("views")),
    "{{REV_TOTAL}}": str(reviews["total_reviews"]), "{{REV_RATING}}": de(float(reviews["average_rating"]), 1), "{{REV_2026}}": str(len(rv_2026)),
    "{{REV_GAP}}": str(leader["reviews_2026_10_12"] - reviews["total_reviews"]),
    "{{LEADER_NAME}}": e(short(leader["name"])), "{{LEADER_REV}}": str(leader["reviews_2026_10_12"]),
    "{{FEE_MONTH}}": de(FEE_MONTH),
    "{{GBP_LINK}}": GBP_LINK,
    "{{SRC_GBP}}": src(GBP_LINK, "In deinem Google-Profil prüfen"),
    "{{SRC_MAPS}}": '<a class="srcl" href="#maps">Kartenbilder ↓</a>',
    "{{CHART}}": chart(), "{{COMP_TABLES}}": comp_tables(), "{{REVIEW_RACE}}": review_race(),
    "{{MAPS_ROWS}}": maps_rows(), "{{SERP_ROWS}}": serp_rows(), "{{GUARD_ROWS}}": guard_rows(), "{{QUARTER}}": quarter(),
    "{{SERP_COST}}": de(serp["cost_usd"], 2),
    "{{RAW_SNIPPET}}": e(json.dumps({"run_id": "dryrun-2026-10-12", "client": "praxis-suriya", "read_at": "2026-10-12", "data_until": "2026-10-09", "last_complete_week": LAST, "baseline": {"from": "2026-06-29", "to": "2026-09-27", "views_week_avg": round(avg("views"), 1), "contacts_week_avg": round(BASE_ACT, 1)}, "sources": ["Google-Profil Leistung", "Google-Bewertungen", "Maps-Messung 15./16.08.", "Google-Suche mobil 12.10."]}, ensure_ascii=False, indent=2)),
}
html = (HERE / "template.html").read_text()
for k, v in repl.items():
    html = html.replace(k, v)
assert "{{" not in html, [l for l in html.splitlines() if "{{" in l][:3]
out = HERE / "suriya-ergebnisse-prototype.html"
out.write_text(html)
# Martin guide: embed poses, CSS and JS so the file is self-contained (brand/martin-guide/inline.py)
import subprocess, sys
subprocess.run([sys.executable, str(HERE.parent.parent / "brand/martin-guide/inline.py"), str(out), str(out)], check=True)
print("written", out)
