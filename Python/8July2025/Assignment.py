basic_salary = float(input("Enter the basic salary: "))

da = basic_salary * 0.05 # 5% of basic
ta = basic_salary * 0.06 # 6% of basic
hra = basic_salary * 0.12 # 12% of basic
pf = basic_salary * 0.15 # 15% of basic

total_salary = basic_salary + da + ta + hra + pf
net_salary = total_salary - pf

print("\n========== PAYSLIP ==========")
print(f"Basic Salary: {basic_salary:.2f}")
print(f"DA (5%): {da:.2f}")
print(f"TA (6%): {ta:.2f}")
print(f"HRA (12%): {hra:.2f}")
print(f"PF (15%): {pf:.2f}")
print("-----------------------------")
print(f"Total Salary: {total_salary:.2f}")
print(f"Net Salary: {net_salary:.2f}")
print("=============================")
