#8. Write a Python function that takes two functions as arguments and applies both functions to a given value in sequence.

# Function that applies two functions to a given value
def apply_functions(func1, func2, value):
    return func2(func1(value))  

# Example functions
def add(x):
    return x + 2

def multiply(x):
    return x * 4

# Example usage
result = apply_functions(add, multiply, 6)  
print(result)  
