#2. b. Write a Python program using a lambda function to sort a list of tuples based on the second element. 

# List of tuples
tuples_list = [(1, 3), (2, 2), (4, 5), (3, 1)]

# Sorting the list of tuples based on the second element using a lambda function
sorted_list = sorted(tuples_list, key=lambda x: x[1])

# Printing the sorted list
print("Sorted list based on the second element:", sorted_list)
