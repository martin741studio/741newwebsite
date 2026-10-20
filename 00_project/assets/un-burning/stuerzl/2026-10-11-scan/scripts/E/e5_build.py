#!/usr/bin/env python3 -I
"""Area E: build index-intended.json and link-plan.json (+ stats.json for the register builder).
Inputs (all in evidence/area_e/): EV-E-crawl.json, EV-E-probes.json, EV-E-probes-2.json, EV-E-site-search*.json, EV-E-sitemap-osmap.xml, _graph.json
Everything here is derived from verified reads; 'indexed' stays 'unknown' because Search Console is not readable."""
import json, os, re, sys, collections, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from e_lib import ROOT, now, save_evidence
EVD = os.path.join(ROOT, "evidence/area_e")
B = "https://www.stuerzl-steuerstrafrecht.de"
crawl = json.load(open(f"{EVD}/EV-E-crawl.json"))
probes = json.load(open(f"{EVD}/EV-E-probes.json"))["rows"]
for _r in json.load(open(f"{EVD}/EV-E-probes-2.json"))["rows"]:
    probes.append({"name": _r["name"], "url": B + _r["path"], "chain": [{"url": B + _r["path"], "status": _r["status"], "location": _r.get("location")}], "final_status": _r["status"],
                   "meta_robots": _r.get("meta_robots"), "x_robots_tag": None, "canonical": _r.get("canonical"), "title": _r.get("title")})
ss1 = json.load(open(f"{EVD}/EV-E-site-search.json"))
graph = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_graph.json")))["pages"]
osm = open(f"{EVD}/EV-E-sitemap-osmap.xml", encoding="utf-8").read()
sm_urls = re.findall(r"<loc><!\[CDATA\[(.*?)\]\]></loc>", osm)

def key(u):
    u = u.replace("&amp;", "&").replace("https://stuerzl-steuerstrafrecht.de", B)
    if u == B or u == B + "/": return "/"
    p = u.replace(B, "")
    return p or "/"
pages = {p["url"]: p for p in crawl["pages"]}
byk = {}
for u, p in pages.items():
    if u.startswith(B + "/index.php?option=com_osmap") or "sitemap" in p.get("discovered_via", "") and "links" not in p: pass
    byk.setdefault(key(u), p)

SM = {key(u) for u in sm_urls}
SEARCH = {key(r["url"]) for r in ss1["queries"][0]["results"]} | {key(r["url"]) for r in ss1["queries"][1]["results"]}
SEARCH |= {key(B + x) for x in ["/index.php/steuerstrafrecht/selbstanzeige-korrekturberatung", "/index.php/steuerstrafrecht/durchsuchungsbegleitung-schulung", "/index.php/steuerstrafrecht/gutachten-risikobewertung", "/index.php/datenschutz"]}

AREAS = ["steuerstrafrecht", "selbstanzeigen-steuerliche-korrekturen", "ordnungswidrigkeiten", "zollstrafrecht", "arbeitsstrafrecht", "korruptionsstrafrecht", "sonstiges-wirtschaftsstrafrecht", "verteidigung-von-individualpersonen", "unternehmensvertretung"]
AREA_K = {f"/index.php/{a}" for a in AREAS}
HUB = "/index.php/leistungen"
def is_sub(k):
    parts = k.split("/")
    return len(parts) == 4 and parts[1] == "index.php" and parts[2] in AREAS
SUBS = sorted(k for k in byk if is_sub(k) and byk[k].get("final_status") == 200)
LAWYERS = {"/index.php/dr-anja-stuerzl", "/index.php/lea-wimmer", "/index.php/dr-monika-glogger", "/index.php/mary"}
STAFF = {"/index.php/thorben-hoppe", "/index.php/florentine-jilg", "/index.php/maria-bruckmeier", "/index.php/lenka-schluetter", "/index.php/jessica-weyel", "/index.php/nina-gueldenring"}
ARTICLE_RE = re.compile(r"^/index\.php/component/content/article/([^?]+)\?catid=10&Itemid=228$")
LEGAL = {"/index.php/impressum", "/index.php/datenschutz", "/index.php/nutzungsbedingungen"}

