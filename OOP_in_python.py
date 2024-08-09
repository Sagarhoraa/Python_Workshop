class sagar:
    def data(self):
        self.id= int(input("Enter the age:"))
        self.name=input("Enter the name:")
        self.salary=float(input("Enter salary:"))
    def printdata(self):
        print("student name:",self.name)
        print("student id:",self.id)
        print("student salary:",self.salary)
obj = sagar()
obj.data()
obj.printdata()
        
        