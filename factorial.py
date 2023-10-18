n = int(input("Enter number : "))


def factorial(n):
    factorial = 1
    if n==0 or n==1 :
        return 1
    for i in range (1, n+1):
        factorial = i * factorial
    return factorial
        
    
result = factorial(n)
        

print("the factorial of ",n," is ", result)