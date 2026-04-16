s = input("Enter a string: ")
result = ""
# remove spaces
for i in s:
    if not i.isspace():
        result += i


print(result)



