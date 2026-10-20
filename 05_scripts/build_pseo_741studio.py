#!/usr/bin/env python3
"""pSEO-Generator 741.studio (Phase B Renderer).

Setzt Shell (Live-Seiten-Skelett: Head+Nav / Footer+Consent) + einzigartigen Body
pro Zelle zusammen, schreibt Title/Meta/Canonical/OG/Schema und liefert eine
QA-Zeile pro Seite. Bodies liegen in 04_site/_pseo/741studio/bodies/<cell>.html —
heute von Claude in der Session geschrieben, später vom Engine-Backend per API.

Aufruf:  python3 05_scripts/build_pseo_741studio.py [--index]
         (Standard: robots=noindex,follow bis zur Freigabe; --index schaltet scharf)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PSEO = ROOT / "04_site/_pseo/741studio"
OUT = PSEO / "out"

INDEXABLE = "--index" in sys.argv
ROBOTS = "index,follow" if INDEXABLE else "noindex,follow"

business = json.loads((PSEO / "business.json").read_text())
services = {s["slug"]: s for s in json.loads((PSEO / "services.json").read_text())}
cities = {c["slug"]: c for c in json.loads((PSEO / "cities.json").read_text())}

# Pilot-Zellen
CELLS = [
    ("local-seo", "nuernberg"),
    ("local-seo", "fuerth"),
    ("webdesign", "erlangen"),
]

shell = (PSEO / "shell.html").read_text()
NAV_END = shell.find('<section class="hero2-section"')
FOOT_START = shell.find("<footer")
assert NAV_END > 0 and FOOT_START > NAV_END, "Shell-Grenzen nicht gefunden"
shell_top, shell_bottom = shell[:NAV_END], shell[FOOT_START:]

# Geschützte Content-CSS: px/clamp statt rem — immun gegen den Webflow-Hack
# (html{font-size:1vw bzw. 1.8vw mobil} lässt rem-Größen kollabieren/explodieren).
PSEO_CSS = """
<style id="pseo-css">
  /* ===== pSEO Design-System (px/clamp — immun gegen html{font-size:1vw}-Hack) ===== */
  .pseo-main{font-size:17px;line-height:1.65;color:#1c1c1a;}
  .pseo-main section{padding:clamp(52px,7vw,92px) 5%;position:relative;overflow:hidden;}
  .pseo-main .pseo-wrap{max-width:1140px;margin:0 auto;}
  .pseo-main .is--cream{background:#faf8f2;}
  .pseo-main .is--dark{background:#111;color:#fff;}
  .pseo-main h1{font-size:clamp(30px,4vw,50px);line-height:1.12;margin:0 0 16px;font-weight:700;}
  .pseo-main h2{font-size:clamp(24px,2.9vw,36px);line-height:1.18;margin:0 0 12px;font-weight:700;}
  .pseo-main h3{font-size:clamp(16.5px,1.5vw,20px);line-height:1.3;margin:0 0 8px;font-weight:700;}
  .pseo-main p{font-size:clamp(15px,1.2vw,17px);line-height:1.7;margin:0 0 14px;max-width:62ch;}
  .pseo-main h1,.pseo-main h2,.pseo-main h3,.pseo-main p,.pseo-main a{overflow-wrap:break-word;}
  .pseo-main .pseo-tagline{text-transform:uppercase;letter-spacing:.12em;font-weight:700;font-size:12.5px;color:#8a6a00;margin-bottom:14px;}
  .pseo-main .is--dark .pseo-tagline{color:#fac118;}
  .pseo-main .seo_highlight{color:#fac118;}
  .pseo-main .pseo-sub{font-size:clamp(16px,1.35vw,19px);color:#4a473f;}
  .pseo-main .is--dark p{color:#d8d5cc;}

  /* Hero */
  .pseo-main .pseo-hero{padding-top:200px;background:linear-gradient(180deg,#fffdf6 0%,#faf6ea 70%,#f7f0dc 100%);}
  @media(min-width:861px){.pseo-main .pseo-hero{padding-top:170px;}}
  .pseo-main .pseo-hero .pseo-wrap{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:clamp(28px,4vw,56px);align-items:center;}
  @media(max-width:860px){.pseo-main .pseo-hero .pseo-wrap{grid-template-columns:minmax(0,1fr);}}

  /* CTA-Zeile + Buttons */
  .pseo-main .pseo-cta{display:flex;flex-wrap:wrap;gap:12px;margin:22px 0 18px;}
  .pseo-main .seo_btn{display:inline-block;background:#fac118;color:#000;padding:15px 28px;border-radius:100px;font-weight:700;font-size:15.5px;text-decoration:none;white-space:normal;text-align:center;max-width:100%;box-shadow:0 6px 18px rgba(250,193,24,.25);transition:transform .15s,box-shadow .15s;}
  .pseo-main .seo_btn:hover{transform:translateY(-2px);box-shadow:0 12px 26px rgba(250,193,24,.4);}
  .pseo-main .seo_btn.is--ghost{background:#fff;border:1.5px solid #e2ddcc;box-shadow:none;}
  .pseo-main .seo_btn.is--dark{background:#111;color:#fff;box-shadow:none;}

  /* Trust-Chips */
  .pseo-main .pseo-chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:6px;}
  .pseo-main .pseo-chip{display:inline-flex;align-items:center;gap:8px;background:#fff;border:1px solid #ece7d8;border-radius:100px;padding:9px 15px;font-size:13px;font-weight:600;box-shadow:0 2px 8px rgba(37,37,37,.05);}
  .pseo-main .pseo-chip::before{content:"✓";display:inline-flex;align-items:center;justify-content:center;width:17px;height:17px;border-radius:50%;background:#fac118;color:#000;font-size:11px;font-weight:800;flex:none;}

  /* Hero-Karte */
  .pseo-main .pseo-herocard{background:#111;color:#fff;border-radius:22px;padding:clamp(24px,2.8vw,36px);box-shadow:0 24px 60px rgba(30,25,5,.18);}
  .pseo-main .pseo-herocard h3{color:#fac118;}
  .pseo-main .pseo-herocard p{color:#d8d5cc;font-size:15px;}

  /* Stat-Band */
  .pseo-main .pseo-stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(18px,3vw,44px);max-width:1140px;margin:0 auto;text-align:center;}
  @media(max-width:640px){.pseo-main .pseo-stats{grid-template-columns:minmax(0,1fr);gap:26px;}}
  .pseo-main .pseo-stat b{display:block;font-size:clamp(30px,3.4vw,46px);line-height:1;color:#fac118;margin-bottom:8px;font-weight:800;}
  .pseo-main .pseo-stat span{font-size:14px;color:#d8d5cc;}

  /* Karten-Raster */
  .pseo-main .pseo-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin-top:26px;}
  .pseo-main .pseo-card{background:#fff;border:1px solid #ece7d8;border-radius:18px;padding:clamp(20px,2.2vw,28px);box-shadow:0 4px 16px rgba(37,37,37,.04);}
  .pseo-main .is--dark .pseo-card{background:#1a1a1a;border-color:#2c2c2c;}
  .pseo-main .pseo-card p{font-size:14.5px;margin:0;}

  /* Prozess-Schritte */
  .pseo-main .pseo-steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-top:26px;counter-reset:step;}
  .pseo-main .pseo-step{background:#fff;border:1px solid #ece7d8;border-radius:18px;padding:22px;position:relative;}
  .pseo-main .pseo-step::before{counter-increment:step;content:counter(step,decimal-leading-zero);font-family:'Press Start 2P',monospace;font-size:13px;color:#fac118;display:block;margin-bottom:12px;}
  .pseo-main .pseo-step p{font-size:14.5px;margin:0;}

  /* Einzugsgebiet */
  .pseo-main .pseo-districts{display:flex;flex-wrap:wrap;gap:9px;margin:16px 0 6px;}
  .pseo-main .pseo-district{background:#fff;border:1px solid #ece7d8;border-radius:100px;padding:8px 15px;font-size:13.5px;font-weight:600;}
  .pseo-main .pseo-district.is--link{border-color:#fac118;background:#fffaf0;}
  .pseo-main .pseo-district a{text-decoration:none;color:inherit;}

  /* FAQ Akkordeon */
  .pseo-main .pseo-faq{max-width:820px;margin:26px auto 0;}
  .pseo-main .pseo-faq details{background:#fff;border:1px solid #ece7d8;border-radius:14px;margin-bottom:10px;padding:0 20px;}
  .pseo-main .is--cream .pseo-faq details{background:#fff;}
  .pseo-main .pseo-faq summary{font-weight:700;font-size:15.5px;padding:17px 26px 17px 0;cursor:pointer;list-style:none;position:relative;line-height:1.4;}
  .pseo-main .pseo-faq summary::-webkit-details-marker{display:none;}
  .pseo-main .pseo-faq summary::after{content:"+";position:absolute;right:0;top:50%;transform:translateY(-50%);font-size:22px;color:#8a6a00;font-weight:400;}
  .pseo-main .pseo-faq details[open] summary::after{content:"–";}
  .pseo-main .pseo-faq details p{padding-bottom:16px;max-width:none;font-size:14.5px;}

  /* CTA-Band */
  .pseo-main .pseo-ctaband{max-width:1140px;margin:0 auto;background:#fac118;border-radius:26px;padding:clamp(32px,4.5vw,58px);text-align:center;}
  .pseo-main .pseo-ctaband h2{margin-bottom:8px;}
  .pseo-main .pseo-ctaband p{margin:0 auto 20px;max-width:56ch;}
  .pseo-main .pseo-ctaband .pseo-cta{justify-content:center;margin:0;}

  /* Sticky WhatsApp */
  .pseo-wa-sticky{position:fixed;right:18px;bottom:18px;z-index:80;width:58px;height:58px;border-radius:50%;background:#25D366;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 26px rgba(0,0,0,.28);text-decoration:none;}
  .pseo-wa-sticky svg{width:30px;height:30px;fill:#fff;}

  /* Pain-Sektion (PAS) */
  .pseo-main .pseo-letter{background:#fff;border:1px solid #ece7d8;border-radius:20px;padding:clamp(24px,3vw,42px);max-width:780px;margin:26px auto 0;box-shadow:0 8px 30px rgba(37,37,37,.05);}
  .pseo-main .pseo-letter p{max-width:none;}
  .pseo-main ul.pseo-checks{list-style:none;padding:0;margin:0 0 18px;}
  .pseo-main ul.pseo-checks li{padding-left:32px;position:relative;margin-bottom:12px;font-size:15.5px;font-weight:600;line-height:1.5;}
  .pseo-main ul.pseo-checks li::before{content:"✓";position:absolute;left:0;top:1px;width:21px;height:21px;border-radius:50%;background:#fac118;color:#000;font-size:12px;font-weight:800;display:flex;align-items:center;justify-content:center;}
  .pseo-main ul.pseo-crosses{list-style:none;padding:0;margin:0 0 18px;}
  .pseo-main ul.pseo-crosses li{padding-left:32px;position:relative;margin-bottom:12px;font-size:15px;line-height:1.5;}
  .pseo-main ul.pseo-crosses li::before{content:"✕";position:absolute;left:0;top:1px;width:21px;height:21px;border-radius:50%;background:#1c1c1a;color:#fff;font-size:11px;font-weight:800;display:flex;align-items:center;justify-content:center;}

  .pseo-main .reveal-up{opacity:1 !important;transform:none !important;}
  .pseo-main ul{margin:0 0 14px;padding-left:22px;}
  .pseo-main li{font-size:clamp(14.5px,1.2vw,16.5px);line-height:1.65;margin-bottom:8px;}
  .pseo-main a:not(.seo_btn):not(.pseo-wa-sticky){color:inherit;text-decoration:underline;text-decoration-color:#fac118;text-decoration-thickness:2px;text-underline-offset:3px;font-weight:600;}
</style>
</head>"""


def faqs_from_body(body: str):
    """FAQ-Paare (h3 endet mit '?') + folgender Absatz fürs FAQPage-Schema."""
    out = []
    for m in re.finditer(r"<(?:h3|summary)>([^<]*\?)</(?:h3|summary)>\s*<p[^>]*>(.*?)</p>", body, re.S):
        q = m.group(1).strip()
        a = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        out.append((q, re.sub(r"\s+", " ", a)))
    return out


def schema_blocks(svc, city, url, faqs):
    biz = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": business["name"], "url": business["siteUrl"],
        "telephone": business["phone"],
        "areaServed": {"@type": "City", "name": city["name"]},
        "priceRange": business["priceRange"],
    }
    service = {
        "@context": "https://schema.org", "@type": "Service",
        "serviceType": f'{svc["name"]} {city["name"]}',
        "provider": {"@type": "ProfessionalService", "name": business["name"], "url": business["siteUrl"]},
        "areaServed": {"@type": "City", "name": city["name"]},
        "url": url,
    }
    faq = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs
        ],
    }
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Start", "item": business["siteUrl"] + "/de/"},
            {"@type": "ListItem", "position": 2, "name": svc["name"],
             "item": business["siteUrl"] + business["hubs"].get(svc["slug"], "/de/")},
            {"@type": "ListItem", "position": 3, "name": f'{svc["name"]} {city["name"]}', "item": url},
        ],
    }
    return "\n".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>'
        for b in [biz, service, faq, crumbs]
    )


def build_cell(svc_slug, city_slug):
    svc, city = services[svc_slug], cities[city_slug]
    slug = f"{svc_slug}-{city_slug}"
    url = f'{business["siteUrl"]}/{slug}/'
    body = (PSEO / "bodies" / f"{slug}.html").read_text()

    title = f'{svc["h1noun"]} {city["name"]} | {business["name"]}'
    desc = f'{svc["h1noun"]} in {city["name"]}: {svc["intro_angle"][:120]} Kostenloses Erstgespräch.'
    faqs = faqs_from_body(body)

    top = shell_top.replace(
        re.search(r"<title>[^<]*</title>", shell_top).group(0),
        f"<title>{title}</title>", 1)
    inject = (
        f'<meta name="description" content="{desc}">\n'
        f'<meta name="robots" content="{ROBOTS}">\n'
        f'<link rel="canonical" href="{url}">\n'
        f'<meta property="og:title" content="{title}">\n'
        f'<meta property="og:description" content="{desc}">\n'
        f'<meta property="og:url" content="{url}">\n'
        f'<meta property="og:type" content="website">\n'
        + schema_blocks(svc, city, url, faqs) + "\n" + PSEO_CSS)
    top = top.replace("</head>", inject, 1)

    quiz = (PSEO / "quiz-embed.html").read_text()
    # Vorher/Nachher-Grid (echter Review-Scan) nach dem Stat-Band, nur Local-SEO-Seiten
    if svc_slug == "local-seo":
        mapsvs = (PSEO / "mapsvs-embed.html").read_text()
        stats_i = body.find("pseo-stats")
        if stats_i > 0:
            close_i = body.find("</section>", stats_i) + len("</section>")
            body = body[:close_i] + "\n" + mapsvs + "\n" + body[close_i:]
    html = top + '<main class="pseo-main">\n' + body + "\n</main>\n" + quiz + "\n" + shell_bottom
    dest = OUT / slug / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html)

    # QA
    text = re.sub(r"<[^>]+>", " ", body)
    words = len(re.findall(r"[A-Za-zÄÖÜäöüß-]{2,}", text))
    levers = sum([
        any(d.split(" ")[0].strip("(),") in body for d in city["districts"]),
        any(n in body.lower() for n in city["neighbours"]),
        city["postal"][0] in body,
        any(l.split(" ")[0] in body for l in city["landmarks"]),
        svc["timeline"].split(" ")[0] in body or "90 Tage" in body,
    ])
    print(f"QA {slug}: {words} Wörter · {len(faqs)} FAQs · ≥{levers} Lokalhebel · robots={ROBOTS}")
    return slug


if __name__ == "__main__":
    print(f"Baue {len(CELLS)} Zellen (robots={ROBOTS}) …")
    for s, c in CELLS:
        build_cell(s, c)
    print("Fertig →", OUT)
