class BankAccount:
    def __init__(self, owner : str, balance: float = 0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount: float):
        self.balance += amount
        
    def withdraw(self, amount: float):
        self.balance -= amount
        
    def display_balance(self):
        print(f"The current balance is {self.balance} for owner {self.owner}.")