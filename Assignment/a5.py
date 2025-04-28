#5.Write a Python function to calculate the percentage for a given marks list and total marks.
#Hint: percentage = (sum of marks / total marks) * 100

def calculate_percentage(marks_list, total_marks):
    total_scored = sum(marks_list)
    percentage = (total_scored / total_marks) * 100
    return percentage

marks = [90, 95, 70, 85, 80]  
total = 500  # Total marks possible

result = calculate_percentage(marks, total)
print(f"Percentage of the student is {result}%")
