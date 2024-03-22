class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -+ amount

    @property
    def is_overdrawn(self):
        return self._balance < 0
    
account = BankAccount("987654", 1000)
print(f"Initial Balance: {account.balance}")

account.deposit(500)
print(f"Balance after deposit: {account.balance}")

account.withdraw(250)
print(f"Balance after withdrawl: {account.balance}")