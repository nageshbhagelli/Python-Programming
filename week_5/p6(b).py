# 6.b Writing to a JSON File:
# Write a Python program that takes user input and writes it to a JSON file.

import json

data = {
    "name": input("Enter your name: "),
    "age": input("Enter your age: "),
    "city": input("Enter your city: ")
}

filename = "user_data.json"

with open(filename, "w") as jsonfile:
    json.dump(data, jsonfile, indent=4)

print("Data written to JSON file.")
