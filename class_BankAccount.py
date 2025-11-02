class BankAccount:
    balance = 0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    
    def withdraw(self, amount):        
        if self.balance > 0:
            self.balance -= amount
            if self.balance <= 0:
                return "you finish your mony"
            return self.balance
        else:
            print("you don't have enough mony")
            return self.balance    
    
    def get_balance(self):
        return self.balance


    
account = BankAccount(1234567,354.59)
print(account.account_number)
print(account.balance)
print(account.deposit(150.41))    
print(account.withdraw(154.59))
print(account.withdraw(150))
print(account.get_balance())
