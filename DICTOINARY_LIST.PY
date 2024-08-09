#CREATE A LIST FOR STUDENT DATA ASKING FOR NAME, AGE , SCHOOL  AND STORE THOSE DATA AND PRINT THOSE DATA.
# User =[
    
# ]
# A =input("Enter name:")
# B= int(input("Enter age:"))
# C= input("Enter school name:")
# student={
#     "name":"A",
#     "age":B,
#     "school":"C"
    
# }
# User.append(student)
student_list=[]
for i in range(1,4):
    name =input("Enter name of student")
    age=int(input("Enter age of student"))
    school = input("Enter school of school")
    student ={
        'name':name,
        'age':age,
        'school':school
    }
    student_list.append(student)
print(student_list)#prints list of dictionaries
for student in student_list:
    print(student['name'])
    print(student['age'])
    print(student['school'])