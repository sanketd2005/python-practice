# f = open("myFile.txt","w")
# print("Name of File : ",f.name)
# print("Mode of File : ",f.mode)
# print("File Readable ? : ",f.readable())
# print("File Writable : ",f.writable())
# print("File Closed : ",f.closed)

# f.close()
# print("File Closed : ",f.closed)


# f = open("myfile.txt","w")
# f.write("\nNashik is a Smart City.")
# # f.write("\nPune is a Smart City.")
# # f.write("\nMumbai is a Smart City.")
# # f.write("\nBanglore is a Smart City.")

# f.close()
# print("File write is done")


# f = open("myfile.txt","a")
# f.write("\nNashik is a Smart City.")
# f.write("\nPune is a Smart City.")
# f.write("\nMumbai is a Smart City.")
# f.write("\nBanglore is a Smart City.")
# f.write("\n\n")

# f.close()
# print("File write is done")


# listFile = open("listContent.txt","w")
# myList = ["prashant","mahesh","suresh"]
# listFile.writelines(str(myList))
# listFile.close()
# print("List content transferred to listContent.txt")

# # READING Data
# f = open("myFile.txt","r")
# print(f.read())
# f.close()

# # USING with STATEMENT
# with open("myFile.txt","w") as myFile:
#     myFile.write("prashant\n")
#     myFile.write("Amit\n")
#     myFile.write("ashish\n")
#     print("File Closed : ",myFile.closed)
# print("File Closed : ",myFile.closed)


# with open("myFile.txt","r") as f:
#     content  = f.read()
#     print(content)


# #================================IMAGE FILE HANDLING===============================================
# dog = open("dog.jpeg","rb")
# puppy = open("puppy.jpeg","wb")
# data  = dog.read()
# print(data)
# puppy.write(ord(data)) 
# dog.close()
# puppy.close()

#--------------------------------CSV FILE HANDLING-----------------------------------------------
# import csv 
# stdFile = open("studentCSV.csv","a",newline="")
# a = csv.writer(stdFile)
# # a.writerow(["StuentID","Roll No","Name","Mobile no."]) # writerow() requires list parameter to set the row values

# id = int(input("Enter Student ID: "))
# rollno = int(input("Enter Student Roll No: "))
# name = input("Enter Student Name: ")
# mobNo = int(input("Enter Student Mobile Number: "))

# a.writerow([id,rollno,name,mobNo])
# print("Record is stored in studentCSV.csv")
# stdFile.close()

