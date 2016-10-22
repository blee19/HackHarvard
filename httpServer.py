
#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self._set_headers()
#        self.wfile.write("<html><body><h1>POST!</h1></body></html>")	
        
        filePath = '../database/historyStorage_%s.json' % (str(time.time()).replace(".", ""))
        with open(filePath, 'w') as f:
            body_unicode = post_data.decode('utf-8')
            json.dump(json.loads(body_unicode), f, ensure_ascii=False)


	
        
def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    run() 


