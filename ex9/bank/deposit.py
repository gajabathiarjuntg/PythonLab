def make_deposit(balance, amount):
    if amount <= 0:
        print("Error: Deposit amount must be positive.")
        return balance
    return balance + amount
