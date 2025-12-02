# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to the account balance."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """
        Deduct amount if sufficient funds exist.
        Returns True if withdrawal succeeds, otherwise False.
        """
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current account balance: ${self.account_balance:.2f}")
