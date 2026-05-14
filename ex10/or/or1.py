print("DIGITAL LOGIC GATES\n")
print("A\tB\tOR")

for a in [0, 1]:
    for b in [0, 1]:
        output = a | b
        print(a, "\t", b, "\t", output)
