print("\nHalf Adder Truth Table")
print("A\tB\tSUM\tCARRY")

for a in [0, 1]:
    for b in [0, 1]:

        sum = a ^ b
        carry = a & b

        print(a, "\t", b, "\t", sum, "\t", carry)
