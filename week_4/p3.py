#3. Write a Python program to find all words in a given string that start with a vowel using regex.

import re

def find_vowel_words(text):
    words = re.findall(r"\b[aeiouAEIOU]\w*", text)
    return words

# Example usage
text = input("Enter a string: ")
print("Words starting with vowels:", find_vowel_words(text))
