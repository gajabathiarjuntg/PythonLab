print("NAND Gate Truth Table\n")
print("A\tB\tNAND")
for a in [0, 1]:
    for b in [0, 1]:
        if a == 1 and b == 1:
            output = 0
        else:
            output = 1
        print(a, "\t", b, "\t", output)
