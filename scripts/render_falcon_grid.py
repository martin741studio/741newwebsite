#!/usr/bin/env python3
"""Rebuild the full Local-Falcon map+pins image when LF's own image renderer
returns a blank basemap. Inputs per report:
  - basemap PNG  (lf-static .../image/<key>       -> blank map, correct area, 1000x1000)
  - heatmap PNG  (lf-static .../heatmap-img/<key> -> 9x9 colored dots, LF's exact rank colors)
  - data_points JSON (lat/lng/rank/found per point)
Draws LF-style pins (color sampled from the heatmap, white rank label) onto the basemap
at the same fixed 9x9 pixel positions LF's working images use.
Usage: render_grid.py <basemap.png> <heatmap.png> <datapoints.json> <out.png>
"""
import sys, json
from PIL import Image, ImageDraw, ImageFont

basemap_p, heatmap_p, dp_p, out_p = sys.argv[1:5]

# --- pin centers measured from a known-good LF image (1000x1000, 9x9) ---
CENTERS_BY_N = {9: [105, 203, 302, 400, 499, 598, 696, 795, 893], 7: [113, 242, 371, 499, 628, 757, 886]}
PIN_R = 24  # radius

# --- load data points, sort into row-major grid: north->south, west->east ---
raw = open(dp_p, encoding="utf-8").read()
d = json.loads(raw[raw.find("{"):])
pts = d["data_points"] if isinstance(d, dict) else d
for p in pts:
    p["lat"] = float(p["lat"]); p["lng"] = float(p["lng"])
lats = sorted({p["lat"] for p in pts}, reverse=True)   # N -> S
lngs = sorted({p["lng"] for p in pts})                 # W -> E
N = len(lats)
assert N == len(lngs) and N in CENTERS_BY_N, (len(lats), len(lngs))
CENTERS = CENTERS_BY_N[N]
grid = {}
for p in pts:
    grid[(lats.index(p["lat"]), lngs.index(p["lng"]))] = p

# --- sample LF's exact color per point from the heatmap image ---
hm_rgba = Image.open(heatmap_p).convert("RGBA")
hm = Image.new("RGB", hm_rgba.size, (255, 255, 255))
hm.paste(hm_rgba, mask=hm_rgba.split()[3])
hw, hh = hm.size
px = hm.load()
# dots are evenly spaced: center of cell i = (i + 0.5) * size/9
hrows = [round((i + 0.5) * hh / N) for i in range(N)]
hcols = [round((i + 0.5) * hw / N) for i in range(N)]

def color_at(r, c):
    col = px[hcols[c], hrows[r]]
    if col[0] > 240 and col[1] > 240 and col[2] > 240:  # landed on background: probe nearby
        for dx in (-8, 8, 0):
            for dy in (-8, 8, 0):
                p2 = px[hcols[c] + dx, hrows[r] + dy]
                if not (p2[0] > 240 and p2[1] > 240 and p2[2] > 240):
                    return p2
    return col

# --- compose ---
base = Image.open(basemap_p).convert("RGB")
S = 4  # supersample factor for smooth circles
big = base.resize((base.width * S, base.height * S), Image.LANCZOS)
dr = ImageDraw.Draw(big)

font_paths = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial Bold.ttf",
]
def load_font(size):
    for fp in font_paths:
        try: return ImageFont.truetype(fp, size)
        except Exception: pass
    return ImageFont.load_default()
font_big = load_font(26 * S)   # 1-2 digit ranks
font_sm  = load_font(19 * S)   # "20+"

for r in range(N):
    for c in range(N):
        p = grid[(r, c)]
        cx, cy = CENTERS[c] * S, CENTERS[r] * S
        col = color_at(r, c)
        rank = p.get("rank")
        found = p.get("found")
        label = str(rank) if (found and isinstance(rank, int) and rank < 20) else "20+"
        dr.ellipse([cx - PIN_R * S, cy - PIN_R * S, cx + PIN_R * S, cy + PIN_R * S], fill=col)
        f = font_big if len(label) <= 2 else font_sm
        bb = dr.textbbox((0, 0), label, font=f)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        dr.text((cx - tw / 2 - bb[0], cy - th / 2 - bb[1]), label, font=f, fill=(255, 255, 255))

out = big.resize(base.size, Image.LANCZOS)
out.save(out_p)
print("saved", out_p)
