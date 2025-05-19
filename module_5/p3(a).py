# 3.a Copy File Contents:
# Write a Python program that reads a file and writes its contents to another file.

source_file = "week_5/source.txt"
destination_file = "week_5/copy.txt"

try:
    with open(source_file, "r") as src, open(destination_file, "w") as dest:
        dest.write(src.read())
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
