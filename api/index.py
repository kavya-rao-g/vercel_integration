import json
from http.server import BaseHTTPRequestHandler

from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # self.send_response(200)
        # self.send_header('Content-type','application/json')
        # self.end_headers()
        # self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))

        query_params = parse_qs(urlparse(self.path).query)

        # Extract names from the query parameters
        names = query_params.get("name", [])


        # marks_data = [{"name":"Qz8Y5uug","marks":18},{"name":"lKZelheI","marks":43},{"name":"MxNg3ItL","marks":32},{"name":"qaeqno","marks":20},{"name":"CMKPj","marks":8},{"name":"N3Ddd0T3","marks":81},{"name":"H2wSm19VC","marks":4},{"name":"q4LJFVI5K","marks":80},{"name":"8","marks":93},{"name":"VHlVPSTZ","marks":91},{"name":"ATo0CG","marks":70},{"name":"hRHf","marks":46},{"name":"NUbNnm36F","marks":79},{"name":"SfQ9jJN","marks":48},{"name":"O9j","marks":41}]

        # query_string = self.path.split('?')[1] if '?' in self.path else ''
        # params = dict(p.split('=') for p in query_string.split('&') if '=' in p)
        # names = params.get('name', [])

        # # If multiple names are passed (e.g. ?name=X&name=Y)
        # if isinstance(names, str):
        #     names = [names]  # Convert single string to list
        
        # Find the corresponding marks for the names
        # result = []
        # for name in names:
        #     matching_entry = next((item for item in marks_data if item["name"] == name), None)
        #     if matching_entry:
        #         # result.append(matching_entry["marks"])
        #         result.append(18)
        #     else:
        #         result.append(20)

        # Prepare JSON response
        return {
            'statusCode': 200,
            'body': json.dumps({"marks": names}),
            'headers': {
                'Content-Type': 'application/json',
            }
        }
        

'''
def handler(request):
    # Extract the 'name' parameters from the query string
    names = request.args.getlist('name')
    
    marks_data = [{"name":"Qz8Y5uug","marks":18},{"name":"lKZelheI","marks":43},{"name":"MxNg3ItL","marks":32},{"name":"qaeqno","marks":20},{"name":"CMKPj","marks":8},{"name":"N3Ddd0T3","marks":81},{"name":"H2wSm19VC","marks":4},{"name":"q4LJFVI5K","marks":80},{"name":"8","marks":93},{"name":"VHlVPSTZ","marks":91},{"name":"ATo0CG","marks":70},{"name":"hRHf","marks":46},{"name":"NUbNnm36F","marks":79},{"name":"SfQ9jJN","marks":48},{"name":"O9j","marks":41}]

    # Get the corresponding marks for the names
    result = []
    for name in names:
        # Find the entry where the name matches
        matching_entry = next((item for item in marks_data if item["name"] == name), None)
        if matching_entry:
            result.append(matching_entry["marks"])
        else:
            result.append(None)  # If name is not found, append None
    
    # Return the response as JSON
    return {
        'statusCode': 200,
        'body': json.dumps({"marks": result}),
        'headers': {
            'Content-Type': 'application/json',
        }
    }

'''