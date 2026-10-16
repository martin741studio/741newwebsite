"""Block tool names, team names, prices, verdict words in client.html. Exit 1 on a hit."""
import re, sys, os
p = os.path.join(sys.argv[1], 'report', 'client.html'); t = open(p, encoding='utf-8').read()
body = re.sub(r'<style.*?</style>', '', t, flags=re.S)
BAN = ['Local Falcon', 'Falcon', 'DataForSEO', 'Ahrefs', 'Supabase', 'Chrome', 'Claude', 'Dinakar', 'Tantri', 'Gayo', 'KEMB', 'Linkemann', 'Voss', '7.999', '3.999', 'Eignung', 'Fit-Check', 'Verdikt', 'SoLV', 'ev_', 'evidence', 'Go-A', 'Martin', 'Dritte', 'Kundin']
hits = [w for w in BAN if re.search(re.escape(w), body)]
print('client.html check:', 'FAIL ' + str(hits) if hits else 'ok'); sys.exit(1 if hits else 0)
