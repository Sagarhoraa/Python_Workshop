 
#user input as many number as argument , 
#def add(*sum):
  #  sum=a+b
 #   return sum
#x = float input("enter first value")
#y = float input ("enter second value")
#c=add(x,y)
#print(c)
def add(*args):
     sum =0
     for i in args:
         sum = sum + 1
print(f"The sum is {sum}")
         
 add (1)
 add(3,3,4,5)
 add(3,2)
         