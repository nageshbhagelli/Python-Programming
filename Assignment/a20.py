# 20. Write a Python program that calculates the percentage of each element 
# in a matrix relative to the total sum of all elements.

import numpy as np

def matrix_percentages(matrix):
    total_sum = np.sum(matrix)
    return (matrix / total_sum) * 100

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = matrix_percentages(matrix)
print("Percentage of each element in the matrix relative to the total sum:")
print(result)
