s1 = float(input("Enter marks of subject 1 : "))
s2 = float(input("Enter marks of subject 2 : "))
s3 = float(input("Enter marks of subject 3 : "))
s4 = float(input("Enter marks of subject 4 : "))
s5 = float(input("Enter marks of subject 5 : "))

total = s1 + s2 + s3 + s4 + s5
percentage = total / 5

print("percentage =",percentage)

if percentage >= 90:
    print("Grade: A ")
    print("reesult : Distiction")
elif percentage>= 75:
    print("Grade: B")
    print("Result : pass")
else:
    print("Grade : Fail")
    print("Result : fail")        
