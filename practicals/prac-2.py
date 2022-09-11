# Write a program to find whether a phrase is a pallidrome or not

phrase = str(input("Enter a phrase: "))

l_phrase = list(phrase)     #convert the phrase into a list
rev_phrase = list(phrase)   #duplicate the list
rev_phrase.reverse()        #reversing the duplicated list

#checking if initial list is same as reversed list
if l_phrase == rev_phrase:  #if both are same then the given phrase is a pallidrome
    print("Given phrase is a pallidrome")
else:                       #else it is not a pallidrome   
    print("Given phrase is not a pallidrome")