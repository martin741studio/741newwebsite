import re, json, glob, os, sys, html
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import save_evidence
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'c1b_analyze.py')).read().split("PATTERNS")[0])
rows=[]
for f in sorted(glob.glob('evidence/area_c/EV-C-site-*.html')):
    k=os.path.basename(f)[10:-5]
    raw=open(f,encoding='utf8',errors='replace').read()
    tx=text(raw)
    lines=[l.strip() for l in tx.split('\n') if l.strip()]
    foot=[l for l in lines if re.search(r'Wiesenh[üu]ttenstra',l) and 'Oberanger' in l and 'Tel.' in l]
    jl=re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',raw,re.S|re.I)
    j=json.loads(jl[0]) if jl else {}
    rows.append({"page":k,"old_address_mentions":len(re.findall(r'Wiesenh[üu]ttenstra(?:ß|ss)e\s*17',tx)),"new_address_mentions":len(re.findall(r'Untermainkai',tx)),
      "munich_address_mentions":len(re.findall(r'Oberanger\s*32',tx)),"footer_line":(foot[0][:200] if foot else None),
      "jsonld_address":j.get("address",{}).get("streetAddress"),"jsonld_phone":j.get("telephone"),
      "jsonld_hours":[(h.get("dayOfWeek"),h.get("opens"),h.get("closes")) for h in j.get("openingHoursSpecification",[])],
      "jsonld_has_munich":("Oberanger" in json.dumps(j)),"jsonld_sameAs":j.get("sameAs")})
extra={"kontakt_page_hours":"Von Montag bis Freitag durchgehend von 09:30 Uhr – 14:30 Uhr (Frankfurt and München, same text)","impressum_munich_address_in_body":False,
       "impressum_address":"Wiesenhüttenstraße 17, 60329 Frankfurt am Main","impressum_phone":"+49 69 29 80 28 87-0 (Fax -9)","kontakt_phone_ffm":"+49 69 29 80 28 87-0","kontakt_phone_muc":"+49 89 72 44 41 7-0","kontakt_emergency":"2 mobile numbers (0160 ...)",
       "phone_formats_seen_on_site":["+49 69 29 80 28 87-0","069 29802887-0","tel:+4969298028870 (link)"]}
save_evidence("EV-C-site-analysis",json.dumps({"pages":rows,"detail":extra},ensure_ascii=False,indent=1),"json","python parse of the 13 saved page HTML files","scripts/area_ac/c1c_site_summary.py over EV-C-site-*.html","area_c")
print(json.dumps(rows[:2],ensure_ascii=False,indent=1)); print(len(rows), sum(1 for r in rows if r['old_address_mentions']), sum(1 for r in rows if r['new_address_mentions']))
