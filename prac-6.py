#write a program to print fibonacci series

# Program to display the Fibonacci sequence up to n-th term

#defining a fibonacci logic
def fibonacci(n):
    if n <= 1:
        return n
    
    else:
        #recursion techniqe is used
        return(fibonacci(n-1)+ fibonacci(n-2))

    #taking input of variables
nterms = int(input("How many terms? :"))

#making a for loop for iterating values 
for i in range(nterms):
    print(fibonacci(i)," ", end=" ")