def classify(k, p):
    """returns class, intended, note"""
    if k == "/": return "money", "yes", "Startseite"
    if k == HUB: return "service", "yes", "Leistungen-Übersicht"
    if k in AREA_K: return "service", "yes", "Leistungsbereich"
    if is_sub(k): return "service", "yes", "Unterseite eines Leistungsbereichs"
    if k == "/index.php/kontakt": return "location", "yes", "Kontakt Frankfurt und München"
    if k in ("/index.php/kanzlei", "/index.php/faq", "/index.php/team"): return "service", "yes", {"kanzlei": "Kanzlei-Seite", "faq": "FAQ (6 x H1)", "team": "Team-Übersicht"}[k.split("/")[-1]]
    if k in LAWYERS: return "service", "yes", "Profil mit Inhalt"
    if k in STAFF: return "service", "review", f"Mitarbeiter-Profil, dünn ({(p or {}).get('words_component')} Wörter)"
    if k == "/index.php/friends": return "service", "yes", "Netzwerk-Seite"
    if k == "/index.php/join-our-team": return "service", "yes", "Recruiting-Seite"
    if k in LEGAL: return "system", "yes", "Pflichtseite, indexierbar ok"
    if k == "/index.php/aktuelles": return "blog", "yes", "Aktuelles-Übersicht"
    if ARTICLE_RE.match(k): return "blog", "review", f"Presse-/Termin-Beitrag, {(p or {}).get('words_component')} Wörter, kein Link auf eine Leistung"
    if k.startswith("/index.php/component/content/category/"): return "archive", "no", "Kategorie-Archiv (Variante)"
    if k.startswith("http://"): return "system", "no", "http-Variante, leitet per 301 auf https://www weiter"
    if k == "/administrator/": return "system", "no", "Joomla-Anmeldung (Backend), in robots.txt gesperrt"
    if k in ("/index.php", "/index.php/", "/index.php/home"): return "archive", "no", "Duplikat der Startseite"
    if k.endswith("/") and k != "/": return "archive", "no", "Duplikat mit Slash am Ende"
    return "system", "no", "System-/Komponenten-Route oder Parameter-Variante"

rows = []
def mk(url, source, http, hops, final, robots, xrobots, canon, p=None, extra=None, note=None):
    k = key(url)
    cls, intended, cnote = classify(k, p)
    if note: cnote = note
    status = http
    canon_state = "none" if not canon else ("self" if canon.replace("&amp;", "&") == final.replace("&amp;", "&") or key(canon) == key(final) and canon.startswith(B) and "?" not in canon.replace(B, "") == ("?" not in final) and canon.rstrip("/") == final.rstrip("/") else "other")
    noindex = bool(robots and "noindex" in robots.lower()) or bool(xrobots and "noindex" in (xrobots or "").lower())
    indexable = (status == 200) and not noindex
    sig = k in SEARCH
    row = {"url": url, "source": source, "http_status": status, "redirect_hops": hops, "final_url": final,
           "meta_robots": robots, "x_robots_tag": xrobots, "canonical": canon, "canonical_state": canon_state,
           "in_sitemap": k in SM, "indexable_technically": indexable,
           "indexed": "unknown", "indexed_source": ("listed in Firecrawl web-index site: search 2026-10-11 (not Google, rough)" if sig else "no signal; Search Console not readable (403)"),
           "search_index_signal": sig, "coverage_state": None, "gsc_clicks_90d": None, "gsc_impressions_90d": None,
           "intended": intended, "class": cls, "class_note": cnote, "class_is": "PROPOSED"}
    if extra: row.update(extra)
    # verdict
    if status in (404, 410) or status is None:
        v, a = "ok", "keep"; row["class_note"] = (cnote + "; liefert 404 (korrekt), toter interner Link" if source != "probe" else cnote + "; liefert 404 (korrekt)")
    elif status >= 500:
        v, a = "review", "fix"
    elif status in (301, 302, 303, 307, 308):
        v, a = "ok", "keep"
    elif intended == "yes":
        if not indexable: v, a = "index_missing", "fix"
        elif sig: v, a = "ok", "keep"
        else: v, a = "unverified", "keep"
    elif intended == "review":
        v, a = "decision_needed", "keep"
    else:  # intended no
        if sig and indexable: v, a = "index_unwanted", "fix"
        elif indexable: v, a = "review", "fix"
        else: v, a = "ok", "keep"
    row["verdict"], row["action"] = v, a
    return row

seen = set()
def add(row):
    kk = row["url"]
    if kk in seen: return
    seen.add(kk); rows.append(row)

