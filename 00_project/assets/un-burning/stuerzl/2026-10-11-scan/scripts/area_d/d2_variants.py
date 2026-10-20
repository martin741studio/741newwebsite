"""D02: host/URL variants, redirect chains, canonical per variant, sitemap/robots/system URLs. GET only."""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *

B = "stuerzl-steuerstrafrecht.de"
V = [
    ("host", f"http://{B}/"), ("host", f"http://www.{B}/"), ("host", f"https://{B}/"), ("host", f"https://www.{B}/"),
    ("host_deep", f"http://www.{B}/index.php/kanzlei"), ("host_deep", f"https://{B}/index.php/kanzlei"),
    ("index_php", f"https://www.{B}/index.php"), ("index_php", f"https://www.{B}/index.php/"),
    ("index_php", f"https://www.{B}/index.php/home"), ("clean_url", f"https://www.{B}/kanzlei"),
    ("clean_url", f"https://www.{B}/steuerstrafrecht"),
    ("trailing_slash", f"https://www.{B}/index.php/kanzlei/"), ("trailing_slash", f"https://www.{B}/index.php/kanzlei"),
    ("case", f"https://www.{B}/index.php/Kanzlei"),
    ("param", f"https://www.{B}/index.php/kanzlei?utm_source=test"),
    ("param", f"https://www.{B}/?foo=bar"),
    ("joomla_raw", f"https://www.{B}/index.php?option=com_content&view=featured"),
    ("joomla_raw", f"https://www.{B}/index.php/component/content/category/allgemein"),
    ("forum_linked", f"https://www.{B}/index.php/lina"),
    ("forum_linked", f"https://www.{B}/images/2023/11/10/portrait_kanzlei2.jpg"),
    ("forum_linked", f"https://www.{B}/images/layout/header-team-11.jpg"),
    ("system", f"https://www.{B}/sitemap.xml"), ("system", f"https://{B}/sitemap.xml"), ("system", f"https://www.{B}/sitemap_index.xml"),
    ("system", f"https://www.{B}/index.php/sitemap"), ("system", f"https://www.{B}/index.php?option=com_xmap&view=xml&id=1"),
    ("system", f"https://www.{B}/robots.txt"), ("system", f"https://www.{B}/llms.txt"),
    ("system", f"https://www.{B}/index.php/schwerpunkte"), ("system", f"https://www.{B}/index.php/zzz-nicht-vorhanden-ub-test"),
    ("system", f"https://www.{B}/zzz-nicht-vorhanden-ub-test"),
    ("system", f"https://www.{B}/index.php/search"), ("system", f"https://www.{B}/index.php?s=test"),
    ("system", f"https://www.{B}/index.php/component/search/?searchword=test"),
    ("system", f"https://www.{B}/administrator/"),
    ("system", f"https://www.{B}/index.php/component/users/login"),
]
rows = []
for kind, u in V:
    chain, r, err = fetch_chain(u)
    row = {"kind": kind, "url": u, "chain": chain, "hops": max(0, len(chain) - 1), "final_url": chain[-1]["url"], "error": err}
    if r is not None:
        row["final_status"] = r.status_code
        ct = (r.headers.get("Content-Type") or "")
        row["content_type"] = ct
        row["x_robots_tag"] = r.headers.get("X-Robots-Tag")
        if "html" in ct.lower() or ct.startswith("text/plain"):
            txt = r.text
            m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*>', txt, re.I)
            row["canonical_tag"] = m.group(0)[:300] if m else None
            m2 = re.search(r'<meta[^>]+name=["\']robots["\'][^>]*>', txt, re.I)
            row["meta_robots"] = m2.group(0)[:200] if m2 else None
            t = re.search(r"<title[^>]*>(.*?)</title>", txt, re.I | re.S)
            row["title"] = re.sub(r"\s+", " ", t.group(1)).strip()[:200] if t else None
            if u.endswith("robots.txt"):
                row["robots_txt_body"] = txt
    else:
        row["final_status"] = None
    rows.append(row)
    print(row["final_status"], row["hops"], u, "->", row["final_url"] if row["final_url"] != u else "", row.get("canonical_tag"))
save_evidence("EV-D-variants", json.dumps({"collected_at": now(), "rows": rows}, ensure_ascii=False, indent=1), "json",
              "requests GET (manual redirect follow)", f"{len(V)} URL variants of {B}, UA {UA}, delay {DELAY}s")
# robots.txt raw
for row in rows:
    if row["url"].endswith("/robots.txt") and "robots_txt_body" in row and row["url"].startswith("https://www"):
        save_evidence("EV-D-robots", row["robots_txt_body"], "txt", "requests GET", f"GET {row['url']}", note=f"status={row['final_status']}")
