#!/usr/bin/env python3
"""Download a Firecrawl screenshot URL and cut it into viewable tiles.
Usage: reftile.py <name> <screenshot-url-or-file-with-url> <out-dir> [max_tiles=6]
Writes <out-dir>/<name>-full.png and tiles <name>-t0.jpg ... (each 1440x900 scaled to 900 wide, easy to open with Read).
Run with /Library/Frameworks/Python.framework/Versions/3.10/bin/python3 (has Pillow)."""
import sys, os, urllib.request
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
name, src, out = sys.argv[1], sys.argv[2], sys.argv[3]
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 6
if os.path.exists(src): src = open(src).read().strip()
os.makedirs(out, exist_ok=True)
p = f'{out}/{name}-full.png'; urllib.request.urlretrieve(src, p)
im = Image.open(p).convert('RGB'); W, H = im.size; n = 0
for y in range(0, H, 900):
    if n >= mx: break
    t = im.crop((0, y, W, min(H, y + 900))); t = t.resize((900, int(t.height * 900 / W))); t.save(f'{out}/{name}-t{n}.jpg', quality=82); n += 1
print(name, W, H, 'tiles', n)
