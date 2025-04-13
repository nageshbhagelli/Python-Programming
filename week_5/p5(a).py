# 5.a Reading a CSV File:
# Write a Python program that reads a CSV file named data.csv and prints its content row by row.

import csv

filename = "data.csv"

try:
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found.")
