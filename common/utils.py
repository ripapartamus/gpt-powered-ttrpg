import json
import re

def safe_json_parse(input_data):
    """
    Safely parses input data as JSON. Handles the following cases:
    1. If the input is already a dict (JSON object), returns it directly.
    2. If the input is a string and doesn't contain triple backticks, parses it as JSON.
    3. If the input is a string with a JSON object enclosed in triple backticks,
       extracts the JSON and parses it.
    """
    # Case 1: Input is already a JSON object (dict)
    if isinstance(input_data, dict):
        return input_data

    # Case 2 & 3: Input is a string
    elif isinstance(input_data, str):
        try:
            # Check for triple backticks and extract JSON
            match = re.search(r"```json\n(.*?)\n```", input_data, re.DOTALL)
            if match:  # JSON object found in triple backticks
                json_string = match.group(1)
            else:  # No triple backticks, use the string as is
                json_string = input_data

            # Attempt to parse the JSON string
            return json.loads(json_string)

        except json.JSONDecodeError:
            print("Failed to decode JSON string.")
            return None

    # Case 4: Invalid input type
    else:
        print("Invalid input type:", type(input_data))
        return None