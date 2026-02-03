#!/usr/bin/env python3
"""
Simple HTTP Server for AI Code Review Educational Website
Run with: python3 app.py
Access at: http://localhost:8000
"""

import http.server
import socketserver
import os
from pathlib import Path

PORT = 8000
DIRECTORY = Path(__file__).parent

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def do_GET(self):
        # Serve index.html for root path
        if self.path == '/' or self.path == '':
            self.path = '/index.html'
        return super().do_GET()

def run_server():
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"\n{'='*60}")
        print(f"🚀 AI Code Review Educational Website")
        print(f"{'='*60}")
        print(f"Server running at: http://localhost:{PORT}")
        print(f"Open your browser and visit the URL above")
        print(f"\nPress Ctrl+C to stop the server")
        print(f"{'='*60}\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✓ Server stopped gracefully")

if __name__ == "__main__":
    run_server()
