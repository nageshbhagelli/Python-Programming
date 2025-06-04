# 7. Write a Python program to compute the mean, median, and standard deviation of a NumPy array.
import numpy as np 

data = np.array([1,2,3,4,5,6,7,8,9])

mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

print(data)
print(f"Mean of data is {mean}")
print(f"Median of data is {median}")
print(f"Standard Deviation of data is {std_dev}")