#4. a. Write a Python program that manually iterates over a list using an iterator object.

def manual_iteration(lst):
    iterator = iter(lst)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

# Example usage
my_list = [1, 2, 3, 4, 5]
manual_iteration(my_list)
