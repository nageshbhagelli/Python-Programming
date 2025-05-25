# 5. Write a Python program to extract all even numbers from a NumPy array.

import numpy as np
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_numbers = data[data % 2 == 0]
print("\nEven numbers:", even_numbers)
