print("\nFull Adder Truth Table")
print("A\tB\tCin\tSUM\tCARRY")

for a in [0, 1]:
    for b in [0, 1]:
        for cin in [0, 1]:

            sum = a ^ b ^ cin
            carry = (a & b) | (b & cin) | (a & cin)

            print(a, "\t", b, "\t", cin, "\t", sum, "\t", carry)
