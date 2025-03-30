class BankAccount:
    def __init__(self , owner_name , balance = 0.0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self , amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance} ")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print ("insufficient funds")
        
my_account = BankAccount("John Doe")
my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(500)