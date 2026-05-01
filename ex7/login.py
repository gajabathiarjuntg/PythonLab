login_db = {
    'admin': 'adminPass!',
    'arjun': 'ece2026'
}

input_username = input("Please enter your username: ")
input_password = input("Please enter your password: ")


if input_username in login_db and login_db[input_username] == input_password:
    print("Login successful! Welcome.")
else:
    print("Invalid username or password. Please try again.")
