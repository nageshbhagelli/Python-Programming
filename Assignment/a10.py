#10. Write a program to calculate the difference between the highest and lowest values in each list.

matrix = [
    [3, 8, 1],
    [1, 6, 9],
    [7, 2, 5]
]

# Calculate the difference between the highest and lowest value in each list
difference = [max(row) - min(row) for row in matrix]

# Using a for loop to print the differences
for i in range(len(difference)):
    print(f"Difference between highest and lowest values in list {i + 1}: {difference[i]}")
