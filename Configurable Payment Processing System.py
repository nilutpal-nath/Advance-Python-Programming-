# Configurable Payment Processing System Using Strategy Pattern

from abc import ABC, abstractmethod

# 1. Define a PaymentStrategy interface with a method pay
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# 2. Implement various payment strategies inheriting from PaymentStrategy
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount):
        return f"Paid ${amount:.2f} using Credit Card ending in {self.card_number[-4:]} (Holder: {self.card_holder})"


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid ${amount:.2f} using PayPal account: {self.email}"


class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        return f"Paid ${amount:.2f} using Bitcoin Wallet: {self.wallet_address[:6]}..."


# 3. Create a PaymentProcessor class that uses a PaymentStrategy to process payments
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        # 4. Allow the PaymentProcessor to switch strategies at runtime
        self.strategy = strategy
        print("Payment strategy updated successfully.")

    def process_payment(self, amount):
        return self.strategy.pay(amount)


# Main Program
if __name__ == "__main__":
    # Initialize with Credit Card
    processor = PaymentProcessor(CreditCardPayment("1234567890123456", "John Doe"))
    print(processor.process_payment(150.75))

    # Switch strategy at runtime to PayPal
    processor.set_strategy(PayPalPayment("john.doe@example.com"))
    print(processor.process_payment(49.99))

    # Switch strategy at runtime to Bitcoin
    processor.set_strategy(BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
    print(processor.process_payment(250.00))