# 11. Write a Python function that takes a list of numbers and returns the percentage of numbers greater than the average.

def percentage_greater_than_average(numbers):
    average = sum(numbers) / len(numbers)
    greater_than_avg = sum(1 for num in numbers if num > average)
    return (greater_than_avg / len(numbers)) * 100

numbers = [10, 20, 30, 40, 50, 60, 70]
result = percentage_greater_than_average(numbers)
print(f"Percentage of numbers greater than the average: {result}%")
