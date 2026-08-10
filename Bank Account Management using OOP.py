class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

account = BankAccount("Kavin", 5000)
account.deposit(2000)
account.withdraw(1000)
account.display()