#!/usr/bin/env python3
"""Sitemap step (checkpoint 2): build the sitetree from the content pool. Validate. Render HTML and xlsx.

Usage: build_sitetree.py --run-dir <content-pool dir>
Reads:  05-sitetree/tree.json (agent judgment: nodes, status, origin, module, job, pool_tag/pool_items, redirects, catchment),
        04-pool/pool.json, 02-competitors/site_urls.json, 05-sitetree/own-metrics.json,
        03-demand/gsc-pages-90d.tsv (optional), volume*.json via pool.json keywords, 03-demand/backlinks-*.json (optional)
Writes: 05-sitetree/sitetree.json, 05-report/content-pool-sitetree.html, 05-report/content-pool-sitetree.xlsx
Exit 1 when a rule fails. Rules (master prompt hard rules 2, 4, 6, 7, 8 plus pool rules):
  S1 every node has an origin (bestand, kunde, programm, vorschlag) and a status (Bleibt, Überarbeiten, Neu, Vorschlag)
  S2 Neu needs origin kunde or programm. Origin vorschlag (keyword or search chance only) must be status Vorschlag
  S3 Bleibt and Überarbeiten need an existing URL that is in the live sitemap
  S4 new slugs: lower case, start and end with "/"; a place in a slug needs a place:<slug> item in the pool
  S5 every pool item with priority A or B and page tag homepage, service:*, authority-page or blog-faq is on at least one node
  S6 no node carries an item that is cut
  S7 KPI counts equal the node counts
  S8 no duplicate path
"""
import argparse, glob, html, json, os, re, statistics
from urllib.parse import unquote, urlparse

H = html.escape
STATUS = ["Bleibt", "Überarbeiten", "Neu", "Vorschlag"]
ORIGIN = ["bestand", "kunde", "programm", "vorschlag"]


def norm_path(u):
    p = urlparse(u).path if "://" in u else u
    return unquote(p).rstrip("/") or "/"


def jl(p):
    return json.load(open(p)) if os.path.exists(p) else None


