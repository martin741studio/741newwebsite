#!/usr/bin/env python3
"""Local server for the Track B element pool. Serves the pool folder and saves votes (POST /save) to votes.json.
Usage: python3 serve_pool.py <port> <pool-folder>
Example: python3 serve_pool.py 8815 00-element-pool
Local only, nothing leaves this computer."""
import sys, json, os, http.server

PORT = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 8815
TARGET_DIR = sys.argv[2] if len(sys.argv) > 2 else os.getcwd()
TARGET_DIR = os.path.abspath(TARGET_DIR)
os.chdir(TARGET_DIR)

class H(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        from urllib.parse import urlparse, parse_qs
        u = urlparse(self.path)
        if u.path != '/save':
            self.send_error(404)
            return
        fn = (parse_qs(u.query).get('f') or ['votes.json'])[0]
        import re
        if not re.fullmatch(r'votes[A-Za-z0-9_.-]*\.json', fn):
            self.send_error(400)
            return
        n = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(n)
        try:
            json.loads(body)
        except Exception:
            self.send_error(400)
            return
        with open(os.path.join(TARGET_DIR, fn), 'wb') as f:
            f.write(body)
        self.send_response(204)
        self.end_headers()

    def log_message(self, *a):
        pass

if __name__ == '__main__':
    print(f"Serving Track B Element Pool from {TARGET_DIR} at http://127.0.0.1:{PORT}/")
    server = http.server.ThreadingHTTPServer(('127.0.0.1', PORT), H)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
