class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        """Read-only access to account balance"""
        return self.__balance

    @property
    def interest(self):
        """Computed property (read-only)"""
        return self.__balance * 0.05

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            

acc = BankAccount("Ali", 1000)

print(acc.balance)
print(acc.interest)

acc.deposit(500)
print(acc.balance)

acc.withdraw(300)
print(acc.balance)