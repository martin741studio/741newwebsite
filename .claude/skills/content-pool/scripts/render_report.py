#!/usr/bin/env python3
"""Render the content pool report: one self-contained HTML file and one formatted xlsx.

Usage: render_report.py --run-dir <content-pool dir>
Reads:  04-pool/pool.json, 04-pool/summary.json, 02-competitors/metrics.json, spend.jsonl
Writes: 05-report/content-pool-report.html, 05-report/content-pool.xlsx

Reading order in the HTML (Martin, 2026-10-11): findings first, one summary card per pillar,
then the homepage map (CRO rows), then detail per pillar, then open client facts, then raw data links.
summary.json tokens: {bench.own} {bench.floor} {bench.median} {bench.n} {spend} {n_items} {<ID>.cov}.
"""
import argparse, html, json, os, re

PRIO_ORDER = {"A": 0, "B": 1, "C": 2, "cut": 3}
PILLARS = [("location", "Location"), ("service", "Main service"), ("brand", "Brand"), ("authority", "Authority")]
CRO_ROWS = [("hero", "1 Hero"), ("beweis-leiste", "2 Proof strip"), ("fuer-mich", "3 Is this for me?"), ("leistungen", "4 Services"),
            ("erster-termin", "5 First visit"), ("ueber", "6 About the practitioner"), ("bewertungen", "7 Reviews"),
            ("faq", "8 FAQ"), ("standort", "9 Location"), ("abschluss-cta", "10 Closing CTA")]
# Landing-page runs (page_tag lp:<persona>): one map per page with these rows (me&you persona pages, 2026-10-12).
LP_ROWS = [("hero", "1 Hero"), ("situation", "2 Situation / recognition"), ("methode", "3 Method"), ("angebot", "4 Offer and format"),
           ("orte-termine", "5 Places and dates"), ("stimmen", "6 Proof"), ("michael", "7 Michael"), ("faq", "8 FAQ"), ("erster-schritt", "9 First step / CTA")]
EMPTY_CELL = '<span class="empty">No pool item.</span>'
STATUS_LABEL = {"draft": "Draft", "needs_client": "Needs client", "adjacent_review": "Adjacent: Martin decides", "approved": "Approved", "cut": "Cut", "done": "Done"}
H = html.escape


def load(run):
    pool = json.load(open(f"{run}/04-pool/pool.json"))
    summ = json.load(open(f"{run}/04-pool/summary.json"))
    return pool, summ


def tokens(text, pool, run):
    b = pool["meta"].get("benchmark") or {}
    ids = {i["id"]: i for i in pool["items"]}

    def rep(m):
        k = m.group(1)
        if k == "bench.own": return f"{b.get('own_homepage_words')}"
        if k == "bench.floor": return f"{b.get('floor_70pct')}"
        if k == "bench.median": return f"{b.get('median_words'):g}"
        if k == "bench.n": return f"{len(b.get('homepages_measured', {}))}"
        if k == "spend": return f"{pool['meta']['spend_usd']:.2f}"
        if k == "n_items": return str(len(pool["items"]))
        mq = re.match(r"gsc\.(listed|brand|training|patient_service)_(impr|clicks|share)", k)
        gs = pool["meta"].get("gsc_summary")
        if mq and gs:
            grp = gs[mq.group(1)]
            if mq.group(2) == "share": return f"{round(100 * grp['impressions'] / gs['listed']['impressions'])} %"
            return f"{grp['impressions' if mq.group(2) == 'impr' else 'clicks']:,}"
        if k == "gsc.total_clicks" and gs: return str(gs["totals_from_gsc_ui"]["clicks"])
        mg = re.match(r"(CP-[A-Z]+-\d+)\.gsc_(impr|clicks|pos)", k)
        if mg and mg.group(1) in ids:
            g = ids[mg.group(1)]["demand"].get("gsc") or {}
            return str({"impr": g.get("impressions"), "clicks": g.get("clicks"), "pos": g.get("best_position")}[mg.group(2)])
        mm = re.match(r"(CP-[A-Z]+-\d+)\.cov", k)
        if mm and mm.group(1) in ids:
            c = ids[mm.group(1)]["competitor"]
            return f"{c['covering']} of {c['denominator']}"
        return m.group(0)

    return re.sub(r"\{([^}]+)\}", rep, text)


