data = {'A': 10, 'B': 50, 'C': 30}

max_key = ""
max_value = 0

for key, value in data.items():
    if value > max_value:
        max_value = value
        max_key = key

print(f"The key with the maximum value is: '{max_key}'")