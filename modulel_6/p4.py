# 4. Write a Python program to split a NumPy array into three equal-sized subarrays.

import numpy as np
split_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
subarrays = np.split(split_array, 3)
print("\nSplit into three subarrays:", subarrays)
