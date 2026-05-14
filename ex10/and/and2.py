print("AND Gate\n")
a = int(input("Enter value of A (0 or 1): "))
b = int(input("Enter value of B (0 or 1): "))

output = a & b

print("\nUser Input Result")
print("A\tB\tAND")
print(a, "\t", b, "\t", output)

print("\nAND Gate Truth Table")
print("A\tB\tAND")
for a in [0, 1]:
    for b in [0, 1]:
        output = a & b
        print(a, "\t", b, "\t", output)
