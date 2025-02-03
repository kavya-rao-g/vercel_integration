from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any domain
        self.send_header('Access-Control-Allow-Methods', 'GET')  # Allow only GET requests
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Allow necessary headers
        self.end_headers()
        # Parse query parameters
        query_params = parse_qs(urlparse(self.path).query)

        # Extract names from the query parameters
        names = query_params.get("name", [])
        print(names)
        # Prepare response
        

        with open("./public/q-vercel-python.json", "r", encoding="utf-8") as file:
            marks_data = json.load(file)  # data is now a dictionary

        # Print the dictionary
        print(marks_data)
        result = []
        for name in names:
            # Find the entry where the name matches
            matching_entry = next((item for item in marks_data if item["name"] == name), None)
            if matching_entry:
                result.append(matching_entry["marks"])
            else:
                result.append(None)  # If name is not found, append None
    

        # Send HTTP response
        #self.send_response(200)
        #self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'marks':result}).encode('utf-8'))


    