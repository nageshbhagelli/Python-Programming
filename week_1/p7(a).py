#7. a. Write a Python program to find the largest of three numbers using if-else statements.

# Function to find the largest of three numbers
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input: Three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
largest = find_largest(num1, num2, num3)

# Output: Print the largest number
print("The largest number is:", largest)
