print("HALF ADDER\n")

a = int(input("Enter value of A (0 or 1): "))
b = int(input("Enter value of B (0 or 1): "))

sum = a ^ b
carry = a & b

print("\nUser Input Result")
print("A\tB\tSUM\tCARRY")
print(a, "\t", b, "\t", sum, "\t", carry)
