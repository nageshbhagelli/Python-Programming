#4. b. Write a Python class that implements an iterator to return even numbers up to a given limit.

class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        if self.num > self.limit:
            raise StopIteration
        return self.num

# Example usage 
limit = int(input("Enter limit: "))
even_numbers = EvenNumbers(limit)
for num in even_numbers:
    print(num)
