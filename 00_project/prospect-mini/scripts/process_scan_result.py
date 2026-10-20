#!/usr/bin/env python3
"""Process completed Local Falcon scan report:
- saves JSON to evidence/falcon-report-<key>.json
- downloads image and converts to 04_site/public/review-assets/<slug>/scan-grid.webp
- generates competitors.md
- updates run-state.json
"""
import sys, json, os, urllib.request, subprocess, datetime, math

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '00_project', 'audit-workflow', 'scripts'))
sys.path.insert(0, os.path.join(ROOT, '00_project', 'prospect-mini', 'scripts'))
import lf_client as lf
import evidence_lib as el

def haversine_km(lat1, lon1, lat2, lon2):
    try:
        la1, lo1, la2, lo2 = map(math.radians, (float(lat1), float(lon1), float(lat2), float(lon2)))
        h = math.sin((la2 - la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2 - lo1)/2)**2
        return 6371 * 2 * math.asin(math.sqrt(h))
    except Exception:
        return 0.0

def process(slug, report_key, keyword):
    pdir = os.path.join(ROOT, '00_project', 'prospects', slug)
    os.makedirs(f'{pdir}/evidence', exist_ok=True)
    asset_dir = os.path.join(ROOT, '04_site', 'public', 'review-assets', slug)
    os.makedirs(asset_dir, exist_ok=True)
    
    sid = lf.session()
    r = lf.call('getLocalFalconReport', {'reportKey': report_key}, sid)
    txt = json.loads(r['result']['content'][0]['text'])
    if txt.get('_mcp_status') == 'processing':
        print(f'{slug}: Still processing')
        return False
        
    data = txt.get('data', txt)
    
    # 1. Save raw report
    rep_file = f'{pdir}/evidence/falcon-report-{report_key}.json'
    with open(rep_file, 'w', encoding='utf-8') as f:
        json.dump(txt, f, indent=2, ensure_ascii=False)
    print(f'{slug}: Saved report to {rep_file}')
    
    # 2. Download and convert image
    img_url = data.get('image')
    if img_url:
        png_temp = f'{pdir}/evidence/scan-grid.png'
        webp_out = f'{asset_dir}/scan-grid.webp'
        subprocess.run(['curl', '-sL', '--max-time', '30', img_url, '-o', png_temp], check=True)
        subprocess.run(['/opt/homebrew/bin/cwebp', '-q', '85', png_temp, '-o', webp_out], check=True)
        print(f'{slug}: Converted scan image to {webp_out}')
    
    # 3. Analyze rankings & competitors
    centre_lat = data.get('lat')
    centre_lng = data.get('lng')
    places = data.get('places') or {}
    places_list = list(places.values()) if isinstance(places, dict) else list(places)
    
    # Find own place
    own = None
    pid = data.get('place_id') or (data.get('location') or {}).get('place_id')
    for p in places_list:
        if p.get('place_id') == pid:
            own = p
            break
    if not own:
        own = data.get('location') or {}
        
    solv = float(data.get('solv') or 0)
    found_in = int(data.get('found_in') or 0)
    
    # Sort competitors by solv descending
    comps = [p for p in places_list if p.get('place_id') != pid]
    comps.sort(key=lambda x: float(x.get('solv') or 0), reverse=True)
    top4 = comps[:4]
    
    # 4. Generate competitors.md
    lines = [
        f'# Scan: {data.get("location", {}).get("name", slug)} (agent D, {datetime.date.today().isoformat()})',
        '',
        f'Report key: `{report_key}`. Evidence: `evidence/falcon-report-{report_key}.json`, `evidence/scan-grid.png`. Web image: `../../04_site/public/review-assets/{slug}/scan-grid.webp`.',
        '',
        '## Scan setup',
        f'- Keyword: **{keyword}**',
        f'- Grid: {data.get("grid_size", "7")} x {data.get("grid_size", "7")} = 49 points, radius {data.get("radius", 5)} km, centre ({centre_lat}, {centre_lng}). Platform: Google. Cost: 49 credits.',
        '',
        '## Result (matches the image)',
        f'- Share of local voice (top 3): **SoLV {solv:.2f} %**.',
        f'- Found in **{found_in} of 49 points**.',
        f'- ARP: {data.get("arp", "n/a")}, ATRP: {data.get("atrp", "n/a")}.',
        f'- Own entry: {own.get("name")}, rating {own.get("rating")}, {own.get("reviews")} reviews.',
        '',
        '## Top 4 competitors by share of local voice',
        '| # | Name | Category (German) | Reviews | Stars | Share (SoLV) | Distance to centre |',
        '|---|---|---|---|---|---|---|'
    ]
    
    for i, c in enumerate(top4, 1):
        dist = haversine_km(centre_lat, centre_lng, c.get('lat', 0), c.get('lng', 0))
        cat = el.cats_de(c)
        lines.append(f'| {i} | {c.get("name")} | {cat} | {c.get("reviews", 0)} | {c.get("rating", "0.0")} | {float(c.get("solv", 0)):.2f} % | {dist:.1f} km |')
        
    comp_file = f'{pdir}/competitors.md'
    with open(comp_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f'{slug}: Wrote {comp_file}')
    
    # 5. Update run-state.json
    run_state_file = f'{pdir}/run-state.json'
    if os.path.exists(run_state_file):
        with open(run_state_file, 'r', encoding='utf-8') as f:
            rs = json.load(f)
        rs.setdefault('steps', {})['scan'] = {
            'agent': 'D',
            'status': 'done',
            'at': datetime.datetime.now().isoformat(),
            'keyword': keyword,
            'report_key': report_key,
            'solv': solv,
            'found_in': found_in,
            'credits': 49,
            'outputs': [
                f'evidence/falcon-report-{report_key}.json',
                f'../../04_site/public/review-assets/{slug}/scan-grid.webp',
                'competitors.md'
            ]
        }
        with open(run_state_file, 'w', encoding='utf-8') as f:
            json.dump(rs, f, indent=1, ensure_ascii=False)
        print(f'{slug}: Updated run-state.json')
        
    return True

if __name__ == '__main__':
    slug = sys.argv[1]
    rep_key = sys.argv[2]
    kw = sys.argv[3]
    process(slug, rep_key, kw)
