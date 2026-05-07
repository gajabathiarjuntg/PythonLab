import simp1

principal = float(input("Enter principal amount (P): "))
rate = float(input("Enter annual interest rate (R%): "))
time = float(input("Enter time period in years (T): "))


result = simp1.calculate_si(principal, rate, time)

print("The calculated Simple Interest is:", round(result, 2))


