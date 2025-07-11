# Q1 Calculate the multiplication and sum of two numbers

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
multiplication_result = n1 * n2
sum_result = n1 + n2
print(f'The multiplication of {n1} and {n2} is {multiplication_result}')
print(f'The sum of {n1} and {n2} is {sum_result}')

# Q2 Declare two variables and print that which variable is largest using ternary operators

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
largest = a if a > b else b
print(f'The largest number between {a} and {b} is {largest}')

# Q3 Python program to convert the temperature in degree centigrade to Fahrenheit

temperature_c = float(input("Enter temperature in Celsius: "))
temperature_f = (temperature_c * 9/5) + 32
print(f'Temperature in Fahrenheit: {temperature_f:.2f}')

# Q4 Python program to find the area of a triangle whose sides are given

height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))
area = 0.5 * base * height
print(f'The area of the triangle is: {area:.2f}')

