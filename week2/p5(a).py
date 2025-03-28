
#5. a. Write a Python program using reduce() to find the maximum number in a list.

from functools import reduce

# List of numbers
user_input = input("Enter numbers separated by spaces: ")

numbers_list = list(map(int, user_input.split()))

# Using reduce() to find the maximum number
max_number = reduce(lambda x, y: x if x > y else y, numbers_list)

# Printing the maximum number
print("The maximum number in the list is:", max_number)
