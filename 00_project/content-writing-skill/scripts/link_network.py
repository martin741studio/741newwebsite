#!/usr/bin/env python3
"""Gate G6c: internal link network over all written pages of one client.

    python3 link_network.py <content-writing-dir> [--slugs assets/<client>/slugs.json] [--final] [--json]

Reads <dir>/*/05-final/page.md and <dir>/*/01-brief/brief.json. Reports incoming copy links per page, links to targets
that are not in the sitemap, slug differences against the planned URL list and pages that share a primary keyword.
Evidence is weak on any fixed link number (Zyppy 2023, Ahrefs 2024), so: fail only on broken targets and keyword clashes;
fewer than 2 incoming links is a warning, and a fail with --final (all pages written).
Writes <dir>/LINK-NETWORK.md.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import TECH_MARK, load_json, strip_frontmatter  # noqa: E402


def norm(u):
    u = u.split("#")[0].split("?")[0].strip().lower()
    if not u.startswith("/"):
        return u
    return "/" + u.strip("/") + "/" if u.strip("/") else "/"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("--slugs")
    ap.add_argument("--final", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    d = Path(a.dir)
    slugs = {}
    sp = Path(a.slugs) if a.slugs else next(iter(sorted((d.parent).glob("slugs.json"))), None)
    if sp and sp.exists():
        slugs = load_json(sp)["slugs"]
    valid = {norm(v) for v in slugs.values() if v}
    pages = {}
    for run in sorted(p for p in d.iterdir() if p.is_dir()):
        pg, br = run / "05-final/page.md", run / "01-brief/brief.json"
        if not (pg.exists() and br.exists()):
            continue
        b = load_json(br)
        node = b.get("sitetree_node")
        url = norm(b.get("url_slug") or slugs.get(node, ""))
        body = strip_frontmatter(pg.read_text(encoding="utf-8")).split(TECH_MARK, 1)[0]
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
        links = [norm(x) for x in re.findall(r"\]\((/[^)\s]*)\)", body)]
        pages[run.name] = {"ptype": b.get("page_type"), "node": node, "url": url, "kw": (b.get("keyword_primary") or "").lower(), "links": links, "planned": norm(slugs.get(node, "")) if node else ""}
    fails, warns = [], []
    by_url = {p["url"]: n for n, p in pages.items()}
    incoming = {n: [] for n in pages}
    for n, p in pages.items():
        for l in p["links"]:
            if l == p["url"]:
                continue
            if l in by_url:
                incoming[by_url[l]].append(n)
            elif valid and l not in valid:
                fails.append(f"{n}: Link auf {l} steht nicht in der Sitemap")
        if p["planned"] and p["url"] and p["planned"] != p["url"]:
            warns.append(f"{n}: Slug {p['url']} weicht vom geplanten {p['planned']} ab")
    kws = {}
    for n, p in pages.items():
        if p["kw"]:
            kws.setdefault(p["kw"], []).append(n)
    for k, v in kws.items():
        if len(v) > 1:
            fails.append(f'Gleiches Haupt-Keyword "{k}" auf {len(v)} Seiten: {", ".join(v)} (Kannibalisierung)')
    # contextual link count per page: 3 to 8 is the library range (warn outside, 25+ is a hub smell)
    for n, p in pages.items():
        k = len(set(p["links"]))
        if k < 3:
            warns.append(f"{n}: nur {k} interne Textlinks (Bibliothek: 3 bis 8)")
        elif k > 25:
            fails.append(f"{n}: {k} interne Links im Text (über 25)")
        elif k > 8:
            warns.append(f"{n}: {k} interne Textlinks (über 8)")
    # hubs and pillars must link down to their children (cluster logic)
    stp = next(iter(sorted(d.parent.glob("content-pool/05-sitetree/sitetree.json"))), None)
    if stp:
        N = {x["id"]: x for x in load_json(stp)["nodes"]}
        for n, p in pages.items():
            kids = [k for k, x in N.items() if x.get("parent") == p["node"] and k in slugs and slugs[k] and x.get("status") != "Bleibt"]
            miss = [k for k in kids if norm(slugs[k]) not in set(p["links"])]
            if kids and miss and N[p["node"]].get("kind") == "hub":
                warns.append(f"{n} (Hub): verlinkt nicht auf {', '.join(miss[:6])}")
    # similarity between our own pages (scaled-content guard): shared 5-word shingles
    def sh(txt):
        w = re.findall(r"\w+", txt.lower())
        return {" ".join(w[i:i+5]) for i in range(max(0, len(w) - 4))}
    texts = {}
    for run in d.iterdir():
        pg = run / "05-final/page.md"
        if pg.exists():
            b2 = strip_frontmatter(pg.read_text(encoding="utf-8")).split(TECH_MARK, 1)[0]
            texts[run.name] = sh(re.sub(r"<!--.*?-->|\[von Kunde[^\]]*\]", "", b2, flags=re.S))
    names = sorted(texts)
    for i, x in enumerate(names):
        for y in names[i+1:]:
            inter = len(texts[x] & texts[y])
            small = max(1, min(len(texts[x]), len(texts[y])))
            if inter / small > 0.25:
                fails.append(f"Ähnlichkeit {int(100*inter/small)} % zwischen {x} und {y} (über 25 %, Scaled-Content-Risiko oder Kannibalisierung)")
    # title/H1 intent clash
    tt = {}
    for run in d.iterdir():
        pg = run / "05-final/page.md"
        if pg.exists():
            m = re.search(r"(?m)^title:\s*(.+)$", pg.read_text(encoding="utf-8"))
            if m: tt[run.name] = set(re.findall(r"[a-zäöüß]{5,}", m.group(1).lower())) - {"stürzl", "steuerstrafrecht"}
    ks = sorted(tt)
    for i, x in enumerate(ks):
        for y in ks[i+1:]:
            if tt[x] and tt[y] and len(tt[x] & tt[y]) / len(tt[x] | tt[y]) > 0.6:
                warns.append(f"Titel von {x} und {y} fast gleich (Intent-Überschneidung prüfen)")
    for n in pages:
        c = len(set(incoming[n]))
        if pages[n].get("ptype") == "news":
            continue
        if c < 2:
            (fails if a.final else warns).append(f"{n}: nur {c} eingehende Textlinks von anderen geschriebenen Seiten")
    out = {"pass": not fails, "fails": fails, "warns": warns,
           "table": {n: {"url": p["url"], "out": len(set(p["links"])), "in": len(set(incoming[n]))} for n, p in pages.items()}}
    md = ["# Link-Netz (G6c)", "", f"Seiten: {len(pages)}. Ergebnis: **{'PASS' if not fails else 'FAIL'}**", "", "| Seite | URL | ausgehende | eingehende |", "| --- | --- | --- | --- |"]
    md += [f"| {n} | {p['url']} | {len(set(p['links']))} | {len(set(incoming[n]))} |" for n, p in pages.items()]
    if fails: md += ["", "## Fehler"] + [f"- {x}" for x in fails]
    if warns: md += ["", "## Hinweise"] + [f"- {x}" for x in warns]
    (d / "LINK-NETWORK.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        print(f"G6c link network: {'FAIL' if fails else 'PASS'} ({len(pages)} pages)")
        for f in fails: print("  FAIL ", f)
        for w in warns[:12]: print("  warn ", w)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
