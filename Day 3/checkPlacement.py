class Subjects:
    def __init__(self):
        self.phy = int(input("Enter Physics marks"))
        self.chem= int(input("Enter Chemistry marks"))
        self.math = int(input("Enter Mathematics marks"))

class Result(Subjects):
    def __init__(self):
        super().__init__()
        self.total = self.phy + self.chem+ self.math
        self.percent = self.total / 3.0
    def checkResult(self):
        if self.phy >= 40 and self.math >= 40 and self.chem >= 40:
            return True
        else:
            return False
    def showMarks(self):
        print("="*50)
        print(f"Physics : {self.phy}")
        print(f"Chemistry: {self.chem}")
        print(f"Mathematics: {self.math}")
        print("="*50)
        print(f"Total Marks : {self.total} / 300")
        print(f"Total Marks : {self.percent} %")
        print("="*50)
        self.res = self.checkResult()
        if self.res == True:
            print("Result:  Pass")
        else:
            print("Result:  Fail")
        print("="*50)
            

    def getGender(self):
        self.gender = input("Enter Your gender (M/F): ")
        
    def checkPlacement(self):
        self.getGender()
        self.showMarks()
        if self.percent >= 65 and self.gender == "M":
            print("You are eligible for placement")
        else:
            print("You are not eligible for placement")
            
        self.showReport()
    def showReport(self):
        if self.phy < 40:
            print(f"Required marks to qualify : {40 - self.phy}")
        elif self.chem < 40:
            print(f"Required marks to qualify : {40 - self.chem}")
        else:
            print(f"Required marks to qualify : {40 - self.math}")
            
        
r = Result()
r.checkPlacement()