def gsc_pages(run):
    out = {}
    path = f"{run}/03-demand/gsc-pages-90d.tsv"
    if os.path.exists(path):
        for line in open(path):
            if line.startswith("#") or line.startswith("path\t") or not line.strip():
                continue
            p, c, i = line.rstrip("\n").split("\t")[:3]
            out[norm_path(p)] = (int(c), int(i))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    a = ap.parse_args()
    run = a.run_dir.rstrip("/")
    tree = jl(f"{run}/05-sitetree/tree.json")
    pool = jl(f"{run}/04-pool/pool.json")
    meta = tree["meta"]
    sites = jl(f"{run}/02-competitors/site_urls.json")[meta["domain"]]
    live_paths = {norm_path(u) for u in sites["urls"]}
    gsc = gsc_pages(run)
    own = {norm_path(m["url"]): m for m in (jl(f"{run}/05-sitetree/own-metrics.json") or []) if m.get("status") == "ok"}
    items = {i["id"]: i for i in pool["items"]}
    vol = {}
    for i in pool["items"]:
        for k in i["keywords"]:
            vol[k["kw"].lower()] = k["volume"]
    errs, warns = [], []
    nodes = tree["nodes"]
    ids = {n["id"] for n in nodes}
    seen_paths = {}
    assigned = set()
    for n in nodes:
        i = n["id"]
        if n["status"] not in STATUS: errs.append(f"{i}: bad status {n['status']}")
        if n["origin"] not in ORIGIN: errs.append(f"{i}: bad origin {n['origin']}")
        if n["status"] == "Neu" and n["origin"] not in ("kunde", "programm"): errs.append(f"{i}: Neu needs origin kunde or programm (S2)")
        if n["origin"] == "vorschlag" and n["status"] != "Vorschlag": errs.append(f"{i}: origin vorschlag must be status Vorschlag (S2)")
        if n.get("parent") and n["parent"] not in ids: errs.append(f"{i}: unknown parent")
        if n["kind"] != "group":
            p = n.get("path")
            if n["status"] in ("Bleibt", "Überarbeiten"):
                if not p: errs.append(f"{i}: {n['status']} needs path (S3)")
                elif norm_path(p) not in live_paths: errs.append(f"{i}: path {p} not in the live sitemap (S3)")
            slug = n.get("slug")
            if slug:
                if slug != slug.lower() or not (slug.startswith("/") and (slug.endswith("/") or slug.endswith(".html"))): errs.append(f"{i}: slug {slug} must be lower case, start with a slash and end with a slash or .html (S4)")
                places_ = [pl.lower() for pl in pool["meta"].get("places", [])]
                if any(pl and pl.replace("ü", "ue").replace("ö", "oe").replace("ä", "ae") in slug.replace("ü", "ue").replace("ö", "oe").replace("ä", "ae") or pl in slug for pl in places_) and not any(x["page_tag"].startswith("place:") for x in pool["items"] if x["priority"] != "cut"):
                    errs.append(f"{i}: place in slug without a place item in the pool (S4)")
            key = norm_path(p or slug or n["id"])
            if key in seen_paths: errs.append(f"{i}: duplicate path with {seen_paths[key]} (S8)")
            seen_paths[key] = i
        # collect pool items
        its = list(n.get("pool_items", []))
        if n.get("pool_tag"):
            its += [x["id"] for x in pool["items"] if x["page_tag"] == n["pool_tag"] and x["priority"] != "cut" and x["id"] not in n.get("pool_exclude", [])]
        n["_items"] = list(dict.fromkeys(its))
        for x in n["_items"]:
            if x not in items: errs.append(f"{i}: unknown pool item {x}")
            elif items[x]["priority"] == "cut": errs.append(f"{i}: carries cut item {x} (S6)")
            else: assigned.add(x)
    # S5 items not on a node
    must = [x for x in pool["items"] if x["priority"] in ("A", "B") and (x["page_tag"] in ("homepage", "authority-page", "blog-faq") or x["page_tag"].startswith("service:"))]
    unassigned = [x["id"] for x in must if x["id"] not in assigned]
    for u in unassigned: errs.append(f"pool item {u} is on no node (S5)")
    # numbers per node
    groups = {}
    for n in nodes:
        if n["kind"] == "group":
            pats = n["group_patterns"]
            hit = [u for u in live_paths if any(re.search(p, u) for p in pats)]
            n["_count"] = len(hit)
            n["_gsc"] = None
            continue
        p = norm_path(n["path"]) if n.get("path") else None
        g = gsc.get(p) if p else None
        if not gsc:
            n["_gsc"] = None  # no GSC data for this client: show nothing, never "not listed"
        elif meta.get("gsc_note") and not g:
            n["_gsc"] = None  # the page data is from another site version: one note for the whole report
        else:
            n["_gsc"] = {"clicks": g[0], "impressions": g[1]} if g else ({"clicks": None, "impressions": None, "note": "not listed in GSC (no impressions)"} if p else None)
        m = own.get(p) if p else None
        n["_words"] = m["words"] if m else None
        n["_schema"] = m["jsonld_types"] if m else None
        n["_kw"] = {"kw": n.get("kw"), "volume": vol.get(n["kw"].lower()) if n.get("kw") else None, "has_volume_record": (n.get("kw") or "").lower() in vol}
        n["_item_info"] = [{"id": x, "priority": items[x]["priority"], "topic": items[x]["topic"], "status": items[x]["status"]} for x in n["_items"] if x in items]
    # KPIs
    page_nodes = [n for n in nodes if n["kind"] != "group"]
    kpi = {s: sum(1 for n in page_nodes if n["status"] == s) for s in STATUS}
    if sum(kpi.values()) != len(page_nodes): errs.append("KPI sum differs from node count (S7)")
    patient = [n for n in page_nodes if n["audience"] in ("patient", "both")]
    kpi_patient = {s: sum(1 for n in patient if n["status"] == s) for s in STATUS}
    # reasons (data only)
    bl_files = sorted(f for f in glob.glob(f"{run}/03-demand/backlinks-*.json") if "payload" not in f)
    bl_doms = [os.path.basename(f)[len("backlinks-"):-len(".json")] for f in bl_files]
    bl_doms.sort(key=lambda d: (d != meta["domain"].replace("www.", ""), d))  # own domain first, then the others by name
    bl = {d: jl(f"{run}/03-demand/backlinks-{d}.json") for d in bl_doms}
    rd = {d: ((v["tasks"][0].get("result") or [{}])[0] or {}).get("referring_domains") for d, v in bl.items() if v}
    out = {"meta": meta, "kpi": kpi, "kpi_patient": kpi_patient, "nodes": [{k: v for k, v in n.items() if not k.startswith("_") or k in ("_items", "_gsc", "_words", "_kw", "_item_info", "_count", "_schema")} for n in nodes],
           "redirect_proposals": tree["redirect_proposals"], "catchment": tree["catchment"], "reasons": tree.get("reasons"), "not_built": tree.get("not_built", []), "referring_domains": rd, "unassigned_items": unassigned, "gsc_available": bool(gsc), "gsc_note": meta.get("gsc_note"),
           "benchmark": pool["meta"].get("benchmark")}
    # catchment volumes
    for c in out["catchment"]:
        c["volumes"] = {k: vol.get(k) for k in c["kw"]}
    json.dump(out, open(f"{run}/05-sitetree/sitetree.json", "w"), ensure_ascii=False, indent=1)
    # redirects numbers
    for r in out["redirect_proposals"]:
        g = gsc.get(norm_path(r["from"]))
        r["gsc"] = {"clicks": g[0], "impressions": g[1]} if g else None
    print(f"{len(nodes)} nodes | KPI {kpi} | patient KPI {kpi_patient} | {len(errs)} errors")
    for w in warns: print("WARN ", w)
    for e in errs: print("ERROR", e)
    render(out, pool, run)
    raise SystemExit(1 if errs else 0)


