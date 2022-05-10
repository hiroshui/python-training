"""
Type hinting exercise with classes
"""


def main():
    """Simple program for illustrative purposes"""
    name : str = ask_name()
    my_account : BankAccount = BankAccount(name)
    my_account.deposit(float(10_000))
    my_account.withdraw(float(5_000))
    my_account.print_balance()


def ask_name() -> str:
    """Return user input"""
    name : str = input("What is your name? ")
    return str(name)


class BankAccount:
    """Simple class for bank accounts"""

    def __init__(self, owner : str) -> None:
        """Initialise account (balance 0)"""
        self.owner : str = owner
        self.balance : float = 0

    def deposit(self, amount : float):
        """Add money to the account"""
#        if not isinstance(amount, float):
#            raise ValueError("Wrong format - we need float!")
        self.balance += amount

    def withdraw(self, amount : float):
        """Withdraw money from the account"""
#        if not isinstance(amount, float):
#            raise ValueError("Wrong format - we need float!")
        self.balance -= amount

    def print_balance(self):
        """Prints full sentence"""
        print(f"Your account has €{self.balance:,}")

def my_sum(numbers : int) -> int:
    """Return mysum using some kind of loop"""
    total : int = 0
    for n in numbers:
        total += n
    return total

if __name__ == "__main__":
    main()
    print(my_sum(50))