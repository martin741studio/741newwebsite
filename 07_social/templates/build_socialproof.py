#!/usr/bin/env python3
# Social-Proof-Stories (1080x1920) aus echten Kunden-Ergebnissen. DE + EN.
# Aufruf: python3 build_socialproof.py   -> output/social_proof/<slug>_<lang>.png
import os, subprocess

LOGO = "file:///Users/martindrendel/741website/04_site/assets/images/logo_white.png"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)

# ================= echte Kunden-Ergebnisse (aus 741-Portfolio) =================
CLIENTS = [
  {"slug":"laserstein","name":"Bernd Laserstein",
   "type_de":"Gesundheitspraxis","type_en":"Health Practice","city":"Freiburg",
   "kw_de":"Körperpsychotherapie","kw_en":"body psychotherapy",
   "kind":"rank","frm":"9","to":"1",
   "sub_de":"Von Platz 9 auf Platz 1 — für die wichtigste Suchanfrage.",
   "sub_en":"From position 9 to #1 — for the key search term."},
  {"slug":"schlirf","name":"Veronika Schlirf",
   "type_de":"Heilpraktikerin","type_en":"Holistic Practitioner","city":"Regensburg",
   "kw_de":"Heilpraktikerin","kw_en":"holistic practitioner",
   "kind":"rank","frm":"15","to":"1",
   "sub_de":"Von Platz 15 auf Platz 1 im gesamten Einzugsgebiet.",
   "sub_en":"From position 15 to #1 across the whole catchment area."},
  {"slug":"menge","name":"Torsten Menge",
   "type_de":"Psychotherapie","type_en":"Psychotherapy","city":"",
   "kw_de":"Onkologie-Psychologie","kw_en":"oncology psychology",
   "kind":"rank","frm":"117","to":"3",
   "sub_de":"Von Platz 117 in die Top 3 — sichtbar statt unsichtbar.",
   "sub_en":"From position 117 into the Top 3 — visible at last."},
  {"slug":"kraft","name":"Physiotherapie Kraft",
   "type_de":"Physiotherapie","type_en":"Physiotherapy","city":"",
   "kw_de":"Krankengymnastik","kw_en":"physiotherapy",
   "kind":"rank","frm":"8","to":"1",
   "sub_de":"Platz 1 für die wichtigste lokale Suchanfrage.",
   "sub_en":"Ranked #1 for the most important local search."},
  {"slug":"abel","name":"Maria Abel",
   "type_de":"Elternberatung & Coaching","type_en":"Parenting & Coaching","city":"Raum Stuttgart",
   "kw_de":"Top-3-Abdeckung","kw_en":"Top-3 coverage",
   "kind":"coverage","frm":"0%","to":"100%",
   "sub_de":"Von unsichtbar auf 100 % Top-3-Abdeckung im Umkreis.",
   "sub_en":"From invisible to 100% Top-3 coverage across the area."},
]

