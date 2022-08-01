def binary_search(sequence, item, Lb, Ub):
    #Perform Binary search
    if Lb > Ub :
        return -5
    #finding mid term for recurrion purpose
    mid = int((Lb + Ub)/2)
    if item == sequence[mid]:
        return mid
    elif item < sequence[mid]:
        Ub = mid - 1
        return binary_search(sequence, item, Ub, Lb)
    #recussing the function
    else:
        Lb = mid + 1
        return binary_search(sequence, Lb, Ub, item)

    
#putting values in eval function
L = eval(input("enter the elemnt in shorted order: "))
#cheking length of input
n = len(L)
element = int(input("Enter the element that you want to search: "))
#calling the function and storing as variable
found = binary_search(L, element, 0, n-1)
print(f"element found at index {found}")
