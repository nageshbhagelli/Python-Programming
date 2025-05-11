# 19. Write a Python function to calculate the cumulative sum of a list of numbers (for percentage calculation).

def cumulative_sum(numbers):
    result = []
    total = 0
    for num in numbers:
        total += num
        result.append(total)
    return result

numbers = [10, 20, 30, 40]
result = cumulative_sum(numbers)
print(f"The cumulative sum is: {result}")
