import numpy as np

# --------------------------------------------------------------------------------------
# 1. Suppose you have a dataset containing daily temperature readings for a city, and you
# want to identify days with extreme temperature conditions. Find days where the
# temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees
# Celsius (cold day).
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
# Calculate Hot and Cold Day's
hot_days = temperatures[temperatures >= 35]
cold_days = temperatures[temperatures < 5]

print(f"Number of hot days (above 35°C): {hot_days}")
print(f"Number of cold days (below 5°C): {cold_days}")

# --------------------------------------------------------------------------------------
# 2. Suppose you have a dataset containing monthly sales data for a company, and you
# want to split this data into quarterly reports for analysis and reporting purposes.
# Input:
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

monthly_sales_reshaped = monthly_sales.reshape(4, -1)
print("Quarterly Sales Data:")
# print(monthly_sales_reshaped)
for i in range(len(monthly_sales_reshaped)):
    print(f'Quarter {i+1} Sales: \n{monthly_sales_reshaped[i]}')
print()
# --------------------------------------------------------------------------------------
# 3. Suppose you have a dataset containing customer data, and you want to split this data
# into two groups: one group for customers who made a purchase in the last 30 days and
# another group for customers who haven't made a purchase in the last 30 days.
# Input:
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])

for i in range(len(last_purchase_days_ago)):
    if last_purchase_days_ago[i] <= 30:
        print(f'Customer ID {customer_ids[i]} made a purchase in the last 30 days.')
    else:
        print(f'Customer ID {customer_ids[i]} has not made a purchase in the last 30 days.')
print()

# --------------------------------------------------------------------------------------
# 4.Suppose you have two sets of employee data—one containing information about
# full-time employees and another containing information about part-time employees. You
# want to combine this data to create a comprehensive employee dataset for HR analysis.
# Input:
# Employee data for full-time employees
full_time_employees = np.array([
[101, 'John Doe', 'Full-Time', 55000],
[102, 'Jane Smith', 'Full-Time', 60000],
[103, 'Mike Johnson', 'Full-Time', 52000]
])
# Employee data for part-time employees
part_time_employees = np.array([
[201, 'Alice Brown', 'Part-Time', 25000],
[202, 'Bob Wilson', 'Part-Time', 28000],
[203, 'Emily Davis', 'Part-Time', 22000]
])

# Combine the two datasets vertically (stacking rows)
combined_employees = np.vstack((full_time_employees, part_time_employees))
# combined_employees = np.concatenate((full_time_employees, part_time_employees))
print("Combined Employee Data:")
print(combined_employees)

