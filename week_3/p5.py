#5. Write a Python program where different classes (Car, Bike, Truck) have the same method
# start_engine(), demonstrating polymorphism.

class Car:
    def start_engine(self):
        return "Car engine started with a roar!"

class Bike:
    def start_engine(self):
        return "Bike engine started with a vroom!"

class Truck:
    def start_engine(self):
        return "Truck engine started with a heavy rumble!"

# Function demonstrating polymorphism
def start_vehicle_engine(vehicle):
    print(vehicle.start_engine())

# Creating objects of Car, Bike, and Truck
car = Car()
bike = Bike()
truck = Truck()

# Demonstrating polymorphism
start_vehicle_engine(car)
start_vehicle_engine(bike)
start_vehicle_engine(truck)