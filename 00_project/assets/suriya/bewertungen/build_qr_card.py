"""QR-Karte für Google-Bewertungen, Praxis Suriya (A6 + 4 Karten auf A4).
Assets (Logo, Icon, Comfortaa) kommen aus der bestehenden Bewertungs-Anleitung."""
import re, io, base64, pathlib, segno

HERE = pathlib.Path(__file__).parent
SRC = HERE.parents[3] / "07_social/templates/bewertungs-anleitung/suriya-bewertung-a4.html"
URL = "https://g.page/r/CdYiMAEOs1KiEBM/review"

src = SRC.read_text()
font = re.search(r'url\((data:font/woff2;base64,[^)]+)\)', src).group(1)
imgs = re.findall(r'<img class="(l|i)" src="(data:image/png;base64,[^"]+)"', src)
logo = dict(imgs)["l"]

buf = io.BytesIO()
segno.make(URL, error="h").save(buf, kind="svg", scale=10, border=0, dark="#2f3329", light=None)
qr = "data:image/svg+xml;base64," + base64.b64encode(buf.getvalue()).decode()

CARD = f"""<div class="card">
<img class="logo" src="{logo}" alt="Praxis Suriya">
<span class="badge">Google-Bewertung · 1 Minute</span>
<h1>Hast du dich bei mir gut aufgehoben gefühlt?</h1>
<p class="intro">Dann freue ich mich sehr über eine kurze Google-Bewertung. Deine Worte helfen anderen Menschen aus Ingelheim und der Umgebung, meine Praxis zu finden.</p>
<div class="qr"><img src="{qr}" alt="QR-Code zur Google-Bewertung"></div>
<ol><li>Kamera auf den Code</li><li>Sterne wählen und zwei, drei Sätze zu deinem Besuch schreiben</li><li>Auf „Posten“ tippen</li></ol>
<p class="sig">Danke dir. Coralie</p>
<p class="foot">Praxis Suriya · Schützenpfad 29, 55218 Ingelheim<br>{URL.replace("https://", "")}</p>
</div>"""

CSS = f"""@font-face{{font-family:"Comfortaa";font-weight:700;src:url({font}) format("woff2")}}
:root{{--dark:#2f3329;--sage:#ccd4cb;--sage-l:#eef2ed;--accent:#80795f;--grey:#5c5a55}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;color:var(--dark);background:#fff}}
.card{{width:105mm;height:148mm;padding:8mm 8mm 6mm;display:flex;flex-direction:column;align-items:center;text-align:center;background:#fff;border-top:3mm solid var(--sage)}}
.logo{{height:13mm;margin-bottom:4mm}}
.badge{{background:var(--dark);color:#fff;font-size:6.5pt;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;border-radius:20px;padding:1.3mm 3.5mm}}
h1{{font-family:"Comfortaa",Arial,sans-serif;font-size:13pt;line-height:1.25;margin:4mm 0 2.5mm}}
.intro{{font-size:8.5pt;line-height:1.45;color:var(--grey)}}
.qr{{margin:4mm 0 3mm;padding:3mm;border:1.5px solid var(--sage);border-radius:4mm;background:var(--sage-l)}}
.qr img{{width:36mm;height:36mm;display:block}}
ol{{text-align:left;font-size:8pt;line-height:1.5;padding-left:5mm;color:var(--dark)}}
ol li::marker{{color:var(--accent);font-weight:700}}
.sig{{font-family:"Comfortaa",Arial,sans-serif;font-size:10pt;margin-top:2.5mm}}
.foot{{margin-top:auto;font-size:6.3pt;color:var(--grey);line-height:1.4;border-top:1px solid var(--sage);padding-top:1.8mm;width:100%}}"""

def page(body, size, extra=""):
    return f'<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Praxis Suriya QR-Karte</title><style>@page{{size:{size};margin:0}}{CSS}{extra}</style></head><body>{body}</body></html>'

(HERE / "suriya-qr-karte-a6.html").write_text(page(CARD, "105mm 148mm"))
grid = ".sheet{width:210mm;height:296mm;display:grid;grid-template-columns:105mm 105mm;grid-template-rows:148mm 148mm}.sheet .card{outline:0.2mm dashed #bbb}"
(HERE / "suriya-qr-karte-4x-a4.html").write_text(page('<div class="sheet">' + CARD * 4 + "</div>", "A4", grid))
print("ok", URL)
