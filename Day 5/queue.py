import sys as system

class Queue:
    def __init__(self,size):
        self.qSize = size
        self.myQueue = []
    
    def isEmpty(self):
        if self.myQueue == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.myQueue) == self.qSize:
            return True
        else:
            return False        

    def enqueue(self,value):
        if self.isFull():
            print("Queue is Full")
        else:
            self.myQueue.append(value)
            print(f"{value} is in the queue")
    
    
    def display(self):
        if self.isEmpty():
            print("Queue is Empty...")
        else:
            for v in self.myQueue:
                print(f"|{v}",end=" ")
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty ")
        else:
            e = self.myQueue.pop(0)
            print(f"{e} is out of Queue Now")
            
    def frontElement(self):
        if self.isEmpty():
            print("Queue is Empty ")
        else:
            print(f"|{self.myQueue[0]}|")
            
    def deleteQueue(self):
        self.myQueue = []
        
        
        
size  = int(input("Enter the size of Queue: "))
queObj = Queue(size)

while True:
    print("1.Enqueue")
    print("2.Display")
    print("3.Dequeue")
    print("4.frontPeek")
    print("5.Delete Queue")
    print("6.Exit")
    print("="*30)
    choice = int(input("Enter Choice: "))
    print("="*30)
    
    match choice:
        case 1:
            value = int(input("Enter Value to be enqueue: "))
            queObj.enqueue(value)
            print("="*30)

        case 2:
            queObj.display()
            print("\n","="*30)
            
            
        case 3:
            queObj.dequeue()
            print("\n","="*30)
        
        case 4:
            queObj.frontElement()
            print("\n","="*30)
            
            
        case 5:
            queObj.deleteQueue()
            print("Queue is Deleted")
            print("\n","="*30)
        
        case 6:
            print("Exit...")
            system.exit()
        
        case _:
            print("Invalid Choice!!!")
