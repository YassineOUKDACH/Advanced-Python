from abc import ABC, abstractmethod

# 1. Strategy Interface (Abstract Base Class)
# This defines the common interface for all supported algorithms.
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# 2. Concrete Strategies
# These classes implement different variations of the algorithm.
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card."

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal."

class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin."

# 3. The Context
# This is the class that requires a specific behavior but doesn't 
# care which strategy is being used.
class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        # We "inject" the strategy here (Dependency Injection)
        self._strategy = strategy 

    def set_strategy(self, strategy: PaymentStrategy):
        # Allows changing the strategy dynamically at runtime
        self._strategy = strategy

    def checkout(self, amount):
        # Delegate the work to the strategy object
        return self._strategy.pay(amount)

# --- Usage ---

# We choose the strategy at the time of purchase
cart = ShoppingCart(CreditCardPayment())
print(cart.checkout(100))  # Output: Paid $100 using Credit Card.

# We can easily swap the strategy on the same object
cart.set_strategy(PayPalPayment())
print(cart.checkout(250))  # Output: Paid $250 using PayPal.

# Or initialize a new cart with a different method
crypto_cart = ShoppingCart(CryptoPayment())
print(crypto_cart.checkout(500)) # Output: Paid $500 using Bitcoin.