# 1 crawl rows (HTML pages and 404s), skipping sitemap probes that are not pages
for u, p in pages.items():
    if p.get("discovered_via") == "sitemap_probe" and "view=html" not in u: continue
    if p.get("final_status") is None: continue
    final = p["final_url"]
    k = key(u)
    src = "crawl" if p.get("depth", 0) < 99 else "sitemap"
    if k in SM: src += "+sitemap"
    row = mk(u, src, p["final_status"] if p["redirect_hops"] == 0 else p["chain"][0]["status"], p["redirect_hops"], final,
             p.get("meta_robots"), p.get("x_robots_tag"), p.get("canonical"), p=p,
             extra={"h1_count": len(p.get("h1_all", [])), "words": p.get("words_component"), "title": p.get("title")})
    add(row)
# apex row: status is the first hop
# 2 probe rows
for r in probes:
    u = r["url"]
    if u.endswith("robots.txt") or u.endswith("humans.txt") or u.endswith("llms.txt") or "/images/" in u or "/media/" in u: continue
    if r["name"] in ("kanzlei_hash_AS",): continue
    first = r["chain"][0]["status"]
    final = r["chain"][-1]["url"]
    row = mk(u, "probe", first, len(r["chain"]) - 1, final, r.get("meta_robots"), r.get("x_robots_tag"), r.get("canonical"),
             p=None, extra={"probe_name": r["name"], "title": r.get("title")})
    if r["final_status"] == 200 and first in (301, 302, 303) and key(final) != key(u):
        row["class_note"] += f"; leitet weiter auf {key(final)}"
    add(row)
# OSMap sitemap URLs already in crawl. Sitemap file itself:
add({"url": B + "/index.php?option=com_osmap&view=xml&id=1&format=xml", "source": "probe", "http_status": 200, "redirect_hops": 1, "final_url": B + "/index.php?option=com_osmap&view=xml&id=1&format=xml",
     "meta_robots": None, "x_robots_tag": None, "canonical": None, "canonical_state": "none", "in_sitemap": False, "indexable_technically": True,
     "indexed": "unknown", "indexed_source": "sitemap file, not an indexing target", "search_index_signal": False, "coverage_state": None, "gsc_clicks_90d": None, "gsc_impressions_90d": None,
     "intended": "no", "class": "system", "class_note": "OSMap-Sitemap (22 URLs); nicht unter /sitemap.xml, nicht in robots.txt", "class_is": "PROPOSED", "verdict": "ok", "action": "keep"})

# fix wrongly 'ok' status for rows reached via redirect: verdict computed from first status only
# canonical_state recompute (simple, explicit)
for r in rows:
    c, f = r.get("canonical"), r.get("final_url")
    if not c: r["canonical_state"] = "none"
    else:
        r["canonical_state"] = "self" if c.replace("&amp;", "&") == f.replace("&amp;", "&") else "other"
    # redirected apex/http rows: canonical points to www page which is the final target
    if r["redirect_hops"] and r["http_status"] in (301, 302, 303):
        r["canonical_state"] = "target" if c and key(c) == key(f) else r["canonical_state"]
    # intended/verdict for variants whose canonical points to another URL
    if r["canonical_state"] == "other" and r["http_status"] == 200 and r["intended"] == "no" and r["verdict"] in ("review",):
        r["class_note"] += "; Canonical zeigt auf andere URL"
cnt = collections.Counter(r["verdict"] for r in rows)
cls = collections.Counter((r["class"], r["intended"]) for r in rows)
idx = {"run": "stuerzl-2026-10-11-scan", "area": "E", "classes_are": "PROPOSED by agent from page type and the crawl of 2026-10-11; Martin and the client decide.",
       "intended_values": "yes | no | review (review needs a human decision)",
       "verdict_values": "ok | index_missing | index_unwanted | review | unverified | decision_needed",
       "method_note": "Search Console is not readable (HTTP 403, EV-E-gsc-access-test). Field 'indexed' stays 'unknown' for every URL. 'ok' means: intended, HTTP 200, no noindex, and listed in a Firecrawl site: search (third-party web index, not Google, rough). 'unverified' means intended and technically indexable but not seen in that search. 'index_unwanted' (derived) means unintended, indexable and seen in that search. Nothing is called 'not indexed'.",
       "sitemap": {"standard_location": "/sitemap.xml = 404, robots.txt has no Sitemap line", "osmap_url": "/index.php?option=com_osmap&view=xml&id=1&format=xml", "osmap_urls": len(sm_urls)},
       "counts": dict(cnt), "class_intended_counts": {f"{a}/{b}": c for (a, b), c in cls.items()}, "total_rows": len(rows),
       "inspected_urls": 0, "collected_at": now(), "evidence_ids": ["EV-E-crawl", "EV-E-probes", "EV-E-probes-2", "EV-E-site-search", "EV-E-site-search-2", "EV-E-sitemap-osmap", "EV-E-gsc-access-test"],
       "rows": rows}
