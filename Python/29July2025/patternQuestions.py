# first pattern

#     1 
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1

# num = int(input('Enter a number to generate the pattern: '))

# for i in range(1, num + 1):
#     for j in range(num - i, 0, -1):
#         print(' ', end='')
#     for j in range(1, i + 1):
#         print(j, end='')
#         print(' ', end='')
#     print()

# for i in range(num-1, 0, -1):
#     for j in range(num - i, 0, -1):
#         print(' ', end='')
#     for j in range(1, i+1):
#         print(j, end='')
#         print(' ', end='')
#     print()


# second pattern -------------------------------------------------------------

# *
# **
# * *
# *  *
# *****

# n = 5  # height of the pyramid

# for i in range(1, n+1):
#     if i == 1 or i == n:
#         print('*' * i)
#     else:
#         print('*' + ' ' * (i-2) + '*')

# third pattern ---------------------------------------------------------------

# 1
# 12
# 1 3
# 1  4
# 12345

# for i in range(1, 6):
#     for j in range(1, i+1):
#         if i == j or i == 1 or i == 5 or j == 5 or j==1:
#             print(j, end='')
#         else:
#             print(' ',end='')
#     print()

# fourth pattern ------------------------------------------------------------------

# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end='')
#     print()

# fifth pattern ------------------------------------------------------------------

# 12345
# 1234
# 123
# 12
# 1

# for i in range(5, 0, -1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

# sixth pattern ---------------------------------------------------------------

# 12345
# 1  4
# 1 3
# 12
# 1

# for i in range(5, 0, -1):
#     for j in range(1, i+1):
#         if i==j or i==1 or i==5 or j==1 or j==5:
#             print(j, end='')
#         else:
#             print(' ', end='')
#     print()

# seventh pattern -----------------------------------------------------------

#     1 
#    1 2 
#   1   3
#  1     4
# 1 2 3 4 5

# n = 5

# for i in range(1, n+1):
#     for j in range(n-i, 0, -1):
#         print(' ', end='')
#     for j in range(1, i+1):
#         if i == j or i == 1 or i == n or j == 1 or j == n:
#             print(j, end='')
#             print(' ', end='')
#         else:
#             print('  ', end='')
#     print()

# Eight pattern ------------------------------------------------------------

#         1 
#       2 3 2 
#     3 4 5 4 3
#   4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5

num = 5

for i in range(1, num + 1):
    for j in range(num-i, 0,-1):
        print(' ', end=' ')
    n = i
    for j in range(1, i+1):
        print(n, end=' ')
        n = n+1
    n = n-2
    for j in range(2, i+1):
        print(n, end=' ')
        n = n-1
    print()



