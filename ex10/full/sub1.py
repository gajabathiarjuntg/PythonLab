print("FULL SUBTRACTOR\n")

a = int(input("Enter value of A (0 or 1): "))
b = int(input("Enter value of B (0 or 1): "))
bin = int(input("Enter value of Bin (0 or 1): "))

difference = a ^ b ^ bin
borrow = int(((not a) & b) | ((not a) & bin) | (b & bin))

print("\nUser Input Result")
print("A\tB\tBin\tDIFF\tBORROW")
print(a, "\t", b, "\t", bin, "\t", difference, "\t", borrow)
