#5. a. Write a Python generator function that yields even numbers up to a given limit.

def even_generator(limit):
    for num in range(0, limit + 1, 2):
        yield num

# Example usage
limit = int(input("Enter limit: "))
for num in even_generator(limit):
    print(num)
