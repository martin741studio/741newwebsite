#!/usr/bin/env python3
"""Render the internal one-page board (self-contained HTML).
Usage: python3 -I render_board.py <catalog.json> <matrix.json> <tasks.json> <out.html> [conflicts.json]
conflicts.json (optional): ["text", ...] source conflicts and evidence gaps for the conflict box.
Layout: 00_project/maps-playbook-report-wireframe.md"""
import json, sys, html, datetime

LAB = {"done": "Erledigt", "partly": "Teilweise", "missing": "Fehlt", "n/a": "Nicht relevant", "unknown": "Unbekannt"}
COL = {"done": ("#C6EFCE", "#0B6623"), "partly": ("#FFEB9C", "#7F6000"), "missing": ("#FFC7CE", "#9C0006"),
       "n/a": ("#E7E6E6", "#595959"), "unknown": ("#DDEBF7", "#1F4E79")}
e = html.escape

def main(cat_p, mat_p, task_p, out_p, conf_p=None):
    cat = json.load(open(cat_p, encoding="utf-8")); mat = json.load(open(mat_p, encoding="utf-8")); tk = json.load(open(task_p, encoding="utf-8"))
    conflicts = json.load(open(conf_p, encoding="utf-8")) if conf_p else []
    cm = {m["id"]: m for m in cat["measures"]}; rows = {r["id"]: r for r in mat["rows"]}
    tot = len(rows); cnt = {k: sum(1 for r in rows.values() if r["status"] == k) for k in LAB}
    gaps = cnt["missing"] + cnt["partly"] + cnt["unknown"]
    fresh = sum(1 for r in rows.values() if r["status"] != "unknown" and not r.get("stale"))
    gates_open = sum(1 for i, r in rows.items() if cm[i]["risk_class"] == "GATE" and r["status"] in ("missing", "partly", "unknown"))
    blocked = sum(1 for t in tk["tasks"] if t["state"] == "blocked")
    as_of = mat["as_of"]
    def bar(ids):
        c = {k: sum(1 for i in ids if rows[i]["status"] == k) for k in LAB}; n = len(ids)
        segs = "".join(f'<span class="seg" style="width:{100*c[k]/n:.2f}%;background:{COL[k][0]};color:{COL[k][1]}" title="{LAB[k]} {c[k]}">{c[k] if c[k] else ""}</span>' for k in LAB if c[k])
        rel = n - c["n/a"]; share = c["done"] / rel if rel else 1
        lamp = "g" if share >= .75 else "y" if share >= .4 else "r"
        return f'<div class="bar">{segs}</div>', lamp, share
    pil_html = ""
    for pil in cat["pillars"]:
        ms = [m for m in cat["measures"] if m["pillar"] == pil]
        b, lamp, sh = bar([m["id"] for m in ms])
        groups = []
        for m in ms:
            if m["group"] not in groups: groups.append(m["group"])
        sub = ""
        for g in groups:
            gb, gl, _ = bar([m["id"] for m in ms if m["group"] == g])
            sub += f'<div class="grow"><span class="gname">{e(g)}</span>{gb}<i class="lamp {gl}"></i></div>'
        pil_html += f'<div class="pillar"><div class="phead"><b>{e(pil)}</b><span>{round(100*sh)} % erledigt</span><i class="lamp {lamp}"></i></div>{b}<div class="groups">{sub}</div></div>'
    top = [t for t in tk["tasks"] if t["state"] != "blocked"][:5]
    top_html = "".join(f'<tr><td class="rk">{t["rank"]}</td><td><b>{t["measure_id"]}</b> {e(t["label_de"])}</td><td>{e(t["action_text"])}</td><td>{e(",".join(t["gate"]) or "–")}</td><td>{e("+".join(t["owner_type"]))}</td><td>{t["score"]}</td><td>{t["phase"]}</td></tr>' for t in top)
    stale = [i for i, r in rows.items() if r.get("stale")]
    cbox = "".join(f"<li>{e(c)}</li>" for c in conflicts)
    if stale: cbox += f"<li>{len(stale)} Zellen sind veraltet (Beweis älter als die Alterregel): {e(', '.join(stale[:12]))}{' …' if len(stale) > 12 else ''}</li>"
    if not cbox: cbox = "<li>Keine Konflikte gefunden.</li>"
    # pillar views
    views = ""
    for pil in cat["pillars"]:
        trs = ""; cur = None
        for m in [m for m in cat["measures"] if m["pillar"] == pil]:
            r = rows[m["id"]]
            if m["group"] != cur:
                cur = m["group"]; trs += f'<tr class="gh"><td colspan="8">{e(cur)}</td></tr>'
            ev = r.get("evidence", [])
            evh = "".join(f'<div class="ev"><span class="t {e(x["type"])}">{e(x["type"])}</span> {e(x["ref"])} · {e(x["date"][:10])}<br><small>{e(x.get("note",""))}</small></div>' for x in ev) or "<div class='ev'>kein Beweis</div>"
            bg, fg = COL[r["status"]]
            stale_i = ' <span title="veraltet">🕓</span>' if r.get("stale") else ""
            gate = f'<span class="gate" title="{e(m["gate_text"])}">Gate {e(",".join(m["gates"]))}</span>' if m["risk_class"] != "DO" else ""
            trs += (f'<tr data-st="{r["status"]}" data-cl="{m["risk_class"]}"><td class="id">{m["id"]}</td><td>{e(m["label_de"])}</td>'
                    f'<td><span class="chip" style="background:{bg};color:{fg}">{LAB[r["status"]]}</span>{stale_i}</td><td>{e(r["finding_de"])}</td>'
                    f'<td><details><summary>{len(ev)} Beweis</summary>{evh}</details></td><td>{gate} <span class="cl {m["risk_class"]}">{m["risk_class"]}</span></td>'
                    f'<td>{e(", ".join(r.get("blocked_by") or []) if (r.get("blocked_by") and r["blocked_by"] != ["none"]) else "–")}</td><td>{e(r.get("task_hint") or "–")}</td></tr>')
        views += f'<section id="v-{pil[:2]}"><h2>{e(pil)}</h2><table><thead><tr><th>ID</th><th>Maßnahme</th><th>Status</th><th>Befund</th><th>Evidenz</th><th>Klasse</th><th>Blocker</th><th>Nächste Aufgabe</th></tr></thead><tbody>{trs}</tbody></table></section>'
    tt = "".join(f'<tr class="{"bl" if t["state"]=="blocked" else ""}"><td>{t["rank"]}</td><td><b>{t["measure_id"]}</b> {e(t["label_de"])}</td><td>{e(t["action_text"])}</td><td>{e("+".join(t["owner_type"]))}</td><td>{t["impact"]}</td><td>{t["confidence"]}</td><td>{t["effort"]}</td><td>{t["risk"]}</td><td><b>{t["score"]}</b></td><td>{t["phase"]}</td><td>{e(", ".join(t["depends_on"]+t["blocked_by"]) or "–")}</td><td>{t["state"]}</td></tr>' for t in tk["tasks"])
    page = f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Maps-Playbook {e(mat['client'])}</title>
