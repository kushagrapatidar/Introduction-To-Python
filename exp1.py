def findprime(n):
    from math import sqrt
    if n>1:
        x=0
        for i in range(2, sqrt(n)+1):
            if n%1==0:
                x=1
                break
        if x==1:
            print(f"{n} is not prime.")
        else:
            print(f"{n} is prime.")
    else:
        print(f"{n} is not prime.")

def isprime():
    n=int(input('Enter the number'))
    findprime(n)