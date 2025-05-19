#6. Write a Python program to search for and extract all phone numbers from a given block of text.
# Assume phone numbers can be in formats like (123) 456-7890 or 123-456-7890.

import re

def extract_phone_numbers(text):
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return re.findall(pattern, text)

# Example usage
text = input("Enter text containing phone numbers: ")
print("Extracted phone numbers:", extract_phone_numbers(text))
