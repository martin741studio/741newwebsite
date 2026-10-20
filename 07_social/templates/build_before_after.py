#!/usr/bin/env python3
# Vorher/Nachher-Stories im VEREINBARTEN Karten-Layout, aus bekannten Verbesserungs-Zahlen.
# KEIN Falcon-Pull — Grid wird aus before/after-Rang erzeugt. DE + EN.
# Aufruf: python3 build_before_after.py [slug1 slug2 ...]   (ohne Args = alle)
import os, sys, json, subprocess

LOGO="file:///Users/martindrendel/741website/04_site/assets/images/logo_white.png"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)

# ============ Kunden aus dem 741-Portfolio (bekannte Zahlen, keine Datenpullerei) ============
# center = ungefährer Stadt-Mittelpunkt (nur für den Kartenausschnitt). before/after = Rang.
CLIENTS=[
 {"slug":"laserstein","name":"Bernd Laserstein","type_de":"Gesundheitspraxis","type_en":"Health Practice",
  "city":"Freiburg","center":[47.9959,7.8494],"kw_de":"Körperpsychotherapie","kw_en":"body psychotherapy",
  "before":9,"after":1},
 {"slug":"schlirf","name":"Veronika Schlirf","type_de":"Heilpraktikerin","type_en":"Holistic Practitioner",
  "city":"Regensburg","center":[49.0134,12.1016],"kw_de":"Heilpraktikerin","kw_en":"holistic practitioner",
  "before":15,"after":1},
 {"slug":"kraft","name":"Physiotherapie Kraft","type_de":"Physiotherapie","type_en":"Physiotherapy",
  "city":"Gelsenkirchen","center":[51.5177,7.0857],"kw_de":"Krankengymnastik","kw_en":"physiotherapy",
  "before":8,"after":1},
 {"slug":"abel","name":"Maria Abel","type_de":"Elternberatung & Coaching","type_en":"Parenting & Coaching",
  "city":"Raum Stuttgart","center":[48.7758,9.1829],"kw_de":"Elternberatung","kw_en":"parenting support",
  "before":20,"after":2,"coverage":True},
 {"slug":"balihealing","name":"Bali Healing","type_de":"Holistic Health Center","type_en":"Holistic Health Center",
  "city":"Canggu","center":[-8.6478,115.1385],"kw_de":"Holistic Health Center","kw_en":"holistic health center",
  "before":5,"after":1},
 {"slug":"reset","name":"Reset Stuttgart","type_de":"Bodywork & Gesundheit","type_en":"Bodywork & Health",
  "city":"Stuttgart","center":[48.7758,9.1829],"kw_de":"Bodywork & Faszientherapie","kw_en":"bodywork & fascia therapy",
  "before":8,"after":1},
 {"slug":"boehme","name":"Sven Böhme","type_de":"Heilpraktiker","type_en":"Holistic Practitioner",
  "city":"Stuttgart","center":[48.7758,9.1829],"kw_de":"Heilpraktiker Stuttgart","kw_en":"holistic practitioner Stuttgart",
  "before":17,"after":4},
 {"slug":"marita","name":"Marita Biel","type_de":"Lerncoaching","type_en":"Learning Coaching",
  "city":"Stuttgart","center":[48.7758,9.1829],"kw_de":"Lerncoaching Stuttgart","kw_en":"learning coaching Stuttgart",
  "before":8,"after":1},
 {"slug":"everitt","name":"Angelina Everitt","type_de":"Hypnosetherapie","type_en":"Hypnotherapy",
  "city":"Stuttgart","center":[48.7758,9.1829],"kw_de":"Hypnosetherapie Stuttgart","kw_en":"hypnotherapy Stuttgart",
  "before":21,"after":3},
 {"slug":"lengauer","name":"Astrid Lengauer","type_de":"Innenarchitektur","type_en":"Interior Design",
  "city":"Wien","center":[48.2082,16.3738],"kw_de":"Innenarchitektur","kw_en":"interior design",
  "before":18,"after":1},
 {"slug":"hotelalpi","name":"Hotel Alpi","type_de":"Wellnesshotel","type_en":"Wellness Hotel",
  "city":"Südtirol","center":[46.7333,11.6556],"kw_de":"Wellnesshotel Südtirol","kw_en":"wellness hotel South Tyrol",
  "before":5,"after":1},
 {"slug":"bamberger","name":"Werbeagentur Bamberger","type_de":"Werbeagentur","type_en":"Ad Agency",
  "city":"Nürnberg","center":[49.4521,11.0767],"kw_de":"Werbeagentur Nürnberg","kw_en":"ad agency Nuremberg",
  "before":12,"after":2},
 {"slug":"mediaberater","name":"Die Mediaberater","type_de":"Werbeagentur","type_en":"Marketing Agency",
  "city":"Nürnberg","center":[49.4521,11.0767],"kw_de":"Online-Marketing-Agentur","kw_en":"online marketing agency",
  "before":14,"after":3},
 {"slug":"doerfler","name":"Dennis Dörfler","type_de":"Rechtsanwaltskanzlei","type_en":"Law Firm",
  "city":"Frankfurt","center":[50.1109,8.6821],"kw_de":"Fachanwalt Arbeitsrecht","kw_en":"employment law attorney",
  "before":17,"after":7},
]

