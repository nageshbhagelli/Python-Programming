# 8. Write a Python program that prints numbers from 1 to 50, but skips multiples of 5 using the continue statement.

# Loop through numbers from 1 to 50
for i in range(1, 51):
    # If the number is a multiple of 5, skip it
    if i % 5 == 0:
        continue
    print(i)
