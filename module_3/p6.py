# 6. Write a Python program that uses operator overloading to add two Vector objects using the + operator.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Operand must be an instance of Vector")
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
# Example usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Uses operator overloading
print(v3)  # Output: Vector(6, 8)