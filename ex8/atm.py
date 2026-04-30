SECRET_PIN = "1234"

try:
    user_pin = input("Enter your 4-digit PIN: ")

    if user_pin != SECRET_PIN:
        raise Exception("Incorrect PIN! Access Denied.")


    balance = float(input("Enter account balance: "))
    withdrawal = float(input("Enter withdrawal amount: "))


    if withdrawal < 0:
        raise ValueError("Withdrawal amount cannot be negative.")
    if withdrawal > balance:
        raise Exception("Insufficient balance!")


    remaining_balance = balance - withdrawal
    print("Withdrawal successful! Remaining balance:", remaining_balance)

except ValueError as ve:
    print("Input Error!",ve)
except Exception as e:
    print("Error!",e)
