
year = int(input("Enter a year :"))
if (year%4==0):
    print("leap year")
    if (year % 400 == 0) or (year % 4 == 0 and year % 100!= 0 ):
        print(year,"is a leap year")
else:
    print(year,"is not leap year")            