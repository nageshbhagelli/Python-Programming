# 4.b Writing a File in Binary Mode:
# Write a Python program that opens an image file in binary mode and writes it to a new file.

source_image = "week_5/python.jpeg"
destination_image = "week_5/copy.jpg"

try:
    with open(source_image, "rb") as src, open(destination_image, "wb") as dest:
        dest.write(src.read())
    print("Image copied successfully.")
except FileNotFoundError:
    print("Source image not found.")
