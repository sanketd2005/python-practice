# # single level inheritance
# class College: # parent class
#     def college_name(self): 
#         print("SITRC")
# #-------------------------------------------------------------
# class Student(College): #child class inheriting College class
#     def student_info(self):
#         print("Name: Sanket Daptare")
#         print("Branch: E&TC")
# #-------------------------------------------------------------
# stud = Student()
# stud.college_name() # accessing parent class method
# stud.student_info()


# # MultiLevel Inheritance
# class College: # parent class
#     def college_name(self): 
#         print("SITRC")
# #-------------------------------------------------------------
# class Student(College): #child class inheriting College class
#     def student_info(self):
#         print("Name: Sanket Daptare")
#         print("Branch: E&TC")
# #-------------------------------------------------------------
# class Exam(Student):
#     def subjects(self):
#         print("Subject 1: Python")
#         print("Subject 2: DBMS")
#         print("Subject 3: C++")

# ex = Exam()
# ex.college_name() # accessing parent class method -> College
# ex.student_info() # accessing parent class method -> Student
# ex.subjects() # # accessing self method -> Exam


# # Multiple Inheritance
# class SubMarks: # parent class -1
#     math = int(input("enter marks for math"))
#     english = int(input("enter marks for english"))
#     C = int(input("enter marks for C"))
#     python = int(input("enter marks for python"))
# #-------------------------------------------------------------
# class PractMarks: # parent class -2
#     cPract = int(input("C practical marks :"))
# #-------------------------------------------------------------
# class Result(SubMarks,PractMarks):  # Child class 
#     def getResult(self):
#         if self.math >=40 and self.english >= 40 and self.C >=40 and self.python >=40 and self.cPract >=20:
#             print("Pass...")
#         else:
#             print("Fail...") 
            
# res = Result()
# res.getResult()

class A:
    def add(self):
        print("A")
class B:
    def add(self):
        print("B")

class C(A,B):
    pass

obj = C()
obj.add()