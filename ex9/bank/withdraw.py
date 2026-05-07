def make_withdrawal(balance, amount):
    if amount <= 0:
        print("Error: Withdrawal amount must be positive.")
        return balance
    if amount > balance:
        print("Error: Insufficient funds.")
        return balance
    return balance - amount
