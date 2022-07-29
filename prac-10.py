f = open("someFile.txt", 'a+')
print(f.closed)
f.close()
print(f.closed)