def score_bar(v):
    return f'<span class="bar"><i style="width:{max(0, min(100, v)):.0f}%"></i></span>'


def item_card(i):
    s, c, d = i["score"], i["competitor"], i["demand"]
    kws = ", ".join(f'{H(k["kw"])} <b>{"no data" if k["volume"] is None else format(k["volume"], ",")}</b>{"" if k["scope"] == "local" else " <em>nat.</em>"}' for k in i["keywords"]) or "none"
    ev = "".join(f'<li><span class="tag">{H(e["type"])}</span> <a href="../{H(e["file"].replace("*", "1"))}">{H(e["file"])}</a> <span class="mut">{H(e["ref"][:140])}</span></li>' for e in i["evidence"])
    samples = ""
    if d["autocomplete_samples"]: samples += "<p><b>Autocomplete:</b> " + H("; ".join(d["autocomplete_samples"])) + "</p>"
    if d["paa_samples"]: samples += "<p><b>People also ask:</b> " + H("; ".join(d["paa_samples"])) + "</p>"
    if d.get("client_signal"): samples += f'<p><b>Client signal:</b> {H(d["client_signal"])}</p>'
    if d.get("trend_note"): samples += f'<p><b>Trend:</b> {H(d["trend_note"])}</p>'
    needs = "".join(f"<li>[FEHLT] {H(n)}</li>" for n in i["needs_client"])
    comp = i["compliance"]
    live_html = ""
    if i.get("live_status") not in (None, "n/a"):
        link = f' (<a href="{H(i["live_url"])}">{H(i["live_url"])}</a>)' if i.get("live_url") else ""
        live_html = f'<p><b>Live site:</b> {H(i["live_status"])}{link} <span class="mut">Auto check. Confirm by hand.</span></p>'
    cflag = f'<span class="pill c-{comp["flag"]}">{comp["mode"].upper()} {comp["flag"]}</span>'
    return f'''<details class="item p-{i["priority"]}" data-prio="{i["priority"]}" data-pillar="{i["pillar"]}">
<summary><span class="rank">{H(i["id"][3:])}</span><span class="prio pr-{i["priority"]}">{i["priority"]}</span>
<span class="topic">{H(i["topic"])}</span>{score_bar(s["total"])}<span class="num">{s["total"]:.0f}</span>
<span class="tag2">{H(i["page_tag"])}</span>{cflag}<span class="st st-{i["status"]}">{STATUS_LABEL[i["status"]]}</span></summary>
<div class="body">
<div class="grid">
<div><h5>Why</h5><p>{H(i["fit_reason"])}</p><p><b>Fit {i["fit"]} of 3.</b> {H(i["audience"]).capitalize()} audience. Item type: {H(i["item_type"])}.{" Section: " + H(i["section_hint"]) if i.get("section_hint") else ""}</p>
{"<p><b>Question:</b> " + H(i["question"]) + "</p>" if i.get("question") else ""}</div>
<div><h5>Numbers</h5><table class="mini"><tr><td>Demand</td><td>{s["demand"]:.0f}</td><td class="mut">basis: {H(d["basis"])}</td></tr>
<tr><td>Gap</td><td>{s["gap"]:.0f}</td><td class="mut">{c["covering"]} of {c["denominator"]} {H(c["set"])} cover it{" (table stakes)" if c["table_stakes"] else ""}</td></tr>
<tr><td>Fit</td><td>{s["fit"]:.0f}</td><td></td></tr><tr><td>Conversion</td><td>{s["conversion"]:.0f}</td><td></td></tr><tr><td>Effort</td><td>{s["effort"]:.0f}</td><td class="mut">higher = less work</td></tr></table></div>
</div>
<p><b>Keywords</b> (searches per month, {H(i["keywords"][0]["volume_date"]) if i["keywords"] else H(d["date"])}): {kws}</p>
{samples}
{live_html}
{"<p><b>Competitors covering it:</b> " + H(", ".join(c["covering_domains"])) + "</p>" if c["covering_domains"] else ""}
{"<p class='mut'>" + H(c["note"]) + "</p>" if c.get("note") else ""}
{"<p><b>Compliance note:</b> " + H(comp["note"]) + "</p>" if comp.get("note") else ""}
{"<p><b>Decision note:</b> " + H(i["decision_note"]) + "</p>" if i.get("decision_note") else ""}
{"<ul class='needs'>" + needs + "</ul>" if needs else ""}
<details class="raw"><summary>Raw data ({len(i["evidence"])} sources)</summary><ul>{ev}</ul></details>
</div></details>'''


