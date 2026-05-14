print("\nXOR Gate Truth Table")
print("A\tB\tXOR")
for a in [0, 1]:
    for b in [0, 1]:
        output = a ^ b
        print(a, "\t", b, "\t", output)