BADGE = {"Bleibt": "b-keep", "Überarbeiten": "b-rev", "Neu": "b-new", "Vorschlag": "b-sug"}
CSS = """
:root{--bg:#f7f6f2;--card:#fff;--ink:#1d2320;--mut:#66706b;--line:#dcd9cf;--acc:#2f5d50;--keep:#6b7280;--rev:#8a6d1f;--new:#2f5d50;--sug:#a23b3b}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#141816;--card:#1c211f;--ink:#e8ece9;--mut:#9aa5a0;--line:#2b322f;--acc:#7fc4ae;--keep:#9aa5a0;--rev:#d6b25a;--new:#7fc4ae;--sug:#e08585}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:1100px;margin:0 auto;padding:24px 16px 80px}h1{font-size:28px;margin:0 0 4px}h2{font-size:22px;margin:36px 0 10px;padding-top:8px;border-top:1px solid var(--line)}h3{font-size:17px;margin:18px 0 6px}
.sub{color:var(--mut);margin:0 0 14px}.mut{color:var(--mut)}.kpis{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0}.kpi{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 16px;min-width:120px}.kpi b{display:block;font-size:26px;line-height:1.1}
.tree{margin:8px 0 0;padding-left:0;list-style:none}.tree ul{list-style:none;margin:6px 0 6px 20px;padding-left:16px;border-left:2px solid var(--line)}
.node{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;margin:6px 0}.node.sug{border-style:dashed;border-color:var(--sug)}
.nh{display:flex;flex-wrap:wrap;gap:8px;align-items:center}.nt{font-weight:600;flex:1 1 280px}.badge{font-size:12px;font-weight:700;color:#fff;border-radius:4px;padding:1px 8px}.b-keep{background:var(--keep)}.b-rev{background:var(--rev)}.b-new{background:var(--new)}.b-sug{background:var(--sug)}
.tag{font-size:12px;border:1px solid var(--line);border-radius:4px;padding:1px 6px;background:var(--bg)}.url{font-family:ui-monospace,Menlo,monospace;font-size:13px;color:var(--acc)}
.job{margin:4px 0 2px}.facts{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:13px;color:var(--mut);margin-top:4px}.facts b{color:var(--ink)}
.chips{margin-top:6px;display:flex;flex-wrap:wrap;gap:4px}.chip{font-size:12px;border:1px solid var(--line);border-radius:999px;padding:1px 9px;background:var(--bg)}.chip i{font-style:normal;font-weight:700;margin-right:4px}
.need{color:#b45309;font-size:13px;margin-top:4px}table{border-collapse:collapse;width:100%;font-size:14px;background:var(--card)}th,td{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}th{background:var(--bg);font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--mut)}.tw{overflow-x:auto}
.note{background:var(--card);border:1px dashed var(--line);border-radius:8px;padding:10px 14px;margin:8px 0;font-size:14px}ol.r li{margin:6px 0}
"""


def fmt(v):
    return "no data" if v is None else f"{v:,}"


