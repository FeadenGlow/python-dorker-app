from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000

if __name__ == "__main__":
    print(f"Serving on http://0.0.0.0:{PORT}")
    HTTPServer(('0.0.0.0', PORT), SimpleHTTPRequestHandler).serve_forever()
