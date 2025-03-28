#5. b.Write a Python program using reduce() to compute the product of all numbers in a given list.

from functools import reduce

#List of numbers
num_list = [1, 2, 3, 4, 5, 6, 7, 8]

# Using reduce() to find the product of all numbers
product = reduce(lambda x, y: x * y, num_list)

# Printing the product
print("The product of all numbers is:", product)
