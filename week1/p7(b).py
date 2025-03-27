#7. b. Write a Python program to print the multiplication table of a given number.

# Function to print the multiplication table of a given number
def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Input: Number for which the multiplication table is required
num = int(input("Enter a number to print its multiplication table: "))

# Print the multiplication table
print_multiplication_table(num)
