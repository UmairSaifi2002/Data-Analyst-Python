# write a Python program that counts the frequency of each word and then prints the words sorted by frequency (descending order). 
# "" sentence = "the cat and the dog and the mouse""""

sentence = "the cat and the dog and the mouse"

words = sentence.split()

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

freq_list = []
for word in freq:
    freq_list.append([word, freq[word]])

print(freq_list)

n = len(freq_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if freq_list[j][1] < freq_list[j + 1][1]:
            freq_list[j], freq_list[j + 1] = freq_list[j + 1], freq_list[j]

print(freq_list)

for word, count in freq_list:
    print(word, ":", count)



