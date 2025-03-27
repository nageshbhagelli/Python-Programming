#10. Write a Python program using the pass statement inside a loop.

# Loop through numbers from 1 to 10
for i in range(1, 11):
    # Skip printing even numbers using pass
    if i % 2 == 0:
        pass
    else:
        print(i)  # Print odd numbers only
