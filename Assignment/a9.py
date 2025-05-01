#9. Write a Python function that accepts a matrix and returns the sum of all its elements

def sum_of_matrix(matrix):
    total_sum = sum(sum(row) for row in matrix)
    return total_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = sum_of_matrix(matrix)
print(f"The sum of all elements in the matrix is {result}")
