def fibonacci(n,a=0,b=1):
    if a==0:
        print(a,end=" ")
    if b<=n:
        print(b,end=" ")
        a=b+a
        a,b=b,a
        fibonacci(n,a,b)