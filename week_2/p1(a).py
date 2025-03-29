#1. a. Write a Python function that takes two numbers as arguments and returns their sum.

def add(num1, num2):
    return num1 + num2

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

sum = add(num1, num2)
print("Sum is:",sum)

