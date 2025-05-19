#2. Write a Python class Student with attributes name and marks, and a method to display the student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Creating an object of the Student class
student1 = Student("Alice", 90)

# Displaying the student details
student1.display_details()