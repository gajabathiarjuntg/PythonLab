# Import individual modules from your custom bank package
from bank.deposit import make_deposit
from bank.withdraw import make_withdrawal

# Initialize a starting account balance
account_balance = 1000.0
print("Initial Account Balance: $", account_balance)

# Perform a deposit operation
dep_amt = float(input("\nEnter amount to deposit: "))
account_balance = make_deposit(account_balance, dep_amt)
print("Updated Balance: $", account_balance)

# Perform a withdrawal operation
with_amt = float(input("\nEnter amount to withdraw: "))
account_balance = make_withdrawal(account_balance, with_amt)
print("Final Balance: $", account_balance)
