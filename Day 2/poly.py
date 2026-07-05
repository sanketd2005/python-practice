# # # Compile Time Polymorphism
# # Method Overloading
# class Arithmatic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
        
# obj = Arithmatic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)

# # constructor overloading

# class Arithmatic:
#     def __init__(self):
#         print("there is no arguement")
#     def __init__(self, a):
#         print("there is one arguement")
#     def __init__(self, a,b):
#         print("there are two arguement")

# obj = Arithmatic()
# obj = Arithmatic(1)
# obj = Arithmatic(1,2)


# ### RUNTIME POLYMORPHISM - 
# # Method Overriding - child class not satisfying the parent class implementation of parent class methods
# class RBI:
#     def homeLoan(self):
#         print("RBI: R. O. I. for Home Loan -> 8%")
        
#     def carLoan(self):
#         print('RBI : R. O. I. for Car Loan -> 7 %')
    
# class SBI(RBI):
#     def homeLoan(self):
#         super().homeLoan()
#         print("SBI: R. O. I. for Home Loan -> 10.5 %")
        
# sbiObj = SBI()
# sbiObj.homeLoan()
# sbiObj.carLoan()



# # Constructor Overriding

# class Father:
#     def __init__(self):
#         print("Father := i am on time at breakfast table")
        
# class Child(Father):
#     def __init__(self):
#         super().__init__() # parent constructor call
#         print("Child := i will be late for breakfast")
    
    
# chObj = Child() # without super() ->  Child := i will be late for breakfast
