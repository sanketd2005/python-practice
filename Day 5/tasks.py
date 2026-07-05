# find max and min elements:
# def maxElement(arr):
#     ele = 0
#     for i in arr:
#         if i > ele:
#             ele = i
#     return ele

# def minElement(arr):
#     ele = arr[0]
#     for i in arr:
#         if ele > i:
#             ele = i
#     return ele
# arr = [5,3,9,2,8]
# print(maxElement(arr))
# print(minElement(arr))

# Majority elements

# def majorityElement(arr):
#     count = []
#     counter = 0
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             pass
    
# arr = [3,3,4,2,4,4,2,4,4]


#---------------------------------CSV TASK--------------------------------------------
import csv
with open("student_record.csv","a",newline="") as F:
    wrt = csv.writer(F)
    # wrt.writerow(["Roll no","Name","Mobile No","Subject 1","Subject 2","Subject 3","total","percentage","email","result","Passing Marks"])
    
    rollNo = int(input("Enter Roll number: "))
    name  = input("Enter Name")
    MobNo =  int(input("Enter Mobile number: "))
    email = input("Enter Email ID")
    s1 = int(input("Enter Marks of Subject 1"))
    s2 = int(input("Enter Marks of Subject 2"))
    s3 = int(input("Enter Marks of Subject 3"))
    
    total = s1+s2+s3
    percentage = total / 3.0
    passingMarks = 0
    
    if s1 > 40 and s2 > 40 and s3>40 :
        result = "Pass"
    else:
        if s1 < 40:
            passingMarks = 40 - s1
        elif s2 < 40:
            passingMarks = 40 - s2
        else:
            passingMarks = 40 - s3
 
        result = "Fail"
    
    wrt.writerow([rollNo,name,MobNo,s1,s2,s3,total,percentage,email,result,passingMarks])
    print("Record saved")
    
    
