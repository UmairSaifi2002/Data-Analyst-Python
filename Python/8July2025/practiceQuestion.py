# Q1. wap to calculate the bonus according to salary.
# input salary from user in float format and calculate its bonus
# according to this percentage :- 10% of salary = 0.10*salary

salary = float(input("Enter your salary: "))
bonus = 0.10 * salary
print(f'The bonus for a salary of {salary} is: {bonus:.2f}')
print(f'The total amount after adding bonus is: {salary + bonus:.2f}')

# Q2 : wap to input marks of english, hindi, maths, science and
# sst from user and print student's total marks and percentage

english_marks = float(input("Enter marks in English: "))
hindi_marks = float(input("Enter marks in Hindi: "))
maths_marks = float(input("Enter marks in Maths: "))
science_marks = float(input("Enter marks in Science: "))
sst_marks = float(input("Enter marks in SST: "))
total_marks = english_marks + hindi_marks + maths_marks + science_marks + sst_marks 
max_marks = 500
percentage = (total_marks / max_marks) * 100
print(f'Total marks obtained: {total_marks}')
print(f'Percentage: {percentage:.2f}%')

