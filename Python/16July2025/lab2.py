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

# WAP to check if a number is +ve or -ve or 0
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print("The number is zero.")

# A toy vendor supplies three types of toys: Battery Based Toys, Key-based
# Toys, and Electrical Charging Based Toys. The vendor gives a discount of
# 10% on orders for battery-based toys if the order is for more than Rs. 1000.
# On orders of more than Rs. 100 for key-based toys, a discount of 5% is
# given, and a discount of 10% is given on orders for electrical charging based
# toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3
# are used for battery based toys, key-based toys, and electrical charging based
# toys respectively. Write a program that reads the product code and the order
# amount and prints out the net amount that the customer is required to pay
# after the discount.

purchase_of_toyA = int(input())
purchase_of_toyB = int(input())
purchase_of_toyC = int(input())

total_cost = 0

cost_of_toyA_after_discount = 0
cost_of_toyB_after_discount = 0
cost_of_toyC_after_discount = 0

if purchase_of_toyA > 1000:
    cost_of_toyA_after_discount = purchase_of_toyA - purchase_of_toyA*0.1

if purchase_of_toyB > 100:
    cost_of_toyB_after_discount = purchase_of_toyB - purchase_of_toyB*0.05

if purchase_of_toyC > 500:
    cost_of_toyC_after_discount = purchase_of_toyC - purchase_of_toyC*0.1

total_cost = cost_of_toyA_after_discount + cost_of_toyB_after_discount + cost_of_toyC_after_discount

print(f'The total Bill after applying the discount: {total_cost}')


# A transport company charges the fare according to following table:

# Distance         Charges
# 1-50             8 Rs./Km
# 51-100           10 Rs./Km
# > 100            12 Rs/Km

distance = int(input('Enter the distance travelled by you: '))

cost = 0

if distance > 100:
    cost = distance * 12
elif distance > 50 and distance < 100 :
    cost = distance * 10
else:
    cost = distance * 8

print(f'Total Cost for {distance}km travelled by you is {cost}')
