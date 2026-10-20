#!/usr/bin/env python3 -I
"""Area E Joomla variant probes. READ ONLY. GET only (redirects not followed beyond recording, then followed up to 6 hops). 0.3 s delay."""
import sys, os, json, re, time, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import requests
from bs4 import BeautifulSoup
from e_lib import save_evidence, now
S = requests.Session(); S.headers.update({"User-Agent": "741-unburning-scan/1.0"})
W = "https://www.stuerzl-steuerstrafrecht.de"
A = "https://stuerzl-steuerstrafrecht.de"
PROBES = [
 ("scheme_http_www", "http://www.stuerzl-steuerstrafrecht.de/"),
 ("scheme_http_apex", "http://stuerzl-steuerstrafrecht.de/"),
 ("apex_deep", A + "/index.php/kanzlei"),
 ("home_index_php", W + "/index.php"),
 ("home_index_php_slash", W + "/index.php/"),
 ("home_index_php_home", W + "/index.php/home"),
 ("home_home", W + "/home"),
 ("noindexphp_kanzlei", W + "/kanzlei"),
 ("noindexphp_leistungen", W + "/leistungen"),
 ("noindexphp_steuerstrafrecht", W + "/steuerstrafrecht"),
 ("noindexphp_faq", W + "/faq"),
 ("trailing_slash", W + "/index.php/kanzlei/"),
 ("uppercase", W + "/index.php/Kanzlei"),
 ("tmpl_component", W + "/index.php/kanzlei?tmpl=component"),
 ("print", W + "/index.php/kanzlei?print=1"),
 ("format_pdf", W + "/index.php/kanzlei?format=pdf"),
 ("format_feed_rss", W + "/index.php/aktuelles?format=feed&type=rss"),
 ("format_feed_atom", W + "/index.php/aktuelles?format=feed&type=atom"),
 ("home_feed", W + "/?format=feed&type=rss"),
 ("utm_param", W + "/index.php/kanzlei?utm_source=test"),
 ("users_login", W + "/index.php/component/users/login"),
 ("users_view_login", W + "/index.php/component/users/?view=login"),
 ("users_registration", W + "/index.php/component/users/registration"),
 ("users_reset", W + "/index.php/component/users/reset"),
 ("users_remind", W + "/index.php/component/users/remind"),
 ("administrator", W + "/administrator/"),
 ("search", W + "/index.php/component/search/?searchword=steuer&searchphrase=all"),
 ("finder", W + "/index.php/component/finder/search?q=steuer"),
 ("tags", W + "/index.php/component/tags/"),
 ("contact_component", W + "/index.php/component/contact/"),
 ("category_no_itemid", W + "/index.php/component/content/category/allgemein"),
 ("category_start10", W + "/index.php/component/content/category/allgemein?Itemid=228&start=10"),
 ("category_start20", W + "/index.php/component/content/category/allgemein?Itemid=228&start=20"),
 ("category_feed", W + "/index.php/component/content/category/allgemein?Itemid=228&format=feed&type=rss"),
 ("article_com_content", W + "/index.php?option=com_content&view=article&id=1"),
 ("featured", W + "/index.php/component/content/featured"),
 ("404_test", W + "/index.php/this-page-does-not-exist-741"),
 ("404_test_root", W + "/this-page-does-not-exist-741"),
 ("schwerpunkte", W + "/index.php/schwerpunkte"),
 ("robots_txt", W + "/robots.txt"),
 ("humans_txt", W + "/humans.txt"),
 ("llms_txt", W + "/llms.txt"),
]
rows = []
for name, url in PROBES:
    chain = []; cur = url; r = None; err = None
    for _ in range(7):
        try:
            r = S.get(cur, allow_redirects=False, timeout=40)
        except Exception as e:
            err = f"{type(e).__name__}: {e}"; chain.append({"url": cur, "status": None, "error": err}); break
        time.sleep(0.3)
        chain.append({"url": cur, "status": r.status_code, "location": r.headers.get("Location")})
        if r.status_code in (301, 302, 303, 307, 308) and r.headers.get("Location"):
            cur = urllib.parse.urljoin(cur, r.headers["Location"]); continue
        break
    row = {"name": name, "url": url, "chain": chain, "final_status": r.status_code if r is not None and not err else None, "error": err}
    if r is not None and not err:
        ct = r.headers.get("Content-Type", ""); row["content_type"] = ct; row["x_robots_tag"] = r.headers.get("X-Robots-Tag")
        row["bytes"] = len(r.content)
        if "html" in ct.lower():
            s = BeautifulSoup(r.content.decode("utf-8", "replace"), "html.parser")
            t = s.find("title"); row["title"] = t.get_text(strip=True) if t else None
            mr = s.find("meta", attrs={"name": re.compile("^robots$", re.I)}); row["meta_robots"] = mr.get("content") if mr else None
            c = s.find("link", rel=lambda v: v and "canonical" in v); row["canonical"] = c.get("href") if c else None
            row["h1"] = [h.get_text(" ", strip=True) for h in s.find_all("h1")][:4]
        else:
            row["body_head"] = r.content[:200].decode("utf-8", "replace")
    rows.append(row)
    print(name, row["final_status"], [c["status"] for c in chain], row.get("meta_robots"), row.get("canonical"))
save_evidence("EV-E-probes", json.dumps({"collected_at": now(), "rows": rows}, indent=1, ensure_ascii=False), "json", "python requests (GET only)",
              "41 GET probes of Joomla URL variants (scheme, host, index.php, trailing slash, case, tmpl/print/pdf/feed, users, search, category pagination, 404); script scripts/E/e3_probes.py")
