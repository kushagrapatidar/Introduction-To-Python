def exchange():
    a,b=input('Enter two values (with spaces):').split()
    print(f'Brfore swaping A:{a}, B:{b}')
    a,b=b,a
    print(f'After swaping A:{a}, B:{b}')