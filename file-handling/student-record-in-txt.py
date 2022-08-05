
st_record_file = open('StudentRecord.txt', 'w')


choice = int(input("Enter the no of reords you want to enter: "))
for i in range(choice):
    sRoll = int(input('Enter roll no. of student: '))
    sName = input('Enter Name of student: ')
    st_record_file.write(str(sRoll) + ',' + str(sName) + '\n')


print("Done updating the file")
