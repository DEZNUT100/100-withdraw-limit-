from Account import Account

class SavingsAccount(Account):
    def __init__(self, owner, balance=0,):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} applied. ")

print("--- Savings Account ---")
saving = SavingsAccount("Alice", 100)
saving.apply_interest()
saving.apply_interest()
