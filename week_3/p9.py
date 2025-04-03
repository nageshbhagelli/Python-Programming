# 9. Create an abstract class Shape with an abstract method calculate_area(), then implement Circle and Square classes.

from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass  # Abstract method to be implemented by subclasses

# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

# Square class inheriting from Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

# Example usage
circle = Circle(5)
square = Square(4)

print(f"Circle Area: {circle.calculate_area():.2f}")
print(f"Square Area: {square.calculate_area():.2f}")