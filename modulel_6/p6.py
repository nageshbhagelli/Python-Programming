# 6. Write a Python program to replace all negative numbers in a NumPy array with zero.

import numpy as np
array_with_negatives = np.array([-3, -1, 0, 2, -5, 6])
array_with_negatives[array_with_negatives < 0] = 0
print("\n6. Replaced negatives with zero:", array_with_negatives)