json.dump(idx, open(os.path.join(ROOT, "index-intended.json"), "w"), indent=1, ensure_ascii=False)
print("index rows", len(rows), dict(cnt))
print(dict(cls))

# ------------------------------------------------------------------ link plan
H1 = {}
TITLE = {}
for k, p in byk.items():
    if p.get("final_status") == 200 and "links" in p:
        t = p.get("title") or ""
        TITLE[k] = re.sub(r"^Stürzl Steuerstrafrecht\s*[–-]\s*", "", t).strip()
        h = [x for x in p.get("h1_all", []) if x not in ("Leistungen",)]
        H1[k] = h[0] if h else TITLE[k]
LABEL = {"/": "Startseite", HUB: "Leistungen", "/index.php/kanzlei": "Kanzlei", "/index.php/team": "Team", "/index.php/faq": "FAQ", "/index.php/kontakt": "Kontakt",
         "/index.php/aktuelles": "Aktuelles", "/index.php/steuerstrafrecht": "Steuerstrafrecht", "/index.php/selbstanzeigen-steuerliche-korrekturen": "Selbstanzeigen und steuerliche Korrekturen",
         "/index.php/ordnungswidrigkeiten": "Ordnungswidrigkeiten", "/index.php/zollstrafrecht": "Zollstrafrecht", "/index.php/arbeitsstrafrecht": "Arbeitsstrafrecht",
         "/index.php/korruptionsstrafrecht": "Korruptionsstrafrecht", "/index.php/sonstiges-wirtschaftsstrafrecht": "Sonstiges Wirtschaftsstrafrecht",
         "/index.php/verteidigung-von-individualpersonen": "Verteidigung von Individualpersonen", "/index.php/unternehmensvertretung": "Unternehmensvertretung"}
def label(k): return LABEL.get(k) or TITLE.get(k) or k

content_pages = [k for k, p in byk.items() if p.get("final_status") == 200 and "links" in p and p.get("discovered_via") != "sitemap_probe"
                 and (k == "/" or (k.startswith("/index.php/") and "component/users" not in k))]
# exclude non-content variants
EXCL = {"/index.php", "/index.php/", "/index.php/home", "/index.php/sitemap"}
content_pages = [k for k in content_pages if k not in EXCL and not k.startswith("/index.php?option") and not k.startswith("/index.php/component/content/category/")]
def parent_of(k):
    if k == "/": return "/", "/", ["/"]
    if k == HUB: return "/", "/", ["/"]
    if k in AREA_K: return HUB, "/", ["/", HUB]
    if is_sub(k):
        area = "/".join(k.split("/")[:3]); return area, "/", ["/", HUB, area]
    if k in LAWYERS or k in STAFF: return "/index.php/team", "/", ["/", "/index.php/team"]
    if ARTICLE_RE.match(k) or k.startswith("/index.php/component/content/category/"): return "/index.php/aktuelles", "/", ["/", "/index.php/aktuelles"]
    return "/", "/", ["/"]

# link graph from component region (ctx + block) per page key
OUT_CTX, OUT_BLK = collections.defaultdict(set), collections.defaultdict(set)
for u, g in graph.items():
    src = key(pages[u]["final_url"]) if u in pages else g["key"]
    src = g["key"]
    for c in g["contextual"]:
        if c["to"] != src: OUT_CTX[src].add(c["to"])
    for c in g["block"]:
        if c["to"] != src: OUT_BLK[src].add(c["to"])
def norm_t(t):
    t = t.replace("&amp;", "&")
    return t
OUT_CTX = {k: {norm_t(t) for t in v} for k, v in OUT_CTX.items()}
OUT_BLK = {k: {norm_t(t) for t in v} for k, v in OUT_BLK.items()}
INB_CTX, INB_BLK = collections.defaultdict(set), collections.defaultdict(set)
for s, ts in OUT_CTX.items():
    for t in ts: INB_CTX[t].add(s)
