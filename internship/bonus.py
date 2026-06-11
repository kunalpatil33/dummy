salary = int(input("Enter Salary :"))
exp = int(input("Enter years of Experience :"))
rating = str(input("Enter performance rating :"))
bonus = 0 
if exp > 5 :
    bonus = bonus + (salary * 20 / 100)
    if rating == "a":
        bonus = bonus + (salary * 10 / 100)
    elif rating == "b":
        bonus = bonus + ( salary * 5 / 100)
    else:
        print("No Extra bonus")    
final_salary = salary + bonus 
print("Final salary : ",final_salary)