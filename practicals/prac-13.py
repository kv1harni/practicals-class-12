#Write a program to write those lines which have the character 'p', from one text file to another

file1 = open('story.txt', 'r')
file2 = open('book.txt', 'w')

lines = file1.readlines()

for i in lines:
    for j in i:
        if j == 'p':
            file2.write(i)

file1.close()
file2.close()