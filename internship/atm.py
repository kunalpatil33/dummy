balance = int (input("Enter balance: "))
amount = int (input("enter withdrawal amount: "))
if amount % 100 == 0 and balance - amount >= 1000:
    print("withdrawal sucessfully")
    total= balance - amount 
    print("remaning amount:",total)   
else :
    print("withdrawal failed")

    
    