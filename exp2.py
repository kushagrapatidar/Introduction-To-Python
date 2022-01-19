def findpalindrome(n):
    if "".join(reversed(n))==n:
        print(f'{n} is palindrome')
    else:
        print(f'{n} is not palindrome')

def ispalindrome():
    n=input('Enter the number: ')
    findpalindrome(n)