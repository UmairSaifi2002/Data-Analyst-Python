# first ------------------------------------------------------------------

file = open('file_name', 'r') 
data = file.readline()

print(data)

# second -----------------------------------------------------------------

# Write a python program to count and display words in a abc.txt

content = ''
# Open the file in read mode
with open("abc.txt", "r") as file:
    content = file.read()

# Split the content into words
words = content.split()
print(words)

# Count the total number of words
word_count = len(words)

# Display the words
print("Words in the file:")
for word in words:
    print(word)

# Display the total word count
print("\nTotal number of words:", word_count)


# third -----------------------------------------------------------------------

import re
# write a program to count a Uppercase words
content = ''
with open('abc.txt', 'r') as file:
    content = file.read()

word_list = content.strip().split()

# using for loop
uppercase_word = 0

for i in word_list:
    if i.isupper():
        print(i)
        uppercase_word = uppercase_word + 1

# print(word_list)

print(f'Total upper-case words is : {uppercase_word}')

# without loop
count = len(re.findall(r'[A-Z]',content))
print(count)


# fourth ----------------------------------------------------------------------

# write a program to count a word which have less than 4 character

content = ''
with open('abc.txt', 'r') as file:
    content = file.read()

data = content.strip().split()

count = 0
for i in data:
    if len(i) < 4:
        print(i)
        count = count + 1

print(count)


#


