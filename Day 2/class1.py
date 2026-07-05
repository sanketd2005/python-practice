# class HOD:
#     def __init__(self):
#         self.name = "Mr. SD"
#         self.age = 21
#         self.id = 122024126
#     def info(self):
#         print(f"Name-> {self.name}")
#         print(f"age-> {self.age}")
#         print(f"ID-> {self.id}")
        
# obj = HOD()
# obj.info()


# class HOD:
#     def __init__(self,name,age,id):
#         self.name = name
#         self.age = age
#         self.id = id
#     def info(self):
#         print(f"Name-> {self.name}")
#         print(f"age-> {self.age}")
#         print(f"ID-> {self.id}")
        
# obj = HOD("SD",21,1001) #Parameterized constructor -> value assigned at obj initialisation
# obj.info()

# # Instance variables
# class New:
#     def __init__(self):
#         self.a = 10

# obj1 = New()
# obj2 = New()
# obj3 = New()
# obj1.a = 20 # instance variable a 
# print(obj1.a) #20
# print(obj2.a) #10
# print(obj3.a) #10

# class New:
#     a = 10
#     def __init__(self):
#         pass

# obj1 = New()
# obj2 = New()
# obj3 = New()
# New.a = 20 # static variable a 
# print(obj1.a) #20
# print(obj2.a) #20
# print(obj3.a) #20


# # static and Dynamic Example
# class College:
#     college_name = "SITRC"
#     def __init__(self):
#         self.studentName = "Sanket"
    
# principal = College()
# teacher = College()
# accountant = College()

# print(f"Principal = {principal.college_name} ... {principal.studentName}")
# print(f"Teacher = {teacher.college_name} ... {teacher.studentName}")
# print(f"Accountant= {accountant.college_name} ... {accountant.studentName}")

# College.college_name = "KKWP"
# principal.studentName = "Sanket Daptare"

# print(f"Principal = {principal.college_name} | {principal.studentName}")
# print(f"Teacher = {teacher.college_name} | {teacher.studentName}")
# print(f"Accountant= {accountant.college_name} | {accountant.studentName}")


# # access and deleting instance variable
# class Student:
#     def __init__(self):
#         #instance vars
#         self.s_name = input("enter name")
#         self.s_rollNo = 1011
#     def getData(self):
#         #instance var
#         self.s_mb = 1024
    
# obj = Student()
# obj.getData() # s_mb initializes
# obj.s_branch = "IT" # external instance variable creation
# # del obj.s_rollNo #deletig instance variable s_rollNo

# print(obj.__dict__)


# # static method : independant from object(instances)

# class Student:
    
#     @staticmethod # decorator mandatory to identify static method
#     def getData(fName,lName): # no self parameter is passed
#         print(f"Your Name {fName + " " + lName}")
        
#     @staticmethod
#     def getContactDetails(mobNo, rno):
#         print(f"Your Mobile number: {mobNo}")
#         print(f"Your Roll number: {rno}")
        
# Student.getData("Sanket", "Daptare")
# Student.getContactDetails(8828502572,121)

