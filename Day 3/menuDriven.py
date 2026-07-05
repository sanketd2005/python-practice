import sys as system

def add():
    a = int(input("Number 1 :"))
    b = int(input("Number 2 :"))
    print(a+b)
def sub():
    a = int(input("Number 1 :"))
    b = int(input("Number 2 :"))
    print(a-b)
def mul():
    a = int(input("Number 1 :"))
    b = int(input("Number 2 :"))
    print(a*b)
def div():
    a = int(input("Number 1 :"))
    b = int(input("Number 2 :"))
    print(a/b)
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division") 
    print("5. Exit")
    choice = int(input("Enter your choice :"))
    
    match choice:
        case 1:
            add()   
        case 2:
            sub()
        case 3:
            mul()
        case 4:
            div()
        case 5:
           system.exit()
        case _:
            print("Invalid choice..")