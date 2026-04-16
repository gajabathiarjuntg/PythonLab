numbers = [15, 42, 7, 89, 23]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("The largest number is:", largest)
