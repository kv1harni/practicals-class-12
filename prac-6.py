#write a program to print fibonacci series

# Program to display the Fibonacci sequence up to n-th term

#defining a fibonacci logic
def fibonacci(n):
    if n <= 1:
        return n
    
    else:
        return(fibonacci(n-1)+ fibonacci(n-2))

nterms = int(input("How many terms? :"))

#making a for loop for iterating values 
for i in range(nterms):
    print(fibonacci(i)," ", end=" ")

