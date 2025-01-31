import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))

        # with open(join('data', 'file.txt'), 'r') as file:
        #   for line in file:
        #     self.wfile.write(line.encode())
        # return
        return