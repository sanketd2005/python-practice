
# try:
#     a  = int(input('Enter value of A :'))
#     b  = int(input('Enter value of b :'))
#     print(a/b)
    
# except ZeroDivisionError:
#     print("can't divide by zero")

# except ValueError:
#     print("NaN : only numbers are allowed")
    
# print("Continue flow....")    


# # TO PRINT CUSTOM MESSAGE ALONG WITH PREDEFINED MESSAGE
# try:
#     a  = int(input('Enter value of A :'))
#     b  = int(input('Enter value of b :'))
#     print(a/b)
    
# except ZeroDivisionError as msg:
#     print("can't divide by zero -> ",msg)

# except ValueError as msg:
#     print("NaN : only numbers are allowed -> ",msg)
    
# print("Continue flow....")    


# # single except block can handle multiple errors:

# try:
#     a  = int(input('Enter value of A :'))
#     b  = int(input('Enter value of b :'))
#     print(a/b)
    
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
    
# print("Continue flow....")    



# try:
#     a  = int(input('Enter value of A :'))
#     b  = int(input('Enter value of b :'))
#     print(a/b)
    
# except :
#     print("Default block of except")  #SyntaxError: default 'except:' must be last
     
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
    
# print("Continue flow....")    


# # else block
# try:
#     a  = int(input('Enter value of A :'))
#     b  = int(input('Enter value of b :'))
#     print(a/b)
    
     
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
# except :
#     print("Default block of except")  #SyntaxError: default 'except:' must be last
    
# else:
#     print("Continue flow.... everything is oKk")    


# # finally block
# try:
#     a  = int(input('Enter value of A :'))
#     b  = int(input('Enter value of b :'))
#     print(a/b)
    
     
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
# except :
#     print("Default block of except")  #SyntaxError: default 'except:' must be last

# finally:
#     print(" Always executes... finally block")    


# #nested try except
# try:
#     a  = int(input('Enter value of A :'))
#     b  = int(input('Enter value of b :'))
#     try:
#        print(a/b)
    
#     except ZeroDivisionError as msg:
#         print(msg)

# except ValueError as message:
#     print(message)
    
# finally:
#     print(" Always executes... finally block")    



# # ALL covered:
# try:
#     a  = int(input('Enter value of A :'))
#     b  = int(input('Enter value of b :'))
#     print(a/b)   
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
# except :
#     print("Default block of except")
# else:
#     print(" Except not executes... Else block")    
# finally:
#     print(" Always executes... finally block")    


# USER DEFINED Exception BY RAISE KEYWORD

bankBal = 12000
if bankBal < 2000:
    raise Exception("YOUR ACCOUNT IS BELOW A ACCESS LIMIT")
else:
    print("Amount withdrawn successfully")