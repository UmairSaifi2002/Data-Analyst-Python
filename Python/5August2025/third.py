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
