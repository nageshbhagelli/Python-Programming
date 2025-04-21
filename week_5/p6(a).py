# 6.a Reading a JSON File:
# Write a Python program that reads a JSON file and prints the content in a structured format.

import json

filename = "Week_5/data.json"

try:
    with open(filename, "r") as jsonfile:
        data = json.load(jsonfile)
    print(json.dumps(data, indent=4))
except FileNotFoundError:
    print("JSON file not found.")
