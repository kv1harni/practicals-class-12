fout = open ("book.txt", 'w')
n = int(input("how many records do you want to add?:"))


for i in range (n):

    print ("enter the number of records you want to add:"+ str(i))
    title = input("enter the keyvalue:")

    price = input ("enter the price of the book:")
    r = title +" , " + price + "\n"
    fout.write(r)

fout.close
