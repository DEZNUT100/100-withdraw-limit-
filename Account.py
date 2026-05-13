class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"deposit {amount} from {self.name}")
        else:
            print("Invalid deposit amount ")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"withdraw {amount} from {self.name}")
        else:
            print("Invalid withdrawal amount ")

    def apply_interest(self):
        interest = self.get_balance() * self.__balance / 100


    def get_balance(self):
        """Public getter for the private __balance"""
        return self.__balance

print("--- Savings Account ---")
savings = SavingsAccount("Alice", 1000)