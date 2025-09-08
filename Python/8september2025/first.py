import numpy as np
import matplotlib.pyplot as plt

# pip install matplotlib
# marks of two persons
a = np.array([23,16,18,50,22,75,28,39,29,38])
b = np.array([34,39,13,32,68,45,24,33,23,12])
# predict which marks are consistent here
# np.var()
# np.mean()
mean_a = np.mean(a)
mean_b = np.mean(b)
var_a = np.var(a)
var_b = np.var(b)
print("Average of Marks for Person A : ", mean_a)
print("Variance of Person A Marks : ", var_a)

print("Average of Marks for Person B : ", mean_b)
print("Variance of Person B Marks : ", var_b)

if var_a < var_b:
    print("Student A is more Consistent!")
else:
    print("Student B is more Consistent!")

# plt.figure(figsize=(10,8))
# plt.plot(a, label="Student A")
# plt.plot(b, label="Student B")

# plt.axhline(mean_a, color='blue', label="Mean A")
# plt.axhline(mean_b, color='red', label="Mean B")

# plt.title("Comparision of Marks of A and B")
# plt.legend()
# plt.grid(True)
# plt.show()

marks = np.array([45,90,34,98,67,89,86,56,76,88,90,98])
print(np.percentile(marks,25))
print(np.percentile(marks,80))
print(np.percentile(marks,57))
print(np.percentile(marks,[20,45,70,90]))

salaries = np.array([25000, 28000, 30000, 35000, 40000,42000, 50000, 52000,60000, 72000])

print(np.percentile(salaries, 25))
print(np.percentile(salaries, 50))
print(np.percentile(salaries, 75))

# 
print(f'Interpretation of 25% of employee earn : ₹{np.percentile(salaries, 25)}')
print(f'Interpretation of 50% of employee earn : ₹{np.percentile(salaries, 50)}')
print(f'Interpretation of 75% of employee earn : ₹{np.percentile(salaries, 75)}')
print(f'Interpretation of middle of 50% and 75% employee earn : ₹{np.percentile(salaries, 75)} - ₹{np.percentile(salaries, 75)}')

plt.boxplot(salaries, vert=False)
plt.title('Salary Distribution of Employee')
plt.xlabel('Salary (₹)')
plt.show()






