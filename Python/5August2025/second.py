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

