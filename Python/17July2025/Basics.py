# Today we will learn about the functions
# there are two type of functions 
# 1. Built-in functions
# 2. User-defined functions

#wap to print the table of n number

n = int(input())
def table(n):
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')
table(n)

# WAP to detect whether a year is a leap year or not
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# WAP to Find the largest among three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 > num2:
    if num1 > num3:
        print(f'{num1} is the largest number')
    else:
        print(f'{num3} is the Largest number')
elif num2 > num3:
    print(f'{num2} is the Largest number')
else:
    print(f'{num3} is the Largest number')
