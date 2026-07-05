def adj_diff(arrsize,arr):
    diff =[]
    for i,j in zip(range(0,arrsize),range(1,arrsize)):
        diff.append(arr[i] - arr[j])
    return diff

arrSize = int(input("Enter Size of Array :"))
arr = []
for i in range(arrSize):
    arr.append(int(input(f"Enter element at {i}")))

print(arr)
d = adj_diff(arrSize,arr)
sum = 0
for i in d:
    sum += d 
    
print(f"Sum of Difference is {sum}")