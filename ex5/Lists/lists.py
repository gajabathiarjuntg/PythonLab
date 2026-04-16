numbers = []
for i in range(5):
    value = int(input("Enter a number: "))
    numbers.append(value)

print("DISPLAYING THE LIST ELEMENTS")
print(numbers)

print("SUM OF LIST ELEMENTS")
print(sum(numbers))

print("SMALLEST LIST ELEMENT")
print(min(numbers))

print("SEARCHING AN ELEMENT IN THE LIST")
find = int(input("Enter a number to search: "))
if find in numbers:
    print(find,"Found")
else:
    print("Not found")

print("REVERSING THE LIST")
print("The original list is : ",numbers)
numbers.reverse()
print("After reversing : ",numbers)

print("COUNTING ODD NUMBERS")
odd_count = 0
for n in numbers:
    if n % 2 != 0:
        odd_count = odd_count + 1
print(odd_count)
