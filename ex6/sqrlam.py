num = []
for i in range(5):
    value = int(input("Enter a number: "))
    num.append(value)

square = list(map(lambda x:x**2, num))
print(square)