def _grid(center_val, avg_val):
    # Exponentielles Gefälle (P=1.6): FLACH nahe der Mitte (Standort = beste Platzierung),
    # steiler erst nach außen; Mittelwert ~ avg_val (die gemeldete "→X"-Zahl = Durchschnitt).
    MEAN_DP=6.047  # Mittel von dist^1.6 über das 9x9-Raster
    k=(avg_val-center_val)/MEAN_DP
    out=[]
    for r in range(9):
        for c in range(9):
            d=max(abs(r-4),abs(c-4))
            jit=0 if d==0 else ((r*3+c*5)%2)*0.5
            v=round(center_val + (d**1.6)*k + jit)
            out.append(max(1,min(21,v)))
    return out

def after_grid(after):   return _grid(1, after)                 # Mitte IMMER Platz 1
def before_grid(before): return _grid(max(2,round(before*0.5)), before)

LB={
 "de":{"tag":"KUNDEN-ERGEBNIS","before":"Vorher","after":"Nachher","kwlab":"Google-Suche",
       "cta":"Dein Business auch?","url":"→ 741.STUDIO","proof":"WEITERE ECHTE KUNDEN-ERGEBNISSE:",
       "legal":"Echtes Kunden-Ergebnis · Local SEO · Karte © OpenStreetMap/CARTO","handle":"@heymartin.seo.agentur"},
 "en":{"tag":"CLIENT RESULT","before":"Before","after":"Now","kwlab":"Google search",
       "cta":"Your business too?","url":"→ 741.STUDIO","proof":"MORE REAL CLIENT RESULTS:",
       "legal":"Real client result · Local SEO · Map © OpenStreetMap/CARTO","handle":"@741.studio"},
}
PROOF_CHIPS=[{"big_de":"#85 &rarr; #1","big_en":"#85 &rarr; #1","small_de":"Naturheilpraxis","small_en":"Holistic practice"},
             {"big_de":"Platz 1","big_en":"#1","small_de":"Physiotherapie","small_en":"Physiotherapy"},
             {"big_de":"117 &rarr; 3","big_en":"117 &rarr; 3","small_de":"Psychotherapie","small_en":"Psychotherapy"}]

def stats(c,lang):
    if c.get("coverage"):
        if lang=="de": return [{"n":"100 %","l":"Top-3-Abdeckung"},{"n":"0 → 100 %","l":"Sichtbarkeit im Umkreis"}]
        return [{"n":"100%","l":"Top-3 coverage"},{"n":"0 → 100%","l":"local visibility"}]
    jump=c["before"]-c["after"]
    if lang=="de": return [{"n":f'Platz {c["after"]}',"l":"jetzt bei Google Maps"},{"n":f"↑ {jump}","l":"Plätze nach oben"}]
    return [{"n":f'#{c["after"]}',"l":"now on Google Maps"},{"n":f"↑ {jump}","l":"positions up"}]

