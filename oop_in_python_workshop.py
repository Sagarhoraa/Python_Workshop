class Student():
    name="sagar"
    age=20
    address="bhadrapur"
    def __init__(self, name,age):
        self.name=name
        self.age=age
        
    def intro(self):
     print("student name:",self.name)
     print("student age:",self.age)
    
    
obj1 = Student("sagar",20)
obj2 = Student("hari",23)
obj1.intro()
    