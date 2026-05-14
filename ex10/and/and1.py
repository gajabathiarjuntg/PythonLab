print("AND Gate Truth Table\n")
print("A\tB\tAND")

for a in [0, 1]:
    for b in [0, 1]:
        if a == 1 and b == 1:
            output = 1
        else:
            output = 0
        print(a, "\t", b, "\t", output)
