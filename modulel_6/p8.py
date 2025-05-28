# 8. Write a Python program to find unique elements in a NumPy array.

import numpy as np
nums = list(map(int, input("Enter list of numbers:").split()))
dup_arr = np.array(nums)
uniq_arr = np.unique(dup_arr)

print(f"Array with duplicates: {dup_arr}")
print(f"Array with unique elements: {uniq_arr}")