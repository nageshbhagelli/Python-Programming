#6. b. Write a decorator that converts the output of a function to uppercase.

# Decorator definition
def to_uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Call the original function
        return result.upper()  # Convert the result to uppercase
    return wrapper

# Example function using the decorator
@to_uppercase
def greet(name):
    return f"Namaste, {name}!"

# Calling the decorated function
print(greet("Vivasvaan"))