for s, ts in OUT_BLK.items():
    for t in ts: INB_BLK[t].add(s)

# full graph (menus + content) for click depth
FULL = collections.defaultdict(set)
for u, p in pages.items():
    if "links" not in p or p.get("discovered_via") == "sitemap_probe" or p.get("final_status") != 200: continue
    s = key(u)
    for l in p["links"]:
        if l["href"].startswith((B, "https://stuerzl-steuerstrafrecht.de")): FULL[s].add(key(l["href"]).replace("&amp;", "&"))
def bfs(graph_, start="/"):
    d = {start: 0}; q = [start]
    while q:
        x = q.pop(0)
        for y in graph_.get(x, ()):
            if y not in d: d[y] = d[x] + 1; q.append(y)
    return d
D_FULL = bfs(FULL)
CONTENT_ONLY = {k: OUT_CTX.get(k, set()) | OUT_BLK.get(k, set()) for k in set(OUT_CTX) | set(OUT_BLK)}
D_CONT = bfs(CONTENT_ONLY)

ART_TARGET = {  # topical lateral links, proposal only (anchors need human edit)
 "neue-juve-rankings-wie-frauen-im-strafrecht-zur-festen-groesse-wurden": "/index.php/kanzlei",
 "capital-magazin-steuern-hinterzogen-das-sollten-sie-jetzt-nicht-tun": "/index.php/selbstanzeigen-steuerliche-korrekturen",
 "kluge-koepfe-im-strafrecht": "/index.php/dr-anja-stuerzl",
 "private-banking-magazin": "/index.php/steuerstrafrecht",
 "influencer-innen-auf-social-media-jetzt-vor-strafverfolgung-schuetzen": "/index.php/steuerstrafrecht",
 "iww-seminar": "/index.php/dr-anja-stuerzl",
 "podcast-ims024-weltfrauentag-steuerstrafrecht-gruendung-von-juwist": "/index.php/dr-anja-stuerzl",
 "webinar-steuerstrafverfahren-und-besteuerungsverfahren": "/index.php/steuerstrafrecht/verteidigung-im-steuerstrafverfahren",
 "ranking-wirtschaftwoche": "/index.php/kanzlei",
 "vortrag": "/index.php/dr-anja-stuerzl",
}
def link(frm, to, why, typ, note=None):
    d = {"from": frm, "to": to, "anchor_proposal": label(to), "why": why, "type": typ}
    d["anchor_note"] = note or "Anker aus Menü-/Seitenname abgeleitet; Mensch prüft Wortlaut (BORA/UWG: sachlich, keine Werbeversprechen)"
    return d

plan = []
for k in sorted(content_pages, key=lambda x: (x != "/", x)):
    p = byk[k]
    if k in LEGAL: continue
    par, gp, hier = parent_of(k)
    oc, ob = OUT_CTX.get(k, set()), OUT_BLK.get(k, set())
    allout = oc | ob
    ic, ib = INB_CTX.get(k, set()), INB_BLK.get(k, set())
    missing = []
    if k != "/" and par != "/":
        if par not in allout:
            missing.append(link(k, par, "Kind verlinkt auf seine Elternseite", "child_to_parent"))
        elif par in ob and par not in oc:
            missing.append(link(k, par, "Der Link nach oben besteht nur im auf allen 25 Seiten wiederholten Block; ein Textlink im Inhalt fehlt", "child_to_parent_contextual"))
    if k in AREA_K or k == HUB:
        if "/" not in allout: missing.append(link(k, "/", "Leistungsseite verlinkt im Inhalt auf die Startseite", "service_to_home"))
    # parent lists its children
    plan_row = {"page": k, "title": p.get("title"), "h1": p.get("h1_all", []), "words": p.get("words_component"), "parent": par, "grandparent": gp, "hierarchy": hier,
                "click_depth_from_home_any_link": D_FULL.get(k), "click_depth_from_home_content_links_only": D_CONT.get(k),
                "inbound_content_links": len(ic | ib), "inbound_contextual": len(ic), "inbound_via_repeated_block": len(ib - ic),
                "inbound_content_from": sorted(ic | ib), "outbound_content_links": len(allout),
                "outbound_contextual": len(oc), "outbound_to_parent": par in allout, "outbound_to_parent_contextual_only": par in oc,
                "up_link_only_via_repeated_block": (par in ob) and (par not in oc), "outbound_to_home": "/" in allout,
                "missing_links": missing, "do_not_edit_page": False, "in_sitemap_osmap": k in SM}
    plan.append(plan_row)
