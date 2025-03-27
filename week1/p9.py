#9. Write a Python program that stops execution if it encounters a negative number in a list using the break statement.

# List of numbers
numbers = [10, 20, 30, -5, 40, 50, 60]

# Iterate through the list
for num in numbers:
    # If a negative number is encountered, stop the loop
    if num < 0:
        print("Negative number encountered. Stopping execution.")
        break
    print(num)