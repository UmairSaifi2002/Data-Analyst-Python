# 1. Python program to print all the even numbers within the given range.

# start_num = int(input('Enter the start number: '))
# end_num = int(input('Enter the end number: '))

# for i in range(start_num, end_num + 1):
#     if i % 2 == 0:
#         print(i, end=' ')

# -----------------------------------------------------------------------------------------------------------------------------------
# 2. Python program to calculate the sum of all numbers from 1 to a given number.

# number = int(input('Enter a number: '))
# sum_of_numbers = 0

# for i in range(1, number + 1):
#     sum_of_numbers += i
# print(f'\nSum of numbers from 1 to {number} is: {sum_of_numbers}')

# -----------------------------------------------------------------------------------------------------------------------------------
# 3.  Python program to calculate the sum of all the odd numbers within the given range.

# start_num = int(input('Enter the start number: '))
# end_num = int(input('Enter the end number: '))
# sum_of_odd_numbers = 0

# for i in range(start_num, end_num + 1):
#     if i % 2 != 0:
#         sum_of_odd_numbers += i
# print(f'Sum of odd numbers from {start_num} to {end_num} is: {sum_of_odd_numbers}')

# -----------------------------------------------------------------------------------------------------------------------------------
# 4. Python program to print a multiplication table of a given number

# number = int(input('Enter a number to print its multiplication table: '))

# for i in range(1, 11):
#     print(f'{number} X {i} = {number * i}')

# -----------------------------------------------------------------------------------------------------------------------------------
# 5. Python program to display numbers from a list using a for loop.
# numbers = [10, 20 ,30, 40, 50]

# for i in numbers:
#     print(i, end=', ')

# -----------------------------------------------------------------------------------------------------------------------------------
# 6. Python program to count the total number of digits in a number.
# number = int(input('\nEnter a number to count its digits: '))

# count = 0

# while number > 0:
#     number = int(number / 10)
#     count = count + 1

# print(f'Total number of digits in the given number is: {count}')

# -----------------------------------------------------------------------------------------------------------------------------------
# 7. Python program to check if the given string is a palindrome.

# string = input('Enter a string to check if it is a palindrome: ')
# is_palindrome = False
# reversed_string = string[::-1]

# if string == reversed_string:
#     is_palindrome = True

# print(f'Is the string "{string}" a palindrome? {is_palindrome}')

# -----------------------------------------------------------------------------------------------------------------------------------
# 8. Python program that accepts a word from the user and reverses it.

# word = input('Enter a word to reverse it: ')

# reversed_word = word[::-1]

# print(f'Reversed word: {reversed_word}')

# -----------------------------------------------------------------------------------------------------------------------------------
# 9. Python program to check if a given number is an Armstrong number

# getting an input from the user
# number = int(input('Enter a number to check if it is an Armstrong number: '))

# # decalaring a variable for calculation
# num = number
# digits = 0

# # finding the digits of the number
# while num > 0:
#     num = int(num / 10)
#     digits += 1

# # printing the number of digits
# print(f'The number of digits in {number} is: {digits}')

# # declaring a variable to store a Armstrong Number
# armstrong_number = 0

# # re -declaring the variable num to the original number
# num = number

# # calculating the Armstrong number
# while num > 0:
#     digit = num % 10
#     armstrong_number += digit ** digits
#     num = int(num / 10)

# # printing the Armstrong number
# print(f'The Armstrong number is: {armstrong_number}')

# # convert the armstrong number to integer for comparison
# armstrong_number = int(armstrong_number)

# # checking if the number is an Armstrong number
# if armstrong_number == number:
#     print('The number is an Armstrong number. ')

# else:
#     print('The number is not an Armstrong Number.')


# -----------------------------------------------------------------------------------------------------------------------------------
# 10. Python program to count the number of even and odd numbers from a series of numbers.

# number_series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 

# even_count = 0
# odd_count = 0

# for i in number_series:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1 

# print(f'Total even numbers: {even_count}')
# print(f'Total odd numbers: {odd_count}')

# -----------------------------------------------------------------------------------------------------------------------------------
# 11. Python program to display all numbers within a range except the prime numbers.

# start_num = int(input('Enter the start number: '))
# end_num = int(input('Enter the end number: '))

# for num in range(start_num, end_num + 1):
#     if num < 2:
#         continue  # Skip numbers less than 2
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if not is_prime:
#         print(num, end=' ')

# -----------------------------------------------------------------------------------------------------------------------------------
# 12. Python program to get the Fibonacci series between 0 to 50.

# first = 0
# second = 1
# print("Fibonacci series between 0 to 50:")
# while first <= 50:
#     print(first, end=' ')
#     next_number = first + second
#     first = second
#     second = next_number

# -----------------------------------------------------------------------------------------------------------------------------------
# 13. Python program to find the factorial of a given number.

# number = int(input('Enter a number to find its factorial: '))

# factorial = 1

# while number > 1:
#     factorial = factorial * number
#     number = number - 1

# print(f'The factorial is: {factorial}')

# -----------------------------------------------------------------------------------------------------------------------------------
# 14. Python program that accepts a string and calculates the number of digits and letters.

# string = int(input('Enter a string to count digits and letters: '))

# alphabet_count = 0
# digit_count = 0

# for i in string:
#     if i.isalpha():
#         alphabet_count += 1
#     elif i.isdigit():
#         digit_count += 1

# print(f'The number of letters in the string is: {alphabet_count}')
# print(f'The number of digits in the string is: {digit_count}')

# -----------------------------------------------------------------------------------------------------------------------------------
# 15. Write a Python program that iterates the integers from 1 to 25

# for i in range(1, 26):
#     print(i, end=' ')

# ------------------------------------------------------------------------------------------------------------------------------------
# 16. Python program to check the validity of password input by users.

# password = input('Enter a password: ')

# is_alpha = False
# is_digit = False
# is_special_char = False

# for char in password:
#     if char.isalpha():
#         is_alpha = True
#     elif char.isdigit():
#         is_digit = True
#     elif char in '!@#$%^&*()_+':
#         is_special_char = True
    
# if len(password) >= 8 and is_alpha and is_digit and is_special_char:
#     print('Password is valid.')
# else:
#     print('Password is invalid. It must be at least 8 characters long, contain letters, digits, and special characters.')

# -----------------------------------------------------------------------------------------------------------------------------------
# 17. Python program to convert the month name to a number of days.

month_name = input('Enter the month name: ').strip().lower()

month_days = {
    'january': 31,
    'february': 28,  # 29 for leap years, but not handled here
    'march': 31,
    'april': 30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31
}

if month_name in month_days:
    print(f'The number of days in {month_name.capitalize()} is: {month_days[month_name]}')
else:
    print('Invalid month name. Please enter a valid month (e.g., January, February, etc.).')





