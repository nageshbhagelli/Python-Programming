#6. How do you add two matrices of the same size using NumPy? Provide an example with 2x2 matrices.

import numpy as np

matrix_1  = np.array([[2, 3], [4, 5]])
matrix_2  = np.array([[6, 7], [8, 9]])

result = matrix_1 + matrix_2
print(result)