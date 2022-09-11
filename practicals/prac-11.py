#Write a program to count number of words in a file

file = open('story.txt', 'r')       #initiating file object 

text = file.read()                  #reading the file content
text_list = text.split()            #splitting the text by empty space and adding each word to a list

print(len(text_list))               #printing out the length of the list which depicts the number count of words

file.close()