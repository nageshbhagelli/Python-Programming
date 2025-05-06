# 15. Write a Python function that finds the second highest and second lowest number in a list.

def second_highest_lowest(numbers):
    unique_numbers = sorted(set(numbers))
    if len(unique_numbers) < 2:
        return None, None
    return unique_numbers[-2], unique_numbers[1]

numbers = [10, 20, 20, 40, 30]

second_highest, second_lowest = second_highest_lowest(numbers)
print(f"Second highest: {second_highest}\nSecond lowest: {second_lowest}")