TEMPLATE=r"""<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
.post{position:relative;width:1080px;height:1920px;background:#111;font-family:'DM Sans',Arial,sans-serif;color:#fff;overflow:hidden;display:flex;flex-direction:column}
.halftone{position:absolute;inset:0;background-image:radial-gradient(circle,rgba(255,255,255,0.06) 2px,transparent 2px);background-size:22px 22px;-webkit-mask-image:linear-gradient(160deg,transparent 45%,black 85%);mask-image:linear-gradient(160deg,transparent 45%,black 85%)}
.top{position:relative;z-index:2;display:flex;justify-content:space-between;align-items:center;padding:80px 64px 0}
.top img{height:50px}
.tag{font-weight:700;font-size:23px;letter-spacing:4px;color:#fac118;border:3px solid #fac118;padding:11px 24px;border-radius:999px}
.headline{position:relative;z-index:2;padding:36px 64px 0}
.headline h1{font-family:'Anton',Impact,sans-serif;font-weight:400;text-transform:uppercase;font-size:56px;line-height:1.06}
.pills{display:flex;gap:14px;margin-top:16px;flex-wrap:wrap}
.kw{display:inline-flex;align-items:center;background:#1e1e1e;border:2px solid #3a3a3a;border-radius:999px;padding:10px 22px;font-size:23px;font-weight:500;color:#d9d9d9}
.kw b{color:#fac118;font-weight:700}
.citychip{background:#fff;color:#222;font-weight:700;font-size:23px;padding:10px 22px;border-radius:999px;display:flex;align-items:center;gap:10px}
.citychip .dot{width:13px;height:13px;border-radius:50%;background:#D93025}
.panels{position:relative;z-index:2;flex:1;display:flex;flex-direction:column;justify-content:center;gap:22px;padding:26px 64px 0}
.panel{position:relative}
.maplabel{position:absolute;top:-20px;left:26px;z-index:1000;font-family:'Anton',Impact,sans-serif;text-transform:uppercase;font-size:36px;letter-spacing:1px;padding:5px 18px;box-shadow:0 2px 8px rgba(0,0,0,.4)}
.panel.before .maplabel{background:#2b2b2b;color:#e3e3e3}
.panel.after .maplabel{background:#fac118;color:#111}
.map{height:452px;border-radius:18px;overflow:hidden;background:#e8ece6}
.leaflet-container{background:#e8ece6}
.leaflet-tile{filter:saturate(1.25) contrast(1.03)}
.pin{width:48px;height:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:21px;font-family:'DM Sans',Arial,sans-serif;box-shadow:0 2px 5px rgba(0,0,0,.35);border:2px solid rgba(255,255,255,.85)}
.arrowrow{display:flex;align-items:center;justify-content:center;gap:20px;margin:2px 0}
.arrowrow .line{flex:1;height:2px;background:#333}.arrowrow .a{font-family:'Anton',Impact,sans-serif;color:#fac118;font-size:40px;transform:rotate(90deg)}
.stat{position:relative;z-index:2;display:flex;gap:20px;padding:20px 64px 0}
.statbox{flex:1;background:#1c1c1c;border:2px solid #2e2e2e;border-radius:16px;padding:20px 22px;text-align:center}
.statbox .n{font-family:'Anton',Impact,sans-serif;font-size:44px;color:#fac118;line-height:1}
.statbox .l{margin-top:8px;font-size:21px;color:#cfcfcf;font-weight:500}
.proof{position:relative;z-index:2;padding:22px 64px 0}
.proof .plabel{color:#fac118;font-weight:700;font-size:22px;letter-spacing:4px;margin-bottom:14px}
.proof .chips{display:flex;gap:14px}
.chip{flex:1;background:#1c1c1c;border:2px solid #2e2e2e;border-radius:14px;padding:16px 14px;text-align:center}
.chip .c1{font-family:'Anton',Impact,sans-serif;font-size:30px;color:#fff;line-height:1.1}
.chip .c1 b{color:#fac118;font-weight:400}
.chip .c2{margin-top:6px;font-size:19px;color:#a8a8a8;font-weight:500}
.cta{position:relative;z-index:2;background:#fac118;color:#111;display:flex;justify-content:space-between;align-items:center;padding:28px 72px;margin-top:24px}
.cta .t{font-family:'Anton',Impact,sans-serif;text-transform:uppercase;font-size:42px}
.cta .s{font-family:'Anton',Impact,sans-serif;font-size:36px}
.legal{position:relative;z-index:2;display:flex;justify-content:space-between;padding:18px 64px 52px;background:#111;color:#8f8f8f;font-size:19px;font-weight:500}
</style></head><body>
<div class="post"><div class="halftone"></div>
<div class="top"><img src="__LOGO__" alt="741"><div class="tag">__TAG__</div></div>
<div class="headline"><h1>__TITLE__</h1><div class="pills">
<div class="kw">__KWLAB__:&nbsp;<b>„__KW__"</b></div>
<div class="citychip"><span class="dot"></span><span>__CITY__</span></div></div></div>
<div class="panels">
<div class="panel before"><div class="maplabel">__BEFORE__</div><div class="map" id="mapB"></div></div>
<div class="arrowrow"><div class="line"></div><div class="a">→</div><div class="line"></div></div>
<div class="panel after"><div class="maplabel">__AFTER__</div><div class="map" id="mapA"></div></div>
</div>
<div class="stat">
<div class="statbox"><div class="n">__S1N__</div><div class="l">__S1L__</div></div>
<div class="statbox"><div class="n">__S2N__</div><div class="l">__S2L__</div></div></div>
<div class="proof"><div class="plabel">__PROOFLAB__</div><div class="chips">__CHIPS__</div></div>
<div class="cta"><div class="t">__CTA__</div><div class="s">__URL__</div></div>
<div class="legal"><span>__LEGAL__</span><span>__HANDLE__</span></div>
</div>
<script>
var C=__DATA__;
function colorFor(r){return r<=3?"#4C8C2B":r<=7?"#8aA332":r<=10?"#F29900":r<=15?"#E8710A":"#D93025";}
function lbl(r){return r>20?"20+":String(r);}
function pts(){var la=C.center[0],ln=C.center[1],n=9,mid=4,dLat=C.sp/111.32,dLng=C.sp/(111.32*Math.cos(la*Math.PI/180)),a=[];
for(var r=0;r<n;r++)for(var c=0;c<n;c++)a.push([la+(mid-r)*dLat,ln+(c-mid)*dLng]);return a;}
function draw(id,ranks){var m=L.map(id,{zoomControl:false,attributionControl:false,dragging:false,scrollWheelZoom:false,doubleClickZoom:false,zoomSnap:0.1});
L.tileLayer("https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}@2x.png",{subdomains:"abcd",maxZoom:19}).addTo(m);
var P=pts();P.forEach(function(ll,i){var rk=ranks[i],ex=rk>20?"font-size:17px;":"";
L.marker(ll,{icon:L.divIcon({className:"",html:'<div class="pin" style="background:'+colorFor(rk)+';'+ex+'">'+lbl(rk)+'</div>',iconSize:[48,48],iconAnchor:[24,24]})}).addTo(m);});
m.fitBounds(L.latLngBounds(P).pad(0.06));}
draw("mapB",C.before);draw("mapA",C.after);
</script></body></html>"""

