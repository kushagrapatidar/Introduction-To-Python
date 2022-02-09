def fib(n):
    t1=0
    t2=1
    for _ in range(0,n):
        print(t1)
        algaTerm=t1+t2
        t1=t2
        t2=algaTerm

fib(int(input('Enter: ')))