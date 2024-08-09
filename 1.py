
    
#write a program to ask a user its name until user say no.
stu =[]
choice ="Y"
name='e'
while(choice=="Y" or choice =="y"):
         name = input("enter the name of student: ")
         while(name[-1]!='a'):
             stu.append(name)
             choice= input("Do you want to enter morne name(Y/N): ")
        
print(f"student names are:{stu}")    
    

