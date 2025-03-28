
#3. b. Write a Python program using map() to compute the square of each number in a given list.

#List of numbers
nums = [1,2,3,4,5,6,7,8,9,10]

#Using map() to calculate square of each number
square = list(map(lambda a: a*a, nums))

#Print the result
print("List of squares of numbers:", square)
