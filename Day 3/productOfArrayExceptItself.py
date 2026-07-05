arr = [1,2,3,4]
prod = []
mul = 1
for i in range(0,len(arr)):
    for j in range((len(arr)-1),-1,-1):
       if arr[i] != arr[j]:
           mul *= arr[j] 
    prod.append(mul)
    mul = 1
print(prod)    