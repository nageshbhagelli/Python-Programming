# 7. Write a Python program demonstrating encapsulation using a class BankAccount with private
# attributes __balance and methods to deposit and withdraw money.

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance  # Accessor method to get balance

# Example usage
account = BankAccount(100)
print("Current Balance:", account.get_balance())
account.deposit(50)
account.withdraw(30)
print("Current Balance:", account.get_balance())

# Attempting to access private attribute directly (will cause an error)
# print(account.__balance)  # Uncommenting this line will raise an AttributeError