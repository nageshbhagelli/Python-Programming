#1. a. Write a Python program to check if a given string contains only letters (a-z, A-Z) using regex.

import re

def contains_only_letters(s):
    return bool(re.fullmatch(r"[a-zA-Z]+", s))

# Example usage
string = input("Enter a string: ")
if contains_only_letters(string):
    print("The string contains only letters.")
else:
    print("The string contains non-letter characters.")