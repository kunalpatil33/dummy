age = int(input("Enter your Age :"))
citizen = str(input("Enter your citizenship :"))
record = str(input("Any criminal record on you (yes/no) :"))

if age > 18 and citizen == "indian" and record == "no":
    print("You are Eligible for voting")
else:
    print("You are not Eligible for voting")
