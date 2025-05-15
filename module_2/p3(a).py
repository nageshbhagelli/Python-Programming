#3. a. Write a Python program using map() to convert a list of strings into uppercase.

# List of strings
strings_list = ["aarya", "bharat", "charan", "dhruv"]

# Using map() to convert each string to uppercase
uppercase_list = list(map(str.upper, strings_list))

# Printing the result
print("List of strings in uppercase:", uppercase_list)
