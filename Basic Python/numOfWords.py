count = 0

file = open('C:Users/dell/Documents/fille', 'r')
for line in file:
    words = line.split(" ")

count = count + len(words)

print("Number of words present in given file" + str(count));

file.close();