#4. a. Write a Python program using filter() to extract even numbers from a list.

# List of numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() to extract even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))

# Printing the even numbers
print("Even numbers :", even_numbers)
