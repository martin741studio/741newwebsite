#!/usr/bin/env python3
"""Local server for the element pool. Serves this folder and saves votes (POST /save) to votes.json here.
Run: python3 serve_pool.py 8815   Open: http://localhost:8815/   Local only, nothing leaves this computer."""
import sys, json, os, http.server
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8815
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
class H(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        from urllib.parse import urlparse, parse_qs
        u = urlparse(self.path)
        if u.path != '/save': self.send_error(404); return
        fn = (parse_qs(u.query).get('f') or ['votes.json'])[0]
        import re
        if not re.fullmatch(r'votes[A-Za-z0-9_.-]*\.json', fn): self.send_error(400); return
        n = int(self.headers.get('Content-Length', 0)); body = self.rfile.read(n)
        try: json.loads(body)
        except Exception: self.send_error(400); return
        open(os.path.join(HERE, fn), 'wb').write(body)
        self.send_response(204); self.end_headers()
    def log_message(self, *a): pass
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), H).serve_forever()
