#write a program to read a text file

file = open('someFile.txt', 'r')
l1 = file.readlines()
line = " "
for i in range(len(l1)):
    l = l1[i].split()
    for j in l:
        line = line + j
        line = line + '#'

print(line)
file.close()