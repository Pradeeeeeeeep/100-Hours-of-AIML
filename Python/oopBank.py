class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.") 
    def display_balance(self):
        print(f"Account owner: {self.owner}, Balance: {self.balance}")
    
BankAccount1 = BankAccount("Alice", 1000)
BankAccount1.display_balance()
BankAccount1.deposit(500)
BankAccount1.withdraw(200) 
BankAccount1.display_balance()