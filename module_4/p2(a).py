#2. a. Write a Python program to handle multiple exceptions (e.g., ZeroDivisionError, ValueError, and TypeError).

def handle_exceptions():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    except TypeError:
        print("Error: Type mismatch occurred.")

# Example usage
handle_exceptions()
