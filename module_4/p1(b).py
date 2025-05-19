#1.b. Write a Python program to validate a strong password (at least 8 characters, including
# uppercase, lowercase, numbers, and special characters) using regex.
import re

def is_strong_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return bool(re.fullmatch(pattern, password))

# Example usage
password = input("Enter a password: ")
if is_strong_password(password):
    print("The password is strong.")
else:
    print("The password is weak.")