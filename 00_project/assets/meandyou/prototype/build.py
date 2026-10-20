#!/usr/bin/env python3
"""Builds index.html (local preview) from page.html and converts generated images."""
import glob, os
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(os.path.expanduser('~/Downloads/meandyou-g2-*.png')):
    name = os.path.basename(f).replace('meandyou-g2-', 'gen-').replace('.png', '.webp')
    out = os.path.join(here, 'assets', name)
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(f):
        im = Image.open(f).convert('RGB'); im.save(out, quality=82, method=6); print('img', name, im.size)
page = open(os.path.join(here, 'page.html'), encoding='utf-8').read()
html = ('<!doctype html><html lang="de"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
        '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>'
        + page + '</body></html>')
open(os.path.join(here, 'index.html'), 'w', encoding='utf-8').write(html); print('index.html', len(html))
