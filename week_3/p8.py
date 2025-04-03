# 8. Create a class Laptop with private attributes for price and model, and public methods to
# access and modify them safely.

class Laptop:
    def __init__(self, model, price):
        self.__model = model  # Private attribute
        self.__price = price  # Private attribute

    # Getter method for model
    def get_model(self):
        return self.__model

    # Setter method for model
    def set_model(self, model):
        if isinstance(model, str) and model.strip():
            self.__model = model
        else:
            print("Invalid model name.")

    # Getter method for price
    def get_price(self):
        return self.__price

    # Setter method for price
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be a positive value.")

# Example usage
laptop = Laptop("Dell XPS 15", 1500)

# Accessing private attributes using getters
print("Model:", laptop.get_model())
print("Price: $", laptop.get_price())

# Modifying private attributes using setters
laptop.set_model("MacBook Pro")
laptop.set_price(2000)

print("Updated Model:", laptop.get_model())
print("Updated Price: $", laptop.get_price())

# Attempting direct access to private attributes (will cause an error)
# print(laptop.__model)  # Uncommenting this line will raise an AttribteError