"""Count words in file."""

file_name = input("Enter the name of the file for word counting: ")
f = open(file_name,"r")
word_count = {}
for line in f:
    line = line.strip()
    line = line.split(" ")
    for word in line:
        word_count[word] = word_count.get(word,0) + 1

#print(word_count)
for word, count in word_count.items():
    print(word, count)