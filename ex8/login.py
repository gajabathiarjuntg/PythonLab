try:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username or not password:
        raise Exception("Username or password cannot be empty!")

    print("Login Successful!")

except Exception as e:
    print("Login Failed:", e)

