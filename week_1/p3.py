#3. Write a Python program to remove all duplicate elements from a given list using sets.

# Function to remove duplicates using a set
def remove_duplicates(lst):
    # Convert the list to a set, which automatically removes duplicates
    unique_elements = set(lst)
    # Convert the set back to a list
    return list(unique_elements)

# Input: List with duplicates
input_list = [1, 2, 2, 3, 4, 1, 5, 6, 4, 7]

# Remove duplicates
output_list = remove_duplicates(input_list)

# Print the result
print("List after removing duplicates:", output_list)