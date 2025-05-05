# 14. Write a Python program to calculate the percentage increase between two numbers (old and new).

def percentage_increase(old, new):
    return ((new - old) / old) * 100

old_value = 50
new_value = 75

result = percentage_increase(old_value, new_value)
print(f"The percentage increase is: {result}%")
