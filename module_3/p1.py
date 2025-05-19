class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2022)

# Displaying the car's attributes
my_car.display_info()