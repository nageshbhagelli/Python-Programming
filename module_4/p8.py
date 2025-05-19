#8. Write a Python program that demonstrates the use of the iter() function on a list and
# manually retrieves elements using the next() function until a StopIteration exception is encountered.

#function
def manual_next(lst):
    iterator = iter(lst)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("End of iteration")
            break

# Example usage
my_list = [10, 20, 30, 40]
manual_next(my_list)