CSS = """
:root{--bg:#f7f6f2;--card:#fff;--ink:#1d2320;--mut:#66706b;--line:#e2e0d8;--acc:#2f5d50;--a:#2f5d50;--b:#8a6d1f;--c:#6b7280;--cut:#a23b3b;--warn:#b45309;--ok:#2f5d50}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#141816;--card:#1c211f;--ink:#e8ece9;--mut:#9aa5a0;--line:#2b322f;--acc:#7fc4ae;--a:#7fc4ae;--b:#d6b25a;--c:#9aa5a0;--cut:#e08585;--warn:#e0a45a;--ok:#7fc4ae}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:24px 16px 80px}
h1{font-size:28px;margin:0 0 4px}h2{font-size:22px;margin:40px 0 12px;padding-top:8px;border-top:1px solid var(--line)}h3{font-size:18px;margin:24px 0 8px}h5{margin:0 0 6px;font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--mut)}
.sub{color:var(--mut);margin:0 0 16px}.meta{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
.chip{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:4px 12px;font-size:13px}
.chip b{color:var(--acc)}
.find{display:grid;gap:10px}.find div{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--acc);border-radius:8px;padding:12px 16px}
.find .ids{display:block;margin-top:6px;font-size:12px;color:var(--mut)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px}
.pcard{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px}
.pcard h3{margin:0 0 6px}.pcard .cnt{font-size:13px;color:var(--mut);margin-bottom:8px}.pcard ol{padding-left:18px;margin:8px 0 0;font-size:14px}
table{border-collapse:collapse;width:100%;font-size:14px;background:var(--card)}th,td{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}th{background:var(--bg);font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--mut)}
.tblwrap{overflow-x:auto}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0 12px}.filters button{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:5px 14px;cursor:pointer;font-size:13px}.filters button.on{background:var(--acc);color:var(--bg);border-color:var(--acc)}
details.item{background:var(--card);border:1px solid var(--line);border-radius:8px;margin:6px 0}details.item>summary{list-style:none;cursor:pointer;display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:10px 12px}
details.item>summary::-webkit-details-marker{display:none}.rank{font-family:ui-monospace,Menlo,monospace;font-size:12px;color:var(--mut)}
.topic{flex:1 1 280px;font-weight:600}.num{font-variant-numeric:tabular-nums;width:28px;text-align:right}.bar{display:inline-block;width:80px;height:8px;background:var(--line);border-radius:4px;overflow:hidden}.bar i{display:block;height:100%;background:var(--acc)}
.prio{display:inline-block;min-width:22px;text-align:center;border-radius:4px;color:#fff;font-weight:700;font-size:12px;padding:1px 6px}.pr-A{background:var(--a)}.pr-B{background:var(--b)}.pr-C{background:var(--c)}.pr-cut{background:var(--cut)}
.tag2,.tag{font-size:12px;background:var(--bg);border:1px solid var(--line);border-radius:4px;padding:1px 6px}.pill{font-size:11px;border-radius:4px;padding:1px 6px;border:1px solid var(--line)}.c-review{color:var(--warn);border-color:var(--warn)}.c-block{color:var(--cut);border-color:var(--cut)}.c-ok{color:var(--ok)}
.st{font-size:12px;color:var(--mut)}.st-needs_client{color:var(--warn)}.st-adjacent_review{color:var(--cut)}
.body{padding:4px 16px 14px;border-top:1px solid var(--line)}.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}@media(max-width:720px){.grid{grid-template-columns:1fr}.bar{display:none}}
.mut{color:var(--mut)}.mini td{border:0;padding:2px 10px 2px 0}.needs{color:var(--warn)}details.raw{margin-top:8px}details.raw summary{cursor:pointer;color:var(--acc);font-size:14px}details.raw li{font-size:13px;margin:3px 0}
.map td:first-child{white-space:nowrap;font-weight:600}.empty{color:var(--mut);font-style:italic}
a{color:var(--acc)}.note{background:var(--card);border:1px dashed var(--line);border-radius:8px;padding:10px 14px;margin:10px 0;font-size:14px}
.hidden{display:none}
"""

