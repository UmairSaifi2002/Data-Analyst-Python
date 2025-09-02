# Q. A company keeps track of the salaries (in ₹) of its employees in a NumPy array.

import numpy as np

salaries = np.array([45000, 52000, 61000, 35000, 72000, 48000, 55000, 39000, 68000, 50000])
# Tasks:
# Sorting

# Sort the salaries in ascending order.

sorted_salaries = np.sort(salaries)
print("Sorted salaries:", sorted_salaries)

# Searching Insertion Index

# The company plans to hire a new employee with a salary of ₹53000.

# Use np.searchsorted() to find the position where this salary should be inserted in the sorted array to maintain order.

insertion_index = np.searchsorted(sorted_salaries, 53000)
print("Insertion index for ₹53000:", insertion_index)

# Extracting Salaries

# Extract and display all salaries greater than ₹50,000 using np.extract().

high_salaries = np.extract(salaries > 50000, salaries)
print("Salaries greater than ₹50,000:", high_salaries)

# Combine Results

# After inserting the new employee’s salary (₹53000) into the sorted list, display the updated salary list.

updated_salaries = np.insert(sorted_salaries, insertion_index, 53000)
print("Updated salary list:", updated_salaries)















