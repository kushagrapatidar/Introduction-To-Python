def binarysearch(arr,s,e,n):
    if n>arr[-1] or n<arr[0]:
        return 0
    i=s+(e-s)//2
    if arr[i]==n:
        return i+1
    elif arr[i]<n:
        s=i+1
        return binarysearch(arr,s,e,n)
    else:
        e=i-1
        return binarysearch(arr,s,e,n)

    
def binary_search():
    arr=list(map(int,input('Enter the elements of array with spaces: ').split()))
    n=int(input('Enter the number to be searched: '))
    index=binarysearch(arr,0,len(arr)-1,n)
    if index==0:
        print(f"{n} not found in the array")
    else:
        print(f'{n} found at index: {index}')
binary_search()