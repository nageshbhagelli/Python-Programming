#4. b. Write a Python program using filter() to remove empty strings from a list.

#List of strings
strings = ["", "dhramaraja", "", "arjuna", "", "bheema", "", "nakula", "sahadeva"]

#Using filter() to remove empty strings from a list
new_strings = list(filter(lambda str: str != "", strings))

#Print the result
print("List of strings without empty strings:", new_strings)
