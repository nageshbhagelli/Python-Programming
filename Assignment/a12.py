# 12. Write a Python function that multiplies two matrices using NumPy.

import numpy as np

def multiply_matrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = multiply_matrices(matrix1, matrix2)

print("Result of matrix multiplication:")
print(result)
