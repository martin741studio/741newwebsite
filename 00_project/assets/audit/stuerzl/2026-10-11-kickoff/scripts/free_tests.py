"""Phase 1: free tool tests: PageSpeed Insights, Google autocomplete (brand), GA4 + GSC via service account. Read only."""
import json, os, urllib.request, urllib.parse, datetime, time
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EV = os.path.join(RUN, 'evidence'); out = {'collected_at': datetime.datetime.now().astimezone().isoformat(timespec='seconds')}
def j(url, headers=None, data=None, timeout=90):
    req = urllib.request.Request(url, data=data, headers=headers or {'User-Agent': 'Mozilla/5.0'})
    try:
        r = urllib.request.urlopen(req, timeout=timeout); return r.status, r.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e: return e.code, e.read().decode('utf-8', 'replace')[:600]
    except Exception as e: return None, str(e)
# 1 PageSpeed (mobile)
u = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?' + urllib.parse.urlencode({'url': 'https://www.stuerzl-steuerstrafrecht.de/', 'strategy': 'mobile', 'category': 'performance'})
s, b = j(u, timeout=120); out['pagespeed_status'] = s
try:
    d = json.loads(b); a = d['lighthouseResult']['audits']
    out['pagespeed'] = {k: a[k].get('displayValue') for k in ('largest-contentful-paint', 'cumulative-layout-shift', 'total-blocking-time', 'first-contentful-paint', 'speed-index') if k in a}
    out['pagespeed']['score'] = d['lighthouseResult']['categories']['performance']['score']
    out['pagespeed']['field_data'] = d.get('loadingExperience', {}).get('metrics', {}) and {k: v.get('category') for k, v in d['loadingExperience']['metrics'].items()}
except Exception: out['pagespeed_raw'] = b[:500]
# 2 autocomplete brand queries
ac = {}
for q in ['stürzl steuerstrafrecht ', 'stürzl steuerstrafrecht erfahrungen', 'anja stürzl anwältin ', 'stürzl steuerstrafrecht frankfurt ', 'kanzlei stürzl abzocke']:
    s, b = j('https://suggestqueries.google.com/complete/search?client=firefox&hl=de&gl=de&q=' + urllib.parse.quote(q))
    try: ac[q] = json.loads(b)[1]
    except Exception: ac[q] = b[:100]
out['autocomplete_brand'] = ac
# 3 GA4 + GSC via service account
try:
    import subprocess, sys
    key = '/Users/martindrendel/741website/.secrets/ga-sc-reporting-bot.json'
    out['sa_key_present'] = os.path.exists(key)
    import importlib.util
    out['google_auth_lib'] = bool(importlib.util.find_spec('google.oauth2'))
except Exception as e: out['sa_err'] = str(e)
json.dump(out, open(os.path.join(EV, 'free-tests-2026-10-11.json'), 'w'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1)[:3500])
