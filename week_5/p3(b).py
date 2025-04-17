# 3.b Count Words in a File:
# Write a Python program that reads a file and counts the number of words in it.

filename = "week_5/source.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        word_count = len(content.split())
    print("Word count:", word_count)
except FileNotFoundError:
    print("File not found.")
