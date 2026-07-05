
class Demo:
    # constructor called only once for each object
    def __init__(self):
        
        print("I am a constructor and i always called first")
    # instance method
    def info(self):
        print("object 1") 
        
obj = Demo()
obj.info()
obj2 = Demo()

# obj2.info()

print(obj)
print(obj2)