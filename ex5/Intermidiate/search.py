numbers = [10, 20, 30, 40, 50]
search_value = 30
found = False

for n in numbers:
    if n == search_value:
        found = True

if found:
    print(search_value, "is in the list!")
else:
    print(search_value, "was not found.")