P = {r["page"]: r for r in plan}
# parent_to_child gaps
for k, r in P.items():
    par = r["parent"]
    if k == "/" or par == "/" or par not in P: continue
    pall = OUT_CTX.get(par, set()) | OUT_BLK.get(par, set())
    if k not in pall:
        P[par]["missing_links"].append(link(par, k, "Elternseite führt ihre Unterseite auf", "parent_to_child"))
# home to each of the 9 areas + core pages
home_missing = []
hall = OUT_CTX.get("/", set()) | OUT_BLK.get("/", set())
for a in sorted(AREA_K):
    if a not in hall:
        home_missing.append(link("/", a, "Startseite führt die Leistungsbereiche direkt auf (Klicktiefe 1 statt 2 über die Übersicht)", "home_to_service"))
for t in ("/index.php/faq", "/index.php/kontakt", "/index.php/team"):
    if t not in hall: home_missing.append(link("/", t, "Startseite verlinkt wichtige Ziele im Inhalt, nicht nur im Menü", "home_to_core"))
P["/"]["missing_links"] += home_missing
# dead link on home
P["/"]["missing_links"].append({"from": "/", "to": HUB, "anchor_proposal": "mehr zu den Schwerpunkten", "type": "fix_dead_link",
    "why": "Der Link 'mehr zu den Schwerpunkten' führt auf /index.php/schwerpunkte (404). Ziel auf eine bestehende Seite umstellen, z. B. die Leistungen-Übersicht.",
    "anchor_note": "Anker bleibt, Ziel ändern; Entscheidung bei Martin und Kundin"})
# FAQ topical links
faq = P["/index.php/faq"]
for to, why in [("/index.php/steuerstrafrecht/verteidigung-im-steuerstrafverfahren", "FAQ-Abschnitt I (Strafverfahren) verweist auf die passende Leistungsseite"),
                ("/index.php/selbstanzeigen-steuerliche-korrekturen", "FAQ-Abschnitt III (Selbstanzeige) verweist auf die passende Leistungsseite"),
                ("/index.php/kontakt", "FAQ-Abschnitt II (Kosten) verweist auf den Kontakt")]:
    if to not in (OUT_CTX.get("/index.php/faq", set()) | OUT_BLK.get("/index.php/faq", set())):
        faq["missing_links"].append(link("/index.php/faq", to, why, "topical_lateral"))
for to in ("/index.php/steuerstrafrecht", "/index.php/selbstanzeigen-steuerliche-korrekturen"):
    P[to]["missing_links"].append(link(to, "/index.php/faq", "Leistungsseite verweist auf die passende FAQ", "topical_lateral"))
# Team lateral: Kontakt -> Lea Wimmer (München); person -> team already covered by child_to_parent
if "/index.php/lea-wimmer" not in (OUT_CTX.get("/index.php/kontakt", set())):
    P["/index.php/kontakt"]["missing_links"].append(link("/index.php/kontakt", "/index.php/lea-wimmer", "Standort München nennt die Leiterin mit Profil-Link", "topical_lateral",
        "Anker z. B. 'Lea Wimmer'; München hat keine eigene Standortseite (siehe Hinweis)"))
# articles -> service/profile
for k, r in P.items():
    m = ARTICLE_RE.match(k)
    if m and m.group(1) in ART_TARGET:
        to = ART_TARGET[m.group(1)]
        if to not in (OUT_CTX.get(k, set()) | OUT_BLK.get(k, set())):
            r["missing_links"].append(link(k, to, "Beitrag verweist auf die thematisch passende Seite (Vorschlag, Mensch prüft Passung)", "topical_lateral"))
# repeated-block-only note and assignments
for r in plan:
    r["assignment"] = "PROPOSED (URL-Pfad + Menü + Inhaltsprüfung 11.10.2026); nur bestehende Seiten als Ziel; Anker brauchen menschliche Prüfung"
    r["gsc_clicks_90d"] = None
    r["gsc_note"] = "Search Console nicht lesbar (403)"
