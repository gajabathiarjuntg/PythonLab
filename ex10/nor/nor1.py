print("NOR Gate Truth Table\n")
print("A\tB\tNOR")
for a in [0, 1]:
    for b in [0, 1]:
        if a == 0 and b == 0:
            output = 1
        else:
            output = 0
        print(a, "\t", b, "\t", output)
