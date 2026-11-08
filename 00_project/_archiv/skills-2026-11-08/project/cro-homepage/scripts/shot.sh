#!/bin/bash
# Headless screenshots of a prototype: first viewport (1440x900) and full page cropped to its real height.
# Usage: shot.sh <url> <out-dir> [prefix]   Example: shot.sh "http://localhost:8801/index.html?shot=1" 07-prototype/screenshots prototype
# Needs Chrome and the Python with Pillow and numpy. Serve the folder first (python3 -m http.server <port>).
URL="$1"; OUT="$2"; P="${3:-prototype}"
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PY=/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
mkdir -p "$OUT"
"$CH" --headless=new --disable-gpu --hide-scrollbars --window-size=1440,900 --virtual-time-budget=9000 --screenshot="$OUT/$P-first-viewport-1440.png" "$URL" >/dev/null 2>&1
"$CH" --headless=new --disable-gpu --hide-scrollbars --window-size=1440,16000 --virtual-time-budget=9000 --screenshot=/tmp/_cro_full.png "$URL" >/dev/null 2>&1
$PY - "$OUT/$P-full-1440.png" <<'PYEOF'
import sys, numpy as np
from PIL import Image
im = Image.open('/tmp/_cro_full.png').convert('RGB'); a = np.array(im).astype(int)
bg = a[-1,0]; rows = np.where((np.abs(a-bg).sum(axis=2)>12).any(axis=1))[0]
H = int(rows.max())+40
if H >= im.height-5: print('WARNING: page is taller than the window, raise 16000')
im.crop((0,0,1440,min(H,im.height))).save(sys.argv[1]); print('full page height', H, '->', sys.argv[1])
PYEOF
