import http.server
import socketserver
import os

PORT = 8000

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

os.chdir('/app')

with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print(f"\n{'='*60}")
    print(f"COG SERVER RUNNING")
    print(f"{'='*60}\n")
    print(f"URL: http://localhost:{PORT}")
    print(f"Frontend: http://localhost:{PORT}/frontend/index.html")
    print(f"COG file: http://localhost:{PORT}/data/cog/srtm_cog.tif")
    print(f"\nPress Ctrl+C to stop\n")
    httpd.serve_forever()