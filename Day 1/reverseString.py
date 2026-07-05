# str1 = "Hello"
# str2 = ""
# n = len(str1)
# print(len(str1))
# for i in range((n-1),-1,-1):
#     str2 += str1[i]

# print(str2)     

str1 = "Sanket"
uniq = ""
n = len(str1)
for i in str1:
    if i not in uniq:
        uniq+=i

print(uniq)     