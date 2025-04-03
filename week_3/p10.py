# 10. Write a Python program that demonstrates abstraction using an interface (abstract class) for
# different payment methods like CreditCard, PayPal, and Bitcoin.

from abc import ABC, abstractmethod

# Abstract class (interface)
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass  # Abstract method to be implemented by subclasses

# CreditCard class implementing Payment interface
class CreditCard(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card (Card Number: {self.card_number[-4:]})")

# PayPal class implementing Payment interface
class PayPal(Payment):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid ${amount} using PayPal (Email: {self.email})")

# Bitcoin class implementing Payment interface
class Bitcoin(Payment):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Paid ${amount} using Bitcoin (Wallet: {self.wallet_address[:6]}...{self.wallet_address[-6:]})")

# Example usage
payment1 = CreditCard("1234567812345678")
payment1.pay(100)

payment2 = PayPal("user@example.com")
payment2.pay(200)

payment3 = Bitcoin("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
payment3.pay(500)