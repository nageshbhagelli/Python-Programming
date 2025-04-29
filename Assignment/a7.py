#7. Write a Python program to find the highest and lowest number in each matrix (2D list).

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

highest = np.max(matrix)
lowest = np.min(matrix)

print(f"Highest element in matrix:{highest}")
print(f"Lowest element in matrix:{lowest}")