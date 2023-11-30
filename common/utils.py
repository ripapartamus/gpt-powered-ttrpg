import json

def safe_json_parse(input_data):
    """
    Safely parses input data as JSON. If the input is already a JSON object (dict in Python),
    it returns it directly. If it's a string, it attempts to parse it as JSON.
    """
    if isinstance(input_data, dict):
        return input_data  # Already a JSON object
    elif isinstance(input_data, str):
        try:
            return json.loads(input_data)  # Parse string as JSON
        except json.JSONDecodeError:
            print("Failed to decode JSON string.")
            return None
    else:
        print("Invalid input type:", type(input_data))
        return None