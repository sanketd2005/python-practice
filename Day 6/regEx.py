# import re as regEx

# count =0

# fd = input("Enter what to search: ")

# pattern = regEx.compile(fd)

# # print(pattern)

# msg = '''Sanket Daptare is a skilled Backend and IoT Developer from Nashik, Maharashtra. 
# This engineering student at the Sandip Institute of Technology & Research Centre focuses on Electronics and Telecommunication Engineering.
# As a programmer, Sanket creates software tools using Python, Java, and Flask. 
# This hackathon winner secured the first runner-up spot at GitGrade 2025 by building an AI GitHub Repository Analyzer. 
# Outside of college, this freelancer and instructor teaches coding and builds web projects for clients.'''

# matcher = pattern.finditer(msg)

# print(type(matcher))
# for match in matcher:
#     count +=1 
#     print(match.start(),"->",match.end()," : ",match.group())

# print(f"The {fd} found {count} times")

#-----------------------------------------------------------------------------------------------------------------------------------


# import re as regEx
# count  = 0
# msg = input("Enter a message :")
# f = input("Enter what to find in message :")

# matcher = regEx.finditer(f,msg)

# for i in matcher:
#     count+=1
#     print(i.start()," -> ",i.end(),"  ",i.group())

# print(f"The {f} found {count} times")

#-----------------------------------------------------------------------------------------------------------------------------------


# # match(): returns only starting occurances
# import re as regEx
# a = input("enter string to perform match operation: ").lower()
# matchRE = regEx.match(a,"Python is very important language".lower())
# print(matchRE)
# if matchRE != None:
#     print(matchRE.start()," -> ",matchRE.end())
# else:
#     print("No match at beginning level")


#-----------------------------------------------------------------------------------------------------------------------------------

# #fullmatch(): matches entire string and returns the start,end and matching group, else None

# import re as regEx
# a = input("Enter string to perform full match :").lower()
# mch = regEx.fullmatch(a,"python is very")

# print(mch)

# if mch!=None:
#     print("Match Found")
#     print(mch.start()," -> ",mch.end())
    
# else:
#     print("\n\n\nFull Match Not found...")

#-----------------------------------------------------------------------------------------------------------------------------------

# #search() : 

# import re as regEx
# a = input("Enter string to perform full match :").lower()
# mch = regEx.search(a,"python is very")

# print(mch)

# if mch!=None:
#     print("Match Found")
#     print(mch.start()," -> ",mch.end())
    
# else:
#     print("\n\n\nFull Match Not found...")

#-----------------------------------------------------------------------------------------------------------------------------------

# # findall() : returns a list of matched characters in a string passed

# import re as regEx
# mtch = regEx.findall('[a-z0-9A-Z]',"123asdfghjk!@#$%^TYUIO") #^ will be except the class, denoted in []
# print(mtch)

#-----------------------------------------------------------------------------------------------------------------------------------


# #sub() : substitute function to replace the characters in a string, syntax -> (charClass,char_to_replace,actual string)

# import re as regEx
# obj = regEx.sub('[a-z]','_',"abCd EFgH iJkL MNOP")
# print(obj)

#-----------------------------------------------------------------------------------------------------------------------------------


# #subn() : substitute function to replace the characters in a string, syntax -> (charClass,char_to_replace,actual string), returns Data,count in tuple form

# import re as regEx
# obj = regEx.subn('[A-M]','_',"abCd EFgH iJkL MNOP")
# print(obj)
# print("the str in obj[0] = ",obj[0])
# print("the no of replacements = ",obj[1])

#-----------------------------------------------------------------------------------------------------------------------------------

# # Email ID verification
# import re as regEx
# email = input("Enter Email ID: ")
# m = regEx.fullmatch("\\w[a-z0-9A-Z_.]*@sitrc[.][org/com]",email)
# if m!=None:
#     print("Email ID is valid...")
# else:
#     print("Email ID is invalid...")
    
    
#-----------------------------------------------------------------------------------------------------------------------------------

# #WAP to check the valid mobile number
# import re as reg
# mobNo = input("Enter Mobile Number:")
# obj = reg.fullmatch("[0-9]\\d{9}",mobNo)

# if obj!=None:
#     print("Number is Valid")
# else:
#     print("Number is Invalid")
  
  
#-----------------------------------------------------------------------------------------------------------------------------------

# # match content from file

# import re as reg
# a = input("Enter content to find in myText.txt :")
# f = open("myText.txt",'r')
# c = f.read()

# mtch = reg.finditer(a,c)
# count = 0
# print(mtch)
# for i in mtch:
#     count+=1
#     print(i.start()," -> ",i.end(),"  ",i.group())

# print(f"The {f} found {count} times")
