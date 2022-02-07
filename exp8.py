def binarysearch(arr,s,e,x):
    if x>arr[-1] or x<arr[0]:
        return 0
    i=s+(e-s)//2
    if arr[i]==x:
        return i+1
    elif arr[i]<x:
        s=i+1
        return binarysearch(arr,s,e,x)
    else:
        e=i-1
        return binarysearch(arr,s,e,x)

    
def binary_search():
    arr=input('Enter the elements of array with spaces: ').split()
    n=input('Enter the number to be searched: ')
    index=binarysearch(arr,0,len(arr)-1,n)
    print(index)
    if index==0:
        print(f"{n} not found in the array")
    else:
        print(f'{n} found at index: {index}')