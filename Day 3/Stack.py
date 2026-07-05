# stack implementation with size limit 
import sys as system

class Stack:
    def __init__(self,stackSize):
        self.stackSize = stackSize #stack size defined 
        self.myStack = [] #list represent stack
        print(f"Stack Created of size: {self.stackSize}")
    
    def push(self,value):
        if self.isFull():
            print("Stack is Full")
        else:
            self.myStack.append(value)
            print(f"Element {value} pushed into Stack...")
    
    def popElement(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            print(f"{self.myStack.pop()} popped from stack")  #mystack[-1]
        
    
    def isFull(self): 
        if len(self.myStack) == self.stackSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if len(self.myStack) == -1:  # alternate -> if self.mystack == []
            return True
        else:
            return False
    
    def showStack(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            for i in range((len(self.myStack)-1),-1,-1):
                print(f"[{self.myStack[i]} ] => { i }")
            
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(f"Top element is {self.myStack[len(self.myStack) - 1]}") #self.myStack[-1]
            
    def deleteStack(self):
        del self.myStack

size = int(input("Enter the size of stack :"))
stackObj = Stack(size)
while True:
    print("-"*50)
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. isEmpty")
    print("5. isFull")
    print("6. display")
    print("7. Delete stack")
    print("8. Exit")
    choice = int(input("Enter Choice: "))
    print("-"*50)
    
    match choice:
        case 1:
            value = int(input("Enter Stack element value to push: "))
            stackObj.push(value)
            print("-"*50)
            
        case 2:
            stackObj.popElement()
            print("-"*50)
            
        case 3:
            stackObj.peek()
            print("-"*50)
            
        case 4:
            if stackObj.isEmpty():
                print("Stack is Empty")
            else:
                print("Stack is not Empty")
            print("-"*50)
            
        case 5:
            if stackObj.isFull():
                print("Stack is Full")
            else:
                print("Stack is not Full")
            print("-"*50)
            
        case 6:
            stackObj.showStack()
            print("-"*50)
            
        case 7:
            stackObj.deleteStack()
            print("Stack Deleted...")
            print("-"*50)
        case 8:
            system.exit()
            
        case _:
            print("Invalid Choice")
        
                                
                
            
            
    