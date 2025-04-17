# 4.a Reading a File in Binary Mode:
# Write a Python program that reads an image or binary file in binary mode and prints its first 100 bytes.

filename = "image.jfif"

try:
    with open(filename, "rb") as file:
        content = file.read(100)
    print("First 100 bytes:", content)
except FileNotFoundError:
    print("File not found.")
