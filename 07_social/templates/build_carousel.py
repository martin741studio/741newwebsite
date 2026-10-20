#!/usr/bin/env python3
# Baut aus CONFIG statische 1080x1080-Slides (HTML) -> Headless-Chrome PNG.
# Pro Thema nur CONFIG unten anpassen. Aufruf: python3 build_carousel.py <output-slug>
import sys, os, subprocess, html

LOGO = "file:///Users/martindrendel/741website/04_site/assets/images/logo_white.png"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # 07_social

# ================= CONFIG — pro Thema nur das hier anpassen =================
CONFIG = {
  "series": "LOCAL SEO PLAYBOOK",
  "handle": "@741.studio",
  "slides": [
    {"type":"cover","eyebrow":"741 PLAYBOOK",
     "title":["SO STEHST DU","BEI GOOGLE MAPS","GANZ OBEN"],"hl":3,
     "sub":'6 Schritte, mit denen lokale Betriebe ins „Map Pack" kommen — und die Anrufe bekommen.'},
    {"type":"stat","big":"46%",
     "lab":["aller Google-Suchen haben eine ","lokale Absicht",". Wer die Top 3 auf der Karte besetzt, gewinnt die meisten Kunden."]},
    {"type":"tip","num":"01","title":"Profil vollständig ausfüllen",
     "txt":'Google rankt den, der sein Unternehmensprofil am besten versteht. <b>Kategorie, alle Leistungen, echte Fotos, korrekte Öffnungszeiten</b> — keine leeren Felder.'},
    {"type":"tip","num":"02","title":"Bewertungen aktiv sammeln",
     "txt":'Nicht nur die Sterne zählen. <b>Menge, Aktualität und deine Antworten</b> auf jede Bewertung sind ein direktes Ranking-Signal — und schaffen Vertrauen.'},
    {"type":"tip","num":"03","title":"Überall die gleichen Daten",
     "txt":'Name, Adresse, Telefon müssen <b>in jedem Verzeichnis identisch</b> sein. Widersprüche verwirren Google und kosten Platzierung.'},
    {"type":"tip","num":"04","title":"Standort-Inhalte auf der Seite",
     "txt":'Deine Website braucht echte Ortsbezüge: <b>Leistung + Stadt</b>, Anfahrt, lokale Referenzen. So versteht Google, wo du relevant bist.'},
    {"type":"tip","num":"05","title":"Sichtbarkeit im Umkreis messen",
     "txt":'Platz 1 direkt am Standort reicht nicht. Miss dein Ranking im <b>gesamten Einzugsgebiet</b> per Grid-Scan — dort entscheidet sich, wer gefunden wird.'},
    {"type":"tip","num":"06","title":"Dranbleiben statt einmalig",
     "txt":'Local SEO ist ein Prozess, kein Projekt. <b>Monatlich Profil pflegen, Bewertungen sammeln, Rankings prüfen</b> — Wettbewerber schlafen nicht.'},
    {"type":"cta","eyebrow":"DEIN NÄCHSTER SCHRITT",
     "title":["WO STEHST DU","AUF DER KARTE?"],
     "sub":"Wir machen dir einen kostenlosen Sichtbarkeits-Check für dein Einzugsgebiet.",
     "url":"→ 741.STUDIO"},
  ]
}
# ===========================================================================

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
html,body { width:1080px; height:1080px; overflow:hidden; }
.slide { position:relative; width:1080px; height:1080px; background:#111;
  font-family:'DM Sans',Arial,sans-serif; color:#fff; overflow:hidden; display:flex; flex-direction:column; }
.halftone { position:absolute; inset:0;
  background-image:radial-gradient(circle, rgba(255,255,255,0.06) 2px, transparent 2px);
  background-size:24px 24px;
  -webkit-mask-image:linear-gradient(150deg,transparent 40%,black 88%); mask-image:linear-gradient(150deg,transparent 40%,black 88%); }
.topbar { position:relative; z-index:2; display:flex; justify-content:space-between; align-items:center; padding:60px 64px 0; }
.topbar img { height:44px; }
.kicker { text-align:right; }
.kicker .k { color:#fac118; font-weight:700; font-size:20px; letter-spacing:4px; }
.kicker .c { color:#7a7a7a; font-weight:700; font-size:20px; letter-spacing:3px; margin-top:4px; }
.body { position:relative; z-index:2; flex:1; display:flex; flex-direction:column; justify-content:center; padding:0 64px; }
.cover .eyebrow { color:#fac118; font-weight:700; font-size:28px; letter-spacing:6px; margin-bottom:28px; }
.cover h1 { font-family:'Anton',Impact,sans-serif; text-transform:uppercase; font-size:112px; line-height:1.0; }
.cover h1 .hl { display:inline-block; background:#fac118; color:#111; padding:0 16px; margin-top:12px; }
.cover .sub { margin-top:40px; font-size:34px; line-height:1.4; color:#e6e6e6; font-weight:500; max-width:820px; }
.tip .num { font-family:'Anton',Impact,sans-serif; font-size:150px; line-height:0.9; color:#fac118; }
.tip h2 { font-family:'Anton',Impact,sans-serif; text-transform:uppercase; font-size:72px; line-height:1.02; margin-top:8px; }
.tip .txt { margin-top:34px; font-size:36px; line-height:1.5; color:#dcdcdc; max-width:900px; }
.tip .txt b { color:#fff; font-weight:700; }
.stat .big { font-family:'Anton',Impact,sans-serif; font-size:230px; line-height:0.9; color:#fac118; }
.stat .lab { font-size:42px; line-height:1.35; color:#fff; font-weight:700; margin-top:20px; max-width:860px; }
.stat .lab span { color:#fac118; }
.slide.cta { background:#fac118; color:#111; }
.slide.cta .eyebrow { font-weight:700; font-size:26px; letter-spacing:5px; margin-bottom:26px; }
.slide.cta h2 { font-family:'Anton',Impact,sans-serif; text-transform:uppercase; font-size:100px; line-height:1.0; }
.slide.cta .sub { margin-top:34px; font-size:36px; line-height:1.4; font-weight:600; max-width:840px; }
.slide.cta .url { margin-top:56px; font-family:'Anton',Impact,sans-serif; font-size:56px; }
.slide.cta .topbar img { filter:invert(1); }
.slide.cta .kicker .k { color:#111; } .slide.cta .kicker .c { color:#6b5a15; }
.foot { position:relative; z-index:2; display:flex; justify-content:space-between; align-items:center;
  padding:0 64px 56px; color:#7a7a7a; font-weight:600; font-size:22px; letter-spacing:1px; }
.swipe { color:#fac118; font-family:'Anton',Impact,sans-serif; font-size:30px; letter-spacing:1px; }
.slide.cta .foot { color:#6b5a15; }
"""

HEAD = ('<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8">'
  '<link href="https://fonts.googleapis.com/css2?family=Anton&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">'
  f'<style>{CSS}</style></head><body>')

def pad(x): return str(x).zfill(2)

def topbar(idx, n, cta=False):
    return (f'<div class="topbar"><img src="{LOGO}" alt="741">'
            f'<div class="kicker"><div class="k">{CONFIG["series"]}</div>'
            f'<div class="c">{pad(idx)} / {pad(n)}</div></div></div>')

def foot(right):
    return f'<div class="foot"><span>741.studio</span>{right}</div>'

def slide_html(s, idx, n):
    swipe = '<span class="swipe">SWIPE →</span>'
    if s["type"]=="cover":
        h1 = "<br>".join((f'<span class="hl">{l}</span>' if i+1==s["hl"] else l) for i,l in enumerate(s["title"]))
        body = f'<div class="body cover"><div class="eyebrow">{s["eyebrow"]}</div><h1>{h1}</h1><div class="sub">{s["sub"]}</div></div>'
        return f'<div class="slide cover"><div class="halftone"></div>{topbar(idx,n)}{body}{foot(swipe)}</div>'
    if s["type"]=="stat":
        lab = "".join((f'<span>{t}</span>' if i==1 else t) for i,t in enumerate(s["lab"]))
        body = f'<div class="body stat"><div class="big">{s["big"]}</div><div class="lab">{lab}</div></div>'
        return f'<div class="slide stat"><div class="halftone"></div>{topbar(idx,n)}{body}{foot(swipe)}</div>'
    if s["type"]=="tip":
        body = f'<div class="body tip"><div class="num">{s["num"]}</div><h2>{s["title"]}</h2><div class="txt">{s["txt"]}</div></div>'
        return f'<div class="slide tip"><div class="halftone"></div>{topbar(idx,n)}{body}{foot(swipe)}</div>'
    if s["type"]=="cta":
        h2 = "<br>".join(s["title"])
        body = f'<div class="body"><div class="eyebrow">{s["eyebrow"]}</div><h2>{h2}</h2><div class="sub">{s["sub"]}</div><div class="url">{s["url"]}</div></div>'
        return f'<div class="slide cta">{topbar(idx,n)}{body}{foot(f"<span>{CONFIG['handle']}</span>")}</div>'
    return ""

def main():
    slug = sys.argv[1] if len(sys.argv)>1 else "carousel"
    outdir = os.path.join(ROOT, "output", slug)
    tmpdir = os.path.join(ROOT, "output", slug, "_html")
    os.makedirs(outdir, exist_ok=True); os.makedirs(tmpdir, exist_ok=True)
    n = len(CONFIG["slides"])
    for i,s in enumerate(CONFIG["slides"], start=1):
        htmlfile = os.path.join(tmpdir, f"slide_{i}.html")
        with open(htmlfile,"w") as f: f.write(HEAD + slide_html(s,i,n) + "</body></html>")
        png = os.path.join(outdir, f"slide_{i}.png")
        subprocess.run([CHROME,"--headless=new","--disable-gpu","--hide-scrollbars",
            "--force-device-scale-factor=1","--window-size=1080,1080",
            "--virtual-time-budget=12000",f"--screenshot={png}",f"file://{htmlfile}"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("rendered", png)

if __name__=="__main__": main()
