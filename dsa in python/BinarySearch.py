def binarySearch(arr,low,high,x):
    if high>=low:
        mid = (low+high) // 2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr,low,mid-1,x)
        elif arr[mid]<x:
            return binarySearch(arr,mid+1,high,x)
    else:
        return -1
    

arr = [2,3,4,5,6,7,8]
x = int(input("Enter the nuber you want to search: "))
result = binarySearch(arr,0,len(arr)-1,x)
if result == -1:
    print("Number Not Found!")
else:
    print(f"Number found at index {result}")
