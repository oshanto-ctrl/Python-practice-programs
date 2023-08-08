# Class that represent bank account
class BankAccount:
    
    def set_details(self, name, balance=0):
        self.name = name 
        self.balance = balance

    def display(self):
        print(f"Account Name {self.name}\nAccount Balance {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


# Instances
b = BankAccount()
b.set_details('Lamichane', 100)
b.display()
b.deposit(5000)
b.display()
b.withdraw(2000)
b.display()
