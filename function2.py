balance = 0
def credit():
    amount= float(input("enter the amount to credit: "))
    balance = balance + amount
    print(f"Your account is credited with rs.{amount} your total balance is rs{balance}")
    
def debit():
    amount= float(input("enter the amount to credit: "))
    balance = balance - amount
    print(f"Your account is debited with rs.{amount} your total balance is rs.{balance}")
def checkbal():
    print(f"Your total balance is rs.{balance}")
    
choice='' 
choice=input("enter your choice Credit/Debit/Checkbalance") 
if (choice=='c'):
    credit()
elif(choice=='d'):
    debit()
elif(choice=='b'):
    checkbal()
else:
    print("invalid input")
                
          
           