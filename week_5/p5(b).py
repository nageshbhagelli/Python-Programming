# 5.b Writing to a CSV File:
# Write a Python program that writes a list of dictionaries to a CSV file with headers.

import csv

data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]

filename = "output.csv"

with open(filename, "w", newline='') as csvfile:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(data)

print("CSV file written successfully.")