<style>
:root{{--bg:#F6F6F4;--card:#fff;--ink:#1A1A1A;--mut:#6B6B6B;--line:#E2E2DE;--y:#FAC118;--yl:#FFF4CC}}
@media (prefers-color-scheme:dark){{:root{{--bg:#151515;--card:#1F1F1F;--ink:#F2F2F2;--mut:#A8A8A8;--line:#333;--yl:#3A3210}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 "DM Sans",system-ui,-apple-system,Segoe UI,Arial,sans-serif}}
.wrap{{max-width:1360px;margin:0 auto;padding:20px 16px 60px}}
header.top{{background:var(--y);color:#1A1A1A;border-radius:10px;padding:14px 20px;display:flex;gap:18px;align-items:baseline;flex-wrap:wrap}}
header.top h1{{margin:0;font:700 22px "Anton","DM Sans",sans-serif;letter-spacing:.5px;text-transform:uppercase}}header.top span{{font-size:13px}}
.tiles{{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin:14px 0}}
.tile{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px}}
.tile b{{display:block;font:400 34px/1.1 "Anton","DM Sans",sans-serif}}.tile span{{color:var(--mut);font-size:12px}}
.tile.y{{background:var(--yl);border-color:var(--y)}}
h2{{font-size:15px;margin:22px 0 8px;text-transform:uppercase;letter-spacing:.6px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px}}
.pillars{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}}
.phead{{display:flex;gap:10px;align-items:center;margin-bottom:8px}}.phead span{{color:var(--mut);font-size:12px;margin-left:auto}}
.bar{{display:flex;height:22px;border-radius:5px;overflow:hidden;background:var(--line);min-width:60px;flex:1}}
.seg{{font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center}}
.groups{{margin-top:10px;display:grid;gap:6px}}.grow{{display:flex;gap:8px;align-items:center}}.gname{{width:150px;font-size:12px;color:var(--mut);flex:none}}
.grow .bar{{height:14px}}.lamp{{display:inline-block;width:11px;height:11px;border-radius:50%;flex:none}}.lamp.g{{background:#2e9e4f}}.lamp.y{{background:#e0a800}}.lamp.r{{background:#d64545}}
table{{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden;font-size:13px}}
th{{background:#1A1A1A;color:#fff;text-align:left;padding:8px 10px;font-size:12px;position:sticky;top:0}}td{{padding:7px 10px;border-top:1px solid var(--line);vertical-align:top}}
tr.gh td{{background:var(--yl);font-weight:700}}td.id,td.rk{{font-weight:700;white-space:nowrap}}
.chip{{display:inline-block;padding:2px 9px;border-radius:12px;font-weight:700;font-size:12px;white-space:nowrap}}
.gate{{background:#F8CBAD;color:#7A3B14;border-radius:4px;padding:1px 6px;font-size:11px;font-weight:700;cursor:help}}
.cl{{font-size:11px;font-weight:700;padding:1px 6px;border-radius:4px}}.cl.DO{{background:#C6EFCE;color:#0B6623}}.cl.GATE{{background:#F8CBAD;color:#7A3B14}}.cl.OUT{{background:#D9D9D9;color:#444}}
details summary{{cursor:pointer;color:var(--mut)}}.ev{{margin:6px 0;font-size:12px;max-width:320px;word-break:break-word}}.t{{font-weight:700;padding:0 5px;border-radius:3px;background:var(--line)}}
ul.conf{{margin:0;padding-left:18px}}ul.conf li{{margin:4px 0}}
.chips{{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0}}.fc{{border:1px solid var(--line);background:var(--card);color:var(--ink);padding:3px 12px;border-radius:14px;cursor:pointer;font:inherit;font-size:12px}}.fc.on{{background:var(--y);border-color:var(--y);color:#1A1A1A;font-weight:700}}
tr.bl td{{color:var(--mut);background:rgba(128,128,128,.08)}}
.cp{{display:flex;gap:14px;align-items:center}}.cp .btn{{background:var(--y);color:#1A1A1A;border-radius:6px;padding:7px 14px;font-weight:700}}
@media (max-width:900px){{.tiles{{grid-template-columns:repeat(2,1fr)}}.pillars{{grid-template-columns:1fr}}table{{display:block;overflow-x:auto}}}}
</style></head><body><div class="wrap">
<header class="top"><h1>Maps-Playbook · {e(mat['client'])}</h1><span>Stand {as_of} · Katalog {e(cat['catalog_version'])} · Modus {e(mat.get('mode','dry run'))} · intern</span></header>
<div class="tiles">
<div class="tile y"><b>{round(100*cnt['done']/tot)} %</b><span>Erledigt ({cnt['done']} von {tot})</span></div>
<div class="tile"><b>{gaps}</b><span>Lücken (fehlt {cnt['missing']}, teilweise {cnt['partly']}, unbekannt {cnt['unknown']})</span></div>
<div class="tile"><b>{round(100*fresh/tot)} %</b><span>Frische Evidenz</span></div>
<div class="tile"><b>{gates_open}</b><span>Gates offen</span></div>
<div class="tile"><b>{blocked}</b><span>Aufgaben blockiert</span></div></div>
<h2>Säulen und Gruppen</h2><div class="pillars">{pil_html}</div>
<h2>Top 5 nächste Aufgaben</h2><table><thead><tr><th>#</th><th>Maßnahme</th><th>Aktion</th><th>Gate</th><th>Wer</th><th>Prio</th><th>Phase</th></tr></thead><tbody>{top_html}</tbody></table>
<h2>Konflikte und Lücken im Beweis</h2><div class="card"><ul class="conf">{cbox}</ul></div>
<h2>Checkpoint A</h2><div class="card cp"><span>Korrekturen: <b>0</b></span><span class="btn">Freigabe für den Aufgaben-Plan</span><span style="color:var(--mut)">Martin liest Seite 1 und sagt „go“.</span></div>
<h2>Maßnahmen je Säule</h2><div class="chips" id="chips"></div>{views}
<h2>Aufgaben</h2><table><thead><tr><th>#</th><th>Maßnahme</th><th>Aktion</th><th>Wer</th><th>Impact</th><th>Konf.</th><th>Aufw.</th><th>Risiko</th><th>Prio</th><th>Phase</th><th>Abhängig / Blocker</th><th>Status</th></tr></thead><tbody>{tt}</tbody></table>
</div><script>
(function(){{var f={{st:null,cl:null}};var box=document.getElementById('chips');
var defs=[['st','done','Erledigt'],['st','partly','Teilweise'],['st','missing','Fehlt'],['st','unknown','Unbekannt'],['st','n/a','Nicht relevant'],['cl','GATE','Gate'],['cl','OUT','OUT']];
defs.forEach(function(d){{var b=document.createElement('button');b.className='fc';b.textContent=d[2];b.onclick=function(){{f[d[0]]=f[d[0]]===d[1]?null:d[1];apply()}};b.dataset.k=d[0]+':'+d[1];box.appendChild(b)}});
function apply(){{document.querySelectorAll('tbody tr[data-st]').forEach(function(r){{var ok=(!f.st||r.dataset.st===f.st)&&(!f.cl||r.dataset.cl===f.cl);r.style.display=ok?'':'none'}});
box.querySelectorAll('.fc').forEach(function(b){{var p=b.dataset.k.split(':');b.classList.toggle('on',f[p[0]]===p[1])}})}}}})();
</script></body></html>"""
    open(out_p, "w", encoding="utf-8").write(page)
    print("wrote", out_p, len(page), "bytes")

if __name__ == "__main__":
    main(*sys.argv[1:6])
