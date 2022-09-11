def Sum_ListEle(LS,n):    
    if n==0:        
        return 0    
    else:        
        return LS[n-1]+Sum_ListEle(LS,n-1)
        
L=eval(input("enter a list of numbers : "))
size=len(L)
total=Sum_ListEle(L,size)
print("Sum of list elements is :", total)

