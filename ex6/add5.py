num = []
for i in range(5):
    value = int(input("Enter a number: "))
    num.append(value)

add5 = [value+5 for value in num]
print(add5)

