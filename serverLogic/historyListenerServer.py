
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
import os

def addToFile(filePath, jsonDict):
    toTruncate = open(filePath, 'rb+')
    toTruncate.seek(-1, os.SEEK_END)
    toTruncate.truncate()

    toAppend = open(filePath,'a')
    toAppend.write(',')
    json.dump(jsonDict['history'][0], toAppend, ensure_ascii=False)
    toAppend.write(']');

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
        # self._set_headers()

        jsonDict = json.loads(post_data.decode('utf-8'))
        filePath = '/home/ubuntu/historyStorage/' + jsonDict['name'] + '.json';
        if(os.path.isfile(filePath)):
            addToFile(filePath, jsonDict)
        else:
            toWrite = open(filePath, 'w')
            json.dump(jsonDict['history'], toWrite, ensure_ascii=False)
        respond(self)


def respond(s):
    s.send_response(200)
    s.send_header("Content-type", "application/json")
    s.end_headers()
    s.wfile.write(bytes('{"tst":"hi"}',"UTF-8"));
    # s.wfile.write(bytes("<html><head><title>Title goes here.</title></head>",'UTF-8'))
    # s.wfile.write(bytes("<body><p>This is a test.</p>",'UTF-8'))
    # s.wfile.write(bytes("<p>You accessed path:</p>",'UTF-8'))
    # s.wfile.write(bytes("</body></html>",'UTF-8'))

def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
