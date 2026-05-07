from calc.sum import compute_sum
from calc.diff import compute_diff

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


sum_result = compute_sum(num1, num2)
diff_result = compute_diff(num1, num2)

print("Addition: ", sum_result)
print("Subtraction: ", diff_result)

