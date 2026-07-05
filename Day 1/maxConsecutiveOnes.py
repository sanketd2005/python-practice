arr = [1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1]
c=[]
count = 0
for i in arr:
    if i == 1:
        count+=1
    else:
        count = 0
    c.append(count)
    
print(c)
print(max(c))