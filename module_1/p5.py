#5. Write a Python program to find the index of an element in a tuple

# Function to find the index of an element in a tuple
def find_index_in_tuple(t, element):
    try:
        # Using the index() method to find the index of the element
        index = t.index(element)
        return index
    except ValueError:
        # If the element is not found, return an error message
        return 0

# Input: Tuple from the user
input_tuple = tuple(input("Enter the elements of the tuple separated by spaces: ").split())

# Input: Element to find
element = input("Enter the element to find the index of: ")

# Find the index of the element in the tuple
result = find_index_in_tuple(input_tuple, element)

# Print the result
if result == 0:
    print("Element not found in tuple.")
else:
    print("The index of the element is:", result)