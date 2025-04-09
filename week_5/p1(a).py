# 1.a Using Built-in Modules:
# Write a Python program that uses the math module to compute the square root, factorial, and GCD of given numbers.

import math

num1 = int(input("Enter a number for square root and factorial: "))
num2 = int(input("Enter another number for GCD: "))

print(f"Square root of {num1}: {math.sqrt(num1)}")
print(f"Factorial of {num1}: {math.factorial(num1)}")
print(f"GCD of {num1} and {num2}: {math.gcd(num1, num2)}")
