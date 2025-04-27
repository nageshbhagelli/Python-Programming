#3. Write a Python program that prints the highest and lowest number from a list.

num_list = [155, 202, 8, 189, 314, 64, 132]

# Using built-in functions
highest = max(num_list)
lowest = min(num_list)
print(f"Highest number: {highest}")
print(f"Lowest number: {lowest}")

#Manually finding the maximum and minimum using for loop and if condition
# Assume the first number is both highest and lowest
highest = num_list[0]
lowest = num_list[0]

# Loop through the list to find highest and lowest
for num in num_list:
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num

print(f"Highest number: {highest}")
print(f"Lowest number: {lowest}")
