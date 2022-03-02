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
def fibonacci_term(n):
    if n==1:
        return 0
    if n==2 or n==3:
        return 1
    return fibonacci_term(n-1)+fibonacci_term(n-2)