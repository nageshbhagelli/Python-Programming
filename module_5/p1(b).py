# 1.b Exploring the random Module:
# Write a Python program using the random module to generate a list of 5 random integers between 1 and 100.

import random

random_numbers = [random.randint(1, 100) for _ in range(5)]
print("Random numbers:", random_numbers)
