def binarysearch(arr,s,e,n):
    if n>arr[-1] or n<arr[0]:
        return 0
    
    mid=s+(e-s)//2
    if n==arr[mid]:
        return mid+1
    elif n<arr[mid]:
        e=mid-1
        return binarysearch(arr,s,e,n)
    elif n>arr[mid]:
        s=mid+1
        return binarysearch(arr,s,e,n)
    
def binary_search():
    arr=input('Enter the elements of array with spaces: ').split()
    n=input('Enter the number to be searched: ')
    index=binarysearch(arr,0,len(arr)-1,n)
    if index==0:
        print(f"{n} not found in the array")
    else:
        print(f'{n} found at index: {index}')