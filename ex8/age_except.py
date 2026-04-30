def check_age(age):
    if age < 0:
        raise Exception("Age cannot be a negative number.")
    else:
        print("Age is valid.")


try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except Exception as e:
    print(e)