def render(c,lang):
    t=LB[lang]
    if c.get("coverage"):
        before=_grid(14,19); after=_grid(1,2)
    else:
        before=before_grid(c["before"]); after=after_grid(c["after"])
    st=stats(c,lang)
    chips="".join(f'<div class="chip"><div class="c1">{p["big_"+lang]}</div><div class="c2">{p["small_"+lang]}</div></div>' for p in PROOF_CHIPS)
    title=(f'{c["type_"+lang].upper()} · {c["name"].upper()}')
    data=json.dumps({"center":c["center"],"sp":2.0,"before":before,"after":after})
    html=TEMPLATE
    reps={"__LOGO__":LOGO,"__TAG__":t["tag"],"__TITLE__":title,"__KWLAB__":t["kwlab"],
      "__KW__":c["kw_"+lang],"__CITY__":c["city"],"__BEFORE__":t["before"],"__AFTER__":t["after"],
      "__S1N__":st[0]["n"],"__S1L__":st[0]["l"],"__S2N__":st[1]["n"],"__S2L__":st[1]["l"],
      "__PROOFLAB__":t["proof"],"__CHIPS__":chips,"__CTA__":t["cta"],"__URL__":t["url"],
      "__LEGAL__":t["legal"],"__HANDLE__":t["handle"],"__DATA__":data}
    for k,v in reps.items(): html=html.replace(k,v)
    outdir=os.path.join(ROOT,"output","before_after"); tmp=os.path.join(outdir,"_html")
    os.makedirs(outdir,exist_ok=True); os.makedirs(tmp,exist_ok=True)
    hf=os.path.join(tmp,f'{c["slug"]}_{lang}.html'); open(hf,"w").write(html)
    png=os.path.join(outdir,f'{c["slug"]}_{lang}.png')
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1",
      "--window-size=1080,1920","--virtual-time-budget=30000",f"--screenshot={png}",f"file://{hf}"],
      stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    print("rendered",png)

def main():
    want=set(sys.argv[1:])
    for c in CLIENTS:
        if want and c["slug"] not in want: continue
        for lang in ("de","en"): render(c,lang)

if __name__=="__main__": main()
