print("\nXNOR Gate Truth Table")
print("A\tB\tXNOR")
for a in [0, 1]:
    for b in [0, 1]:
        output = int(not (a ^ b))
        print(a, "\t", b, "\t", output)
