print("\nFull Subtractor Truth Table")
print("A\tB\tBin\tDIFF\tBORROW")

for a in [0, 1]:
    for b in [0, 1]:
        for bin in [0, 1]:

            difference = a ^ b ^ bin
            borrow = int(((not a) & b) | ((not a) & bin) | (b & bin))

            print(a, "\t", b, "\t", bin, "\t", difference, "\t", borrow)
