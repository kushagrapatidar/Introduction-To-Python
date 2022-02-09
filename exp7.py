def fibonacci(n,a=0,b=1):
    if a==0:
        print(a,end=" ")
    if b<=n:
        print(b,end=" ")
        a=b+a
        a,b=b,a
        fibonacci(n,a,b)

def fibonacci_iter(n):
    i=0
    j=1
    while i<=n:
        print(i,end=" ")
        i=i+j
        i,j=j,i
        