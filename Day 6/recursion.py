# # factorial solution
# def fact(num):
#     if num <= 1:
#         return 1
#     else:
#         return num*fact(num-1) #recursive call

# print(fact(4))

#==========================================================================================
# def isPalindrome(strng):
#     if len(strng)== 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])

# print(isPalindrome("awesome"))
# print(isPalindrome("foobar"))
# print(isPalindrome("tacocat"))
# print(isPalindrome("tacocat"))

#==========================================================================================

# def power(base, exponent):
#     if exponent ==0:
#         return 1
#     return base * power(base,exponent-1)

# print(power(2,0))
# print(power(2,1))
# print(power(2,2))
# print(power(2,3)) # 2*power(2,2)-> 2*power(2,1)-> 2*power


#==========================================================================================

# def productOfArr(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArr(arr[1:])

# print(productOfArr([1,2,3]))
# print(productOfArr([1,2,3,4,12]))

#==========================================================================================

# def recursiveRange(num):
#     if num <=0:
#         return 0
#     return num + recursiveRange(num-1)

# print(recursiveRange(5))
# print(recursiveRange(6))
# print(recursiveRange(7))

#==========================================================================================

def fib(num):
    if (num < 2):
        return num
    return fib(num-1)+fib(num-2)

print(fib(4))
print(fib(10))
'''
fib(9) + fib(8)
fib(8)+fib(7)

'''


print(fib(21))

# 0 1 1 2 3 5 8 13 21 34 55 