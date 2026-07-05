def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1,2,3,4,5,6,7,8,9]
target = 7
result = linearSearch(arr,target)
if result >= 0:
    print("Element found at index : ",result)
else:
    print("Element not found")