def render_node(n, kids):
    cls = "node sug" if n["status"] == "Vorschlag" else "node"
    loc = n.get("path") or n.get("slug") or ""
    facts = []
    if n["kind"] == "group":
        facts.append(f'<span><b>{n["_count"]}</b> URLs in the live sitemap</span>')
    else:
        k = n["_kw"]
        if k["kw"]: facts.append(f'<span>Keyword <b>{H(k["kw"])}</b> {("(" + fmt(k["volume"]) + ("" if k["volume"] is None else "/month") + ")") if k["has_volume_record"] else "(not in the volume data)"}</span>')
        g = n["_gsc"]
        if g and g["impressions"] is not None: facts.append(f'<span>GSC 3 months: <b>{g["clicks"]}</b> clicks, <b>{g["impressions"]:,}</b> impressions</span>')
        elif g: facts.append('<span>GSC: not listed (no impressions)</span>')
        if n["_words"] is not None: facts.append(f'<span><b>{n["_words"]:,}</b> words today</span>')
    chips = "".join(f'<span class="chip"><i>{c["priority"]}</i>{H(c["topic"])} <span class="mut">{c["id"]}</span></span>' for c in n.get("_item_info", []))
    needs = "".join(f'<div class="need">[FEHLT] {H(x)}</div>' for x in n.get("needs_client", []))
    note = f'<div class="mut">{H(n["note"])}</div>' if n.get("note") else ""
    s = f'<li><div class="{cls}"><div class="nh"><span class="nt">{H(n["title"])}</span><span class="badge {BADGE[n["status"]]}">{n["status"]}</span><span class="tag">{H(n["module"])}</span><span class="tag">origin: {n["origin"]}</span></div>'
    if loc: s += f'<div class="url">{H(loc)}{" (new)" if n.get("slug") else ""}</div>'
    s += f'<div class="job">{H(n["job"])}</div>{note}<div class="facts">{"".join(facts)}</div>{"<div class=chips>" + chips + "</div>" if chips else ""}{needs}</div>'
    if kids: s += "<ul>" + "".join(render_node(k, [x for x in kids_of(n["_all"], k["id"])]) for k in kids) + "</ul>"
    return s + "</li>"


def kids_of(nodes, pid):
    return [n for n in nodes if n.get("parent") == pid]


