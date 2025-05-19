#2. b. Write a Python program that prompts the user for an integer input and handles the case where the input is not an integer.

def get_integer():
    while True:
        try:
            num = int(input("Enter an integer: "))
            print("You entered:", num)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Example usage
get_integer()
