#working with txt files in python


#opening a text file in append mode
f = open("someFile.txt", 'a+')

#printing wheater the file obj is closed or not
print(f.closed)  #returns -> False as File is not closed

#closing the file 
f.close()

#again printing is file is closed
print(f.closed) #returns true

