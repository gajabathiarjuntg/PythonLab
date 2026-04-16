s = input("Enter string: ")
upper = 0
lower = 0

for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")
