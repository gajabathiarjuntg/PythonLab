num = []
for i in range(5):
    value = int(input("Enter a number: "))
    num.append(value)


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(num[start:end])
