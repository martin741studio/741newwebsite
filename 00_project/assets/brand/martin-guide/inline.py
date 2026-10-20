#!/usr/bin/env python3
"""Make an HTML deliverable self-contained: replace Martin pose src paths with data URIs and inline martin-guide.css/js.
Usage: python3 inline.py in.html out.html   (pose files are looked up in the poses/ folder next to this script)"""
import sys, re, base64, os
HERE = os.path.dirname(os.path.abspath(__file__))
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding='utf-8').read()
def uri(m):
    name = os.path.basename(m.group(2)); p = os.path.join(HERE, 'poses', name)
    if not os.path.exists(p): return m.group(0)
    return m.group(1) + 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode() + '"'
h = re.sub(r'(src=")([^"]*martin-[a-z-]+\.webp)"', uri, h)
h = re.sub(r'<link[^>]+martin-guide\.css"[^>]*>', '<style>' + open(os.path.join(HERE, 'martin-guide.css')).read() + '</style>', h)
h = re.sub(r'<script[^>]+martin-guide\.js"[^>]*></script>', '<script>' + open(os.path.join(HERE, 'martin-guide.js')).read() + '</script>', h)
open(dst, 'w', encoding='utf-8').write(h); print('written', dst, len(h)//1024, 'KB')
