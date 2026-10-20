#!/usr/bin/env python3
"""Convert the output of scripts/gsc-client-export.mjs into the two evidence files the content pool reads.

Usage: gsc_to_tsv.py <gsc-api.json> <03-demand dir>
Writes: gsc-queries-90d.tsv (query, clicks, impressions, position) and gsc-pages-90d.tsv (path, clicks, impressions).
Totals: GSC hides rare (anonymised) queries. The sum of the query rows is lower than the sum of the page rows. Both are written in the file header.
"""
import json, sys
from urllib.parse import urlparse, unquote

src, out = sys.argv[1], sys.argv[2].rstrip("/")
d = json.load(open(src))
rng = f"{d['range']['start']} to {d['range']['end']}"
q = d["queries"]
pg = d["pages"]
qc, qi = sum(r["clicks"] for r in q), sum(r["impressions"] for r in q)
pc, pi = sum(r["clicks"] for r in pg), sum(r["impressions"] for r in pg)
with open(f"{out}/gsc-queries-90d.tsv", "w") as f:
    f.write(f"# Source: Google Search Console API via scripts/gsc-client-export.mjs, property {d['site']}, {rng} ({d['range']['days']} days), Web.\n")
    f.write(f"# {len(q)} queries listed. Query rows add up to {qc} clicks and {qi} impressions. Page rows add up to {pc} clicks and {pi} impressions (GSC hides anonymised queries).\n")
    f.write("query\tclicks\timpressions\tposition\n")
    for r in sorted(q, key=lambda r: -r["impressions"]):
        f.write(f"{r['keys'][0]}\t{r['clicks']}\t{r['impressions']}\t{r['position']}\n")
with open(f"{out}/gsc-pages-90d.tsv", "w") as f:
    f.write(f"# Source: Google Search Console API via scripts/gsc-client-export.mjs, property {d['site']}, {rng}, Web. {len(pg)} pages.\n")
    f.write("path\tclicks\timpressions\n")
    for r in sorted(pg, key=lambda r: -r["clicks"] * 1000 - r["impressions"]):
        f.write(f"{unquote(urlparse(r['keys'][0]).path) or '/'}\t{r['clicks']}\t{r['impressions']}\n")
print(json.dumps({"range": rng, "queries": len(q), "query_clicks": qc, "query_impr": qi, "pages": len(pg), "page_clicks": pc, "page_impr": pi}))
