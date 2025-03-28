#1. b. Write a Python function that accepts a list of numbers and returns the maximum number in the list.

def find_max(numbers):
    # Check if the list is empty
    if not numbers:
        return None  # Return None if the list is empty
    return max(numbers)

# Taking input from the user
user_input = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers_list = list(map(int, user_input.split()))

# Find and print the maximum number
max_number = find_max(numbers_list)
print(f"The maximum number is: {max_number}")