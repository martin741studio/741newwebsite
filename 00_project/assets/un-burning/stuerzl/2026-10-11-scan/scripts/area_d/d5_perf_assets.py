"""D07/perf re-verify (no rendering tool allowed): TTFB x3, asset counts and byte weight of the home page, assets under robots-disallowed paths, PSI attempt."""
import sys, os, json, re, time, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *
from bs4 import BeautifulSoup

HOME = "https://www.stuerzl-steuerstrafrecht.de/"
ttfb = []
for i in range(3):
    t0 = time.perf_counter()
    r = SESS.get(HOME, stream=True, timeout=40)
    ttfb.append(round(time.perf_counter() - t0, 2))
    r.close()
    time.sleep(DELAY)
r = SESS.get(HOME, timeout=40)
html = r.text
soup = BeautifulSoup(html, "html.parser")
assets = {"js": set(), "css": set(), "img": set()}
for s in soup.find_all("script", src=True):
    assets["js"].add(urllib.parse.urljoin(HOME, s["src"]))
for l in soup.find_all("link", href=True):
    if "stylesheet" in (l.get("rel") or []):
        assets["css"].add(urllib.parse.urljoin(HOME, l["href"]))
for i in soup.find_all("img"):
    for a in ("src", "data-src"):
        if i.get(a):
            assets["img"].add(urllib.parse.urljoin(HOME, i[a]))
for m in re.finditer(r"url\(['\"]?([^'\")]+\.(?:jpe?g|png|webp|gif|svg))", html, re.I):
    assets["img"].add(urllib.parse.urljoin(HOME, m.group(1)))
disallow = ["/administrator/", "/bin/", "/cache/", "/cli/", "/components/", "/includes/", "/installation/", "/language/", "/layouts/", "/libraries/", "/logs/", "/modules/", "/plugins/", "/tmp/"]
rows, totals, blocked = [], {"js": 0, "css": 0, "img": 0}, []
for kind, urls in assets.items():
    for u in sorted(urls):
        host = urllib.parse.urlparse(u).netloc
        path = urllib.parse.urlparse(u).path
        row = {"kind": kind, "url": u, "own_host": host.endswith("stuerzl-steuerstrafrecht.de")}
        if any(path.startswith(d) for d in disallow) and row["own_host"]:
            row["blocked_by_robots"] = True
            blocked.append(u)
        try:
            rr = SESS.get(u, timeout=40)
            row["status"] = rr.status_code
            row["bytes"] = len(rr.content)
            if rr.status_code == 200:
                totals[kind] += len(rr.content)
        except Exception as e:
            row["error"] = f"{type(e).__name__}: {str(e)[:100]}"
        rows.append(row)
        time.sleep(DELAY)
        print(row.get("status"), kind, row.get("bytes"), u[:100], "BLOCKED" if row.get("blocked_by_robots") else "")
res = {"collected_at": now(), "home": HOME, "ttfb_s_3_runs": ttfb, "html_bytes": len(r.content),
       "counts": {k: len(v) for k, v in assets.items()}, "bytes_by_kind": totals, "own_host_assets_blocked_by_robots": blocked, "assets": rows}
print(ttfb, res["counts"], totals, len(blocked))
save_evidence("EV-D-perf-assets", json.dumps(res, ensure_ascii=False, indent=1), "json", "requests GET (curl-equivalent timing, no rendering)",
              f"TTFB x3 + GET of every asset referenced by the home page HTML, UA {UA}", note="static asset count and weight only; LCP needs a rendering tool and was NOT measured")
# PSI attempt (free Google API, keyless)
psi_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + urllib.parse.quote(HOME, safe="") + "&strategy=mobile&category=PERFORMANCE"
pr = SESS.get(psi_url, timeout=120)
save_evidence("EV-D-psi-attempt", pr.content, "json", "requests GET (PageSpeed Insights API v5, keyless)", "GET runPagespeed mobile for the home page", note=f"status={pr.status_code}; quota error means unreadable")
print("psi", pr.status_code)
