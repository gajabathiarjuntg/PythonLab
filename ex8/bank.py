balance = 1000.0  # Starting balance

try:
    deposit = float(input("Enter deposit amount: "))

    if deposit <= 0:
        raise Exception("Deposit amount must be greater than zero!")

    balance = balance + deposit
    print("Updated balance after deposit:", balance)

except Exception as e:
    print("Transaction Failed:", e)