JS = """
document.querySelectorAll('.filters').forEach(function(f){f.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
f.querySelectorAll('button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');var v=b.dataset.f;
document.querySelectorAll('details.item').forEach(function(d){d.classList.toggle('hidden',!(v==='all'||d.dataset.prio===v||(v==='client'&&d.querySelector('.st-needs_client'))||(v==='adj'&&d.querySelector('.st-adjacent_review'))))})})});
"""


def render_html(pool, summ, run):
    m = pool["meta"]
    items = sorted(pool["items"], key=lambda i: (PRIO_ORDER[i["priority"]], -i["score"]["total"]))
    live = [i for i in items if i["priority"] != "cut"]
    out = [f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{H(summ["title"])}</title><style>{CSS}</style></head><body><div class="wrap">']
    out.append(f'<h1>{H(summ["title"])}</h1><p class="sub">{H(summ["subtitle"])}</p>')
    b = m.get("benchmark") or {}
    out.append('<div class="meta">' + "".join(f'<span class="chip">{t}</span>' for t in [
        f'Date <b>{H(m["run_date"])}</b>', f'Mode <b>{H(m["mode"])}</b>', f'Items <b>{len(live)}</b> live, <b>{len(items) - len(live)}</b> cut',
        f'Paid data <b>{m["spend_usd"]:.2f} USD</b> of {m["cap_usd"]:.0f} USD cap', f'Competitor sites <b>{len(pool["competitors"])}</b> ({len(m.get("unreadable_competitors", []))} unreadable)',
        f'Validator <b>passed</b>']) + '</div>')
    out.append('<h2 id="findings">What you must know first</h2><div class="find">')
    for f in summ["findings"]:
        out.append(f'<div>{H(tokens(f["text"], pool, run))}<span class="ids">Items: {H(", ".join(f["items"]))}</span></div>')
    out.append('</div>')
    out.append('<h2 id="pillars">The four pillars</h2><div class="cards">')
    for key, label in PILLARS:
        pi = [i for i in live if i["pillar"] == key]
        top = pi[:3]
        n_client = sum(1 for i in pi if i["status"] == "needs_client")
        out.append(f'<div class="pcard"><h3>{label}</h3><div class="cnt">{len(pi)} items · {sum(1 for i in pi if i["priority"] == "A")} A · {n_client} need the client</div><p>{H(summ["pillars"][key])}</p><b>Top items</b><ol>' + "".join(f'<li>{H(i["topic"])} <span class="mut">({i["score"]["total"]:.0f})</span></li>' for i in top) + '</ol></div>')
    out.append('</div>')
    lp_tags = sorted({i["page_tag"] for i in live if i["page_tag"].startswith("lp:")})
    if lp_tags and not any(i["page_tag"] == "homepage" for i in live):
        cell = lambda its: "<br>".join(f'<span class="prio pr-{i["priority"]}">{i["priority"]}</span> {H(i["topic"])} <span class="mut">{i["id"]}</span>' for i in its)
        out.append('<h2 id="map">Page maps: one per landing page</h2><p class="mut">Rows are the landing-page sections. Each row lists the pool items for it, best first.</p>')
        for t in lp_tags:
            out.append(f'<h3>{H(t)}</h3><div class="tblwrap"><table class="map"><tr><th>Section</th><th>Pool items (best first)</th></tr>')
            for key, label in LP_ROWS:
                its = [i for i in live if i["page_tag"] == t and i.get("section_hint") == key]
                out.append(f'<tr><td>{label}</td><td>{cell(its) or EMPTY_CELL}</td></tr>')
            rest = [i for i in live if i["page_tag"] == t and i.get("section_hint") not in dict(LP_ROWS)]
            if rest: out.append(f'<tr><td>Whole page</td><td>{cell(rest)}</td></tr>')
            out.append('</table></div>')
    else:
        out.append('<h2 id="map">Homepage map: where the pool plugs into the CRO blueprint</h2><p class="mut">The 10 rows are the CRO P0 blueprint. The pool never removes a row. It ranks what goes into each row.</p><div class="tblwrap"><table class="map"><tr><th>CRO row</th><th>Pool items (best first)</th></tr>')
        for key, label in CRO_ROWS:
            its = [i for i in live if i.get("section_hint") == key and i["page_tag"] == "homepage"]
            cell = "<br>".join(f'<span class="prio pr-{i["priority"]}">{i["priority"]}</span> {H(i["topic"])} <span class="mut">{i["id"]}</span>' for i in its) or '<span class="empty">No pool item. The CRO blueprint row stays as is.</span>'
            out.append(f'<tr><td>{label}</td><td>{cell}</td></tr>')
        other = [i for i in live if i["page_tag"] == "homepage" and not i.get("section_hint")]
        if other:
            out.append('<tr><td>Whole page</td><td>' + "<br>".join(f'<span class="prio pr-{i["priority"]}">{i["priority"]}</span> {H(i["topic"])} <span class="mut">{i["id"]}</span>' for i in other) + '</td></tr>')
        out.append('</table></div>')
    # other pages
    tags = {}
    for i in live:
        if i["page_tag"] != "homepage" and not (lp_tags and i["page_tag"].startswith("lp:")): tags.setdefault(i["page_tag"], []).append(i)
    if tags: out.append('<h3>Items for other pages (one line each, ready for the next page run)</h3><div class="tblwrap"><table><tr><th>Page tag</th><th>Items</th></tr>')
    for t in sorted(tags): out.append(f'<tr><td>{H(t)}</td><td>' + "<br>".join(f'<span class="prio pr-{i["priority"]}">{i["priority"]}</span> {H(i["topic"])} <span class="mut">{i["id"]}</span>' for i in tags[t]) + '</td></tr>')
    if tags: out.append('</table></div>')
    out.append('<h2 id="detail">Detail per pillar</h2><div class="filters"><button class="on" data-f="all">All</button><button data-f="A">A</button><button data-f="B">B</button><button data-f="C">C</button><button data-f="client">Needs client</button><button data-f="adj">Adjacent</button></div>')
    for key, label in PILLARS:
        out.append(f'<h3>{label}</h3>' + "".join(item_card(i) for i in items if i["pillar"] == key and i["priority"] != "cut"))
    cut = [i for i in items if i["priority"] == "cut"]
    out.append('<h2 id="cut">Cut items and why</h2>' + "".join(item_card(i) for i in cut))
    out.append('<h2 id="decisions">Decisions for Martin</h2><ol>' + "".join(f"<li>{H(d)}</li>" for d in summ["decisions"]) + '</ol>')
    needs = {}
    for i in live:
        for n in i["needs_client"]: needs.setdefault(n, []).append(i["id"])
    out.append('<h2 id="client">Open facts from the client</h2><div class="tblwrap"><table><tr><th>[FEHLT]</th><th>Blocks items</th></tr>' + "".join(f'<tr><td>{H(n)}</td><td>{H(", ".join(v))}</td></tr>' for n, v in needs.items()) + '</table></div><p class="mut">The full list for the client is in 01-client/client-baseline.md section 8 and in the German form.</p>')
    # competitors
    mets = json.load(open(f"{run}/02-competitors/metrics.json"))
    out.append('<h2 id="raw">Raw data</h2><h3>Competitor pages measured</h3><div class="tblwrap"><table><tr><th>Page</th><th>Tier</th><th>Words</th><th>H2</th><th>FAQ</th><th>Price</th><th>Rating</th><th>Method</th></tr>')
    for r in mets:
        dom = next((d for d in pool["competitors"] if d in r["url"]), "own site")
        tier = pool["competitors"].get(dom, {}).get("tier", "client")
        if r["status"] != "ok":
            out.append(f'<tr><td>{H(r["url"][:80])}</td><td>{tier}</td><td colspan="6"><b>unreadable</b>: {H(str(r.get("reason")))}. Not read as "nothing found".</td></tr>')
        else:
            out.append(f'<tr><td><a href="../02-competitors/metrics.json">{H(r["url"].replace("https://", "")[:70])}</a></td><td>{tier}</td><td>{r["words"]}</td><td>{len(r["h2"])}</td><td>{"yes" if r["faq_signal"] else "-"}</td><td>{"yes" if r["price_mention"] else "-"}</td><td>{"yes" if r["rating_mention"] else "-"}</td><td>{r["fetch_method"]}</td></tr>')
    out.append('</table></div>')
    files = [("01-client/client-baseline.md", "client facts and [FEHLT] list"), ("02-competitors/metrics.json", "page measures"), ("02-competitors/site_urls.json", "competitor sitemaps"),
             ("02-competitors/serp-1.json", "SERPs of the key searches (serp-1.json, serp-2.json, ...)"), ("03-demand/volume.json", "search volumes, call 1"), ("03-demand/volume2.json", "search volumes, call 2"),
             ("03-demand/autocomplete.json", "Google autocomplete tree"), ("03-demand/trends.json", "Google Trends"), (f"03-demand/ranked-{m['domain']}.json", "own rankings (more ranked-*.json for competitors)"),
             ("03-demand/gsc-queries-90d.tsv", "own Search Console queries"), ("04-pool/pool.json", "the pool, machine-readable"), ("spend.jsonl", "every paid call and its cost")]
    out.append('<h3>Files</h3><ul>' + "".join(f'<li><a href="../{p}">{p}</a> <span class="mut">{d}</span></li>' for p, d in files if os.path.exists(os.path.join(run, p))) + '</ul>')
    out.append(f'</div><script>{JS}</script></body></html>')
    return "\n".join(out)


def render_xlsx(pool, run, path):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
    from openpyxl.utils import get_column_letter
    wb = Workbook()
    head = PatternFill("solid", fgColor="2F5D50")
    hf = Font(bold=True, color="FFFFFF")
    thin = Side(style="thin", color="DDDDDD")
    fills = {"A": "D6EBDD", "B": "F6EBC8", "C": "E7E7E7", "cut": "F3D3D3"}

    def sheet(ws, headers, rows, widths, prio_col=None):
        ws.append(headers)
        for c in ws[1]:
            c.fill, c.font = head, hf
            c.alignment = Alignment(wrap_text=True, vertical="center")
        for r in rows: ws.append(r)
        for n, w in enumerate(widths, 1): ws.column_dimensions[get_column_letter(n)].width = w
        for row in ws.iter_rows(min_row=2):
            for c in row:
                c.alignment = Alignment(wrap_text=True, vertical="top")
                c.border = Border(top=thin, bottom=thin, left=thin, right=thin)
            if prio_col is not None:
                p = row[prio_col].value
                if p in fills: row[prio_col].fill = PatternFill("solid", fgColor=fills[p])
        ws.freeze_panes = "C2"
        ws.auto_filter.ref = ws.dimensions
        ws.row_dimensions[1].height = 32

    items = sorted(pool["items"], key=lambda i: (PRIO_ORDER[i["priority"]], -i["score"]["total"]))
    ws = wb.active
    ws.title = "Pool"
    rows = []
    for n, i in enumerate(items, 1):
        s, c, d = i["score"], i["competitor"], i["demand"]
        rows.append([n, i["id"], i["priority"], i["pillar"], i["page_tag"], i.get("section_hint") or "", i["topic"], i["audience"], i["item_type"], s["total"], s["demand"], s["gap"], s["fit"], s["conversion"], s["effort"],
                     d["volume_max"], d["basis"], f'{c["covering"]}/{c["denominator"]}', "yes" if c["table_stakes"] else "", i["fit"], i["compliance"]["flag"], i["status"], i["live_status"], "; ".join(i["needs_client"]), i["owner"],
                     i["fit_reason"], i.get("decision_note") or "", "; ".join(f'{e["type"]}:{e["file"]}' for e in i["evidence"])])
    sheet(ws, ["#", "ID", "Prio", "Pillar", "Page tag", "Homepage row", "Topic", "Audience", "Type", "Score", "Demand", "Gap", "Fit pts", "Conv.", "Effort pts", "Max volume", "Demand basis", "Competitors covering", "Table stakes", "Fit 0-3", "HWG", "Status", "Live site (auto)", "Needs from client", "Owner", "Why", "Decision note", "Sources"],
          rows, [5, 12, 6, 11, 22, 14, 52, 9, 12, 7, 8, 7, 7, 7, 8, 10, 12, 12, 8, 7, 9, 15, 12, 40, 8, 50, 40, 50], prio_col=2)
    ws2 = wb.create_sheet("Keywords")
    rows = [[i["id"], k["kw"], k["scope"], k["volume"] if k["volume"] is not None else "no data", k["volume_date"], k["volume_source"]] for i in items for k in i["keywords"]]
    sheet(ws2, ["Item", "Keyword", "Scope", "Searches / month", "Date", "Source"], rows, [12, 44, 10, 16, 12, 50])
    ws3 = wb.create_sheet("Competitors")
    mets = json.load(open(f"{run}/02-competitors/metrics.json"))
    rows = []
    for r in mets:
        dom = next((d for d in pool["competitors"] if d in r["url"]), "client")
        tier = pool["competitors"].get(dom, {}).get("tier", "client")
        if r["status"] != "ok": rows.append([r["url"], tier, "unreadable", "", "", "", "", "", str(r.get("reason"))])
        else: rows.append([r["url"], tier, r["words"], len(r["h2"]), len(r["h3"]), "yes" if r["faq_signal"] else "", "yes" if r["price_mention"] else "", ", ".join(r["jsonld_types"])[:80], r["fetch_method"]])
    sheet(ws3, ["URL", "Tier", "Words", "H2", "H3", "FAQ", "Price", "Schema types", "Method / reason"], rows, [70, 8, 10, 6, 6, 6, 7, 50, 20])
    ws4 = wb.create_sheet("Needs client")
    needs = {}
    for i in items:
        if i["priority"] == "cut": continue
        for n in i["needs_client"]: needs.setdefault(n, []).append(i["id"])
    sheet(ws4, ["[FEHLT] fact", "Blocks items"], [[n, ", ".join(v)] for n, v in needs.items()], [80, 50])
    wb.save(path)


def write_pool_top(pool, run):
    """Hand-off for CRO Step 3: homepage items by CRO row, plus items that need the client. German topics stay as written."""
    live = sorted([i for i in pool["items"] if i["priority"] != "cut"], key=lambda i: (PRIO_ORDER[i["priority"]], -i["score"]["total"]))
    m = pool["meta"]
    L = [f"# Pool-Top: {m['client']}", "", f"Stand: {m['built']}. Quelle: `04-pool/pool.json` (Content-Pool, Dry-Run). Eingabe für CRO Step 3 (Copy).",
         "Regel: Die 10 CRO-Zeilen bleiben. Der Pool sagt, was in jede Zeile gehört. Items mit Status `needs_client` bleiben Entwurf, bis die Kundin antwortet.", ""]
    for key, label in CRO_ROWS:
        its = [i for i in live if i.get("section_hint") == key and i["page_tag"] == "homepage"]
        L.append(f"## {label}")
        if not its:
            L += ["Kein Pool-Item. CRO-Blueprint gilt unverändert.", ""]
            continue
        for i in its:
            kw = ", ".join(k["kw"] + (f" ({k['volume']}/Mon)" if k["volume"] else " (keine Daten)") for k in i["keywords"][:4])
            L.append(f"- **{i['topic']}** [{i['priority']}, {i['score']['total']:.0f}, {i['id']}, {i['status']}]")
            L.append(f"  - Warum: {i['fit_reason']}")
            if kw: L.append(f"  - Suchbegriffe: {kw}")
            if i["compliance"].get("note"): L.append(f"  - {i['compliance']['note']}")
            for n in i["needs_client"]: L.append(f"  - [FEHLT] {n}")
        L.append("")
    other = [i for i in live if i["page_tag"] == "homepage" and not i.get("section_hint")]
    if other:
        L.append("## Ganze Seite")
        L += [f"- **{i['topic']}** [{i['priority']}, {i['id']}]" for i in other] + [""]
    open(f"{run}/04-pool/pool-top.md", "w").write("\n".join(L))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    a = ap.parse_args()
    run = a.run_dir.rstrip("/")
    pool, summ = load(run)
    os.makedirs(f"{run}/05-report", exist_ok=True)
    open(f"{run}/05-report/content-pool-report.html", "w").write(render_html(pool, summ, run))
    render_xlsx(pool, run, f"{run}/05-report/content-pool.xlsx")
    write_pool_top(pool, run)
    print("wrote", f"{run}/05-report/content-pool-report.html", "and content-pool.xlsx")


if __name__ == "__main__":
    main()
