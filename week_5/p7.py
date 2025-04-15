# 7. Write a Python program that tries to open a non-existent file and gracefully handles the FileNotFoundError.

filename = "non_existent.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
    print("File content:", content)
except FileNotFoundError:
    print("Error: The file does not exist.")

