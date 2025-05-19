#3. Write a Python program where Dog and Cat classes inherit from a base class Animal, and implement a method speak().

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects of Dog and Cat
dog = Dog()
cat = Cat()

# Displaying their sounds
print("Dog says:", dog.speak())
print("Cat says:", cat.speak())