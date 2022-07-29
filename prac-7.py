def binary_search(sequence, item, Lb, Ub):
    if Lb > Ub :
        return -5
    
    mid = int((Lb + Ub)/2)
    if item == sequence[mid]:
        return mid
    elif item < sequence[mid]:
        Ub = mid - 1
        return binary_search(sequence, item, Ub, Lb)

    else:
        Lb = mid + 1
        return binary_search(sequence, Lb, Ub, item)

L = eval(input("enter the elemnt in shorted order: "))
n = len(L)
element = int(input("Enter the element that you want to search: "))
found = binary_search(L, element, 0, n-1)
print(f"element found at index {found}")