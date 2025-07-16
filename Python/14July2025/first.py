# left shift 
a = 50
b = a << 2  # Shift bits of 'a' to the left by 2 positions
print(b) # 200
c = a >> 2  # Shift bits of 'a' to the right by 2 positions
print(c) # 12

# important note 
# if we do right shift to a number means it will be divided by 2 every time
num = 100
print(num >> 1)  # 50
print(num >> 2)  # 25
print(num >> 3)  # 12
print(num >> 4)  # 6
print(num >> 5)  # 3
print(num >> 6)  # 1
print(num >> 7)  # 0

num1 = 1
print(num1 << 1) # 2
print(num1 << 2) # 4
print(num1 << 3) # 8

# 'in' or 'not in' operator
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(1 in l)  # True
print(11 in l)  # False
print(1 not in l)  # False
print(11 not in l)  # True


