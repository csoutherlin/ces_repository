class BankAccount:
    def __init__(self, name, balance):
        self.account_holder = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error, insufficient funds")
        else:
            self.balance -= amount
        return amount

chris_account = BankAccount("Chris", 1000)

chris_account.deposit(2000)

print(chris_account.balance)

chris_account.withdraw(1000)

print(chris_account.balance)