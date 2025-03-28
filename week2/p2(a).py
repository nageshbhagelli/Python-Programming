#2. a. Write a Python program using a lambda function to find the product of two numbers.

product = lambda a, b: a*b

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print("The product using lambda is:",product(num1, num2))