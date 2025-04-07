#5. b. Write a Python generator that generates an infinite sequence of Fibonacci numbers.

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage
fib_gen = fibonacci_generator()
for _ in range(10):  # Print first 10 Fibonacci numbers
    print(next(fib_gen))
