#7. Write a Python program where a function returns a lambda function that multiplies a number by a given factor.

# Function that returns a lambda function
def multiplier(factor):
    return lambda x: x * factor

# Example usage
multiply = multiplier(2)  
 

# Test the lambda functions
print(multiply(10))  
 