
fp = open('C:\\Users\\umair\\OneDrive\\Desktop\\AnuDIP\\Data-Analyst-Python\\Python\\4August2025\\file.txt', 'r')

data = fp.read()
print(data)
fp.close()


fp = open('C:\\Users\\umair\\OneDrive\\Desktop\\AnuDIP\\Data-Analyst-Python\\Python\\4August2025\\file.txt', 'w')
name = input()
age = str(input())
course = str(input())
info = name + ' ' + age + ' ' + course
fp.write(info)
fp.close()
