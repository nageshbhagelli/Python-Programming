def factorial(n):
    if(n == 0 or n ==1):
        return 1
    else:
        return n * factorial(n -1)
    
num = int(input("Enter a number: "))
if(num < 0):
    print("Factorial of negaitive numbers is not defined!")
else:
    result = factorial(num)
    print(f"Factorial of {num} is {result}")