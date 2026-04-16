balance = 5000
correct_pin = 1234


def show_menu():
    global balance  # Use 'global' to update the balance variable outside the function
    print("\n1. Check Balance\n2. Withdraw Money")
    choice = int(input("Choose 1 or 2: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful! New balance:", balance)
        else:
            print("Not enough money!")


# Main Login Loop
for i in range(3):
    pin = int(input("Enter your 4-digit PIN: "))

    if pin == correct_pin:
        print("Login Success!")
        show_menu()
        break  # Exit the loop after success
    else:
        print("Wrong PIN. Try again.")
