#!/usr/bin/env python3
"""Gate G6b: build and check JSON-LD that matches the visible page.

    python3 schema_tool.py make  <run_dir> [--page 05-final/page.md]   -> writes 05-final/schema.jsonld
    python3 schema_tool.py check <run_dir> [--page 05-final/page.md] [--json]

Evidence (Ahrefs 2026, Google AI features doc 2025/2026): schema gives no proven ranking or AI-citation lift and FAQ rich results ended in 2026.
So schema is kept honest and small: WebPage + BreadcrumbList + LegalService/Organization (confirmed NAP only) + Person (person pages) + Article (blog).
FAQPage only if brief.schema_faq is true. Markup must match visible text. No placeholder text in markup.
brief.nap_file points to the locked data (see assets/<client>/nap.json).
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import PLACEHOLDER_RE, TECH_MARK, frontmatter, load_json, strip_frontmatter, visible_text  # noqa: E402

ROOT = Path("/Users/martindrendel/741website")


def faq_pairs(raw):
    body = strip_frontmatter(raw).split(TECH_MARK, 1)[0]
    m = re.search(r"<!--\s*S\d\d\s+\w+\s*\|[^>]*element:\s*faq[^>]*-->(.*?)<!--\s*/S\d\d\s*-->", body, flags=re.S)
    if not m:
        return []
    out = []
    for q, a in re.findall(r"(?ms)^###\s+(.+?\?)\s*$(.*?)(?=^###|\Z)", m.group(1)):
        out.append((q.strip(), visible_text(a, keep_placeholders=True).strip()))
    return out


def breadcrumbs(brief, base):
    node = brief.get("sitetree_node")
    st = next((p for p in [ROOT / f"00_project/assets/{brief.get('client_slug')}/content-pool/05-sitetree/sitetree.json"] if p.exists()), None)
    items = [("Startseite", base + "/")]
    if node and st:
        N = {n["id"]: n for n in load_json(st)["nodes"]}
        chain, cur = [], node
        while cur in N and cur != "ST-00" and len(chain) < 6:
            chain.append(N[cur]); cur = N[cur].get("parent")
        sp = ROOT / f"00_project/assets/{brief.get('client_slug')}/slugs.json"
        slugs = load_json(sp)["slugs"] if sp.exists() else {}
        for n in reversed(chain):
            slug = (brief.get("url_slug") if n["id"] == node else None) or slugs.get(n["id"]) or n.get("slug") or ""
            if slug:
                items.append((re.sub(r"\s*\(.*?\)\s*$", "", n["title"]), base + slug))
    return items


def make(run, page_rel):
    raw = (run / page_rel).read_text(encoding="utf-8")
    brief = load_json(run / "01-brief/brief.json")
    fm = frontmatter(raw)
    nap = load_json(Path(brief["nap_file"]) if Path(brief.get("nap_file", "")).is_absolute() else ROOT / brief["nap_file"])
    base = nap["base_url"]
    url = base + (brief.get("url_slug") or fm.get("url_slug") or "/")
    org_id = base + "/" + nap["organization"]["id"]
    g = []
    wp = {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": fm.get("title", ""), "description": fm.get("meta", ""), "inLanguage": "de",
          "isPartOf": {"@id": base + "/#website"}, "breadcrumb": {"@id": url + "#breadcrumb"}}
    g.append(wp)
    bc = breadcrumbs(brief, base)
    g.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb",
              "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(bc)]})
    org = {"@type": nap["organization"]["type"], "@id": org_id, "name": nap["organization"]["name"], "url": base + "/", "email": nap["organization"]["email"]}
    locs = []
    for L in nap["locations"]:
        addr = {"@type": "PostalAddress", "addressLocality": L["city"], "postalCode": L["postalCode"], "addressCountry": L["country"]}
        if L.get("street") and str(L["status"]).startswith("bestätigt"):
            addr["streetAddress"] = L["street"]
        locs.append({"@type": "LegalService", "name": nap["organization"]["name"] + " " + L["city"], "telephone": L["telephone"], "address": addr, "parentOrganization": {"@id": org_id}})
    org["department"] = locs
    if nap["organization"].get("sameAs"):
        org["sameAs"] = nap["organization"]["sameAs"]
    g.append(org)
    pt = brief.get("page_type")
    # Person: by URL match against nap.json people, not only on practitioner-typed pages,
    # so a team roster or a mention on another page still resolves the same node.
    slug = brief.get("url_slug", "")
    pid = next((k for k, v in nap.get("people", {}).items() if v.get("url_slug") == slug), None)
    if pid:
        p = nap["people"][pid]
        person = {"@type": "Person", "@id": url + "#person", "name": p["name"], "jobTitle": p.get("jobTitle", ""), "url": url, "worksFor": {"@id": org_id}}
        if p.get("credentials"):
            person["hasCredential"] = [{"@type": "EducationalOccupationalCredential", "name": c} for c in p["credentials"]]
        if p.get("sameAs"):
            person["sameAs"] = p["sameAs"]
        g.append(person)
        wp["about"] = {"@id": url + "#person"}
    # Service: any page that sells one thing (service, location, cost) gets a minimal Service node,
    # tied to the Organization and, for location pages, to that office.
    if pt in ("service", "location", "cost"):
        svc = {"@type": "Service", "@id": url + "#service", "serviceType": fm.get("keyword") or brief.get("keyword_primary") or fm.get("title", ""),
               "provider": {"@id": org_id}, "url": url}
        city = brief.get("local_city")
        if city:
            svc["areaServed"] = {"@type": "City", "name": city}
        g.append(svc)
        wp["mainEntity"] = {"@id": url + "#service"}
    if pt == "blog":
        a = brief.get("byline", {})
        g.append({"@type": "Article", "@id": url + "#article", "headline": fm.get("title", ""), "inLanguage": "de",
                  "datePublished": fm.get("published", ""), "dateModified": fm.get("last_checked", ""),
                  "author": {"@type": "Person", "name": a.get("name", "")}, "publisher": {"@id": org_id}, "mainEntityOfPage": {"@id": url + "#webpage"}})
    if brief.get("schema_faq"):
        pairs = [(q, a) for q, a in faq_pairs(raw) if not PLACEHOLDER_RE.search(a)]
        if pairs:
            g.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]})
    doc = {"@context": "https://schema.org", "@graph": g}
    out = run / "05-final/schema.jsonld"
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    return out


def check(run, page_rel):
    raw = (run / page_rel).read_text(encoding="utf-8")
    brief = load_json(run / "01-brief/brief.json")
    fm = frontmatter(raw)
    fails, warns = [], []
    f = run / "05-final/schema.jsonld"
    if not f.exists():
        return ["schema.jsonld fehlt (schema_tool.py make)"], []
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"schema.jsonld ist kein gültiges JSON: {e}"], []
    txt = json.dumps(d, ensure_ascii=False)
    if d.get("@context") != "https://schema.org":
        fails.append("@context fehlt")
    g = d.get("@graph", [])
    types = {x.get("@type") for x in g}
    for need in ("WebPage", "BreadcrumbList"):
        if need not in types:
            fails.append(f"{need} fehlt")
    if PLACEHOLDER_RE.search(txt) or "[FEHLT" in txt or "TODO" in txt:
        fails.append("Platzhalter im Markup")
    wp = next((x for x in g if x.get("@type") == "WebPage"), {})
    if wp.get("name") != fm.get("title"):
        fails.append("WebPage.name ist nicht der Seitentitel")
    for x in g:
        if x.get("@type") == "Organization" or x.get("@type") == "LegalService" and x.get("@id", "").endswith("#kanzlei"):
            for dep in x.get("department", []):
                if "streetAddress" not in dep.get("address", {}):
                    warns.append(f"{dep['name']}: Straße fehlt im Markup (Adresse nicht bestätigt)")
        if x.get("@type") == "Person" and not x.get("name"):
            fails.append("Person ohne Name")
        if x.get("@type") == "Article":
            if not x.get("datePublished"):
                warns.append("Article ohne datePublished (erst nach Freigabe des Kunden setzen)")
            if not x.get("author", {}).get("name"):
                warns.append("Article ohne Autorenname")
        if x.get("@type") == "FAQPage":
            vis = {q for q, _ in faq_pairs(raw)}
            marked = {e["name"] for e in x.get("mainEntity", [])}
            if not marked <= vis:
                fails.append("FAQPage enthält Fragen, die nicht sichtbar auf der Seite stehen")
    for x in g:
        for k in ("url", "item"):
            v = x.get(k)
            if isinstance(v, str) and not v.startswith("https://"):
                fails.append(f"{k} nicht absolut: {v}")
    if brief.get("page_type") == "practitioner" and "Person" not in types:
        fails.append("Person fehlt auf Personenseite")
    if brief.get("page_type") == "blog" and "Article" not in types:
        fails.append("Article fehlt auf Blogseite")
    return fails, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["make", "check"])
    ap.add_argument("run_dir")
    ap.add_argument("--page", default="05-final/page.md")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    run = Path(a.run_dir)
    if a.cmd == "make":
        print(make(run, a.page))
        return 0
    fails, warns = check(run, a.page)
    if a.json:
        print(json.dumps({"pass": not fails, "fails": fails, "warns": warns}, ensure_ascii=False, indent=1))
    else:
        print(f"G6b schema: {'FAIL' if fails else 'PASS'}")
        for f in fails: print("  FAIL ", f)
        for w in warns: print("  warn ", w)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
