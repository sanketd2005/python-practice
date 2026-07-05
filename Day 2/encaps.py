# # """
# # __varname : for private
# # _varname: for protected
# # no u
# # """


# # class Base:
# #     def __init__(self):
# #         print("Parent class constructor called")
# #         print('-'*50)
# #         self.a = "Sanket" #public data member
# #         self.__c = "Atharva" #private data member
        
# # class Derived(Base):
# #     def __init__(self):
# #         # calling constructor of Base class
# #         Base.__init__(self)
# #         print("calling members of a Base class: ")
# #         # print("Inside derived constructor : ",self.a)  ## accessible
# #         # print('-'*50)
# #         # print(self.__c) #not accessible
        
# # # obj1 = Derived()
# # # print("Outside class by derived_obj: ",obj1.a) #accessible
# # # print(obj1.__c) # not accessible
# # # print('-'*50)

# # obj2Base = Base()
# # print("Outside class by base_obj :",obj2Base.a)
# # print(obj2Base.__c)


# """
# __varname : for private
# _varname: for protected
# no underscore for public, by default all members are public
# """


# # class Base:
# #     def __init__(self):
# #         print("Parent class constructor called")
# #         print('-'*50)
# #         self.a = "Sanket" #public data member
# #         self._c = "Atharva" #private data member
        
# # class Derived(Base):
# #     def __init__(self):
# #         # calling constructor of Base class
# #         Base.__init__(self)
# #         print("calling members of a Base class: ")
# #         print("Inside derived constructor : ",self.a)  ## accessible
# #         print('-'*50)
# #         print(self._c) # accessible
        
# # obj1 = Derived()
# # print("Outside class by derived_obj: ",obj1.a) #accessible
# # print(obj1._c) #  accessible
# # print('-'*50)

# # # obj2Base = Base()
# # # print("Outside class by base_obj :",obj2Base.a)
# # # print(obj2Base._c)


# # private and public method 
# class RBI:
#     def publicPolicy(self):
#         print("publicPolicy from RBI")
#         print('*'*50)
#     def __privatePolicy(self):
#         print(" __privatePolicy from RBI")
        
# class SBI(RBI):
#     def __init__(self):
#         RBI.__init__(self)
        
#     def callingPublicMethod(self):
#         print("INSIDE SBI CLASS")
#         print('*'*50)
        
#         self.publicPolicy()
#     def callingPrivateMethods(self):
#         self.__privatePolicy()
        
# # sbiObj = SBI()
# # # sbiObj.callingPublicMethod()
# # # sbiObj.callingPrivateMethods()
# # sbiObj.publicPolicy()
# # sbiObj.__privatePolicy()

# rbiObj = RBI()
# rbiObj.publicPolicy()
# rbiObj.__privatePolicy()
# # rbiObj._RBI__privatePolicy()


