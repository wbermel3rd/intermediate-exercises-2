class BankAccount: 

    def __init__(self, account_name, starting_balance):
        self.accountName = account_name
        self.accountBal = starting_balance

    def deposit(self, amount):
        self.accountBal += amount

    def withdraw(self, amount):
        if(self.accountBal >= amount):
            self.accountBal -= amount
        else:
            print("Insufficient Funds")
    
    def getBalance(self):
        return (self.accountName + " has a balance of $" + str(self.accountBal))
