def ispalindrome(string):
    
    if "".join(reversed(string))==string:
        print(string+' is palindrome')
    else:
        print(string+' is not palindrome')