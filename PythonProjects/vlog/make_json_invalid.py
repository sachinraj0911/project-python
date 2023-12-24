"""This code is about tp make the valid json data to invalid json format"""
import json
import os

# Get the current script's directory
script_dir = os.path.dirname(__file__)
# Construct the absolute path to the data file
relative_path = 'support/json_data.json'
absolute_path = os.path.join(script_dir, relative_path)
with open(absolute_path, 'r') as file:
    # Load the JSON data
    data = json.load(file)

# Dump the json data in python string
str_data = json.dumps(data)
# Here making valid json data to invalid json by replacing first occurrence of "}" by ",}"
invalid_json = str_data.replace("}", ",}")
print(invalid_json)