def render(out, pool, run):
    nodes = out["nodes"]
    for n in nodes: n["_all"] = nodes
    top = [n for n in nodes if not n.get("parent")]
    k, kp, b = out["kpi"], out["kpi_patient"], out.get("benchmark") or {}
    own_home = next((n for n in nodes if n["id"] == "ST-00"), {})
    rd = out["referring_domains"]
    h = [f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sitemap: {H(out["meta"]["client"])}</title><style>{CSS}</style></head><body><div class="wrap">']
    h.append(f'<h1>Sitemap: {H(out["meta"]["client"])}</h1><p class="sub">Built from the content pool of {H(out["meta"]["built"])}. Internal working document for Martin. Not the client report.</p>')
    h.append('<div class="kpis">' + "".join(f'<div class="kpi"><b>{k[s]}</b>{s}<br><span class="mut">patient site: {kp[s]}</span></div>' for s in STATUS) + f'<div class="kpi"><b>{len(out["redirect_proposals"])}</b>Redirect proposals</div></div>')
    if out.get("gsc_note"):
        h.append(f'<div class="note">{H(out["gsc_note"])}</div>')
    h.append('<p class="mut">Status: Bleibt = page stays as it is. Überarbeiten = URL stays, text new. Neu = new page with an origin in the client content or in the programme. Vorschlag = comes from search data only. Agree it with the client first (dashed card).</p>')
    if out.get("reasons"):
        svc = [n["_words"] for n in nodes if (n.get("pool_tag") or "").startswith("service:") and n.get("_words")]
        wmap = {n["id"]: n.get("_words") for n in nodes}

        def tok(m):
            k = m.group(1)
            if k == "home_words": return str(own_home.get("_words"))
            if k == "floor": return str(b.get("floor_70pct"))
            if k == "median": return f"{b.get('median_words'):g}"
            if k == "svc_min": return str(min(svc)) if svc else "?"
            if k == "svc_max": return str(max(svc)) if svc else "?"
            if k.startswith("words:"): return str(wmap.get(k.split(":", 1)[1]))
            if k == "rd": return ", ".join(f"{d} {v}" for d, v in rd.items())
            return m.group(0)

        h.append('<h2>Why the core topics are hard to find today</h2><ol class="r">')
        for r_ in out["reasons"]:
            h.append("<li>" + H(re.sub(r"\{([^}]+)\}", tok, r_)).replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>") + "</li>")
        h.append('</ol>')
    h.append('<h2>The tree</h2><ul class="tree">' + "".join(render_node(n, kids_of(nodes, n["id"])) for n in top) + '</ul>')
    h.append('<h2>Catchment (four levels)</h2><div class="tw"><table><tr><th>Level</th><th>Places</th><th>Search volume / month</th><th>Action</th></tr>')
    for c in out["catchment"]:
        v = ", ".join(f'{H(k2)} {fmt(v2)}' for k2, v2 in c["volumes"].items()) or "none"
        h.append(f'<tr><td>{c["level"]} {H(c["name"])}</td><td>{H(", ".join(c["places"])) or "none"}</td><td>{v}</td><td>{H(c["action"])}</td></tr>')
    h.append('</table></div><p class="mut">Rule: a place page needs demand, a catchment signal and unique local facts. No place passes all three today. "no data" means the volume tool has no record, not zero demand.</p>')
    h.append('<h2>Redirect proposals (client must agree)</h2>')
    if not out["redirect_proposals"]:
        h.append('<p class="mut">None. One candidate pair was checked: /ernaehrungstherapie-hildegard-von-bingen is a training page (Course markup, "Kurs buchen"), not a duplicate of /ernährungsberatung. It stays in the Viriditas area.</p>')
    else:
        h.append('<div class="tw"><table><tr><th>From</th><th>To</th><th>GSC today</th><th>Why</th></tr>')
    for r in out["redirect_proposals"]:
        g = r.get("gsc"); gt = f'{g["clicks"]} clicks, {g["impressions"]} impressions' if g else ("not listed" if out.get("gsc_available") else "no GSC data")
        h.append(f'<tr><td class="url">{H(r["from"])}</td><td class="url">{H(r["to"])}</td><td>{gt}</td><td>{H(r["reason"])}</td></tr>')
    if out["redirect_proposals"]:
        h.append('</table></div>')
    if out.get("not_built"):
        h.append('<h2>Not built, and why</h2><ul>' + "".join(f"<li>{H(x)}</li>" for x in out["not_built"]) + '</ul>')
    open_needs = [(n["title"], x) for n in nodes for x in n.get("needs_client", [])]
    if open_needs:
        h.append('<h2>Open facts that block nodes</h2><ul>' + "".join(f"<li>{H(t)}: {H(x)}</li>" for t, x in open_needs) + '</ul>')
    h.append('<h2>Programme link</h2><p class="mut">Module tags come from the structure master prompt: M2 Startseite, M5 Standort- und Leistungsseiten, M6 Behandlerseite, M8 Hub und Spoke, M10 Online-Angebote und Conversion. The programme plan file was not found under ~/Downloads. Check the tags against the plan.</p>')
    h.append('</div></body></html>')
    os.makedirs(f"{run}/05-report", exist_ok=True)
    open(f"{run}/05-report/content-pool-sitetree.html", "w").write("\n".join(h))
    # xlsx
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
    from openpyxl.utils import get_column_letter
    wb = Workbook(); ws = wb.active; ws.title = "Sitetree"
    hdr = ["ID", "Parent", "Page", "Status", "Origin", "Module", "URL (existing or new)", "Audience", "Job", "Keyword", "Searches / month", "GSC clicks", "GSC impressions", "Words today", "Pool items", "Needs from client", "Note"]
    ws.append(hdr)
    fills = {"Bleibt": "E7E7E7", "Überarbeiten": "F6EBC8", "Neu": "D6EBDD", "Vorschlag": "F3D3D3"}
    for n in nodes:
        g = n.get("_gsc") or {}
        kw = n.get("_kw") or {}
        ws.append([n["id"], n.get("parent") or "", n["title"], n["status"], n["origin"], n["module"], n.get("path") or n.get("slug") or "", n["audience"], n["job"], kw.get("kw") or "", kw.get("volume") if kw.get("has_volume_record") else ("not in data" if kw.get("kw") else ""), g.get("clicks"), g.get("impressions"), n.get("_words"), ", ".join(n.get("_items", [])), "; ".join(n.get("needs_client", [])), n.get("note") or ""])
    head = PatternFill("solid", fgColor="2F5D50"); thin = Side(style="thin", color="DDDDDD")
    for c in ws[1]: c.fill, c.font, c.alignment = head, Font(bold=True, color="FFFFFF"), Alignment(wrap_text=True, vertical="center")
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = Alignment(wrap_text=True, vertical="top"); c.border = Border(top=thin, bottom=thin, left=thin, right=thin)
        row[3].fill = PatternFill("solid", fgColor=fills[row[3].value])
    for i, w in enumerate([8, 8, 40, 13, 10, 18, 40, 9, 60, 30, 12, 9, 12, 10, 40, 40, 50], 1): ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "D2"; ws.auto_filter.ref = ws.dimensions
    wb.save(f"{run}/05-report/content-pool-sitetree.xlsx")


if __name__ == "__main__":
    main()
