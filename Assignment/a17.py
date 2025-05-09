# 17. Write a Python function to find the most frequent element in a list of numbers.

from collections import Counter

def most_frequent(numbers):
    count = Counter(numbers)
    return count.most_common(1)[0][0]

numbers = [1, 2, 2, 3, 3, 3, 4]
result = most_frequent(numbers)
print(f"The most frequent element is: {result}")
