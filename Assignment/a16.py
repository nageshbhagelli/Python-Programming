# 16. Write Python code to compute the sum of the diagonal elements of a square matrix.

import numpy as np

def sum_of_diagonal(matrix):
    return np.trace(matrix)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = sum_of_diagonal(matrix)
print(f"The sum of the diagonal elements of a square matrix is: {result}")
