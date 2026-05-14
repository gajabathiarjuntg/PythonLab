print("HALF SUBTRACTOR\n")

a = int(input("Enter value of A (0 or 1): "))
b = int(input("Enter value of B (0 or 1): "))

diff = a ^ b
borrow = int(not a) & b

print("\nUser Input Result")
print("A\tB\tDIFF\tBORROW")
print(a, "\t", b, "\t", diff, "\t", borrow)
