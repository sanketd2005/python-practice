# nested loop practice : TIME COMPLEXITY -> O(n^N), always. where N-> No. of Loops

# '''
# 1 1 1 
# 2 2 2
# 3 3 3 
# '''
# for i in range(1,4): #outer loop  -> rows
#     for j in range(1,4): #inner loop -> cols
#         print(i,end=" ")
#     print()

#--------------------------------------------------------------------------------------------------

# '''
# n = 5
# ----------
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3 
# 4 4 4 4 4
# 5 5 5 5 5
# ----------
# '''
# n  = int(input("Enter a number: "))
# for i in range(1,n+1): #outer loop  -> rows
#     for j in range(1,n+1): #inner loop -> cols
#         print(i,end=" ")
#     print()

#--------------------------------------------------------------------------------------------------

# '''
# n = 5
# 5 5 5 5 5 
# 4 4 4 4 4 
# 3 3 3 3 3 
# 2 2 2 2 2 
# 1 1 1 1 1 

# '''
# n  = int(input("Enter a number: "))
# for i in range(1,n+1): #outer loop  -> rows
#     for j in range(1,n+1): #inner loop -> cols
#         print(n+1-i,end=" ")
#     print()

#--------------------------------------------------------------------------------------------------
 
# '''
# n = 5
# -----------
# *
# **
# ***
# ****
# *****
# ------------
# '''

# n = int(input("Enter Number :"))
# for i in range(1,n+1):
#     print("*"*i)
    
#--------------------------------------------------------------------------------------------------    

# '''
# n = 5
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
# '''

# n = int(input("Enter Number :"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+i),end=" ")  #chr(): ASCII(int) -> Alphabet/special character
#     print()

#--------------------------------------------------------------------------------------------------

# '''
# n = 5
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# '''

# n = int(input("Enter Number :"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")  
#     print()

#--------------------------------------------------------------------------------------------------

# '''
# n = 5
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 
# '''

# n = int(input("Enter Number :"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")  #chr(): ASCII(int) -> Alphabet/special character
#     print()

#--------------------------------------------------------------------------------------------------

# '''
# n = 5
# having delay of 2 sec
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1 
# '''

# import time 
# n = int(input("Enter an Number: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         time.sleep(0.5)
#         print(n+1-i,end=" ")
#     print()

#--------------------------------------------------------------------------------------------------


# '''
# Enter an Number: 6
# E E E E E E 
# D D D D D 
# C C C C 
# B B B 
# A A 
# @ 
# '''

# n = int(input("Enter an Number: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+n-i),end=" ")
#     print()

#--------------------------------------------------------------------------------------------------


# '''
# Enter an Number: 5
#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
# '''

# import time
# n = int(input("Enter an Number: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(0.2)
#         print("*",end=" ")
#     print()

