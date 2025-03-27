#4. Write a Python program to count the occurrences of each character in a given string using a dictionary.

# Function to count the occurrences of each character in the string
def count_characters(s):
    # Create an empty dictionary to store character counts
    char_count = {}
    
    # Iterate over each character in the string
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # If the character is not in the dictionary, add it with count 1
        else:
            char_count[char] = 1
    
    return char_count

# Input: String from the user
input_string = input("Enter a string: ")

# Count the occurrences of each character
result = count_characters(input_string)

# Print the result
print("Character occurrences:", result)