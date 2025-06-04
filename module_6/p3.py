# 3. Write a Python program to concatenate two NumPy arrays.

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))
print("\n3. Concatenated array:", concatenated)
