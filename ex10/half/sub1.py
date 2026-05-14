print("\nHalf Subtractor Truth Table")
print("A\tB\tDIFF\tBORROW")

for a in [0, 1]:
    for b in [0, 1]:

        diff = a ^ b
        borrow = int(not a) & b

        print(a, "\t", b, "\t", diff, "\t", borrow)
