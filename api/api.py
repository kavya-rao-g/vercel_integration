import json

# Marks data structure
marks_data = [
    {"name": "Qz8Y5uug", "marks": 18},
    {"name": "lKZelheI", "marks": 43},
    {"name": "MxNg3ItL", "marks": 32},
    {"name": "qaeqno", "marks": 20},
    {"name": "CMKPj", "marks": 8},
    {"name": "N3Ddd0T3", "marks": 81}
]

def handler(request):
    try:
        # Extract query parameters
        query_params = request.args
        
        # Get the 'name' parameters from the query string (could be multiple 'name' parameters)
        names = query_params.getlist('name')  # Use getlist to handle multiple values for 'name'
        
        print(f"Received names: {names}")  # For debugging purposes

        # Find the corresponding marks for the names
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
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'An error occurred: ' + str(e)}),
            'headers': {
                'Content-Type': 'application/json',
            }
        }
