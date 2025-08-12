# lab7

# ------------------------------------------------------------------------------------------------------------------------------------
# 1. Write a Python program to sum all the items in a list.

# list1 = [1,2,3,4,5]
# sum = 0

# for num in list1:
#     sum = sum + num

# print(f'Sum of all the items in a list : {sum}')

# ------------------------------------------------------------------------------------------------------------------------------------
# 2. Write a Python program to get the largest and smallest number from a list without builtin functions.

# list2 = [1,2,3,4,5,4,32,6,-1]

# max = list2[0]
# min = list2[0]

# for num in list2:
#     if num > max:
#         max = num
#     if num < min:
#         min = num

# print(f'Max num is: {max}\nMin num is: {min}')

# ------------------------------------------------------------------------------------------------------------------------------------
# 3. Write a Python program to find duplicate values from a list and display those.

# list3 = [1,2,3,4,5,6,3,1,4,6,7,3,34,7]

# duplicates = []

# for index, value in enumerate(list3):
#     num = value 
#     num_index = index
#     list_part = list3[index+1:]
#     if num in list_part and not(num in duplicates):
#         duplicates.append(num)
        
# print(duplicates)

# ------------------------------------------------------------------------------------------------------------------------------------
# 4. Write a Python program to split a given list into two parts where the length of the first part of the list is given.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list: 3
# Splitted the said list into two parts:
# ([1, 1, 2], [3, 4, 4, 5, 1])


# n = 3

# list4 = [1, 1, 2, 3, 4, 4, 5, 1]

# first_list = list4[:n]
# second_list = list4[n+1:]

# print(first_list)
# print(second_list)

# ------------------------------------------------------------------------------------------------------------------------------------
# 5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
# Original list:
# ['red', 'green', 'white', 'black']
# Traverse the said list in reverse order:
# black
# white
# green
# red

# list5 = ['red', 'green', 'white', 'black']

# for i in range(len(list5)-1,-1,-1):
#     print(list5[i])








