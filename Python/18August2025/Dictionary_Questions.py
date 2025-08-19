# Q1. Write a Python program and calculate the mean of the below dictionary

# test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

# sum = 0
# num = 0

# for key,value in test_dict.items():
#     sum = sum + value
#     num = num + 1
    
# mean = sum / num

# print(mean)

# --------------------------------------------------------------------------------------
# Q2. Write a Python script to concatenate the following dictionaries to create a new one.

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# # final_dict = {**dic1, **dic2, **dic3}
# final_dict = dic1 | dic2 | dic3

# print(final_dict)

# --------------------------------------------------------------------------------------
# Q3. Write a Python program to get the key, value and item in a dictionary

# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print('Key  Value')
# for key,value in dict_num.items():
#     print(f'{key}    {value}')

# -------------------------------------------------------------------------------------
# Q4. Write a program to drop a key's having None value

# input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}

# filtered = {k:v for k,v in input_dict.items() if v is not None}

# input_dict.clear()
# input_dict.update(filtered)

# print(input_dict)




