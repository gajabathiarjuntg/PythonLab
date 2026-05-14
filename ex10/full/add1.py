print("FULL ADDER\n")

a = int(input("Enter value of A (0 or 1): "))
b = int(input("Enter value of B (0 or 1): "))
cin = int(input("Enter value of Cin (0 or 1): "))

sum = a ^ b ^ cin
carry = (a & b) | (b & cin) | (a & cin)

print("\nUser Input Result")
print("A\tB\tCin\tSUM\tCARRY")
print(a, "\t", b, "\t", cin, "\t", sum, "\t", carry)
