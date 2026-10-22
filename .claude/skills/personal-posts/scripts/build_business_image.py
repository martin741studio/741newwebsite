#!/usr/bin/env python3
"""Build the Instagram/Facebook image for a 741 Studio business-account post:
reuses the same 07_social headless-Chrome render pipeline as
build_personal_image.py, but with the 741-BRANDED template
(07_social/templates/business_post_quote.html) -- Martin's go, 2026-10-22: full
741 branding for the business account (contrast: no branding on the personal
account, see build_personal_image.py).

Usage:
  build_business_image.py "<pull-quote text>" <platform>

platform: instagram | facebook (both render 1080x1080; same image serves both)
Writes to 07_social/output/business/<platform>_<slug>.png and prints its path.
"""
import html, os, re, subprocess, sys, tempfile

ROOT = '/Users/martindrendel/741website'
TEMPLATE = os.path.join(ROOT, '07_social', 'templates', 'business_post_quote.html')
OUT_DIR = os.path.join(ROOT, '07_social', 'output', 'business')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:40]


def build(quote, platform):
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(TEMPLATE) as f:
        page = f.read()
    page = page.replace('{{QUOTE}}', html.escape(quote))

    tmp_html = tempfile.NamedTemporaryFile(suffix='.html', delete=False, dir=OUT_DIR)
    tmp_html.write(page.encode('utf-8'))
    tmp_html.close()

    slug = slugify(quote.split('.')[0] or quote)
    out_png = os.path.join(OUT_DIR, f'{platform}_{slug}.png')

    cmd = [
        CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
        '--force-device-scale-factor=1', '--window-size=1080,1080',
        '--virtual-time-budget=12000', f'--screenshot={out_png}',
        f'file://{tmp_html.name}',
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    os.unlink(tmp_html.name)
    return out_png


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    quote, platform = sys.argv[1], sys.argv[2]
    if platform not in ('instagram', 'facebook'):
        sys.exit('platform must be instagram or facebook')
    path = build(quote, platform)
    print(path)
