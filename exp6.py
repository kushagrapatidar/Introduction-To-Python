def factorial(n,a=0,b=1):
    if b<=n:
        print(b,end=" ")
        a=b+a
        a,b=b,a
        factorial(n,a,b)