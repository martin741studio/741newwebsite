"""Read-only scan of public site text for risky advertising-law words (law firm profile). Output is a hint list for a human."""
import re, json, os, urllib.request, datetime
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://www.stuerzl-steuerstrafrecht.de'
PAGES = ['/', '/index.php/kanzlei', '/index.php/steuerstrafrecht', '/index.php/selbstanzeigen-steuerliche-korrekturen', '/index.php/faq', '/index.php/dr-anja-stuerzl']
WORDS = r'(erfolgsquote|erfolgreich\w*|beste[rnms]?\b|f[üu]hrend\w*|spezialist\w*|experte\w*|expertin\w*|garantie\w*|garantiert|g[üu]nstig\w*|marktführer|nummer 1|#1|100 ?%)'
out = {'collected_at': datetime.datetime.now().astimezone().isoformat(timespec='seconds'), 'scope': PAGES, 'hits': {}}
for p in PAGES:
    try:
        b = urllib.request.urlopen(urllib.request.Request(BASE + p, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30).read().decode('utf-8', 'replace')
    except Exception as e: out['hits'][p] = {'error': str(e)}; continue
    t = re.sub(r'\s+', ' ', re.sub(r'<script.*?</script>|<style.*?</style>|<[^>]+>', ' ', b, flags=re.S | re.I))
    hs = []
    for m in re.finditer(WORDS, t, re.I):
        hs.append(t[max(0, m.start() - 60): m.end() + 60])
    out['hits'][p] = {'words': len(t.split()), 'hits': hs[:12]}
json.dump(out, open(os.path.join(RUN, 'evidence', 'adlaw-scan-2026-10-11.json'), 'w'), ensure_ascii=False, indent=1)
for p, v in out['hits'].items(): print(p, v.get('words'), len(v.get('hits', [])), [h[:90] for h in v.get('hits', [])[:3]])
