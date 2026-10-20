#!/usr/bin/env python3
"""Build the client matrix workbook (XlsxWriter, never openpyxl).
Usage: <venv>/bin/python build_sheet.py <catalog.json> <matrix.json> <tasks.json> <out.xlsx> [client-label]
Design: 00_project/maps-playbook-sheet-design.md"""
import json, sys, datetime
import xlsxwriter

LAB = {"done": "Erledigt", "partly": "Teilweise", "missing": "Fehlt", "n/a": "Nicht relevant", "unknown": "Unbekannt"}
FILL = {"Erledigt": ("#C6EFCE", "#0B6623"), "Teilweise": ("#FFEB9C", "#7F6000"), "Fehlt": ("#FFC7CE", "#9C0006"),
        "Nicht relevant": ("#E7E6E6", "#595959"), "Unbekannt": ("#DDEBF7", "#1F4E79")}
TABS = [("01 P1 Google-Profil", "P1 Google-Profil"), ("02 P2 Website", "P2 Website"), ("03 P3 Off-Page", "P3 Off-Page")]

def main(cat_p, mat_p, task_p, out_p, label=None):
    cat = json.load(open(cat_p, encoding="utf-8")); mat = json.load(open(mat_p, encoding="utf-8"))
    tk = json.load(open(task_p, encoding="utf-8"))
    cm = {m["id"]: m for m in cat["measures"]}; rows = {r["id"]: r for r in mat["rows"]}
    wb = xlsxwriter.Workbook(out_p)
    F = lambda **k: wb.add_format({**dict(font_name="Arial", font_size=10, valign="top"), **k})
    title = F(bold=True, font_size=14, bg_color="#FAC118", font_color="#1A1A1A", valign="vcenter")
    hdr = F(bold=True, bg_color="#1A1A1A", font_color="#FFFFFF", border=1, text_wrap=True, valign="vcenter")
    grp = F(bold=True, bg_color="#F2F2F2", border=1)
    cell = F(border=1, text_wrap=True); cellz = F(border=1, text_wrap=True, bg_color="#FAFAFA")
    bold = F(border=1, bold=True)
    date = F(border=1, num_format="dd.mm.yyyy"); num = F(border=1, num_format="0.0")
    sf = {k: F(border=1, bg_color=v[0], font_color=v[1], bold=True) for k, v in FILL.items()}
    cls_f = {"DO": F(border=1, bg_color="#C6EFCE"), "GATE": F(border=1, bg_color="#F8CBAD"), "OUT": F(border=1, bg_color="#D9D9D9")}
    as_of = datetime.date.fromisoformat(mat["as_of"])
    client = label or mat["client"]
    counts = {k: sum(1 for r in rows.values() if r["status"] == k) for k in LAB}

    # ---- 00 Übersicht
    ws = wb.add_worksheet("00 Übersicht"); ws.hide_gridlines(2); ws.set_column("A:A", 3); ws.set_column("B:H", 22)
    ws.merge_range("B1:H1", f"Maps-Playbook {client} · Stand {as_of.strftime('%d.%m.%Y')} · Katalog {cat['catalog_version']}", title); ws.set_row(0, 30)
    tot = len(rows); gaps = counts["missing"] + counts["partly"] + counts["unknown"]
    fresh = sum(1 for r in rows.values() if not r.get("stale") and r["status"] != "unknown")
    big = F(bold=True, font_size=20, bg_color="#FAC118", align="center", valign="vcenter", border=1)
    cap = F(font_size=9, align="center", border=1, bg_color="#FFF4CC", valign="vcenter")
    for c, (n, t) in zip("BDF", [(f"{round(100*counts['done']/tot)} %", "Erledigt"), (str(gaps), "Lücken (fehlt, teilweise, unbekannt)"), (f"{round(100*fresh/tot)} %", "Frische Evidenz")]):
        ws.merge_range(f"{c}3:{chr(ord(c)+1)}4", n, big); ws.merge_range(f"{c}5:{chr(ord(c)+1)}5", t, cap)
    ws.set_row(2, 26); ws.set_row(3, 26)
    r0 = 7
    for j, h in enumerate(["Säule / Gruppe", "Erledigt", "Teilweise", "Fehlt", "Nicht relevant", "Unbekannt", "Ampel"]):
        ws.write(r0, 1 + j, h, hdr)
    r = r0 + 1
    green = F(border=1, bg_color="#C6EFCE", bold=True, align="center"); yel = F(border=1, bg_color="#FFEB9C", bold=True, align="center"); red = F(border=1, bg_color="#FFC7CE", bold=True, align="center")
    for tab, pil in TABS:
        ms = [m for m in cat["measures"] if m["pillar"] == pil]
        groups = []
        for m in ms:
            if m["group"] not in groups: groups.append(m["group"])
        ws.write(r, 1, pil, grp); [ws.write(r, c, "", grp) for c in range(2, 8)]; r += 1
        for g in groups:
            gm = [m["id"] for m in ms if m["group"] == g]
            c = {k: sum(1 for i in gm if rows[i]["status"] == k) for k in LAB}
            rel = len(gm) - c["n/a"]; share = (c["done"] / rel) if rel else 1
            f, tx = (green, "●") if share >= .75 else (yel, "●") if share >= .4 else (red, "●")
            ws.write(r, 1, "   " + g, cell)
            for j, k in enumerate(["done", "partly", "missing", "n/a", "unknown"]): ws.write(r, 2 + j, c[k], cell)
            ws.write(r, 7, tx, f); r += 1
    r += 1
    ws.merge_range(r, 1, r, 7, "Top 5 nächste Aufgaben", title); r += 1
    for j, h in enumerate(["Rang", "Maßnahme", "Aktion", "Gate", "Wer", "Aufwand", "Phase"]): ws.write(r, 1 + j, h, hdr)
    r += 1
    ws.set_column("D:D", 38)
    top = [t for t in tk["tasks"] if t["state"] != "blocked"][:5]
    for t in top:
        for j, v in enumerate([t["rank"], f"{t['measure_id']} {t['label_de']}", t["action_text"], ",".join(t["gate"]) or "-", "+".join(t["owner_type"]), {1: "S", 2.5: "M", 4.5: "L"}.get(t["effort"], "S"), t["phase"]]):
            ws.write(r, 1 + j, v, cell)
        ws.set_row(r, 42); r += 1
    r += 1
    ws.merge_range(r, 1, r, 7, "Blockiert", title); r += 1
    for t in [t for t in tk["tasks"] if t["state"] == "blocked"][:8]:
        ws.write(r, 1, t["measure_id"], cell); ws.merge_range(r, 2, r, 4, t["label_de"], cell)
        ws.merge_range(r, 5, r, 7, "wartet auf: " + ", ".join(t["depends_on"] + t["blocked_by"]), cell); r += 1
    # ---- pillar tabs
    heads = [("ID", 7), ("Gruppe", 20), ("Maßnahme", 34), ("Status", 14), ("Befund", 52), ("Evidenz", 26), ("Datum", 11), ("Alter (Tage)", 9),
             ("Frisch?", 9), ("Konfidenz", 13), ("Klasse", 9), ("Gate", 8), ("Blocker", 16), ("Nächste Aufgabe", 40), ("Prio", 8), ("Phase", 9)]
    prio = {t["measure_id"]: t["score"] for t in tk["tasks"]}
    for tab, pil in TABS:
        ws = wb.add_worksheet(tab); ws.hide_gridlines(2)
        for j, (h, w) in enumerate(heads): ws.set_column(j, j, w)
        ws.merge_range(0, 0, 0, len(heads) - 1, f"{pil} · {client} · Stand {as_of.strftime('%d.%m.%Y')}", title); ws.set_row(0, 28)
        for j, (h, w) in enumerate(heads): ws.write(1, j, h, hdr)
        ws.set_row(1, 28); ws.freeze_panes(2, 3)
        r = 2; cur = None; z = False
        for m in [m for m in cat["measures"] if m["pillar"] == pil]:
            if m["group"] != cur:
                cur = m["group"]; ws.merge_range(r, 0, r, len(heads) - 1, cur, grp); r += 1
            rw = rows[m["id"]]; z = not z; base = cellz if z else cell
            ev = rw.get("evidence", [])
            first = ev[0] if ev else None
            ev_label = (first["type"] + ": " + first["ref"].split("/")[-1][:40]) if first else "-"
            newest = max((datetime.date.fromisoformat(e["date"][:10]) for e in ev), default=None)
            age = (as_of - newest).days if newest else None
            vals = [m["id"], m["group"], m["label_de"], LAB[rw["status"]], rw["finding_de"], None, newest, age,
                    "Nein" if rw.get("stale") else ("Ja" if ev else "-"), rw.get("confidence", "none"), m["risk_class"],
                    ",".join(m["gates"]) or "-", ", ".join(rw.get("blocked_by") or []) or "-", rw.get("task_hint") or "-", prio.get(m["id"]), m["phase"]]
            for j, v in enumerate(vals):
                if j == 3: ws.write(r, j, v, sf[v])
                elif j == 5:
                    ref = first["ref"] if first else ""
                    if ref.startswith("http"): ws.write_url(r, j, ref, base, string=ev_label)
                    else: ws.write(r, j, ev_label, base)
                elif j == 6:
                    if v: ws.write_datetime(r, j, datetime.datetime.combine(v, datetime.time()), date)
                    else: ws.write(r, j, "", base)
                elif j == 10: ws.write(r, j, v, cls_f[v])
                elif j == 14:
                    if v is None: ws.write(r, j, "", base)
                    else: ws.write_number(r, j, v, num)
                elif j == 0: ws.write(r, j, v, bold)
                else: ws.write(r, j, "" if v is None else v, base)
            ws.set_row(r, 44); r += 1
        last = r - 1
        ws.data_validation(2, 3, last, 3, {"validate": "list", "source": list(LAB.values())})
        ws.data_validation(2, 9, last, 9, {"validate": "list", "source": ["verified", "derived", "client_stated", "none"]})
        ws.data_validation(2, 15, last, 15, {"validate": "list", "source": ["d1-30", "m2+", "later"]})
        ws.conditional_format(2, 14, last, 14, {"type": "3_color_scale", "min_color": "#FFFFFF", "mid_color": "#FFF2CC", "max_color": "#FAC118"})
        ws.conditional_format(2, 8, last, 8, {"type": "cell", "criteria": "==", "value": '"Nein"', "format": wb.add_format({"font_color": "#9C0006", "bold": True})})
        ws.autofilter(1, 0, last, len(heads) - 1)
    # ---- tasks
    ws = wb.add_worksheet("04 Aufgaben"); ws.hide_gridlines(2)
    th = [("Rang", 6), ("ID", 7), ("Maßnahme", 32), ("Aktion", 50), ("Wer", 16), ("Aufwand", 9), ("Risiko", 8), ("Gate", 8), ("Prio", 8), ("Impact", 8),
          ("Konfidenz", 10), ("Phase", 9), ("Abhängig von", 16), ("Status", 12), ("Batch", 8), ("Freigabe Kunde", 12), ("Go Martin", 10)]
    for j, (h, w) in enumerate(th): ws.set_column(j, j, w)
    ws.merge_range(0, 0, 0, len(th) - 1, f"Aufgaben {client} · Stand {as_of.strftime('%d.%m.%Y')}", title); ws.set_row(0, 28)
    for j, (h, w) in enumerate(th): ws.write(1, j, h, hdr)
    ws.freeze_panes(2, 3); grey = F(border=1, text_wrap=True, bg_color="#EDEDED", font_color="#7F7F7F")
    for k, t in enumerate(tk["tasks"]):
        rr = 2 + k; f = grey if t["state"] == "blocked" else cell
        vals = [t["rank"], t["measure_id"], t["label_de"], t["action_text"], "+".join(t["owner_type"]), {1: "S", 2.5: "M", 4.5: "L"}.get(t["effort"], "S"), t["risk"],
                ",".join(t["gate"]) or "-", t["score"], t["impact"], t["confidence"], t["phase"], ", ".join(t["depends_on"] + t["blocked_by"]) or "-", t["state"], "", "", ""]
        for j, v in enumerate(vals): ws.write(rr, j, v, f)
        ws.set_row(rr, 36)
    last = 1 + len(tk["tasks"])
    ws.data_validation(2, 13, last, 13, {"validate": "list", "source": cat["task_states"]})
    ws.data_validation(2, 15, last, 16, {"validate": "list", "source": ["Ja"]})
    ws.autofilter(1, 0, last, len(th) - 1)
    # ---- evidence
    ws = wb.add_worksheet("05 Evidenz"); ws.hide_gridlines(2)
    eh = [("Typ", 10), ("Referenz", 60), ("Datum", 11), ("Alter", 8), ("Regel (Tage)", 11), ("Stützt Maßnahmen", 40), ("Notiz", 50)]
    for j, (h, w) in enumerate(eh): ws.set_column(j, j, w)
    ws.merge_range(0, 0, 0, len(eh) - 1, "Evidenz-Index", title); ws.set_row(0, 28)
    for j, (h, w) in enumerate(eh): ws.write(1, j, h, hdr)
    idx = {}
    for i, rw in rows.items():
        for e in rw.get("evidence", []):
            k = (e["type"], e["ref"], e["date"][:10]); idx.setdefault(k, {"ids": [], "note": e.get("note", "")})["ids"].append(i)
    for n, ((ty, ref, dt), v) in enumerate(sorted(idx.items(), key=lambda x: x[0][2], reverse=True)):
        dd = datetime.date.fromisoformat(dt)
        for j, val in enumerate([ty, ref, None, (as_of - dd).days, cat["age_rules_days"][ty], ", ".join(v["ids"]), v["note"]]):
            if j == 2: ws.write_datetime(2 + n, j, datetime.datetime.combine(dd, datetime.time()), date)
            else: ws.write(2 + n, j, val, cell)
    ws.freeze_panes(2, 0)
    # ---- legend
    ws = wb.add_worksheet("99 Legende"); ws.hide_gridlines(2); ws.set_column("A:A", 20); ws.set_column("B:B", 90)
    ws.merge_range("A1:B1", "Legende", title); ws.set_row(0, 28)
    leg = [("Erledigt", "In place. Evidence is fresh."), ("Teilweise", "A part is in place. The finding names what is missing."), ("Fehlt", "Not in place."),
           ("Nicht relevant", "Not relevant. The finding names the reason."), ("Unbekannt", "No data, or evidence older than the age rule. Never a guess."),
           ("Alter-Regeln", "live 30 Tage, scan 60 Tage, document 180 Tage."), ("Klasse", "DO = do. GATE = only after a gate. OUT = out of scope."),
           ("Konfidenz", "verified = read from source in the rule. derived = computed. client_stated = told, no proof (never sets Erledigt)."),
           ("Prio", "impact x confidence / (effort + risk)."), ("Katalog", f"Version {cat['catalog_version']}.")]
    for g, tx in cat["gates"].items(): leg.append((f"Gate {g}", tx))
    for k, (a, b) in enumerate(leg, 2):
        ws.write(k, 0, a, bold if a in LAB.values() else cell); ws.write(k, 1, b, cell)
    wb.close()
    print("wrote", out_p)

if __name__ == "__main__":
    main(*sys.argv[1:6])
