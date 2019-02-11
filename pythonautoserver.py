import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",PORT), Handler) as httpd:
    print("========== Sup Fool, you're Connected on PORT " + str(PORT) + "==========")
    httpd.serve_forever()