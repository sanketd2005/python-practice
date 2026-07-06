#accept name and marks , save to dict, using name access marks from dict
n = int(input("Enter Number of student: "))
student = {}

for i in range(n):
    name = input("Enter Student Name :").lower()
    marks = int(input("Enter Student Marks :"))
    student[name] = marks
    
while True:
    name = input("Enter Name of Student to get Marks :").lower()
    marks = student.get(name,-1)
    if marks == -1:
        print("student Not Found")
    else:
        print(f"The marks of {name.title()} are {marks}")
    opt = input("Do you want to find another student marks [yes|no]:").lower()
    if opt == 'yes':
        break
    
print("Thanks for using this application")