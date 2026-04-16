def show_salary(basic):
    da = basic * 0.1
    hra = basic * 0.2
    gross = basic + da + hra

    print(f"\nBasic Salary: {basic}")
    print(f"DA (10%): {da}")
    print(f"HRA (20%): {hra}")
    print(f"Total Gross Salary: {gross}")



amount = float(input("Enter Basic Salary: "))
show_salary(amount)