L = {
 "de":{"badge":"KUNDEN-ERGEBNIS","before":"VORHER","after":"JETZT","rank":"PLATZ",
       "kwlab":"Suchanfrage bei Google","cta":"Dein Business auch?","url":"→ 741.STUDIO",
       "foot":"Echtes Kunden-Ergebnis · Local SEO","handle":"@heymartin.seo.agentur",
       "covlab":"Sichtbarkeit im Umkreis"},
 "en":{"badge":"CLIENT RESULT","before":"BEFORE","after":"NOW","rank":"#",
       "kwlab":"Google search term","cta":"Your business too?","url":"→ 741.STUDIO",
       "foot":"Real client result · Local SEO","handle":"@741.studio",
       "covlab":"Local visibility"},
}

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
.slide{position:relative;width:1080px;height:1920px;background:#111;font-family:'DM Sans',Arial,sans-serif;color:#fff;overflow:hidden;display:flex;flex-direction:column}
.halftone{position:absolute;inset:0;background-image:radial-gradient(circle,rgba(255,255,255,.06) 2px,transparent 2px);background-size:24px 24px;-webkit-mask-image:linear-gradient(160deg,transparent 42%,black 88%);mask-image:linear-gradient(160deg,transparent 42%,black 88%)}
.topbar{position:relative;z-index:2;display:flex;justify-content:space-between;align-items:center;padding:110px 72px 0}
.topbar img{height:50px}
.badge{font-weight:700;font-size:23px;letter-spacing:4px;color:#fac118;border:3px solid #fac118;padding:12px 26px;border-radius:999px}
.body{position:relative;z-index:2;flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 72px}
.eyebrow{color:#fac118;font-weight:700;font-size:26px;letter-spacing:5px;margin-bottom:22px}
.name{font-family:'Anton',Impact,sans-serif;text-transform:uppercase;font-size:82px;line-height:1.0}
.kw{display:inline-flex;align-items:center;margin-top:26px;background:#1e1e1e;border:2px solid #3a3a3a;border-radius:999px;padding:12px 26px;font-size:27px;font-weight:500;color:#e0e0e0}
.kw b{color:#fac118;font-weight:700;margin-left:8px}
.hero{display:flex;align-items:stretch;gap:24px;margin-top:60px}
.card{flex:1;border-radius:22px;padding:40px 24px;text-align:center}
.card.before{background:#1c1c1c;border:2px solid #2e2e2e;color:#8f8f8f}
.card.after{background:#fac118;color:#111}
.card .lab{font-weight:700;font-size:24px;letter-spacing:3px}
.card .val{font-family:'Anton',Impact,sans-serif;font-size:104px;line-height:0.95;margin-top:12px}
.card .small{font-size:26px;font-weight:700;letter-spacing:2px;opacity:.85}
.arrow{display:flex;align-items:center;font-family:'Anton',Impact,sans-serif;font-size:80px;color:#fac118}
.sub{margin-top:54px;font-size:37px;line-height:1.45;color:#e8e8e8;font-weight:500;max-width:900px}
.ctaband{position:relative;z-index:2;background:#fac118;color:#111;display:flex;justify-content:space-between;align-items:center;padding:40px 72px;margin-top:56px}
.ctaband .t{font-family:'Anton',Impact,sans-serif;text-transform:uppercase;font-size:46px}
.ctaband .u{font-family:'Anton',Impact,sans-serif;font-size:40px}
.foot{position:relative;z-index:2;display:flex;justify-content:space-between;align-items:center;padding:24px 72px 96px;background:#111;color:#8f8f8f;font-weight:600;font-size:22px;letter-spacing:1px}
"""
HEAD=('<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8">'
 '<link href="https://fonts.googleapis.com/css2?family=Anton&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">'
 f'<style>{CSS}</style></head><body>')

def slide(c, lang):
    t=L[lang]
    typ=c["type_"+lang]; city=c["city"]
    eyebrow=(typ+" · "+city) if city else typ
    kw=c["kw_"+lang]; sub=c["sub_"+lang]
    if c["kind"]=="rank":
        rk=t["rank"]
        bef=(f'{rk} {c["frm"]}' if lang=="de" else f'{rk}{c["frm"]}')
        aft=(f'{rk} {c["to"]}' if lang=="de" else f'{rk}{c["to"]}')
        kwlab=t["kwlab"]
    else:
        bef=c["frm"]; aft=c["to"]; kwlab=t["covlab"]
    hero=(f'<div class="hero">'
          f'<div class="card before"><div class="lab">{t["before"]}</div><div class="val">{bef}</div></div>'
          f'<div class="arrow">→</div>'
          f'<div class="card after"><div class="lab">{t["after"]}</div><div class="val">{aft}</div></div></div>')
    body=(f'<div class="body"><div class="eyebrow">{eyebrow.upper()}</div>'
          f'<div class="name">{c["name"]}</div>'
          f'<div class="kw">{kwlab}: <b>„{kw}"</b></div>'
          f'{hero}<div class="sub">{sub}</div></div>')
    top=(f'<div class="topbar"><img src="{LOGO}" alt="741"><div class="badge">{t["badge"]}</div></div>')
    cta=(f'<div class="ctaband"><div class="t">{t["cta"]}</div><div class="u">{t["url"]}</div></div>')
    foot=f'<div class="foot"><span>{t["foot"]}</span><span>{t["handle"]}</span></div>'
    return f'<div class="slide"><div class="halftone"></div>{top}{body}{cta}{foot}</div>'

def main():
    outdir=os.path.join(ROOT,"output","social_proof"); tmp=os.path.join(outdir,"_html")
    os.makedirs(outdir,exist_ok=True); os.makedirs(tmp,exist_ok=True)
    for c in CLIENTS:
        for lang in ("de","en"):
            hf=os.path.join(tmp,f'{c["slug"]}_{lang}.html')
            with open(hf,"w") as f: f.write(HEAD+slide(c,lang)+"</body></html>")
            png=os.path.join(outdir,f'{c["slug"]}_{lang}.png')
            subprocess.run([CHROME,"--headless=new","--disable-gpu","--hide-scrollbars",
              "--force-device-scale-factor=1","--window-size=1080,1920","--virtual-time-budget=12000",
              f"--screenshot={png}",f"file://{hf}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            print("rendered",png)

if __name__=="__main__": main()