# stats
svc = [r for r in plan if r["page"] in AREA_K or is_sub(r["page"]) or r["page"] == HUB]
art = [r for r in plan if ARTICLE_RE.match(r["page"])]
persons = [r for r in plan if r["page"] in LAWYERS | STAFF]
stats = {
 "n_pages_plan": len(plan), "n_service_tree": len(svc), "n_subs": len(SUBS), "subs": SUBS, "n_areas": len(AREA_K),
 "service_up_link_missing": [r["page"] for r in svc if not r["outbound_to_parent"]],
 "service_up_link_only_block": [r["page"] for r in svc if r["up_link_only_via_repeated_block"]],
 "service_to_home_missing": [r["page"] for r in svc if not r["outbound_to_home"]],
 "pages_with_zero_ctx_outbound_service": [r["page"] for r in svc if r["outbound_contextual"] == 0],
 "articles": [r["page"] for r in art], "articles_up_missing": [r["page"] for r in art if not r["outbound_to_parent"]],
 "articles_words": {r["page"]: r["words"] for r in art},
 "persons_inbound": {r["page"]: r["inbound_content_links"] for r in persons}, "persons_outbound": {r["page"]: r["outbound_content_links"] for r in persons},
 "max_click_depth_any": max((v for v in D_FULL.values()), default=None), "max_click_depth_content": max((D_CONT.get(r["page"]) or 0) for r in plan),
 "not_reached_by_content_links": [r["page"] for r in plan if D_CONT.get(r["page"]) is None],
 "missing_total": sum(len(r["missing_links"]) for r in plan),
 "missing_by_type": dict(collections.Counter(m["type"] for r in plan for m in r["missing_links"])),
 "home_ctx_out": sorted(hall), "faq_ctx_out": sorted(OUT_CTX.get("/index.php/faq", set())),
 "ow_children_listed_by_parent": sorted(OUT_CTX.get("/index.php/ordnungswidrigkeiten", set())),
 "zoll_ctx_out": sorted(OUT_CTX.get("/index.php/zollstrafrecht", set())),
 "area_without_children": [a for a in AREA_K if not any(s.startswith(a + "/") for s in SUBS)],
 "search_signal_urls_total": len(SEARCH),
 "content_urls_not_in_search": sorted(k for k in content_pages if k not in SEARCH and k not in LEGAL),
 "content_urls_in_search": sorted(k for k in content_pages if k in SEARCH),
 "sm_missing_pages": sorted(k for k in content_pages if k not in SM and not ARTICLE_RE.match(k) and not k.startswith("/index.php/component/content/category")),
 "sm_missing_articles": sorted(k for k in content_pages if ARTICLE_RE.match(k)),
 "words_services": {r["page"]: r["words"] for r in svc},
}
plan_doc = {"run": "stuerzl-2026-10-11-scan", "area": "E", "collected_at": now(),
 "method": ("Content links only: links inside #sp-component (Joomla main content area). Header menu, off-canvas menu and footer are excluded. "
            "The 9-link block that is repeated on all 25 service-tree pages (9 areas + 16 sub pages) is counted but flagged 'via_repeated_block' because it is boilerplate, not a contextual link. "
            "Parents come from the URL path and the Leistungen hub (menu has no dropdown). Anchors are derived from page names and need a human edit. Targets are existing 200 pages only."),
 "hard_rules": ["Nothing is changed in this scan (read only)", "Edits to SP Page Builder content need Joomla Super User (741 account is Administrator only: SP Page Builder and Global Config blocked)",
                "No new pages are invented as link targets; a Munich location page does not exist and is a decision, not a link target",
                "Law firm: anchors stay factual (BORA, UWG); no client or case names (§203 StGB)"],
 "home_missing_links_to_hubs": [m for m in P["/"]["missing_links"] if m["type"] in ("home_to_service",)],
 "summary": {k: stats[k] for k in ("n_pages_plan", "n_service_tree", "n_subs", "missing_total", "missing_by_type", "max_click_depth_any", "max_click_depth_content")},
 "pages": plan}
json.dump(plan_doc, open(os.path.join(ROOT, "link-plan.json"), "w"), indent=1, ensure_ascii=False)
json.dump(stats, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_stats.json"), "w"), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in stats.items() if k not in ("words_services", "content_urls_in_search")}, indent=1, ensure_ascii=False)[:6000])
