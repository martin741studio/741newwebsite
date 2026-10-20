import re, json, glob, html, os
from html.parser import HTMLParser
class T(HTMLParser):
    def __init__(s): super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in('script','style','noscript'): s.skip+=1
    def handle_endtag(s,t):
        if t in('script','style','noscript') and s.skip: s.skip-=1
        if t in('p','div','br','li','tr','h1','h2','h3','h4','footer','header'): s.out.append('\n')
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
def text(h):
    p=T(); p.feed(h); return re.sub(r'[ \t\xa0]+',' ',''.join(p.out))
PATTERNS = {"old_addr": r"Wiesenh[üu]ttenstra(?:ß|ss)e\s*17", "new_addr": r"Untermainkai\s*26", "leuschner23": r"Leuschner[- ]?Stra(?:ß|ss)e\s*23","leuschner27": r"Leuschner[- ]?Stra(?:ß|ss)e\s*27",
 "ffm_phone": r"(?:\+49\s*\(?0?\)?\s*69|069)[\s\-/]*29[\s\-]*80[\s\-]*28[\s\-]*87", "muc_phone": r"(?:\+49\s*\(?0?\)?\s*89|089)[\s\-/]*72[\s\-]*44[\s\-]*41[\s\-]*70","oberanger":r"Oberanger\s*32","neuhauser":r"Neuhauser"}
res={}
for f in sorted(glob.glob('evidence/area_c/EV-C-site-*.html')):
    k=os.path.basename(f)[10:-5]
    raw=open(f,encoding='utf8',errors='replace').read()
    tx=text(raw)
    r={m:len(re.findall(p,tx,re.I)) for m,p in PATTERNS.items()}
    # non-visible (attributes, scripts, JSON-LD)
    r_raw={m:len(re.findall(p,raw,re.I)) for m,p in PATTERNS.items()}
    jl=re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',raw,re.S|re.I)
    r['jsonld_blocks']=len(jl)
    r['raw_counts']=r_raw
    res[k]=r
    print(k, {a:b for a,b in r.items() if a!='raw_counts' and b}, 'RAW', {a:b for a,b in r_raw.items() if b})
json.dump(res,open('/private/tmp/claude-501/-Users-martindrendel-741website/f05926a2-9f20-4657-bfb4-7f32c430b2f1/scratchpad/site_counts.json','w'),indent=1)
