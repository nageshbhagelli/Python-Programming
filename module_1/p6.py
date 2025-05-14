#6. Write a Python program to generate the first N Fibonacci numbers using both recursion and iteration.

# Recursive function to generate the Nth Fibonacci number
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative function to generate the first N Fibonacci numbers
def fibonacci_iterative(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# Input: Number of Fibonacci numbers to generate
N = int(input("Enter the number of Fibonacci numbers to generate: "))

# Generate Fibonacci numbers using recursion
print("Fibonacci numbers (recursive):")
for i in range(N):
    print(fibonacci_recursive(i), end=" ")

print("\n")

# Generate Fibonacci numbers using iteration
print("Fibonacci numbers (iterative):")
print(fibonacci_iterative(N))