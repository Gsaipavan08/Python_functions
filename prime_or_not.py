n= int(input("enter number : "))

def check_prime(n):
    for i in range(2,n):
        if n%i==0:
            print("not a prime")
            break
    else:
        print("prime")

check_prime(n)