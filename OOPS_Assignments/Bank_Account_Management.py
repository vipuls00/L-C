from abc import ABC, abstractmethod

class BankAccountBase(ABC):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit_funds(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}, New Balance: {self.balance}")
        else:
            print("Invalid deposit amount.")
    
    @abstractmethod
    def withdraw_funds(self, amount):
        pass

class SavingsAccountWithWithdrawalLimit(BankAccountBase):
    def __init__(self, initial_balance=0):
        super().__init__(initial_balance)
        self.withdrawal_limit = 5000
    
    def withdraw_funds(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Withdrawal limit exceeded! Max: {self.withdrawal_limit}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")

class CurrentAccountWithFullBalanceAccess(BankAccountBase):
    def withdraw_funds(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")

savings_account = SavingsAccountWithWithdrawalLimit(10000)
savings_account.deposit_funds(2000)
savings_account.withdraw_funds(6000)
savings_account.withdraw_funds(4000)

current_account = CurrentAccountWithFullBalanceAccess(15000)
current_account.withdraw_funds(20000)
current_account.withdraw_funds(5000)
