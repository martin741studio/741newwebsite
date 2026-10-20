"""D02/D03: category feed URLs and malformed pagination links found in the baseline crawl and in page HTML. GET only."""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *
B="https://www.stuerzl-steuerstrafrecht.de"
U=[B+"/index.php/component/content/category/allgemein?format=feed&type=rss&Itemid=228",
   B+"/index.php/component/content/category/allgemein?format=feed&type=atom&Itemid=228",
   B+"/index.php/component/content/category/allgemein?Itemid=228&start=10",
   B+"/index.php/component/content/category/allgemein?Itemid=0&amp;start=10",
   B+"/index.php/component/content/category/allgemein?Itemid=0&start=10"]
rows=[]
for u in U:
    chain,r,err=fetch_chain(u)
    row={"url":u,"chain":chain,"final_status":r.status_code if r is not None else None,"error":err}
    if r is not None:
        ct=r.headers.get("Content-Type"); row["content_type"]=ct
        t=re.search(r"<title[^>]*>(.*?)</title>", r.text, re.I|re.S); row["title"]=re.sub(r"\s+"," ",t.group(1)).strip()[:120] if t else None
        c=re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*>', r.text, re.I); row["canonical_tag"]=c.group(0)[:250] if c else None
        row["bytes"]=len(r.content)
    rows.append(row); print(row["final_status"], row.get("content_type"), u[-80:], row.get("canonical_tag"))
# raw pagination href in saved Aktuelles/category page
raw=[]
for fn in os.listdir(os.path.join(EVID,"area_d")):
    if fn.startswith("EV-D-page-") and "category_allgemein" in fn:
        h=open(os.path.join(EVID,"area_d",fn),encoding="utf-8",errors="replace").read()
        for m in re.finditer(r'href="([^"]*start=10[^"]*)"', h): raw.append({"file":fn,"raw_href":m.group(1)})
        for m in re.finditer(r'<link[^>]+(?:rss|atom)[^>]*>', h): raw.append({"file":fn,"feed_link_tag":m.group(0)[:250]})
print(raw[:6])
save_evidence("EV-D-feeds-pagination", json.dumps({"collected_at":now(),"rows":rows,"raw_hrefs":raw},ensure_ascii=False,indent=1),"json","requests GET + regex on saved HTML","feed and pagination URLs of the news category")
