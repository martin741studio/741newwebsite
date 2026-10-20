import pathlib, re, json

ROOT = pathlib.Path('/Users/martindrendel/741website')
HERE = pathlib.Path(__file__).parent
tpl = (ROOT / '04_site/de/pages/wachstums-abo.html').read_text(encoding='utf8').split('\n')
head = '\n'.join(tpl[:509])          # up to and incl. {{> header_de }}
tail = '\n'.join(tpl[889:1049])      # {{> footer_de }} … {{> consent }}
assert '{{> header_de }}' in tpl[508] and '{{> footer_de }}' in tpl[889] and '{{> consent }}' in tpl[1048]

TITLE = 'KI-Website: per Chat ändern, ohne Website-Abo | 741.Studio'
DESC = 'Die 741 KI-Website änderst du per Chat. Feste Regeln und eine Prüfung bei jeder Änderung schützen Design und Rankings. Hosting 0 €, 24/7 Hilfe von 741.'
URL = 'https://741.studio/de/pages/ki-website.html'

head = re.sub(r'<title>.*?</title>', f'<title>{TITLE}</title>', head, count=1)
head = re.sub(r'<meta content="[^"]*" name="description"/>', f'<meta content="{DESC}" name="description"/>', head, count=1)
head = re.sub(r'<link href="[^"]*" rel="canonical"/>', f'<link href="{URL}" rel="canonical"/>', head, count=1)
head = re.sub(r'<meta content="[^"]*" property="og:title"/>', f'<meta content="{TITLE}" property="og:title"/>', head, count=1)
head = re.sub(r'<meta content="[^"]*" property="og:description"/>', f'<meta content="{DESC}" property="og:description"/>', head, count=1)
head = re.sub(r'<meta content="[^"]*" property="twitter:title"/>', f'<meta content="{TITLE}" property="twitter:title"/>', head, count=1)
head = re.sub(r'<meta content="[^"]*" property="twitter:description"/>', f'<meta content="{DESC}" property="twitter:description"/>', head, count=1)
head = head.replace('<head>', '<head>\n<meta name="robots" content="noindex,nofollow"/>', 1)

faq = re.findall(r'<summary>(.*?)</summary><p>(.*?)</p>', (HERE / 'sections.html').read_text(encoding='utf8'))
ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "Service", "name": "741 KI-Website", "provider": {"@type": "Organization", "name": "741.Studio", "url": "https://741.studio/"},
     "description": DESC, "areaServed": "DE", "url": URL},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
extra_head = ('<link rel="stylesheet" href="/review-assets/martin-guide/martin-guide.css">\n'
              f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
              '<style>' + (HERE / 'page.css').read_text(encoding='utf8') + '</style>\n</head>')
head = head.replace('</head>', extra_head, 1)

body = (HERE / 'sections.html').read_text(encoding='utf8')
page = head + '\n' + body + '\n' + tail + '\n<script src="/review-assets/martin-guide/martin-guide.js" defer></script>\n</body>\n</html>\n'
out = ROOT / '04_site/de/ki-website-vorschau.html'
out.write_text(page, encoding='utf8')
print('written', out, len(page))
