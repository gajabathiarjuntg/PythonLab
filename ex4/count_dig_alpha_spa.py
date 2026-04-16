s = input("Enter string: ")
alphabets = 0  
digits = 0
spaces = 0
others = 0

for char in s:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1

print(f"Alphabets: {alphabets}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Others: {others}")
