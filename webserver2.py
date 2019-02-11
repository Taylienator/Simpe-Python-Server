import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print('==========Serving on Port' + str(PORT) + '==========')
    httpd.serve_forever()
