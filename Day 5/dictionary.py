# mydict = {
#     101: "prashant",
#     102:"ashish",
#     "103": "mohini",
#     "104" : "triveni",
#     101 : "ashish",
#     104: "ashish"
# } #values are updateing wrt keys

# print(mydict)
# # print(type(mydict))  # <class 'dict'>

# a = mydict[102] # accessing value using key
# print(a)

# # we can replace a key value explicitly
# mydict[102] = "peter"
# print(mydict)

# # by default loop access keys only 
# for k in mydict:
#     print(k) # k = 101 102 103 104 104 

# # to print only values from dictionary
# for v in mydict.values():
#     print(v) # ashish ashish mohini triveni ashish 

# #To get key and value together
# for k,v in mydict.items():
#     print(k,v)
#     # 101 ashish
#     # 102 ashish
#     # 103 mohini
#     # 104 triveni
#     # 104 ashish
    
# # New key and value pair can be added :
# mydict["mobile no"] = 4646862521
# print(mydict) #{101: 'ashish', 102: 'ashish', '103': 'mohini', '104': 'triveni', 104: 'ashish', 'mobile no': 4646862521}

# # DICTIONARY FUNCTIONS
# mydict = {
#     101:"prashant",
#     "profession" : "developer",
#     "empid":1001
# }

# mydict.pop(101) #pop removes an item with the associated key that has passed as arguement
# print(mydict)

# mydict = {
#     101:"prashant",
#     "profession" : "developer",
#     "empid":1001
# }

# newdict = mydict.copy() # clone of mydict using copy()
# print(newdict)

#============================================TASKS==================================================
# check dictionary is empty or not
def checkEmpty(dict1):
    if dict1 == {}:
        return "Empty"
    else:
        return "Not Empty"

# key with max value
def getMaxKey(dict1):
    maxVal = dict1["A"]
    for k in dict1:
        if dict1[k] > maxVal:
            maxVal = k
    return maxVal        


mydict = {
    "A":50,
    "B":30,
    "C":70
}
print()
di = {}
print(checkEmpty(mydict))
print(checkEmpty(di))
print(getMaxKey(mydict))

#Reverse key value pair
# #