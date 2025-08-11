# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# first_num = int(input('Enter a first number : '))
# second_num = int(input('Enter a second number : '))

# try:
#     divide = first_num/second_num
#     print(divide)
# except ZeroDivisionError:
#     print('Please donot give 0 as an input')


# -----------------------------------------------------------------------------------

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# try:
#     num = int(input('Enter an integer number : '))
#     print('You Enter an Integer Value')
# except ValueError:
#     print('Enter a Valid integer')

# ------------------------------------------------------------------------------------

# 3. 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

# file_name = input('Enter a File name : ')

# try:
#     with open(file_name, 'r') as file:
#         data = file.read()
#     print(data)
# except FileNotFoundError:
#     print('File is not Available')

# ------------------------------------------------------------------------------------

# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical

try:
    number_one = input('Enter first number : ')
    number_second = input('Enter second number : ')
    if not (number_one.replace('.','').isdigit() and number_second.replace('.','').isdigit()):
        raise TypeError("Both inputs must be numerical values.")
except TypeError as e:
    print(f'TypeError: {e}')




