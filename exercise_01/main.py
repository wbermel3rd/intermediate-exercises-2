from BankAccount import BankAccount

account_name = "Johnny"
account_balance = 50.0

account = BankAccount(account_name, account_balance)

account.deposit(25.0)
account.withdraw(5.0)

print(account.getBalance())
