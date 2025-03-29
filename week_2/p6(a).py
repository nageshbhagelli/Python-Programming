
#6. a. Write a Python decorator that prints &quot;Before calling function&quot; and &quot;After calling 
# unction&quot; around the execution of any function.

# Decorator definition
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling function")
        result = func(*args, **kwargs)  # Call the original function
        print("After calling function")
        return result
    return wrapper

# Example function using the decorator
@decorator
def greet(name):
    print(f"Namaste, {name}!")

# Calling the decorated function
greet("Vivasvaan")
