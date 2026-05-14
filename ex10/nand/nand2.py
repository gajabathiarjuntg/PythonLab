print("\nNAND Gate Truth Table")
print("A\tB\tNAND")
for a in [0, 1]:
    for b in [0, 1]:
        output = int(not(a & b))
        print(a, "\t", b, "\t", output)
