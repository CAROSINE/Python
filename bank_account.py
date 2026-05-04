# Bank Account system with deposit & withdraw

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print("Current Balance:", self.balance)


# object create
acc = BankAccount("Mahin", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()
