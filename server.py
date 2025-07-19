import http.server
import socketserver
import webbrowser
import os

PORT = 7777  # You can change this to any free port

# Change directory to where your index.html is located
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(PROJECT_DIR)

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return  # Suppress terminal log output

print(f"✅ Starting RakshaBandhan Card on http://localhost:{PORT}")
try:
    with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
        webbrowser.open(f"http://localhost:{PORT}")
        httpd.serve_forever()
except OSError:
    print(f"❌ Port {PORT} is already in use. Try a different port.")


