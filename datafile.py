from secrets import choice


st_record = [ ]

choice = int(input("Enter the no of reords you want to enter: "))
for i in range(choice):
    sRoll = int(input('Enter roll no. of student: '))
    sName = input('Enter Name of student: ')
    st_dict = {'roll': sRoll, 'name' : sName}
    st_record.append(st_dict)

print(st_record)