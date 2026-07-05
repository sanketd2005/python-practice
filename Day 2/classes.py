class Student:
    #data members
    roll_no = 10
    #member functions
    def message(self):
        print("hello student")

studObj = Student()
print(studObj.roll_no)
studObj.message()
print(studObj)
