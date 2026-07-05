#move all the zeros to the end without changing the order of non zero elements

arr=[0,10,1,0,3]
print(arr)

for i in arr:
    if i == 0:
        arr.remove(i)
        arr.append(i)

print(arr)