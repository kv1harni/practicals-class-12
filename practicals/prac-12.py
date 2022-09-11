#Write a program to count the number of times the occurrence of 'is' word in a text file

file = open('story.txt', 'r')
count = 0

text = file.read()
text_list = text.split()

for i in text_list:
    if i == 'is':
        count += 1
print(count)

file.close()