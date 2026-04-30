try:
    a = input("Enter a number: ")
    number = int(a)
    print("You Have Entered a Number : ",number)

except ValueError:
    print("The Entered input is not a Whole Number")
