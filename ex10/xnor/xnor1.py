print("XNOR Gate Truth Table\n")
print("A\tB\tXNOR")
for a in [0, 1]:
    for b in [0, 1]:
        if a == b:
            output = 1
        else:
            output = 0
        print(a, "\t", b, "\t", output)
