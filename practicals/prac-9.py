#write a program to read a text file

#opening the file object using the open() method
file = open('someFile.txt', 'r')

#reading lines
l1 = file.readlines()

#empty variable to store line
line = " "

#iterating through the number of lines
for i in range(len(l1)):
    l = l1[i].split()
    for j in l:
        line = line + j
        line = line + '#'
#printing the line
print(line)

#closing the file
file.close()
