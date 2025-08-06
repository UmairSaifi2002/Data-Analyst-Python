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


