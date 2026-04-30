try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a / b
    print(c)

except Exception as e:
    print("The Exception Message is ",e)
