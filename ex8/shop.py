try:
    price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity: "))

    if price < 0 or quantity < 0:
        raise ValueError("Price or quantity cannot be negative!")

    total_bill = price * quantity
    print("Total bill amount:", total_bill)

except ValueError as e:
    print("Error:", e)
