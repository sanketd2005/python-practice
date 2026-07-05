# # Q-1
# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])

# # Q-2
# a=[1,2,3,4,5,6,7,8,9]
# a[::2] = 10,20,30,40,50,60
# print(a)
# ValueError: attempt to assign sequence of size 6 to extended slice of size 5

# # Q-3
# a = [1,2,3,4,5]
# print(a[3:0:-1])
# [4, 3, 2]

# # Q - 4
# def func(value,values):
#     var = 1
#     values[0] = 44

# t = 1
# v  = [1,2,3]
# func(t,v)
# print(t,v[0])   # 1 44


# # Q-5
# arr = [
#     [1,2,3,4],
#     [4,5,6,7],
#     [8,9,10,11],
#     [12,13,14,15]
# ]

# for i in range(0,4):
#     print(arr[i].pop())  # 4 7 11 15

# # Q-6
# def f(i,values = []):
#     values.append(i)
#     print(values)

# f(1)
# f(2)
# f(3)
# # sol -
# # [1]
# # [1, 2]
# # [1, 2, 3]

# # Q-7
# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1] = arr[i]

# for i in range(0,6):
#     print(arr[i],end=" ")  #2 3 4 5 6 6 


# # Q - 8
# fruit_list1 = ['apple','Berry','Cherry','Papaya']
# fruit_list2 = fruit_list1 # address of fruit_list1, points to fruit_list1
# fruit_list3 = fruit_list1[:] # copy of fruit_list1

# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0 #22
# for ls in (fruit_list1,fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum+=1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print(sum) 


# # Q - 9
# init_tuple = ()
# print(init_tuple.__len__()) # 0

# #Q - 10
# init_a = 'a','b'
# init_b = ('a','b')

# print(init_a == init_b) #true


# # Q 11

# init_a = '1','2'
# init_b = ('2','3')

# print(init_a+init_b) #('1', '2', '2', '3')

# Q 12
# l = [1,2,3]
# init_t = ('Python',)*(l.__len__() - l[::-1][0])
# print(l[::-1][0])
# print()
# print(init_t)

##Q 13
# init_tuple = ('Python')*3
# print(type(init_tuple)) #<class 'str'>

# DICTIONARY 
# #Q 14
# a = {
#     (1,2):1,
#     (2,3):2,
#     (4,5):3
# }

# print(a[4,5]) # 3

# ## Q15
# a = {
#     'a':1,'b':2,'c':3
# }
# print(a['a','b']) # KeyError: ('a', 'b')

# # Q 16
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
        
#     else:
#         fruit[index] =1
# addone('Apple')
# addone('Banana')
# addone('apple')

# print(len(fruit))
# print(fruit)

# # 3
# # {'Apple': 1, 'Banana': 1, 'apple': 1}


# # Q 17
# arr={}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
    
# print(sum)

# # {1: 2, '1': 2}
# # 4


# # Q 18
# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4

# print(my_dict)
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
    
# print(sum)
# # {1: 4, '1': 2}
# # 6

# # Q 19
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum =0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)
# # 30
# # {(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}

# # Q 20
# box = {}
# jars = {}
# crates = {}

# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4

# crates['box'] = box
# crates['jars'] = jars

# print(len(crates[box]))
# # TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')

##Q21
# dict ={'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])
# 96
# 98
# 97

## Q 22 -> POINTERS 
# math = 50
# chem = 50
# phy = 50
# print(id(math))
# print(id(phy))
# print(id(chem))

# # id -> address of variable

## Q 23
# rec = {
#     "Name":"Python",
#     "Age" : "20"
# }
# r = rec.copy()

# print(id(r))
# print(id(rec))
# print(id(rec) == id(r))

## Q 24
# rec={"name":"python","age":"20","addr":"NJ","Country":"USA"}
# id1 = id(rec)
# del rec

# rec={"name":"python","age":"20","addr":"NJ","Country":"USA"}
# id2 = id(rec)
# print(id(id1))
# print(id(id2))
# print(id1 == id2)


###TYPECASTING...
# print(int(3.14))
# # print(int('10+5j'))
# print(int(True))
# print(int(False))
# # print(int('4.22'))
# print(int('4'))

# print(float(3.14))
# # print(float('10+5j'))
# print(float(True))
# print(float(False))
# print(float('4.22'))
# print(float('4'))


# print(bool(3))
# print(bool('10+5j'))
# print(bool(True))
# print(bool(False))
# print(bool('4.22'))
# print(bool('4'))
# print(bool(0+0j))