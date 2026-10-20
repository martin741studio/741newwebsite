import sys, json, collections
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import ROOT, now
R = json.load(open(ROOT + "/harm-register.json"))
cnt = collections.Counter((i["area"], i["severity"]) for i in R["items"])
run = {
 "run_id": R["run"]["run_id"], "client": "Praxis Suriya", "client_id": R["run"]["client_id"], "domain": "suriya-praxis.de", "mode": "dryrun",
 "started_at": "2026-10-11T01:21:28+02:00", "finished_at": now(), "timezone": "Europe/Berlin", "elapsed_note": "about 25 minutes wall clock",
 "params": R["run"]["params"],
 "cost": {"eur": 0, "dataforseo": 0, "firecrawl_credits_plan": 19, "note": "Firecrawl used plan credits: 5 searches (14+2 credits) and 3 scrapes (3 credits). No extra spend. No Falcon scan. No DataForSEO call."},
 "read_only_proof": {"writes_to_client_assets": 0, "wordpress_or_novamira_calls": 0, "supabase_writes": 0, "note": "Only GET requests, one auth POST for the Supabase login token, one OAuth token POST for Google, and POSTs to the read-only URL Inspection endpoint. Writes only inside this folder."},
 "counts_by_area_and_severity": {a: {s: cnt[(a, s)] for s in ("blocks_revenue", "leaks_link_power", "cosmetic")} for a in "ACDE"},
 "bedrock": R["run"]["bedrock"],
 "tools_tested": [
  {"tool": "GSC URL Inspection API (searchconsole.googleapis.com/v1/urlInspection/index:inspect, service account reporting-bot)", "result": "WORKS. 25 of 25 calls HTTP 200 with coverageState, canonical, last crawl time. Property https://suriya-praxis.de/ has siteFullUser. Daily limit 2000 URLs, so all 89 sitemap URLs fit in a later run. One extra call failed with 403 because of a script bug (output path sent as URL); that call is not in the evidence."},
  {"tool": "GSC API sites.list + sitemaps.list", "result": "WORKS. Found a stale submitted sitemap /slow-healing-blog/ with 2 errors. The 'indexed' counter in sitemaps.list shows 0 for all sitemaps and must not be trusted."},
  {"tool": "Local Falcon MCP (read)", "result": "FAILED / NOT AVAILABLE. No Local Falcon tool is connected in this session (tool search found none). GBP live name, address, phone, categories and reviews were NOT read. Fallback: BASELINE-REPORT.md section 11 (30.09.), marked client_stated."},
  {"tool": "firecrawl_search", "result": "WORKS. 5 queries, 20 results each (last one 5). Good for finding duplicate and wrong listings."},
  {"tool": "firecrawl_scrape", "result": "WORKS for cylex (curl got 403) and mapquest (curl got 202 empty). goyellow returned 410 Gone."},
  {"tool": "RDAP (rdap.denic.de) and whois (whois.denic.de)", "result": "WORKS technically, but DENIC does not disclose holder, registrar or contacts for .de. Only name servers (Cyon), status, last changed 2023-05-04. Holder check needs the registrar login or DENIC web-whois."},
  {"tool": "dig / curl", "result": "WORKS. NS, A, MX, TXT, SOA, headers."},
  {"tool": "Supabase PostgREST GET (admin login from standup.env)", "result": "WORKS. client_locations, client_citations (56 rows), scans (10 rows), clients. Only GET."},
  {"tool": "Google Autocomplete (suggestqueries.google.com)", "result": "WORKS, free. No negative suggestions for the brand."},
  {"tool": "Direct fetch of listings", "result": "PARTIAL. 200: infobel x2, theralupa x2, golocal, jameda, aerzte.de, xing, work5, instagram, wildcrumble, allgemeine-zeitung. Blocked or failed: cylex 403, 11880 403, maptons 403, mapquest 202, goyellow 410, facebook 400, linkedin 999, branchen-info.net connection refused."}
 ],
 "sources_unreadable": [
  {"source": "GBP live profile (name, address, phone, categories, reviews)", "error": "Local Falcon MCP not connected; browser read forbidden in this run"},
  {"source": "GBP owners and managers, GA4 roles, GSC owners, CMS admin list, registrar account, GTM, Ads", "error": "need a logged-in browser read; not attempted by rule"},
  {"source": "https://www.11880.com/ listing page", "error": "HTTP 403 (only the search-result excerpt was read)"},
  {"source": "https://zw.maptons.com/p/3112170407", "error": "HTTP 403 (only the search snippet was read)"},
  {"source": "https://ingelheim-am-rhein.branchen-info.net/schuetten-iris/3170134/", "error": "connection refused"},
  {"source": "https://www.facebook.com/coraliesuriyapperuma/ , https://de.linkedin.com/in/coralie-suriyapperuma-coach , https://www.instagram.com/suriya.praxis/", "error": "Facebook HTTP 400, LinkedIn HTTP 999, Instagram HTTP 200 but page not parsed (login wall expected). Profile NAP not read."},
  {"source": "Second Cylex entry page, second MapQuest entry page", "error": "entry pages not opened; seen only inside other pages or snippets"},
  {"source": "GSC Page indexing report (404 list, 'crawled not indexed' list)", "error": "not exposed by the API; the 21.09. numbers (39 indexed / 43 not) are from the baseline report"},
  {"source": "Index state of 64 sitemap URLs", "error": "not inspected in this run (sample of 25 only)"},
  {"source": "Backlink anchors (UB.D10)", "error": "not run, opt-in flag off"}
 ],
 "deviations_from_data_model": [
  "index-intended.json: 'intended' may be 'review'; 'verdict' may be 'unverified' or 'decision_needed'. These values are additions.",
  "Area B has no checks in the catalog list. bedrock.areas shows B = grey.",
  "Area A rows are verify-only. They use approval 'blocked' where a browser read is missing."
 ],
 "not_written": ["findings-summary.md: the environment blocked writing a summary .md file; the summary was returned in the chat message instead"],
 "files": ["run.json", "harm-register.json", "who-owns-what.json", "nap-master.json", "nap-corrections.json", "redirect-map.json", "index-intended.json", "link-plan.json", "manifest.json", "evidence/", "scripts/"]
}
json.dump(run, open(ROOT + "/run.json", "w"), ensure_ascii=False, indent=1)
print("run.json written")
