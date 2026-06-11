a = int(input("Enter first angle:"))
b = int(input("Enter second angle:"))
c = int(input("Enter third angle:"))

if a + b + c ==180 :
    print("valid Triangle")



    if a and b and c == 60 :
        print("Equilatral Triangle")
    elif a == b or b == c or c == a :
        print("Isoscale triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not valiid Triangle")