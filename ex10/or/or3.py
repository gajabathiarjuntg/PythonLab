print("OR Gate Truth Table\n")
print("A\tB\tOR")

for a in [0, 1]:
    for b in [0, 1]:
        if a == 0 and b == 0:
            output = 0
        else:
            output = 1
        print(a, "\t", b, "\t", output)
