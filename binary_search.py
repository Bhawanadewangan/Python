def binary_sear(arr, low, high, x):
    if high >= low:
        mid = (high+low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_sear(arr, low, mid - 1, x)
        else:
            return binary_sear(arr , mid + 1, high, x)
    else:
        return -1
arr = [2, 3, 4, 10, 40, 9, 650, 1, 100, 1.23]
x= 40
result=binary_sear(arr,0,len(arr)-1,x)
if result!= -1:
    print("element is present at index")
else:
    print("element is not present at index")



